#include <cstdint>
#include <exception>
#include <fstream>
#include <fmt/format.h>
#include <fmt/ranges.h>

#include <argparse/argparse.hpp>
#include <cppcodec/base64_rfc4648.hpp>
#include <limits>
#include <stdexcept>

using str = std::string;
constexpr __uint128_t U128MAX = std::numeric_limits<__uint128_t>::max();

void PrintText(const str& Text){
    fmt::println(
        "Input\t{} chars, {} bytes at {:p}\n-> {}\n",
        Text.length(), sizeof(Text), fmt::ptr(&Text), Text
    );
}

std::string ReadFile(const std::string& path){
    std::ifstream in(path, std::ios::binary);

    if(!in) throw std::runtime_error("Cannot open: " + path);

    return std::string(
        std::istreambuf_iterator<char>(in),
        std::istreambuf_iterator<char>()
    );
}

void WriteTo(const str& File, const str& Content){
    if(File == "__NONE__"){
        return;
    } else {
        std::fstream Out(File, std::ios::out | std::ios::trunc);

        if(Out.is_open()){
            try{
                Out.write(Content.data(), Content.size());
                // Out << Content << "\n\n";
                Out.close();
            } catch (std::exception& e){
                fmt::println("Error while writing to file -> {}", e.what());
            }
        } else {
            throw std::domain_error("Failed to open");
        }
    }
}

void Encode(const str& Text, const int& Depth, const bool& Force, const bool& PrintDepth, const str& File){
    fmt::println("{}\n", fmt::format("{:-^30}", " Encoding "));
    PrintText(Text);
    auto Output = Text;

    for(int i = 1; i <= Depth; i++){
        Output = cppcodec::base64_rfc4648::encode(Output);
        if(PrintDepth){ fmt::println("(it {}) {}", i, Output); };
    }

    if(File == "__NONE__"){
        fmt::println(
            "\nOutput\t{} chars, {} bytes at {:p}, {} iterations\n-> {}\n",
            Output.length(), sizeof(Output), fmt::ptr(&Output), Depth, Output
        );
    } else {
        fmt::println(
            "\nOutput\t{} chars, {} bytes at {:p}, {} iterations\n-> {}... (written in {})\n",
            Output.length(), sizeof(Output), fmt::ptr(&Output), Depth, Output.substr(0, 5), File
        );

        auto Content = fmt::format(
            "Input = {}\nIterations = {}\n\nOuput:{}\n",
            Text, Depth, Output
        );
        WriteTo(File, Content);
    }
};

void Decode(const str& Encoded, const int& Depth, const bool& PrintDepth, const str& File){
    fmt::println("{}\n", fmt::format("{:-^30}", " Decoding "));
    PrintText(Encoded);

    str Output = Encoded;
    std::vector<uint8_t> Bytes;

    int it;
    try{
        for(int i = 1; i <= Depth; i++){
            Bytes  = cppcodec::base64_rfc4648::decode(Output);
            Output = str(Bytes.begin(), Bytes.end());

            it = i;

            if(PrintDepth){ fmt::println("(it {}) {}", i, Output); };
        }
    } catch(const std::exception& e){
        fmt::println("Too many iterations, returning last iteration ({}) \nError -> {}", it, e.what());
        std::exit(1);
    }

    if(File == "__NONE__"){
        fmt::println(
            "\nOutput\t{} chars, {} bytes at {:p}, {} iterations\n Str   -> {}\n Bytes -> {}",
            Output.length(), sizeof(Output), fmt::ptr(&Output), it, Output, Bytes
        );
    } else {
        fmt::println(
            "\nOutput\t{} chars, {} bytes at {:p}, {} iterations\n Str   -> {}\n Bytes -> {}",
            Output.length(), sizeof(Output), fmt::ptr(&Output), it, Output, Bytes
        );
        auto Content = fmt::format(
            "Input ({} chars):\n-> {}\nOutput ({} chars)\n-> {}",
            Encoded.length(), Encoded, Output.length(), Output
        );
        WriteTo(File, Content);
    }
}

void ForceDecode(const str& Encoded, const bool& PrintDepth, const str& File){
    fmt::println("{}\n", fmt::format("{:-^30}", " Decoding "));
    PrintText(Encoded);

    str Output = Encoded;
    std::vector<uint8_t> Bytes;

    str Depth = "";

    int it;
    try{
        for(__uint128_t i = 1; i <= U128MAX; i++){
            Bytes  = cppcodec::base64_rfc4648::decode(Output);
            Output = str(Bytes.begin(), Bytes.end());

            it = i;

            if(PrintDepth){
                auto tx =  fmt::format("(it {}) {}", i, Output);
                fmt::println("{}", tx);
                Depth += fmt::format("{}\n", tx);
            };
        }
    } catch(const std::exception& e){
        if(Encoded == Output){
            throw std::invalid_argument("Invalid string!");
        } else {
            fmt::println("Found depth ({})", it);
        }
    }

    if(File == "__NONE__"){
        fmt::println(
            "\nOutput\t{} chars, {} bytes at {:p}, {} iterations\n Str   -> {}\n Bytes -> {}",
            Output.length(), sizeof(Output), fmt::ptr(&Output), it, Output, Bytes
        );
    } else {
        fmt::println(
            "\nOutput\t{} chars, {} bytes at {:p}, {} iterations\n Str   -> {}\n Bytes -> {}",
            Output.length(), sizeof(Output), fmt::ptr(&Output), it, Output, Bytes
        );
        auto Content = fmt::format(
            "Input ({} chars):\n-> {}\nIterations:\n{}\nOutput ({} chars)\n-> {}",
            Encoded.length(), Encoded, Depth, Output.length(), Output
        );
        WriteTo(File, Content);
    }
}


int main(const int argc, const char** argv){
    argparse::ArgumentParser Args("Level0");

    str Text, Mode, File;
    int Depth;
    bool Force;
    bool PrintDepth;

    // Text input
    Args.add_argument("--Text", "-t")
        .default_value<str>("Hello!")
        .help("Text to encode, use prefix __FILE__<file>.txt to read from .txt file")
        .store_into(Text);

    // Mode: Encode/Decode
    Args.add_argument("--Mode", "-m")
        .default_value<str>("E")
        .help("Mode: 'e' to Encode, 'd' to Decode, 'df' to Force Decode")
        .store_into(Mode);

    Args.add_argument("--Depth", "-d")
        .default_value<int>(1)
        .help("How many iterations for encoding/decoding")
        .store_into(Depth);

    Args.add_argument("--Force", "-f")
        .default_value<bool>(false)
        .help("Force to proceed for >= 30 iterations")
        .default_value(false)
        .implicit_value(true)
        .store_into(Force);

    Args.add_argument("--PrintD", "-pd")
        .default_value<bool>(false)
        .help("Print iterations")
        .default_value(false)
        .implicit_value(true)
        .store_into(PrintDepth);

    Args.add_argument("--File", "-fl")
        .default_value("__NONE__")
        .help(".txt file to write output")
        .store_into(File);

    Args.parse_args(argc, argv);

    if(Text.substr(0, 8) == "__FILE__" && Text.substr(Text.length()-4, Text.length()) == ".txt"){
        str FileToRead = Text.substr(8, Text.length());
        Text = ReadFile(FileToRead);
    }

    if(Depth >= 30 && !Force){
        fmt::println("Iterations more than 30 can cause out of memory error, proceed?\n['y' to continue, 'n' to abort]");
        char stat;
        std::cin >> stat;
        if(stat == 'n'){
            fmt::println("Aborting");
            exit(1);
        }
    } else if (Depth >= 30 && Force) {
        fmt::println("Warning: Doing more than 30 can cause out of memory error");
    }

    try {
        if(Mode == "E" || Mode == "e"){

            Encode(Text, Depth, Force, PrintDepth, File);

        } else if (Mode == "D" || Mode == "d"){

            Decode(Text, Depth, PrintDepth, File);

        } else if(Mode == "DF" || Mode == "df"){

            ForceDecode(Text, PrintDepth, File);

        } else {
            fmt::println("Invalid mode! (E/D)");
        }

    } catch(const std::exception& e){
        fmt::println("Error! Invalid input or bad character\n{}", e.what());
        exit(1);
    }

    return 0;
}

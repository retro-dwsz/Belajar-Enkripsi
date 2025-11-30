#include <cstdint>
#include <cstdlib>
#include <exception>
#include <stdexcept>

#include <Tools/Files.hpp>
#include <fmt/format.h>
#include <fmt/ranges.h>

#include <argparse/argparse.hpp>

using str = std::string;

void PrintText(const str& Text){
    fmt::println(
        "Input\t{} chars, {} B at {:p}\n-> {}\n",
        Text.length(), Text.size(), fmt::ptr(&Text), Text
    );
}

namespace Lv1 {
    std::string XorCipher(const std::string& text, const std::string& key){
        std::string out;
        out.reserve(text.size());

        for(size_t i = 0; i < text.size(); i++){
            out.push_back(text[i] ^ key[i % key.size()]);
        }
        return out;
    }

    std::string Vigenere(const std::string& text, const std::string& key, bool encrypt){
        std::string out;
        out.reserve(text.size());

        for(size_t i = 0; i < text.size(); i++){
            int t = (unsigned char)text[i];
            int k = (unsigned char)key[i % key.size()];

            int r = encrypt ? (t + k) % 256
                            : (t - k + 256) % 256;

            out.push_back((char)r);
        }
        return out;
    }

    std::string Substitute(
        const std::string& text,
        const std::array<unsigned char, 256>& map)
    {
        std::string out;
        out.reserve(text.size());

        for(unsigned char c : text){
            out.push_back(map[c]);
        }
        return out;
    }

}

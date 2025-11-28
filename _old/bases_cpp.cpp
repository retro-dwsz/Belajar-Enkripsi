#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdexcept>
#include <cassert>

class basesEnD {
public:
    class encoder{
        public:
            std::string encodeBase1(const std::string& data) {
                return std::string(data.size(), '1');
            }
            std::string encodeBase2(const std::string& data) {
                std::string result;
                for (char c : data) {
                    result += std::bitset<8>(c).to_string();
                }
                return result;
            }
            std::string encodeBase4(const std::string& data) {
                std::string binary = encodeBase2(data);
                std::string result;
                for (char bit : binary) {
                    if (bit == '0') result += "A";
                    else result += "B";
                }
                return result;
            }
            std::string encodeBase8(const std::string& data) {
                std::ostringstream oss;
                for (char c : data) {
                    oss << std::oct << std::setw(3) << std::setfill('0') << (int)c;
                }
                return oss.str();
            }
            std::string encodeBase16(const std::string& data) {
                std::ostringstream oss;
                for (unsigned char c : data) {
                    oss << std::hex << std::setw(2) << std::setfill('0') << (int)c;
                }
                return oss.str();
            }
            std::string encodeBase32(const std::string& data) {
                // Base32 implementation is omitted for brevity.
                return "Not implemented";
            }
            std::string encodeBase64(const std::string& data) {
                // Base64 implementation is omitted for brevity.
                return "Not implemented";
            }
            std::string encodeBase128(const std::string& data) {
                // Base128 implementation is omitted for brevity.
                return "Not implemented";
            }
            std::string encodeBase256(const std::string& data) {
                return data;
            }
    };

    class decoder{
        public:
            std::string decodeBase1(const std::string& encoded) {
                return std::string(encoded.size(), 'a');
            }
            std::string decodeBase2(const std::string& encoded) {
                std::string result;
                for (size_t i = 0; i < encoded.size(); i += 8) {
                    std::bitset<8> bits(encoded.substr(i, 8));
                    result += char(bits.to_ulong());
                }
                return result;
            }
            std::string decodeBase4(const std::string& encoded) {
                std::string binary;
                for (char c : encoded) {
                    if (c == 'A') binary += '0';
                    else if (c == 'B') binary += '1';
                }
                return decodeBase2(binary);
            }
            std::string decodeBase8(const std::string& encoded) {
                std::string result;
                for (size_t i = 0; i < encoded.size(); i += 3) {
                    std::istringstream iss(encoded.substr(i, 3));
                    int val;
                    iss >> std::oct >> val;
                    result += char(val);
                }
                return result;
            }
            std::string decodeBase16(const std::string& encoded) {
                std::string result;
                for (size_t i = 0; i < encoded.size(); i += 2) {
                    std::string byte = encoded.substr(i, 2);
                    char chr = (char)(int)strtol(byte.c_str(), nullptr, 16);
                    result += chr;
                }
                return result;
            }
            std::string decodeBase32(const std::string& encoded) {
                // Base32 implementation is omitted for brevity.
                return "Not implemented";
            }
            std::string decodeBase64(const std::string& encoded) {
                // Base64 implementation is omitted for brevity.
                return "Not implemented";
            }
            std::string decodeBase128(const std::string& encoded) {
                // Base128 implementation is omitted for brevity.
                return "Not implemented";
            }
            std::string decodeBase256(const std::string& encoded) {
                return encoded;
            }
    };
};

int main(int argc, char const *argv[]) {
    basesEnD::encoder encoder;
    basesEnD::decoder decoder;
    // Make into UI
    // std::string data = "Hello, World!";
    std::string data = "Hallå, tév év ä text sà Filieïndo";

    // Base16 Example
    std::string encoded = encoder.encodeBase16(data);
    std::cout << "Encoded Base16: " << encoded << std::endl;

    std::string decoded = decoder.decodeBase16(encoded);
    std::cout << "Decoded Base16: " << decoded << std::endl;

    return 0;
}
import base64

class basesEnD:
    class encoder:
        @staticmethod
        def encode_base1(data: str) -> str:
            """Encode string to Base1 (unary)"""
            return '1' * len(data)

        @staticmethod
        def encode_base2(data: str) -> str:
            """Encode string to Base2 (binary)"""
            return ''.join(format(ord(char), '08b') for char in data)

        @staticmethod
        def encode_base4(data: str) -> str:
            """Encode string to Base4 (quaternary)"""
            return ''.join(format(ord(char), '08b') for char in data).replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D')

        @staticmethod
        def encode_base8(data: str) -> str:
            """Encode string to Base8 (octal)"""
            return ''.join(format(ord(char), '03o') for char in data)

        @staticmethod
        def encode_base16(data: str) -> str:
            """Encode string to Base16 (hexadecimal)"""
            return data.encode().hex()

        @staticmethod
        def encode_base32(data: str) -> str:
            """Encode string to Base32"""
            return base64.b32encode(data.encode()).decode()

        @staticmethod
        def encode_base64(data: str) -> str:
            """Encode string to Base64"""
            return base64.b64encode(data.encode()).decode()

        @staticmethod
        def encode_base128(data: str) -> str:
            """Encode string to Base128 (using Base64 for simplicity)"""
            # Base128 is unusual; we'll simulate it by treating data as bytes
            return base64.b64encode(data.encode()).decode()

        @staticmethod
        def encode_base256(data: str) -> bytes:
            """Encode string to Base256 (bytes)"""
            return data.encode()

    class decoder:
        @staticmethod
        def decode_base1(encoded: str) -> str:
            """Decode Base1 to string (not reversible)"""
            return 'a' * len(encoded)
        
        @staticmethod
        def decode_base2(encoded: str) -> str:
            """Decode Base2 (binary) to string"""
            chars = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
            return ''.join(chr(int(char, 2)) for char in chars)
        
        @staticmethod
        def decode_base4(encoded: str) -> str:
            """Decode Base4 (quaternary) to string"""
            encoded = encoded.replace('A', '00').replace('B', '01').replace('C', '10').replace('D', '11')
            chars = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
            return ''.join(chr(int(char, 2)) for char in chars)
        
        @staticmethod
        def decode_base8(encoded: str) -> str:
            """Decode Base8 (octal) to string"""
            chars = [encoded[i:i+3] for i in range(0, len(encoded), 3)]
            return ''.join(chr(int(char, 8)) for char in chars)
        
        @staticmethod
        def decode_base16(encoded: str) -> str:
            """Decode Base16 (hexadecimal) to string"""
            return bytes.fromhex(encoded).decode()
        
        @staticmethod
        def decode_base32(encoded: str) -> str:
            """Decode Base32 to string"""
            return base64.b32decode(encoded).decode()
        
        @staticmethod
        def decode_base64(encoded: str) -> str:
            """Decode Base64 to string"""
            return base64.b64decode(encoded).decode()
        
        @staticmethod
        def decode_base128(encoded: str) -> str:
            """Decode Base128 (simulated using Base64) to string"""
            return base64.b64decode(encoded).decode()
        
        @staticmethod
        def decode_base256(encoded: bytes) -> str:
            """Decode Base256 (bytes) to string"""
            return encoded.decode()

from colorama import init, Fore as F
import sys, os

init(autoreset=True)

# arg1: text
# arg2: base
# arg3: Enc/Dec
def main(arg):
    args = []
    for i in sys.argv:
        args.append(i)

    # Example usage:
    encoder = basesEnD()
    data = args[0]

    # Base64 Example:
    encoded = encoder.encode_base64(data)
    print("Encoded Base64:", encoded)

    decoded = encoder.decode_base64(encoded)
    print("Decoded Base64:", decoded)

main(sys.argv)
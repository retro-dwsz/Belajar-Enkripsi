import base64
import sys
from colorama import init, Fore as F

init(autoreset=True)

class basesEnD:
    class encoder:
        @staticmethod
        def encode_base1(data: str) -> str:
            return '1' * len(data)

        @staticmethod
        def encode_base2(data: str) -> str:
            return ''.join(format(ord(char), '08b') for char in data)

        @staticmethod
        def encode_base4(data: str) -> str:
            return ''.join(format(ord(char), '08b') for char in data).replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D')

        @staticmethod
        def encode_base8(data: str) -> str:
            return ''.join(format(ord(char), '03o') for char in data)

        @staticmethod
        def encode_base16(data: str) -> str:
            return data.encode().hex()

        @staticmethod
        def encode_base32(data: str) -> str:
            return base64.b32encode(data.encode()).decode()

        @staticmethod
        def encode_base64(data: str) -> str:
            return base64.b64encode(data.encode()).decode()

        @staticmethod
        def encode_base128(data: str) -> str:
            return base64.b64encode(data.encode()).decode()

        @staticmethod
        def encode_base256(data: str) -> bytes:
            return data.encode()

    class decoder:
        @staticmethod
        def decode_base1(encoded: str) -> str:
            return 'a' * len(encoded)
        
        @staticmethod
        def decode_base2(encoded: str) -> str:
            chars = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
            return ''.join(chr(int(char, 2)) for char in chars)
        
        @staticmethod
        def decode_base4(encoded: str) -> str:
            encoded = encoded.replace('A', '00').replace('B', '01').replace('C', '10').replace('D', '11')
            chars = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
            return ''.join(chr(int(char, 2)) for char in chars)
        
        @staticmethod
        def decode_base8(encoded: str) -> str:
            chars = [encoded[i:i+3] for i in range(0, len(encoded), 3)]
            return ''.join(chr(int(char, 8)) for char in chars)
        
        @staticmethod
        def decode_base16(encoded: str) -> str:
            return bytes.fromhex(encoded).decode()
        
        @staticmethod
        def decode_base32(encoded: str) -> str:
            return base64.b32decode(encoded).decode()
        
        @staticmethod
        def decode_base64(encoded: str) -> str:
            return base64.b64decode(encoded).decode()
        
        @staticmethod
        def decode_base128(encoded: str) -> str:
            return base64.b64decode(encoded).decode()
        
        @staticmethod
        def decode_base256(encoded: bytes) -> str:
            return encoded.decode()

def main():
    # Parse command-line arguments
    args = sys.argv[1:]
    text = None
    enc_base = None
    is_decode = False
    brute_force = False

    for i in range(len(args)):
        if args[i].startswith("--text="):
            text = args[i].split("=", 1)[1]
        elif args[i].startswith("--enc="):
            enc_base = args[i].split("=", 1)[1]
        elif args[i] == "--dec=True":
            is_decode = True
        elif args[i] == "--brute=True":
            brute_force = True

    if text is None:
        print(F.RED + "No text provided!")
        return

    encoder = basesEnD.encoder()
    decoder = basesEnD.decoder()

    if enc_base:
        if not is_decode:
            if enc_base == "1":
                print("Encoded Base1:", encoder.encode_base1(text))
            elif enc_base == "2":
                print("Encoded Base2:", encoder.encode_base2(text))
            elif enc_base == "4":
                print("Encoded Base4:", encoder.encode_base4(text))
            elif enc_base == "8":
                print("Encoded Base8:", encoder.encode_base8(text))
            elif enc_base == "16":
                print("Encoded Base16:", encoder.encode_base16(text))
            elif enc_base == "32":
                print("Encoded Base32:", encoder.encode_base32(text))
            elif enc_base == "64":
                print("Encoded Base64:", encoder.encode_base64(text))
            elif enc_base == "128":
                print("Encoded Base128:", encoder.encode_base128(text))
            elif enc_base == "256":
                print("Encoded Base256:", encoder.encode_base256(text))
            else:
                print(F.RED + "Unknown encoding base!")
        else:
            if enc_base == "1":
                print("Decoded Base1:", decoder.decode_base1(text))
            elif enc_base == "2":
                print("Decoded Base2:", decoder.decode_base2(text))
            elif enc_base == "4":
                print("Decoded Base4:", decoder.decode_base4(text))
            elif enc_base == "8":
                print("Decoded Base8:", decoder.decode_base8(text))
            elif enc_base == "16":
                print("Decoded Base16:", decoder.decode_base16(text))
            elif enc_base == "32":
                print("Decoded Base32:", decoder.decode_base32(text))
            elif enc_base == "64":
                print("Decoded Base64:", decoder.decode_base64(text))
            elif enc_base == "128":
                print("Decoded Base128:", decoder.decode_base128(text))
            elif enc_base == "256":
                print("Decoded Base256:", decoder.decode_base256(text.encode()))
            else:
                print(F.RED + "Unknown decoding base!")
    elif brute_force:
        print(F.GREEN + "Brute force decoding...")
        for base in range(2, 11):
            try:
                decode_func = getattr(decoder, f"decode_base{2**base}")
                print(f"Base {2**base}: {decode_func(text)}")
            except Exception as e:
                print(F.RED + f"Base {2**base} failed: {e}")

if __name__ == "__main__":
    main()

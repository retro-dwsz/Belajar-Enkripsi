import tkinter as tk
from tkinter import ttk, scrolledtext
import base64

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

# Create the main application window
root = tk.Tk()
root.title("Base Encoder/Decoder")

# Window size and configuration
root.geometry("500x400")
root.resizable(False, False)

# Create the main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create and place widgets
# Input Label and Textbox
ttk.Label(main_frame, text="Input Text:").grid(row=0, column=0, sticky=tk.W)
input_text = scrolledtext.ScrolledText(main_frame, width=40, height=3, wrap=tk.WORD)
input_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Base Encoding/Decoding Label and Dropdown
ttk.Label(main_frame, text="Base:").grid(row=2, column=0, sticky=tk.W)
base_choice = tk.StringVar()
base_menu = ttk.Combobox(main_frame, textvariable=base_choice)
base_menu['values'] = ('Base1', 'Base2', 'Base4', 'Base8', 'Base16', 'Base32', 'Base64', 'Base128', 'Base256')
base_menu.grid(row=3, column=0, sticky=tk.W)

# Mode (Encode/Decode)
ttk.Label(main_frame, text="Mode:").grid(row=2, column=1, sticky=tk.W)
mode_choice = tk.StringVar(value="Encode")
ttk.Radiobutton(main_frame, text="Encode", variable=mode_choice, value="Encode").grid(row=3, column=1, sticky=tk.W)
ttk.Radiobutton(main_frame, text="Decode", variable=mode_choice, value="Decode").grid(row=3, column=1, sticky=tk.E)

# Result Label and Textbox
ttk.Label(main_frame, text="Result:").grid(row=4, column=0, sticky=tk.W)
result_text = scrolledtext.ScrolledText(main_frame, width=40, height=3, wrap=tk.WORD)
result_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Function to perform encoding/decoding
def perform_action():
    input_data = input_text.get("1.0", tk.END).strip()
    base = base_choice.get().lower()
    mode = mode_choice.get().lower()
    
    if not input_data:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter some text.")
        return
    
    encoder = basesEnD.encoder()
    decoder = basesEnD.decoder()

    try:
        if mode == "encode":
            if base == "base1":
                result = encoder.encode_base1(input_data)
            elif base == "base2":
                result = encoder.encode_base2(input_data)
            elif base == "base4":
                result = encoder.encode_base4(input_data)
            elif base == "base8":
                result = encoder.encode_base8(input_data)
            elif base == "base16":
                result = encoder.encode_base16(input_data)
            elif base == "base32":
                result = encoder.encode_base32(input_data)
            elif base == "base64":
                result = encoder.encode_base64(input_data)
            elif base == "base128":
                result = encoder.encode_base128(input_data)
            elif base == "base256":
                result = encoder.encode_base256(input_data).decode()
        else:
            if base == "base1":
                result = decoder.decode_base1(input_data)
            elif base == "base2":
                result = decoder.decode_base2(input_data)
            elif base == "base4":
                result = decoder.decode_base4(input_data)
            elif base == "base8":
                result = decoder.decode_base8(input_data)
            elif base == "base16":
                result = decoder.decode_base16(input_data)
            elif base == "base32":
                result = decoder.decode_base32(input_data)
            elif base == "base64":
                result = decoder.decode_base64(input_data)
            elif base == "base128":
                result = decoder.decode_base128(input_data)
            elif base == "base256":
                result = decoder.decode_base256(input_data.encode())
        
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {e}")

# Action Button
action_button = ttk.Button(main_frame, text="Perform Action", command=perform_action)
action_button.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Start the main application loop
root.mainloop()

import random
import string
import unicodedata as uni

def generate_char_map(mapping_length=10):
    """Generate a mapping from a wide range of characters to a string of characters."""
    char_map = {}
    
    # Define a broad character set including letters, digits, punctuation, and diacritics
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation +
        ''.join(chr(i) for i in range(0x00C0, 0x00FF)) +  # Latin-1 Supplement
        ''.join(chr(i) for i in range(0x0100, 0x017F)) +  # Latin Extended-A
        ''.join(chr(i) for i in range(0x0180, 0x024F)) +  # Latin Extended-B
        ''.join(chr(i) for i in range(0x0250, 0x02AF)) +  # IPA Extensions
        ''.join(chr(i) for i in range(0x2C60, 0x2C7F)) +  # Latin Extended-C
        ''.join(chr(i) for i in range(0x1E00, 0x1EFF)) # Latin Extended Additional
        
        # # Java Script
        # + 
        # ''.join(chr(i) for i in range(0xA980, 0xA98F)) +
        # ''.join(chr(i) for i in range(0xA990, 0xA99F)) +
        # ''.join(chr(i) for i in range(0xA9A0, 0xA9AF)) +
        # ''.join(chr(i) for i in range(0xA9B0, 0xA9BF)) +
        # ''.join(chr(i) for i in range(0xA9C0, 0xA9CF)) +
        # ''.join(chr(i) for i in range(0xA9D0, 0xA9DF))
    )
    
    # Generate a random string of specified length for each character
    for char in characters:
        char_map[char] = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=mapping_length))
    
    return char_map

class CustomEncryptor:
    def __init__(self):
        pass

    def encrypt(self, text, char_map):
        """Encrypt the text by substituting each character based on the provided char_map."""
        encrypted_text = ''.join(char_map.get(char, char) for char in text)
        return encrypted_text

    def decrypt(self, encrypted_text, char_map):
        """Decrypt the text by reversing the substitution based on the provided char_map."""
        # Reverse the char_map to map from encoded strings back to original characters
        reverse_map = {v: k for k, v in char_map.items()}
        decrypted_text = ''
        i = 0
        mapping_length = len(next(iter(reverse_map.keys())))  # Determine the length of mapping used
        while i < len(encrypted_text):
            # Extract substring of the mapping length
            substring = encrypted_text[i:i + mapping_length]
            # Map it back to the original character
            decrypted_text += reverse_map.get(substring, '?')
            i += mapping_length
        return decrypted_text

# Contoh penggunaan
# mapping_length = 10  # Bisa diubah ke 100 untuk map 100 karakter

char_map = generate_char_map(mapping_length=1)

encrypt = CustomEncryptor()

text = "Hallå, tév év ä text sà Filieïndo"

print("Original Text: ", text)

# Enkripsi
encrypted_text = encrypt.encrypt(text, char_map)
print("Encrypted Text: ", encrypted_text)

# Dekripsi
decrypted_text = encrypt.decrypt(encrypted_text, char_map)
print("Decrypted Text: ", decrypted_text)

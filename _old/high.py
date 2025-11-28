import base64
from time import sleep

def encr(data: str, layer: int = 2, decrypt: bool = False) -> str:
    # Jika decrypt=True, maka lakukan dekripsi; jika tidak, lakukan enkripsi
    if decrypt:
        for _ in range(layer):
            data = base64.b64decode(data).decode("utf-8")
    else:
        for _ in range(layer):
            data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    
    return data

class main():
    def main1(self):
        # Contoh penggunaan:
        # Enkripsi "hello" dengan 2 layer
        encrypted_2_layers = encr("hello", 2)
        print(f"Encrypted (2 layers): {encrypted_2_layers}")

        # Enkripsi "hello" dengan 3 layer
        encrypted_3_layers = encr("hello", 3)
        print(f"Encrypted (3 layers): {encrypted_3_layers}")

        # Dekripsi kembali string yang dienkripsi dengan 2 layer
        decrypted_2_layers = encr(encrypted_2_layers, 2, decrypt=True)
        print(f"Decrypted (2 layers): {decrypted_2_layers}")

        # Dekripsi kembali string yang dienkripsi dengan 3 layer
        decrypted_3_layers = encr(encrypted_3_layers, 3, decrypt=True)
        print(f"Decrypted (3 layers): {decrypted_3_layers}")

    def main2(self):
        tx = "Hallå, tév év ä text sà Filieïndo"

        print(tx)
        for i in range(10):
            print(f"\nEncrypt {i} layer(s)\n> {encr(tx, i)}")
            sleep(1)
        # tx_e2 = encr(tx, 2)
        # print(f"tx = {tx}\ntx_e2 = {tx_e2}")

        # tx_d2 = encr(tx_e2, 2, True)
        # print(f"\ntx_d2 = {tx_d2}")
    def main3(self):
        tx = r"Vm0wd2VFNUdWWGhTV0d4VFYwZG9WVll3WkRSV2JGbDNXa1JTVjFadGVGcFpNRnByVmpKS1IxTnNiRlZpUjAweFZteGtTMUl4WkhOWGJGcFhUVEZKZWxkV1VrSmxSMDE0Vkd4V1ZHSkhVazlaVjNoaFZWWmFjbGt6YUZOaVZscFpWbTEwWVZWR1duUlZiRkpXWWtaS1dGVnNXbXRXTVZaeVpFWk9UbFp1UWpaV2JUQXhVekZaZVZOc2JGSmlSa3BZV1d0YVMxZEdWbk5YYlVaVFRWWndNRlZ0TVRCVWJGbDRVMnh3VjFaNlJYZFdha1pYWkVaS1dXTkdTbWxTYkhCWVYxZDRiMVV4VWtkV2JsSnNVMFUxY1ZadGRHRmxWbEY0VjJ0MFZXSkdjRmxhU0hCSFZqRmFObEpVUWxwaGEzQk1WV3BHVTJOc1pITlZiV3hYVFcxb1lWWnRNVEJXTVVweVRWWmtWbUpIYUhOVk1GVXhZMnhXYzFWclpGaFNiSEJKVkZaU1ExZHNXWGhYYm1oV1ZteEtWMVZHUlRsUVVUMDk="
        print(f"decrypted: {encr(tx, 9, True)}")

def app():
    m = main()
    try:
        m.main3()
    except KeyboardInterrupt or MemoryError or ValueError as e:
        print(f"ERROR!\n> {e}")
        exit(1)

app()
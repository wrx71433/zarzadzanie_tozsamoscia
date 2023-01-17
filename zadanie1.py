import base64

def base64_encryption(text):
    #kodowanie na base64
    encoded_text = base64.b64encode(text.encode())
    #ewentualne dekodowanie
    decoded_text = base64.b64decode(encoded_text).decode()
    return encoded_text

print(base64_encryption("test"))

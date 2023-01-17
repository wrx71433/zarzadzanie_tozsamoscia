import random
import string

def create_secure_password():
    password = ""
    length = random.randint(8, 16)
    characters = string.ascii_lowercase
    characters += string.ascii_uppercase
    characters += string.digits
    characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(create_secure_password())

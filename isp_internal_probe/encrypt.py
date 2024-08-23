import json
import os
from cryptography.fernet import Fernet
import keyring
from keyrings.alt import file


keyring.set_keyring(file.PlaintextKeyring())


def set_password(service, username, password):
    keyring.set_password(service, username, password)


# Generate a secret key for encryption and decryption
def generate_key():
    key = Fernet.generate_key().decode('utf-8')
    set_password("Gyan_LinkEye", "Key", key)


# Load the secret key from a file
def load_key():
    key = keyring.get_password("Gyan_LinkEye", "Key")
    if key:
        return key
    else:
        return "Password not found in keyring."


def encrypt_json(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(json.dumps(data).encode())
    with open("data.json", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)


if __name__ == "__main__":
    generate_key()

    key = load_key()
    data_to_encrypt = json.load(open("config.json", "r"))

    encrypt_json(data_to_encrypt, key)

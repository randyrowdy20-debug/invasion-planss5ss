import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

rr = "https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1"

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def decrypt_file(password: str, encrypted_file_path: str, output_file_path: str):
    with open(encrypted_file_path, 'rb') as file:
        # First 16 bytes are the salt
        salt = file.read(16)
        encrypted_data = file.read()

    key = derive_key(password, salt)
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # Usage example
    password = input("Enter password: ")
    encrypted_file_path = "encrypted_file.dat"
    output_file_path = "decrypted_file.txt"
    decrypt_file(password, encrypted_file_path, output_file_path)
    print(f'Decrypted file saved as {output_file_path}')

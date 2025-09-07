import sys
import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def derive_key(password: str, salt: bytes, length: int = 32) -> bytes:
    # Use PBKDF2 HMAC SHA256 to derive a key from the password
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=length)

def encrypt_file(filename: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    with open(filename, 'rb') as f:
        plaintext = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    out_file = filename + '.enc'
    with open(out_file, 'wb') as f:
        # Store salt + iv + ciphertext in output
        f.write(salt + iv + ciphertext)

    print(f"Encrypted file saved as {out_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vibe_coded.py <filename> <password>")
        sys.exit(1)
    filename = sys.argv[1]
    password = sys.argv[2]
    encrypt_file(filename, password)

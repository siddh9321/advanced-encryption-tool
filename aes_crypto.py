from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_aes_key():
    return os.urandom(32)  # AES-256

def encrypt_aes(key, data):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    return iv + encryptor.update(data)

def decrypt_aes(key, encrypted_data):
    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data[16:])
from core.aes_crypto import generate_aes_key, encrypt_aes, decrypt_aes
from core.rsa_crypto import encrypt_rsa, decrypt_rsa

def hybrid_encrypt(public_key, data):
    aes_key = generate_aes_key()
    encrypted_data = encrypt_aes(aes_key, data)
    encrypted_key = encrypt_rsa(public_key, aes_key)
    return encrypted_key + b"||" + encrypted_data

def hybrid_decrypt(private_key, encrypted):
    encrypted_key, encrypted_data = encrypted.split(b"||")
    aes_key = decrypt_rsa(private_key, encrypted_key)
    return decrypt_aes(aes_key, encrypted_data)
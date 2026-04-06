from cryptography.hazmat.primitives import serialization

def save_private_key(private_key, filename="private_key.pem"):
    with open(filename, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def save_public_key(public_key, filename="public_key.pem"):
    with open(filename, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def load_private_key(filename="private_key.pem"):
    with open(filename, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def load_public_key(filename="public_key.pem"):
    with open(filename, "rb") as f:
        return serialization.load_pem_public_key(f.read())
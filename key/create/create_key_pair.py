from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096
)
public_key = private_key.public_key()

pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("rsa_secret_key.pem", "wb") as private_key_file:
    private_key_file.write(pem_private_key)

with open("rsa_public_key.pem", "wb") as public_key_file:
    public_key_file.write(pem_public_key)

print("Key pair generated")
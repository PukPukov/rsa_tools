from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature

def verify_signature(public_key_pem, signed_message_file):
    with open(public_key_pem, 'rb') as pub_file:
        public_key = load_pem_public_key(pub_file.read())

    with open(signed_message_file, 'r', encoding="utf-8") as file:
        signed_message = file.read()

    message_start = signed_message.find("-----BEGIN SIGNED MESSAGE-----") + len("-----BEGIN SIGNED MESSAGE-----")
    message_end = signed_message.find("-----END SIGNED MESSAGE-----")
    signature_start = signed_message.find("-----BEGIN SIGNATURE-----") + len("-----BEGIN SIGNATURE-----")
    signature_end = signed_message.find("-----END SIGNATURE-----")
    
    if message_start == -1 or message_end == -1 or signature_start == -1 or signature_end == -1:
        raise ValueError("Illegal format")

    message = signed_message[message_start:message_end].strip()
    signature = signed_message[signature_start:signature_end].strip()
    signature = ''.join(signature.splitlines())

    from base64 import b64decode
    signature = b64decode(signature)

    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=20
            ),
            hashes.SHA256()
        )
        print("Message is genuine")
    except InvalidSignature:
        print("VALIDATION FAILED")

verify_signature("rsa_public_key.pem", "signed_message.txt")
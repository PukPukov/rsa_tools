from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
import base64

message_file = "message.txt"
private_key_file = "rsa_secret_key.pem"
output_file = "signed_message.txt"

forbidden_tokens = ["-----BEGIN SIGNED MESSAGE-----", "-----END SIGNED MESSAGE-----", "-----BEGIN SIGNATURE-----", "-----END SIGNATURE-----"]

with open(message_file, "r", encoding="utf-8") as f:
    message = f.read().strip()

if any(token in message for token in forbidden_tokens):
    print("Message contains format tokens. Can't create signed message file")
else:
    with open(private_key_file, "rb") as f:
        private_key_data = f.read()
    private_key = load_pem_private_key(private_key_data, password=None, backend=default_backend())

    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=20
        ),
        hashes.SHA256()
    )

    signature_base64 = base64.b64encode(signature).decode("utf-8")

    def split_into_lines(data, line_length=64):
        return '\n'.join([data[i:i+line_length] for i in range(0, len(data), line_length)])

    signature_pem = split_into_lines(signature_base64)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("-----BEGIN SIGNED MESSAGE-----\n")
        f.write(message + "\n")
        f.write("-----END SIGNED MESSAGE-----\n")
        f.write("-----BEGIN SIGNATURE-----\n")
        f.write(signature_pem + "\n")
        f.write("-----END SIGNATURE-----\n")

    print(f"Message and signature saved to {output_file}")
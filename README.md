Dead simple RSA-based message genuinity verification tool.

### key/create/create_key_pair.py

**Output:**
- `rsa_secret_key.py`
- `rsa_public_key.py`

### message/sign/sign_message.py

**Input:**  
- `message.txt`
- `rsa_secret_key.pem`

**Output:**  
- `signed_message.txt`

### message/verify/verify_message.py

**Input:**
- `signed_message.txt`
- `rsa_public_key.pem`

## Installation
- Install Python
- Install `cryptography` lib (`pip install cryptography`)

## Additional information

All inputs and outputs are files in the same directory as python file. You just provide them and run python file. All dynamic files already excluded in gitignore.

Why not GnuPG or OpenSSL? They are not that simple, and gnupg also is using its own no-one-asked-for key format.  
Postquantum variant? Later. 4096-bit RSA key is unlikely to be broken in the next one or two years, so we have some time. It is recommended to self-sign expiration date with key by start of 2028 and put it near to public key.
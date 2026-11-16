
# ==========================================
# RSA ENCRYPTION AND DECRYPTION
# Subject: Data Security and Privacy (BAD703)
# Project: Public Key Cryptography System
# ==========================================

import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# STEP 1: Generate RSA Public and Private Keys
def generate_keys():

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return public_key, private_key


# STEP 2: Encrypt the Plaintext using Public Key
def encrypt_message(message, public_key):

    encrypted_message = public_key.encrypt(
        message.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_message


# STEP 3: Decrypt the Ciphertext using Private Key
def decrypt_message(encrypted_message, private_key):

    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return decrypted_message.decode("utf-8")


# STEP 4: Main Program
if __name__ == "__main__":

    print("=" * 45)
    print("       RSA ENCRYPTION SYSTEM")
    print("=" * 45)

    # Generate keys
    public_key, private_key = generate_keys()

    print("\nRSA keys generated successfully!")

    # Accept plaintext
    message = input("\nEnter your message: ")

    # Encryption
    encrypted = encrypt_message(message, public_key)

    # Display ciphertext
    ciphertext = base64.b64encode(encrypted).decode("utf-8")

    print("\nEncrypted Message (Ciphertext):")
    print(ciphertext)

    # Decryption
    decrypted = decrypt_message(encrypted, private_key)

    print("\nDecrypted Message:")
    print(decrypted)

    # Verification
    print("\nVerification:")

    if message == decrypted:
        print("SUCCESS: Original and decrypted messages match!")
    else:
        print("ERROR: Messages do not match!")

    print("\n" + "=" * 45)
    print("       RSA EXECUTION COMPLETED")
    print("=" * 45)

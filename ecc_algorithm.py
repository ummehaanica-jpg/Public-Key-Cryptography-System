
# ==========================================
# ECC ENCRYPTION AND DECRYPTION
# Subject: Data Security and Privacy (BAD703)
# Project: Public Key Cryptography System
# ==========================================

import os
import base64

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import serialization


# STEP 1: Generate ECC Public and Private Keys
def generate_keys():

    private_key = ec.generate_private_key(
        ec.SECP256R1()
    )

    public_key = private_key.public_key()

    return public_key, private_key


# STEP 2: Derive AES Key from Shared Secret
def derive_key(shared_secret):

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ECC-ECIES-Demo"
    ).derive(shared_secret)

    return derived_key


# STEP 3: Encrypt Message using ECC Hybrid Encryption
def encrypt_message(message, receiver_public_key):

    # Generate temporary ECC key pair
    ephemeral_private_key = ec.generate_private_key(
        ec.SECP256R1()
    )

    ephemeral_public_key = ephemeral_private_key.public_key()

    # Generate shared secret using ECDH
    shared_secret = ephemeral_private_key.exchange(
        ec.ECDH(),
        receiver_public_key
    )

    # Derive AES encryption key
    aes_key = derive_key(shared_secret)

    # Generate a random nonce
    nonce = os.urandom(12)

    # Encrypt message using AES-GCM
    aesgcm = AESGCM(aes_key)

    ciphertext = aesgcm.encrypt(
        nonce,
        message.encode("utf-8"),
        None
    )

    # Serialize temporary public key
    ephemeral_public_bytes = ephemeral_public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.CompressedPoint
    )

    return ephemeral_public_bytes, nonce, ciphertext


# STEP 4: Decrypt Message using ECC Hybrid Encryption
def decrypt_message(
    ephemeral_public_bytes,
    nonce,
    ciphertext,
    receiver_private_key
):

    # Reconstruct temporary public key
    ephemeral_public_key = ec.EllipticCurvePublicKey.from_encoded_point(
        ec.SECP256R1(),
        ephemeral_public_bytes
    )

    # Generate the same shared secret
    shared_secret = receiver_private_key.exchange(
        ec.ECDH(),
        ephemeral_public_key
    )

    # Derive the same AES key
    aes_key = derive_key(shared_secret)

    # Decrypt ciphertext
    aesgcm = AESGCM(aes_key)

    decrypted_message = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )

    return decrypted_message.decode("utf-8")


# STEP 5: Main Program
if __name__ == "__main__":

    print("=" * 45)
    print("       ECC ENCRYPTION SYSTEM")
    print("=" * 45)

    # Generate receiver keys
    public_key, private_key = generate_keys()

    print("\nECC keys generated successfully!")
    print("Elliptic Curve: SECP256R1")

    # Accept plaintext
    message = input("\nEnter your message: ")

    # Encryption
    ephemeral_public, nonce, encrypted = encrypt_message(
        message,
        public_key
    )

    print("\nEncrypted Message (Ciphertext):")
    print(base64.b64encode(encrypted).decode("utf-8"))

    print("\nEphemeral Public Key:")
    print(base64.b64encode(ephemeral_public).decode("utf-8"))

    # Decryption
    decrypted = decrypt_message(
        ephemeral_public,
        nonce,
        encrypted,
        private_key
    )

    print("\nDecrypted Message:")
    print(decrypted)

    # Verification
    print("\nVerification:")

    if message == decrypted:
        print("SUCCESS: Original and decrypted messages match!")
    else:
        print("ERROR: Messages do not match!")

    print("\n" + "=" * 45)
    print("       ECC EXECUTION COMPLETED")
    print("=" * 45)

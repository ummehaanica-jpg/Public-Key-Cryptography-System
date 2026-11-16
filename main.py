
import base64
import time

from rsa_algorithm import (
    generate_keys as rsa_generate_keys,
    encrypt_message as rsa_encrypt,
    decrypt_message as rsa_decrypt
)

from ecc_algorithm import (
    generate_keys as ecc_generate_keys,
    encrypt_message as ecc_encrypt,
    decrypt_message as ecc_decrypt
)


# --------------------------------------------------
# 1. RSA ENCRYPTION AND DECRYPTION
# --------------------------------------------------

def run_rsa():

    print("\n========== RSA ENCRYPTION AND DECRYPTION ==========")

    try:
        message = input("Enter the message to encrypt: ")

        print("\nGenerating RSA keys...")
        public_key, private_key = rsa_generate_keys()

        print("RSA keys generated successfully!")

        encrypted_message = rsa_encrypt(message, public_key)

        print("\nEncrypted Ciphertext:")
        print(base64.b64encode(encrypted_message).decode("utf-8"))

        decrypted_message = rsa_decrypt(
            encrypted_message, private_key
        )

        print("\nDecrypted Message:")
        print(decrypted_message)

        if decrypted_message == message:
            print("\nVerification: SUCCESS")
            print("Original and decrypted messages match!")
        else:
            print("\nVerification: FAILED")

    except Exception as error:
        print("\nRSA operation failed:", error)


# --------------------------------------------------
# 2. ECC ENCRYPTION AND DECRYPTION
# --------------------------------------------------

def run_ecc():

    print("\n========== ECC ENCRYPTION AND DECRYPTION ==========")

    try:
        message = input("Enter the message to encrypt: ")

        print("\nGenerating ECC keys...")
        public_key, private_key = ecc_generate_keys()

        print("ECC keys generated successfully!")

        ephemeral_public, nonce, encrypted_message = ecc_encrypt(
            message, public_key
        )

        print("\nEphemeral Public Key:")
        print(base64.b64encode(ephemeral_public).decode("utf-8"))

        print("\nEncrypted Ciphertext:")
        print(base64.b64encode(encrypted_message).decode("utf-8"))

        decrypted_message = ecc_decrypt(
            ephemeral_public,
            nonce,
            encrypted_message,
            private_key
        )

        print("\nDecrypted Message:")
        print(decrypted_message)

        if decrypted_message == message:
            print("\nVerification: SUCCESS")
            print("Original and decrypted messages match!")
        else:
            print("\nVerification: FAILED")

    except Exception as error:
        print("\nECC operation failed:", error)


# --------------------------------------------------
# 3. RSA AND ECC PERFORMANCE COMPARISON
# --------------------------------------------------

def compare_algorithms():

    print("\n========== RSA VS ECC COMPARISON ==========")

    message = "Data Security and Privacy Project"

    try:
        # RSA Performance

        print("\nMeasuring RSA Performance...")

        start = time.perf_counter()
        rsa_public, rsa_private = rsa_generate_keys()
        rsa_key_generation = time.perf_counter() - start

        start = time.perf_counter()
        rsa_ciphertext = rsa_encrypt(message, rsa_public)
        rsa_encryption = time.perf_counter() - start

        start = time.perf_counter()
        rsa_plaintext = rsa_decrypt(
            rsa_ciphertext, rsa_private
        )
        rsa_decryption = time.perf_counter() - start

        # ECC Performance

        print("Measuring ECC Performance...")

        start = time.perf_counter()
        ecc_public, ecc_private = ecc_generate_keys()
        ecc_key_generation = time.perf_counter() - start

        start = time.perf_counter()
        ephemeral_public, nonce, ecc_ciphertext = ecc_encrypt(
            message, ecc_public
        )
        ecc_encryption = time.perf_counter() - start

        start = time.perf_counter()
        ecc_plaintext = ecc_decrypt(
            ephemeral_public,
            nonce,
            ecc_ciphertext,
            ecc_private
        )
        ecc_decryption = time.perf_counter() - start

        # Verification

        print("\n========== VERIFICATION ==========")

        print(
            "RSA:",
            "SUCCESS" if rsa_plaintext == message else "FAILED"
        )

        print(
            "ECC:",
            "SUCCESS" if ecc_plaintext == message else "FAILED"
        )

        # Display comparison

        print("\n========== PERFORMANCE RESULTS ==========")

        print("\n{:<25} {:<15} {:<15}".format(
            "Operation", "RSA (seconds)", "ECC (seconds)"
        ))

        print("-" * 55)

        print("{:<25} {:<15.6f} {:<15.6f}".format(
            "Key Generation",
            rsa_key_generation,
            ecc_key_generation
        ))

        print("{:<25} {:<15.6f} {:<15.6f}".format(
            "Encryption",
            rsa_encryption,
            ecc_encryption
        ))

        print("{:<25} {:<15.6f} {:<15.6f}".format(
            "Decryption",
            rsa_decryption,
            ecc_decryption
        ))

        print("\nComparison completed successfully!")

        print("\nNote: These timings are from a single test run.")

    except Exception as error:
        print("\nComparison failed:", error)


# --------------------------------------------------
# 4. MAIN MENU
# --------------------------------------------------

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("       PUBLIC KEY CRYPTOGRAPHY SYSTEM")
        print("              RSA AND ECC")
        print("=" * 55)

        print("\n1. RSA Encryption and Decryption")
        print("2. ECC Encryption and Decryption")
        print("3. Compare RSA and ECC")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            run_rsa()

        elif choice == "2":
            run_ecc()

        elif choice == "3":
            compare_algorithms()

        elif choice == "4":
            print("\nThank you for using our project!")
            print("Exiting the system...")
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 4.")


# --------------------------------------------------
# 5. PROGRAM EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    main()

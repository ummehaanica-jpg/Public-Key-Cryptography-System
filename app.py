
import streamlit as st
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


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="SecureCrypt | RSA & ECC",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1220, #111d30);
    color: #f1f5f9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

.main-heading {
    font-size: 38px;
    font-weight: 800;
    color: #55d6be;
    text-align: center;
    letter-spacing: 1px;
}

.sub-heading {
    color: #a8b8cc;
    text-align: center;
    font-size: 15px;
    margin-bottom: 25px;
}

.section-heading {
    color: #55d6be;
    font-size: 25px;
    font-weight: 700;
}

.info-card {
    background: #17283d;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #29445b;
    min-height: 125px;
}

.info-card h3 {
    color: #55d6be;
    margin-bottom: 8px;
}

.info-card p {
    color: #c5d2df;
    font-size: 14px;
}

div.stButton > button {
    background: linear-gradient(90deg, #087f75, #16a394);
    color: white;
    border: none;
    border-radius: 9px;
    height: 45px;
    font-weight: 700;
    width: 100%;
}

div.stButton > button:hover {
    background: #20b7a5;
    color: white;
    border: none;
}

[data-testid="stSidebar"] {
    background-color: #101c2c;
}

.footer {
    text-align: center;
    color: #8496aa;
    font-size: 13px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-heading">🔐 SECURECRYPT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-heading">'
    'PUBLIC KEY CRYPTOGRAPHY PLATFORM | RSA & ECC'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

st.sidebar.markdown(
    "<h2 style='color:#55d6be;'>SECURECRYPT</h2>",
    unsafe_allow_html=True
)

st.sidebar.caption("Cryptography & Data Protection")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Dashboard",
        "RSA Encryption",
        "ECC Encryption",
        "RSA vs ECC Comparison",
        "About Project"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### Project Information")
st.sidebar.write("**Subject:** Data Security and Privacy")
st.sidebar.write("**Project:** RSA and ECC")
st.sidebar.write("**Semester:** VII")

st.sidebar.divider()

st.sidebar.caption("MS Engineering College, Bengaluru")


# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    st.markdown(
        '<div class="section-heading">Welcome to SecureCrypt</div>',
        unsafe_allow_html=True
    )

    st.write(
        "An interactive public key cryptography application "
        "demonstrating RSA and Elliptic Curve Cryptography (ECC)."
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🔑 RSA Cryptography</h3>
            <p>
            RSA is an asymmetric encryption algorithm that uses
            a public key for encryption and a private key
            for decryption.
            </p>
            <p><b>Key size:</b> 2048 bits</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🛡️ ECC Cryptography</h3>
            <p>
            ECC uses elliptic curve mathematics. This application
            demonstrates ECDH key agreement with AES-GCM encryption.
            </p>
            <p><b>Curve:</b> SECP256R1</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Application Features")

    feature1, feature2, feature3 = st.columns(3)

    with feature1:
        st.metric("Algorithms", "2", "RSA + ECC")

    with feature2:
        st.metric("Key Generation", "Enabled")

    with feature3:
        st.metric("Verification", "Enabled")

    st.divider()

    st.subheader("How to Use")

    st.markdown("""
    1. Select **RSA Encryption** to test RSA.
    2. Select **ECC Encryption** to test ECC.
    3. Enter a plaintext message.
    4. Generate ciphertext and decrypt it.
    5. Verify whether the original message is recovered.
    6. Open **RSA vs ECC Comparison** to compare execution times.
    """)


# ==================================================
# RSA ENCRYPTION
# ==================================================

elif page == "RSA Encryption":

    st.markdown(
        '<div class="section-heading">RSA Encryption & Decryption</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Encrypt plaintext using an RSA public key and recover "
        "the original message using the corresponding private key."
    )

    message = st.text_area(
        "Enter your plaintext message",
        placeholder="Type your confidential message here...",
        height=130,
        key="rsa_message"
    )

    if st.button("🔐 Encrypt and Decrypt with RSA"):

        if not message:
            st.warning("Please enter a message first.")

        else:
            try:
                with st.spinner("Generating RSA keys and processing..."):

                    public_key, private_key = rsa_generate_keys()

                    encrypted = rsa_encrypt(message, public_key)

                    decrypted = rsa_decrypt(
                        encrypted, private_key
                    )

                st.success("RSA encryption and decryption completed!")

                st.subheader("Encryption Result")

                ciphertext = base64.b64encode(
                    encrypted
                ).decode("utf-8")

                st.text_area(
                    "RSA Ciphertext (Base64)",
                    value=ciphertext,
                    height=110
                )

                st.subheader("Decryption Result")

                st.text_area(
                    "Recovered Plaintext",
                    value=decrypted,
                    height=90
                )

                if decrypted == message:
                    st.success(
                        "✓ Verification Successful! "
                        "Original and decrypted messages match."
                    )
                else:
                    st.error("Verification Failed!")

                st.info(
                    "RSA configuration: 2048-bit key, "
                    "OAEP padding and SHA-256."
                )

            except Exception as error:
                st.error(f"RSA operation failed: {error}")


# ==================================================
# ECC ENCRYPTION
# ==================================================

elif page == "ECC Encryption":

    st.markdown(
        '<div class="section-heading">ECC Encryption & Decryption</div>',
        unsafe_allow_html=True
    )

    st.write(
        "This demonstration uses Elliptic Curve Diffie-Hellman "
        "(ECDH) to derive a symmetric key, followed by AES-GCM "
        "to encrypt and decrypt the message."
    )

    message = st.text_area(
        "Enter your plaintext message",
        placeholder="Type your confidential message here...",
        height=130,
        key="ecc_message"
    )

    if st.button("🛡️ Encrypt and Decrypt with ECC"):

        if not message:
            st.warning("Please enter a message first.")

        else:
            try:
                with st.spinner("Generating ECC keys and processing..."):

                    public_key, private_key = ecc_generate_keys()

                    ephemeral_public, nonce, encrypted = ecc_encrypt(
                        message, public_key
                    )

                    decrypted = ecc_decrypt(
                        ephemeral_public,
                        nonce,
                        encrypted,
                        private_key
                    )

                st.success("ECC encryption and decryption completed!")

                st.subheader("Ephemeral Public Key")

                st.code(
                    base64.b64encode(
                        ephemeral_public
                    ).decode("utf-8")
                )

                st.subheader("Encrypted Ciphertext")

                st.text_area(
                    "ECC Ciphertext (Base64)",
                    value=base64.b64encode(
                        encrypted
                    ).decode("utf-8"),
                    height=110
                )

                st.subheader("Decryption Result")

                st.text_area(
                    "Recovered Plaintext",
                    value=decrypted,
                    height=90
                )

                if decrypted == message:
                    st.success(
                        "✓ Verification Successful! "
                        "Original and decrypted messages match."
                    )
                else:
                    st.error("Verification Failed!")

                st.info(
                    "ECC configuration: SECP256R1, ECDH, "
                    "HKDF-SHA256 and AES-256-GCM."
                )

            except Exception as error:
                st.error(f"ECC operation failed: {error}")


# ==================================================
# RSA VS ECC COMPARISON
# ==================================================

elif page == "RSA vs ECC Comparison":

    st.markdown(
        '<div class="section-heading">RSA vs ECC Performance Analysis</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Measure and compare the key generation, encryption "
        "and decryption execution times."
    )

    test_message = "Data Security and Privacy Project"

    st.info(f"Test message: {test_message}")

    if st.button("📊 Run Performance Comparison"):

        try:
            with st.spinner("Benchmarking RSA and ECC..."):

                # RSA measurements

                start = time.perf_counter()
                rsa_public, rsa_private = rsa_generate_keys()
                rsa_keygen = time.perf_counter() - start

                start = time.perf_counter()
                rsa_cipher = rsa_encrypt(test_message, rsa_public)
                rsa_encrypt_time = time.perf_counter() - start

                start = time.perf_counter()
                rsa_plain = rsa_decrypt(
                    rsa_cipher, rsa_private
                )
                rsa_decrypt_time = time.perf_counter() - start

                # ECC measurements

                start = time.perf_counter()
                ecc_public, ecc_private = ecc_generate_keys()
                ecc_keygen = time.perf_counter() - start

                start = time.perf_counter()
                ephemeral, nonce, ecc_cipher = ecc_encrypt(
                    test_message, ecc_public
                )
                ecc_encrypt_time = time.perf_counter() - start

                start = time.perf_counter()
                ecc_plain = ecc_decrypt(
                    ephemeral,
                    nonce,
                    ecc_cipher,
                    ecc_private
                )
                ecc_decrypt_time = time.perf_counter() - start

            st.success("Performance analysis completed!")

            # Verification

            col1, col2 = st.columns(2)

            with col1:
                if rsa_plain == test_message:
                    st.success("RSA Verification: SUCCESS")
                else:
                    st.error("RSA Verification: FAILED")

            with col2:
                if ecc_plain == test_message:
                    st.success("ECC Verification: SUCCESS")
                else:
                    st.error("ECC Verification: FAILED")

            # Convert seconds to milliseconds

            rsa_values = [
                rsa_keygen * 1000,
                rsa_encrypt_time * 1000,
                rsa_decrypt_time * 1000
            ]

            ecc_values = [
                ecc_keygen * 1000,
                ecc_encrypt_time * 1000,
                ecc_decrypt_time * 1000
            ]

            st.subheader("Performance Results")

            st.table({
                "Operation": [
                    "Key Generation",
                    "Encryption",
                    "Decryption"
                ],
                "RSA (milliseconds)": [
                    f"{value:.4f}" for value in rsa_values
                ],
                "ECC (milliseconds)": [
                    f"{value:.4f}" for value in ecc_values
                ]
            })

            st.subheader("Visual Performance Comparison")

            st.caption("Execution time in milliseconds. Lower values indicate less time.")

            st.bar_chart({
                "RSA": rsa_values,
                "ECC": ecc_values
            })

            st.caption(
                "Note: These are single-run measurements. "
                "RSA uses OAEP encryption, whereas ECC uses "
                "ECDH-based key derivation with AES-GCM. "
                "They are different cryptographic constructions."
            )

        except Exception as error:
            st.error(f"Comparison failed: {error}")


# ==================================================
# ABOUT PROJECT
# ==================================================

elif page == "About Project":

    st.markdown(
        '<div class="section-heading">About Our Project</div>',
        unsafe_allow_html=True
    )

    st.subheader("Public Key Cryptography System: RSA and ECC")

    st.write("""
    This project demonstrates two important public key
    cryptographic approaches used in modern information security.

    RSA uses asymmetric encryption with a public and private key.

    ECC uses elliptic curve cryptography. Our implementation
    demonstrates ECDH-based shared key derivation and AES-GCM
    authenticated encryption.
    """)

    st.divider()

    st.subheader("Project Objectives")

    st.markdown("""
    - Understand public key cryptography.
    - Implement RSA encryption and decryption.
    - Implement ECC-based hybrid encryption.
    - Compare execution times of both implementations.
    - Verify successful recovery of the original plaintext.
    """)

    st.divider()

    st.subheader("Technologies Used")

    st.markdown("""
    - **Programming Language:** Python
    - **Cryptography Library:** Python Cryptography
    - **Frontend:** Streamlit
    - **Algorithms:** RSA, ECC, ECDH, HKDF and AES-GCM
    - **Development Environment:** Visual Studio Code
    """)

    st.divider()

    st.subheader("Project Team")

    st.markdown("""
    **Department:** Artificial Intelligence and Machine Learning

    **College:** MS Engineering College, Bengaluru

    **Semester:** VII

    **Subject:** Data Security and Privacy (BAD703)
    """)

    st.markdown("### Team Members")

    st.write("1. Umme Haani C A — 1ME23AI027")
    st.write("2. Jehsta K B — 1ME23AI013")
    st.write("3. Talakal Vinayaka — 1ME23AI025")

    st.divider()

    st.markdown("### Project Guide")
    st.write("**Dr. Rahul**")


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown("""
<div class="footer">
    <b>SECURECRYPT</b><br>
    Public Key Cryptography System: RSA and ECC<br>
    Data Security and Privacy | VII Semester<br>
    MS Engineering College, Bengaluru
</div>
""", unsafe_allow_html=True)

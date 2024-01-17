from cryptography.fernet import Fernet

# Generate a random key for encryption (store this securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_string(input_string):
    encrypted_bytes = cipher_suite.encrypt(input_string.encode())
    return encrypted_bytes


def decrypt_string(encrypted_bytes):
    decrypted_bytes = cipher_suite.decrypt(encrypted_bytes)
    return decrypted_bytes.decode()

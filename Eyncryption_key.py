import secrets

# Specify the desired key length in bytes (e.g., 32 bytes for AES-256)
key_length = 16

# Generate a secure random key
encryption_key = secrets.token_bytes(key_length)

# Print the key in hexadecimal format (common for encryption keys)
print("Encryption key (hex):", encryption_key.hex())

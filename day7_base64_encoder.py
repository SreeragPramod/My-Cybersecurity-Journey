import base64

print("--- Base64 Encoder / Decoder ---")

# We use 'def' to define our own custom tool (a Function)
def encode_message(secret_text):
    # Convert text to bytes, encode it in base64, and convert it back to readable text
    encoded_bytes = base64.b64encode(secret_text.encode())
    return encoded_bytes.decode()

def decode_message(encoded_text):
    # Reverse the process: Decode the base64 text back to normal
    decoded_bytes = base64.b64decode(encoded_text.encode())
    return decoded_bytes.decode()


# --- Now we actually use the tools we just built! ---

original_message = "The firewall password is admin123"
print("1. Original Message:", original_message)

# Let's hide the message using our custom encoder tool
hidden_message = encode_message(original_message)
print("2. Encoded (Base64):", hidden_message)

# Let's reveal the hidden message using our decoder tool
revealed_message = decode_message(hidden_message)
print("3. Decoded back to normal:", revealed_message)

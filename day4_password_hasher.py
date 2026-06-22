import hashlib
print("--- SHA-256 Password Hasher ---")
print("This tool converts passwords into an unreadable hash.")

secret_password = input("\Enter a password to secure: ")
hashed_result = hashlib.sha256(secret_password.encode()).hexdigest()

print("\n[!] Original Password:", secret_password)
print("[!] Securing data...")
print("[!] Hashed Output:", hashed_result)
print("\nEven if a hacker steals this hash, they cannot reverse it back to the password!")

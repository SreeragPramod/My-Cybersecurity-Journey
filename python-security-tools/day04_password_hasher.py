"""
Day 04 - Password Hashing: Insecure vs. Secure Methods
Demonstrates why plain SHA-256 is unsuitable for password storage,
and shows the correct approach using salting.

Security concept: SHA-256 is fast by design (good for file integrity,
bad for passwords) because speed lets attackers brute-force or use
rainbow tables against it. Salting + slow algorithms (bcrypt, scrypt,
Argon2) are the real-world standard. This script illustrates the
difference using SHA-256 + a random salt as a minimal example.
"""
import hashlib
import os


def insecure_hash(password):
    """Plain SHA-256 - vulnerable to rainbow tables. For demonstration only."""
    return hashlib.sha256(password.encode()).hexdigest()


def secure_hash(password):
    """
    SHA-256 with a random salt. Better than plain SHA-256, but note:
    in production, use bcrypt/scrypt/Argon2 instead - they are
    deliberately slow, which is what actually defeats brute force.
    """
    salt = os.urandom(16)
    salted = salt + password.encode()
    hashed = hashlib.sha256(salted).hexdigest()
    return salt.hex(), hashed


def verify_password(password, salt_hex, stored_hash):
    salt = bytes.fromhex(salt_hex)
    salted = salt + password.encode()
    return hashlib.sha256(salted).hexdigest() == stored_hash


if __name__ == "__main__":
    password = input("Enter a password to secure: ")

    print("\n--- Insecure: Plain SHA-256 ---")
    plain = insecure_hash(password)
    print(f"Hash: {plain}")
    print("Risk: Same password always produces same hash -> vulnerable to")
    print("precomputed rainbow tables and fast brute-force attacks.")

    print("\n--- Secure: Salted SHA-256 ---")
    salt_hex, salted_hash = secure_hash(password)
    print(f"Salt: {salt_hex}")
    print(f"Hash: {salted_hash}")
    print("Why it's better: the random salt means the same password")
    print("produces a different hash every time, defeating rainbow tables.")

    print("\n--- Verification Test ---")
    is_valid = verify_password(password, salt_hex, salted_hash)
    print(f"Password verification: {'PASSED' if is_valid else 'FAILED'}")

    print("\n[Note] In production, use bcrypt, scrypt, or Argon2 instead of")
    print("SHA-256 - they are intentionally slow, which is the real defense")
    print("against brute force, not just salting alone.")

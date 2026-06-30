"""
Day 02 - Password Strength Checker
Evaluates password strength based on length and character composition
(uppercase, lowercase, digits, special characters).
Security use case: This is the same logic used in account signup forms
to enforce password policies and reduce credential-based attacks.
"""
import re


def check_strength(password):
    if not password:
        return "INVALID", "Password cannot be empty."

    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    if length < 8:
        return "LOW", "Too short. Aim for at least 8 characters."
    elif length < 12 or criteria_met < 3:
        return "MODERATE", "Add uppercase, numbers, or symbols to strengthen it."
    else:
        return "STRONG", "Good length and character variety."


def main():
    password = input("Enter a password to test: ")
    level, feedback = check_strength(password)
    print(f"\n[Security Level: {level}]")
    print(f"Feedback: {feedback}")


if __name__ == "__main__":
    main()

# Password Strength Evaluation Tool (CLI Version - No GUI)

import re
import math

# Using regex and entropy points 

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def calculate_entropy(password):
    char_space = 0

    if any(c.islower() for c in password):
        char_space += 26
    if any(c.isupper() for c in password):
        char_space += 26
    if any(c.isdigit() for c in password):
        char_space += 10
    if any(not c.isalnum() for c in password):
        char_space += 32

    if char_space == 0:
        return 0

    entropy = len(password) * math.log2(char_space)
    return round(entropy, 2)


def has_repeated_chars(password):
    return len(set(password)) < len(password) / 2


def is_common_password(password):
    common = ["123456", "password", "qwerty", "abc123", "111111"]
    return password.lower() in common


def evaluate_password(password):
    if is_common_password(password):
        return "Very Weak (Common Password)", 0

    strength = check_password_strength(password)
    entropy = calculate_entropy(password)

    if has_repeated_chars(password):
        strength = "Weak"

    return strength, entropy


# User input

if __name__ == "__main__":
    password = input("Enter password: ")
    strength, entropy = evaluate_password(password)

    print("\nPassword Strength:", strength)
    print("Entropy:", entropy, "bits")

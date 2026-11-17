"""
OneBitBrains - Smart Password Auditor & Generator
A security tool to evaluate password strength and generate strong alternatives.
"""

import random
import string
from typing import Dict


def check_password_length(password: str, min_length: int = 12) -> bool:
    """
    Checks if the password meets the minimum required length.

    Args:
        password (str): The password string to evaluate.
        min_length (int): Minimum acceptable length (default is 12).

    Returns:
        bool: True if the password is long enough, False otherwise.
    """
    return len(password) >= min_length


# Justin


def analyze_character_types(password: str) -> Dict[str, bool]:
    """
    Checks which character categories are present in the password.

    Args:
        password (str): The password string to analyze.

    Returns:
        Dict[str, bool]: Dictionary indicating presence of uppercase,
        lowercase, digits, and symbols.
    """
    analysis = {
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digits": any(char.isdigit() for char in password),
        "symbols": any(char in string.punctuation for char in password)
    }
    return analysis
    

# ---


# TODO (Marko): Add calculate_strength_score function here


# TODO (Iriome): Add generate_secure_password function here


# TODO (Josè): Add format_security_report function here


# --- Interactive Execution ---
if __name__ == "__main__":
    print("========================================")
    print("  ONEBITBRAINS - PASSWORD SECURITY TOOL ")
    print("========================================")

    user_password = input("Enter a password to test its strength: ").strip()

    if user_password:
        # 1. Check length (Nicolò)
        is_long_enough = check_password_length(user_password)
        print(f"Length check (>= 12 chars): {'Passed' if is_long_enough else 'Failed'} ({len(user_password)} chars)")

        # TODO: Call the remaining team functions once added

        # Justin
        char_breakdown = analyze_character_types(user_password)
        print(f"Character breakdown: {char_breakdown}")
    
    else:
        print("\nError: Empty input. Please run the program again and enter a password.")

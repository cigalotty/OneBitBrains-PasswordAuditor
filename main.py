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


# TODO (Justin): Add analyze_character_types function here


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
    else:
        print("\nError: Empty input. Please run the program again and enter a password.")

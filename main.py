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
    

# Marko
def calculate_strength_score(length_ok: bool, char_analysis: Dict[str, bool]) -> int:
    """
    Computes a security score from 0 to 100 based on length and character variety.
    Args:
        length_ok (bool): Whether the password meets the length requirement.
        char_analysis (Dict[str, bool]): Presence of different character types.
    Returns:
        int: Total security score (0-100).
    """
    score = 0

    if length_ok:
        score += 40

    for is_present in char_analysis.values():
        if is_present:
            score += 15

    return min(score, 100)

# Iriome
def generate_secure_password(length: int = 14) -> str:
    """
    Generates a random, cryptographically strong password containing all
    character types.
    Args:
    length (int): Desired length of the generated password (default is
    14).
    Returns:
    str: A newly generated strong password.
    """
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_=+")
    ]
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    remaining_length = max(0, length - 4)
    password_chars.extend(random.choice(all_chars) for _ in
    range(remaining_length))
    random.shuffle(password_chars)
    return "".join(password_chars)


# Jose
def format_security_report(password: str, score: int, char_analysis: Dict[str, bool]) -> str:
    """
    Formats the audit results into a readable report and suggests a new password
    if weak.

    Args:
        password (str): The evaluated password.
        score (int): Calculated security score (0-100).
        char_analysis (Dict[str, bool]): Character breakdown.

    Returns:
        str: Formatted final security report.
    """
    if score >= 85:
        rating = "STRONG"
    elif score >= 55:
        rating = "MEDIUM"
    else:
        rating = "WEAK"

    report = "\n========================================\n"
    report += "    ONEBITBRAINS PASSWORD AUDIT REPORT   \n"
    report += "========================================\n"
    report += f"Password Length : {len(password)} characters\n"
    report += f"Uppercase       : {'Yes' if char_analysis['uppercase'] else 'No'}\n"
    report += f"Lowercase       : {'Yes' if char_analysis['lowercase'] else 'No'}\n"
    report += f"Numbers         : {'Yes' if char_analysis['digits'] else 'No'}\n"
    report += f"Symbols         : {'Yes' if char_analysis['symbols'] else 'No'}\n"
    report += f"\nSecurity Score  : {score}/100 ({rating})\n"

    if score < 85:
        suggested = generate_secure_password(14)
        report += "\n[!] Recommendation: Your password can be improved.\n"
        report += f"[+] Suggested Strong Password: {suggested}\n"
    else:
        report += "\n[OK] Great job! Your password meets high security standards.\n"

    report += "========================================"
    return report


# --- Interactive Execution ---
if __name__ == "__main__":
    print("========================================")
    print("  ONEBITBRAINS - PASSWORD SECURITY TOOL ")
    print("========================================")

    user_password = input("Enter a password to test its strength: ").strip()

    if user_password:
        is_long_enough = check_password_length(user_password)
        char_breakdown = analyze_character_types(user_password)
        final_score = calculate_strength_score(is_long_enough, char_breakdown)
        
        report_output = format_security_report(user_password, final_score, char_breakdown)
        print(report_output)
    else:
        print("\nError: Empty input. Please run the program again and enter a password.")

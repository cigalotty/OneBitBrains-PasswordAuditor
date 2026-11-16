# OneBitBrains — Smart Password Auditor & Generator

A lightweight Python CLI tool developed by **Team OneBitBrains** (Justin, Marko, Iriome, Jose, and Nicolò) for the *Professional Skills for Engineers* course at ULPGC.

## Features
- **Length Check (`check_password_length`):** Verifies if the password meets the 12-character minimum threshold.
- **Character Analysis (`analyze_character_types`):** Checks for uppercase, lowercase, digits, and special symbols.
- **Strength Scoring (`calculate_strength_score`):** Computes a 0–100 security score.
- **Password Generator (`generate_secure_password`):** Generates a random 14-character strong password if the score is below 85.
- **Audit Report (`format_security_report`):** Prints a clear, structured security summary.

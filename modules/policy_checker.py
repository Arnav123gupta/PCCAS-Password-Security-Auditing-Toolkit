"""Evaluate a password against a configurable security policy."""

import string

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "welcome123"
}

def check_password_policy(
    password,
    min_length=12,
    require_uppercase=True,
    require_lowercase=True,
    require_digit=True,
    require_symbol=True
):
    if not isinstance(password, str) or not password:
        raise ValueError("Password cannot be empty.")

    checks = {
        "minimum_length": len(password) >= min_length,
        "uppercase": (not require_uppercase) or any(c.isupper() for c in password),
        "lowercase": (not require_lowercase) or any(c.islower() for c in password),
        "digit": (not require_digit) or any(c.isdigit() for c in password),
        "symbol": (not require_symbol) or any(c in string.punctuation for c in password),
        "not_common": password.lower() not in COMMON_PASSWORDS
    }

    failures = [name for name, passed in checks.items() if not passed]

    return {
        "passed": len(failures) == 0,
        "checks": checks,
        "failures": failures,
        "policy": {
            "minimum_length": min_length,
            "uppercase_required": require_uppercase,
            "lowercase_required": require_lowercase,
            "digit_required": require_digit,
            "symbol_required": require_symbol
        }
    }

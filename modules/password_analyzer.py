import math
import string

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "welcome123"
}


def analyze_password(password):
    if not isinstance(password, str) or not password:
        raise ValueError("Password cannot be empty.")

    charset = 0

    checks = {
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digits": any(c.isdigit() for c in password),
        "symbols": any(c in string.punctuation for c in password)
    }

    if checks["lowercase"]:
        charset += 26
    if checks["uppercase"]:
        charset += 26
    if checks["digits"]:
        charset += 10
    if checks["symbols"]:
        charset += len(string.punctuation)

    entropy = len(password) * math.log2(charset) if charset else 0

    score = sum(checks.values())

    if len(password) >= 16:
        score += 2
    elif len(password) >= 12:
        score += 1

    common = password.lower() in COMMON_PASSWORDS

    if common:
        rating = "WEAK"
    elif len(password) < 12 or score <= 3:
        rating = "WEAK"
    elif score <= 5:
        rating = "MODERATE"
    else:
        rating = "STRONG"

    recommendations = []

    if len(password) < 12:
        recommendations.append("Use at least 12 characters.")
    if not checks["uppercase"]:
        recommendations.append("Consider uppercase characters.")
    if not checks["lowercase"]:
        recommendations.append("Consider lowercase characters.")
    if not checks["digits"]:
        recommendations.append("Consider including numbers.")
    if not checks["symbols"]:
        recommendations.append("Consider including symbols.")
    if common:
        recommendations.append("Avoid commonly used passwords.")

    return {
        "length": len(password),
        "entropy_estimate": round(entropy, 2),
        "score": score,
        "rating": rating,
        "common_password": common,
        "recommendations": recommendations
    }


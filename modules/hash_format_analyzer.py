"""Structural hash-format hints; never verifies or cracks a hash."""

def analyze_hash_format(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Hash sample cannot be empty.")
    value = value.strip().lower()
    if any(c not in "0123456789abcdef" for c in value):
        return {"length": len(value), "possible_format": "UNKNOWN",
                "confidence": "NONE",
                "note": "Sample contains non-hexadecimal characters."}
    formats = {
        32: ("MD5 / NTLM", "AMBIGUOUS"),
        40: ("SHA-1", "POSSIBLE"),
        64: ("SHA-256", "POSSIBLE"),
        128: ("SHA-512", "POSSIBLE"),
    }
    result = formats.get(len(value))
    if result is None:
        return {"length": len(value), "possible_format": "UNKNOWN",
                "confidence": "NONE",
                "note": "Length does not match supported examples."}
    name, confidence = result
    note = ("Length alone cannot distinguish MD5 from NTLM."
            if len(value) == 32 else
            "Length and hexadecimal characters are structural clues only.")
    return {"length": len(value), "possible_format": name,
            "confidence": confidence, "note": note}

def analyze_sample_catalog():
    """Use fixed synthetic examples instead of reading system credential stores."""
    samples = {
        "synthetic_32": "a" * 32,
        "synthetic_40": "b" * 40,
        "synthetic_64": "c" * 64,
        "synthetic_128": "d" * 128,
    }
    return {name: analyze_hash_format(value) for name, value in samples.items()}

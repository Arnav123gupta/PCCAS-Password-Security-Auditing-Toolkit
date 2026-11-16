"""Identify possible hash formats using safe structural checks only."""

def analyze_hash_format(value):
    if not isinstance(value, str) or not value:
        raise ValueError("Hash sample cannot be empty.")

    value = value.strip().lower()

    if not value:
        raise ValueError("Hash sample cannot be empty.")

    if any(char not in "0123456789abcdef" for char in value):
        return {
            "length": len(value),
            "possible_format": "UNKNOWN",
            "confidence": "NONE",
            "note": "Sample contains non-hexadecimal characters."
        }

    formats = {
        32: ("MD5 / NTLM", "AMBIGUOUS"),
        40: ("SHA-1", "POSSIBLE"),
        64: ("SHA-256", "POSSIBLE"),
        128: ("SHA-512", "POSSIBLE"),
    }

    result = formats.get(len(value))

    if result is None:
        return {
            "length": len(value),
            "possible_format": "UNKNOWN",
            "confidence": "NONE",
            "note": "Length does not match supported examples."
        }

    name, confidence = result

    note = (
        "Length alone cannot distinguish MD5 from NTLM."
        if len(value) == 32
        else "Length and hexadecimal characters are only structural clues."
    )

    return {
        "length": len(value),
        "possible_format": name,
        "confidence": confidence,
        "note": note
    }


if __name__ == "__main__":
    samples = {
        "sample_32": "a" * 32,
        "sample_40": "b" * 40,
        "sample_64": "c" * 64,
        "sample_128": "d" * 128,
    }

    import json
    print(json.dumps({
        name: analyze_hash_format(value)
        for name, value in samples.items()
    }, indent=4))

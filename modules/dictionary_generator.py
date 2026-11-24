"""Generate synthetic password-security test data. No real wordlists."""
import json
from pathlib import Path

TEST_CASES = [
    {"password": "12345678", "expected": "WEAK"},
    {"password": "password123", "expected": "WEAK"},
    {"password": "Welcome123", "expected": "WEAK"},
    {"password": "Hello123!", "expected": "WEAK"},
    {"password": "RiverBlue2026", "expected": "MODERATE"},
    {"password": "N7!vQ2@pL9#xR4$m", "expected": "STRONG"},
    {"password": "T8#kLm2@Qp7!Vz5$", "expected": "STRONG"},
]

def generate_test_dataset(output_path="data/test_cases.json"):
    """Write fixed synthetic examples for local policy testing."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(TEST_CASES, indent=4), encoding="utf-8")
    return {"count": len(TEST_CASES), "output": str(path), "status": "success"}

def generate_dictionary_demo(output_path="data/dictionary_demo.json"):
    """Create a labeled demonstration dataset, not a password-guessing list."""
    records = [
        {"sample_id": "SYN-001", "pattern": "short_numeric", "risk": "HIGH"},
        {"sample_id": "SYN-002", "pattern": "common_word_plus_digits", "risk": "HIGH"},
        {"sample_id": "SYN-003", "pattern": "predictable_word_plus_year", "risk": "MEDIUM"},
        {"sample_id": "SYN-004", "pattern": "long_mixed_sample", "risk": "LOW"},
    ]
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=4), encoding="utf-8")
    return {"count": len(records), "output": str(path), "status": "success",
            "note": "Labeled synthetic patterns only; no candidate wordlist generated."}

if __name__ == "__main__":
    print(json.dumps(generate_test_dataset(), indent=2))
    print(json.dumps(generate_dictionary_demo(), indent=2))

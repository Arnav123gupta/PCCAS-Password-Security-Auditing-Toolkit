"""Generate harmless synthetic password test cases for security auditing."""

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
    """Save synthetic examples; never reads real user or system passwords."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(TEST_CASES, file, indent=4)

    return {
        "count": len(TEST_CASES),
        "output": str(path),
        "status": "success",
    }


if __name__ == "__main__":
    result = generate_test_dataset()
    print(json.dumps(result, indent=4))

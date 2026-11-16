import json
from modules.dictionary_generator import (
    TEST_CASES,
    generate_test_dataset,
)


def test_dataset_has_seven_examples():
    assert len(TEST_CASES) == 7


def test_dataset_has_required_fields():
    for item in TEST_CASES:
        assert "password" in item
        assert "expected" in item


def test_dataset_file_is_created(tmp_path):
    output = tmp_path / "sample.json"
    result = generate_test_dataset(output)

    assert result["status"] == "success"
    assert output.exists()

    saved_data = json.loads(output.read_text(encoding="utf-8"))
    assert len(saved_data) == 7

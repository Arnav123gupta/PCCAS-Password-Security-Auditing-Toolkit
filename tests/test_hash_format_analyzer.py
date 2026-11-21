import pytest
from modules.hash_format_analyzer import analyze_hash_format


def test_32_character_hash_is_ambiguous():
    result = analyze_hash_format("a" * 32)
    assert result["possible_format"] == "MD5 / NTLM"
    assert result["confidence"] == "AMBIGUOUS"


def test_sha256_length():
    result = analyze_hash_format("b" * 64)
    assert result["possible_format"] == "SHA-256"


def test_invalid_characters():
    result = analyze_hash_format("xyz123")
    assert result["possible_format"] == "UNKNOWN"


def test_empty_input():
    with pytest.raises(ValueError):
        analyze_hash_format("")


def test_sha512_length():
    result = analyze_hash_format("c" * 128)
    assert result["possible_format"] == "SHA-512"


def test_non_string_hash_rejected():
    with pytest.raises(ValueError):
        analyze_hash_format(None)


def test_whitespace_only_hash_rejected():
    with pytest.raises(ValueError):
        analyze_hash_format("   ")

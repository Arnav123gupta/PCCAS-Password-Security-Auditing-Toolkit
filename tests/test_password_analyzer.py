import pytest
from modules.password_analyzer import analyze_password


def test_empty_password():
    with pytest.raises(ValueError):
        analyze_password("")


def test_common_password():
    result = analyze_password("password123")
    assert result["rating"] == "WEAK"
    assert result["common_password"] is True


def test_strong_candidate():
    result = analyze_password("N7!vQ2@pL9#xR4$m")
    assert result["rating"] == "STRONG"


def test_password_length():
    result = analyze_password("Hello123!")
    assert result["length"]  ==  9



def test_non_string_input_rejected():
    with pytest.raises(ValueError):
        analyze_password(None)


def test_score_limitations_are_documented():
    result = analyze_password("N7!vQ2@pL9#xR4$m")
    assert "educational indicator" in result["limitations"]

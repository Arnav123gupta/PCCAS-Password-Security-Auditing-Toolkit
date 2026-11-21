import pytest
from modules.policy_checker import check_password_policy


def test_strong_candidate_passes():
    result = check_password_policy("N7!vQ2@pL9#xR4$m")
    assert result["passed"] is True
    assert result["failures"] == []


def test_common_password_fails():
    result = check_password_policy("password123")
    assert result["passed"] is False
    assert "not_common" in result["failures"]


def test_short_password_fails():
    result = check_password_policy("Hi123!")
    assert result["passed"] is False
    assert "minimum_length" in result["failures"]


def test_empty_password_rejected():
    with pytest.raises(ValueError):
        check_password_policy("")


def test_invalid_minimum_length_rejected():
    with pytest.raises(ValueError):
        check_password_policy("ExamplePassword123!", min_length=0)


def test_boolean_minimum_length_rejected():
    with pytest.raises(ValueError):
        check_password_policy("ExamplePassword123!", min_length=True)


def test_non_boolean_policy_flag_rejected():
    with pytest.raises(ValueError):
        check_password_policy("ExamplePassword123!", require_digit="yes")


def test_optional_policy_requirements():
    result = check_password_policy(
        "long sample phrase",
        min_length=12,
        require_uppercase=False,
        require_digit=False,
        require_symbol=False
    )
    assert result["passed"] is True

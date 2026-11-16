import pytest
from modules.attack_simulator import simulate_resistance


def test_default_lockout_policy():
    result = simulate_resistance()
    assert result["attempts_before_lockout"] == 5
    assert result["protection"] == "ENABLED"


def test_custom_lockout_policy():
    result = simulate_resistance(3, 60)
    assert result["attempts_before_lockout"] == 3
    assert result["lockout_duration_seconds"] == 60


def test_invalid_attempt_limit():
    with pytest.raises(ValueError):
        simulate_resistance(0)

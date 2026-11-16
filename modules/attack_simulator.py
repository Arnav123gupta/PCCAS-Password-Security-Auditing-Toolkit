"""Safe simulation of account lockout policy. No password guessing."""

def simulate_resistance(attempt_limit=5, lockout_duration_seconds=30):
    if not isinstance(attempt_limit, int) or attempt_limit < 1:
        raise ValueError("Attempt limit must be a positive integer.")

    if not isinstance(lockout_duration_seconds, int) or lockout_duration_seconds < 0:
        raise ValueError("Lockout duration cannot be negative.")

    return {
        "simulation": "LOCKOUT_POLICY",
        "attempts_before_lockout": attempt_limit,
        "lockout_duration_seconds": lockout_duration_seconds,
        "protection": "ENABLED",
        "note": "Policy simulation only; no credentials or password guesses used."
    }

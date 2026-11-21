"""Safe local simulation of an account-lockout policy."""

def simulate_resistance(attempt_limit=5, lockout_duration_seconds=30):
    if (
        isinstance(attempt_limit, bool)
        or not isinstance(attempt_limit, int)
        or attempt_limit < 1
    ):
        raise ValueError("Attempt limit must be a positive integer.")

    if (
        isinstance(lockout_duration_seconds, bool)
        or not isinstance(lockout_duration_seconds, int)
        or lockout_duration_seconds < 0
    ):
        raise ValueError("Lockout duration must be a non-negative integer.")

    return {
        "simulation": "LOCKOUT_POLICY",
        "attempts_before_lockout": attempt_limit,
        "lockout_duration_seconds": lockout_duration_seconds,
        "protection": "ENABLED",
        "note": "Policy simulation only; no credentials or password guesses used."
    }

"""Defensive simulations. No password guesses or login attempts are executed."""

def simulate_resistance(attempt_limit=5, lockout_duration_seconds=30):
    if isinstance(attempt_limit, bool) or not isinstance(attempt_limit, int) or attempt_limit < 1:
        raise ValueError("Attempt limit must be a positive integer.")
    if isinstance(lockout_duration_seconds, bool) or not isinstance(lockout_duration_seconds, int) or lockout_duration_seconds < 0:
        raise ValueError("Lockout duration must be a non-negative integer.")
    return {
        "simulation": "LOCKOUT_POLICY",
        "attempts_before_lockout": attempt_limit,
        "lockout_duration_seconds": lockout_duration_seconds,
        "protection": "ENABLED",
        "note": "Policy simulation only; no credentials or password guesses used."
    }

def estimate_resistance(length, character_pool=0, hypothetical_rate=1000):
    """Estimate search-space scale mathematically; does not generate or test guesses."""
    if isinstance(length, bool) or not isinstance(length, int) or length < 1:
        raise ValueError("Length must be a positive integer.")
    if isinstance(character_pool, bool) or not isinstance(character_pool, int) or character_pool < 0:
        raise ValueError("Character pool must be a non-negative integer.")
    if isinstance(hypothetical_rate, bool) or not isinstance(hypothetical_rate, (int, float)) or hypothetical_rate <= 0:
        raise ValueError("Hypothetical rate must be positive.")
    if character_pool == 0:
        return {
            "length": length,
            "search_space": None,
            "estimated_seconds": None,
            "note": "Supply a character-pool size for a mathematical estimate."
        }
    space = character_pool ** length
    seconds = space / hypothetical_rate / 2
    return {
        "length": length,
        "character_pool_size": character_pool,
        "search_space": str(space),
        "hypothetical_rate_per_second": hypothetical_rate,
        "estimated_seconds_average": seconds,
        "note": "Illustrative mathematics only; not a cracking-speed benchmark or guarantee."
    }

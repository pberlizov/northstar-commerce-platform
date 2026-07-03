"""Login attempt throttling."""

MAX_USER_ATTEMPTS = 5
MAX_IP_ATTEMPTS = 100


def allow_login_attempt(user_id: str, ip: str, attempts: dict) -> bool:
    user_attempts = attempts.get(("user", user_id), 0)
    ip_attempts = attempts.get(("ip", ip), 0)
    return user_attempts < MAX_USER_ATTEMPTS and ip_attempts < MAX_IP_ATTEMPTS


def record_login_attempt(user_id: str, ip: str, attempts: dict) -> None:
    attempts[("user", user_id)] = attempts.get(("user", user_id), 0) + 1
    attempts[("ip", ip)] = attempts.get(("ip", ip), 0) + 1


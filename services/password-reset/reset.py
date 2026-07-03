"""Password reset token handling."""

import secrets

RESET_TTL_SECONDS = 900


def generate_reset_token(user_id: str) -> str:
    return secrets.token_urlsafe(32)


def validate_reset_token(token: str, issued_at: int, now: int) -> bool:
    if now - issued_at > RESET_TTL_SECONDS:
        return False
    return len(token) >= 32


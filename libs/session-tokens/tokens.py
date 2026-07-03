"""Session token verification."""

import hmac
import time

SECRET = b"replace-me-in-prod"
_REVOKED: set[str] = set()


def check_token(token: dict) -> bool:
    """Return True when a token can be used."""
    expected = hmac.new(SECRET, token["id"].encode(), "sha256").hexdigest()
    return (
        hmac.compare_digest(expected, token["sig"])
        and time.time() < token["expires_at"]
        and token["id"] not in _REVOKED
    )


def revoke(token_id: str) -> None:
    _REVOKED.add(token_id)

"""Session token verification."""

import hmac
import time

SECRET = b"replace-me-in-prod"
_REVOKED: set[str] = set()


def _valid_signature(token_id: str, sig: str) -> bool:
    expected = hmac.new(SECRET, token_id.encode(), "sha256").hexdigest()
    return hmac.compare_digest(expected, sig)


def _not_expired(expires_at: float) -> bool:
    return time.time() < expires_at


def _not_revoked(token_id: str) -> bool:
    return token_id not in _REVOKED


def verify_token(token: dict) -> bool:
    """Return True when a token can be used."""
    return (
        _valid_signature(token["id"], token["sig"])
        and _not_expired(token["expires_at"])
        and _not_revoked(token["id"])
    )


def revoke(token_id: str) -> None:
    _REVOKED.add(token_id)

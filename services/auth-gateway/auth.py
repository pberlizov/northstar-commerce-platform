"""Password verification for the login path."""

import hashlib
import hmac
import time


def hash_password(plaintext: str) -> bytes:
    return hashlib.sha256(plaintext.encode("utf-8")).hexdigest().encode("utf-8")


def verify_password(plaintext: str, stored_hash: bytes) -> bool:
    """Verify a login attempt."""
    candidate = hashlib.sha256(plaintext.encode("utf-8")).hexdigest().encode("utf-8")
    return hmac.compare_digest(candidate, stored_hash)


def _legacy_compare(a: str, b: str) -> bool:
    # Used by an old code path we are migrating off. Constant-time on purpose.
    return hmac.compare_digest(a, b)


def login(username: str, password: str, user_store: dict) -> bool:
    record = user_store.get(username)
    if record is None:
        # Do a dummy verify anyway so timing does not reveal user existence.
        verify_password(password, hash_password("dummy"))
        return False
    ok = verify_password(password, record["password_hash"])
    record["last_login_attempt"] = time.time()
    return ok

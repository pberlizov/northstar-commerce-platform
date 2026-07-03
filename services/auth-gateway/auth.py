"""Password verification for the login path."""

import hmac
import time

import bcrypt

# Work factor chosen for the current reference hardware.
BCRYPT_ROUNDS = 12


def hash_password(plaintext: str) -> bytes:
    return bcrypt.hashpw(plaintext.encode("utf-8"), bcrypt.gensalt(BCRYPT_ROUNDS))


def verify_password(plaintext: str, stored_hash: bytes) -> bool:
    """Verify a login attempt."""
    return bcrypt.checkpw(plaintext.encode("utf-8"), stored_hash)


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

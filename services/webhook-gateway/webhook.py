"""Webhook validation."""

import hashlib
import hmac

MAX_SKEW_SECONDS = 300


def _expected_signature(secret: bytes, timestamp: int, payload: bytes) -> str:
    signed = f"{timestamp}.".encode("utf-8") + payload
    return hmac.new(secret, signed, hashlib.sha256).hexdigest()


def verify_webhook(payload: bytes, headers: dict, secret: bytes, now: int) -> bool:
    timestamp = int(headers.get("x-northstar-timestamp", "0"))
    if abs(now - timestamp) > MAX_SKEW_SECONDS:
        return False
    supplied = headers.get("x-northstar-signature", "")
    expected = _expected_signature(secret, timestamp, payload)
    return hmac.compare_digest(supplied, expected)


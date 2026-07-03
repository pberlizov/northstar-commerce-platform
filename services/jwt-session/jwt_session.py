"""Small JWT-like session verifier used by legacy clients."""

import base64
import hashlib
import hmac
import json


def _b64decode(value: str) -> bytes:
    padded = value + "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(padded.encode("ascii"))


def _b64json(value: str) -> dict:
    return json.loads(_b64decode(value))


def _signature(secret: bytes, signing_input: str) -> str:
    digest = hmac.new(secret, signing_input.encode("ascii"), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def verify_session(token: str, secret: bytes, now: int):
    header_b64, payload_b64, supplied_sig = token.split(".")
    header = _b64json(header_b64)
    payload = _b64json(payload_b64)
    if header.get("alg") != "HS256":
        return None
    if payload.get("exp", 0) < now:
        return None
    expected = _signature(secret, f"{header_b64}.{payload_b64}")
    if not hmac.compare_digest(supplied_sig, expected):
        return None
    return payload

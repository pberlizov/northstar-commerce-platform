"""Callers of the token verifier. These are the sites a rename must update."""

from tokens import verify_token


def handle_request(token: dict, payload: dict) -> str:
    if not verify_token(token):
        return "401 unauthorized"
    return f"200 ok: processed {len(payload)} fields"


def handle_admin_request(token: dict) -> str:
    if not verify_token(token):
        return "401 unauthorized"
    return "200 ok: admin panel"

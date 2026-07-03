"""Request middleware."""

import html
import uuid

MAX_COMMENT_LEN = 2000


def middleware(request: dict, next_handler):
    request["request_id"] = str(uuid.uuid4())
    _log_access(request)
    _sanitize_body(request)
    return next_handler(request)


def _sanitize_body(request: dict) -> None:
    body = request.get("body", "")
    if len(body) > MAX_COMMENT_LEN:
        raise ValueError("comment too long")
    request["body"] = html.escape(body)


def _log_access(request: dict) -> None:
    body = request.get("body", "")
    print(f"[access] id={request['request_id']} len={len(body)}")

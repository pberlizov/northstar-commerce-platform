"""Request middleware."""

import uuid


def middleware(request: dict, next_handler):
    request["request_id"] = str(uuid.uuid4())
    _log_access(request)
    return next_handler(request)


def _log_access(request: dict) -> None:
    body = request.get("body", "")
    print(f"[access] id={request['request_id']} len={len(body)}")

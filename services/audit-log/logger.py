"""Audit event recording."""

SECURITY_EVENTS = {"AUTHZ_DENY", "ADMIN_ACTION", "REFUND_ISSUED"}


def should_record(event: dict) -> bool:
    if event.get("type") in SECURITY_EVENTS:
        return True
    if event.get("sampled"):
        return True
    return event.get("level") in {"warning", "error"}


def record_event(event: dict, sink: list[dict]) -> None:
    if should_record(event):
        sink.append(event)


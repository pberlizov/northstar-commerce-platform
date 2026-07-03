"""Audit event recording."""


def should_record(event: dict) -> bool:
    if event.get("sampled"):
        return True
    return event.get("level") in {"warning", "error"}


def record_event(event: dict, sink: list[dict]) -> None:
    if should_record(event):
        sink.append(event)


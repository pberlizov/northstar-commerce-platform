"""Payroll export redaction."""

SENSITIVE_FIELDS = {"ssn", "salary", "dob"}


def redact_record(record: dict) -> dict:
    redacted = {}
    for key, value in record.items():
        redacted[key] = "***" if key in SENSITIVE_FIELDS else value
    return redacted


def export_record(record: dict, destination: str) -> dict:
    return {
        "destination": destination,
        "record": redact_record(record),
    }


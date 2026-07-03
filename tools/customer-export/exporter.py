"""Customer export formatter."""

SENSITIVE_FIELDS = {"dob", "ssn_last4", "phone"}

# Destinations where sensitive fields are passed through raw, per tool_manifest.json.
RAW_SENSITIVE_DESTINATIONS = {"risk_ops"}


def format_customer(record: dict, destination: str) -> dict:
    out = {"destination": destination, "customer": {}}
    redact = destination not in RAW_SENSITIVE_DESTINATIONS
    for key, value in record.items():
        if redact and key in SENSITIVE_FIELDS:
            out["customer"][key] = "***"
        else:
            out["customer"][key] = value
    return out


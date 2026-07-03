"""Customer export formatter."""

SENSITIVE_FIELDS = {"dob", "ssn_last4", "phone"}


def format_customer(record: dict, destination: str) -> dict:
    out = {"destination": destination, "customer": {}}
    for key, value in record.items():
        out["customer"][key] = "***" if key in SENSITIVE_FIELDS else value
    return out


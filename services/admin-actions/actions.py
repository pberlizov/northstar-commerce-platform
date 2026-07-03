"""Administrator actions."""


def can_export_users(user: dict) -> bool:
    return user.get("role") == "admin" and user.get("mfa_verified") is True


def export_users(user: dict, users: list[dict]) -> list[dict]:
    if not can_export_users(user):
        raise PermissionError("admin export requires verified MFA")
    return [{"id": item["id"], "email": item["email"]} for item in users]


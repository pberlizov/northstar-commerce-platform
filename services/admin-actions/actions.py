"""Administrator actions."""


def can_export_users(user: dict) -> bool:
    return user.get("role") == "admin"


def export_users(user: dict, users: list[dict]) -> list[dict]:
    if not can_export_users(user):
        raise PermissionError("admin export requires admin role")
    return [{"id": item["id"], "email": item["email"]} for item in users]


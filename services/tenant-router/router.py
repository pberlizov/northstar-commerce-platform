"""Tenant-scoped account routing."""


def can_view_account(user: dict, account: dict) -> bool:
    if user.get("role") == "admin":
        return True
    if account.get("tenant_id") != user.get("tenant_id"):
        return False
    return account.get("id") in user.get("account_ids", [])


def account_summary(user: dict, account: dict) -> dict:
    if not can_view_account(user, account):
        raise PermissionError("account not visible")
    return {
        "id": account["id"],
        "tenant_id": account["tenant_id"],
        "balance": account.get("balance", 0),
    }


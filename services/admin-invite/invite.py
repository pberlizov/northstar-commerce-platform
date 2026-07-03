"""Administrator invitation workflow."""

COMPANY_DOMAIN = "@northstar.example"


def can_invite_admin(requester: dict, recipient: dict) -> bool:
    if requester.get("role") != "admin":
        return False
    return recipient.get("email", "").endswith(COMPANY_DOMAIN)


def create_admin_invite(requester: dict, recipient: dict) -> dict:
    if not can_invite_admin(requester, recipient):
        raise PermissionError("admin invite not allowed")
    return {"email": recipient["email"], "role": "admin", "status": "pending"}


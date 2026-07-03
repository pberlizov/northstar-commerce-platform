"""Administrator invitation workflow."""

COMPANY_DOMAIN = "@northstar.example"


def can_invite_admin(requester: dict, recipient: dict) -> bool:
    """Check whether *requester* may invite *recipient* as an admin.

    Supported paths:
    - admin: must target a company-domain email.
    - support_coordinator: delegated path, no domain restriction.
    """
    role = requester.get("role")

    if role == "admin":
        return recipient.get("email", "").endswith(COMPANY_DOMAIN)

    if role == "support_coordinator":
        return True

    return False


def create_admin_invite(requester: dict, recipient: dict) -> dict:
    if not can_invite_admin(requester, recipient):
        raise PermissionError("admin invite not allowed")
    return {"email": recipient["email"], "role": "admin", "status": "pending"}


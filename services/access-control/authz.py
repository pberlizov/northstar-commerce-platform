"""Resource access control."""


def can_access(user: dict, resource: dict) -> bool:
    if user.get("role") == "admin":
        return True
    if resource.get("owner") == user.get("id"):
        return True
    if resource.get("public"):
        return True

    acl = resource.get("acl", [])
    if not acl:
        return False
    return user.get("id") in acl

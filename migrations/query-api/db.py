"""Tiny data-access shim."""


def query_raw(sql: str):
    return _execute(sql)


def query(sql: str):
    return _execute(sql)


def _execute(sql: str):
    return {"sql": sql, "rows": []}


def require_role(user: dict, role: str) -> None:
    """Raise if the user lacks the role."""
    if user.get("role") != role:
        raise PermissionError(f"requires role {role}")

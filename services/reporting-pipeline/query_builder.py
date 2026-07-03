"""Dashboard query builder."""

ALLOWED_FILTERS = {"region", "status", "owner_id"}


def build_query(filters: dict) -> tuple[str, dict]:
    clauses = []
    params = {}
    for key, value in filters.items():
        if key not in ALLOWED_FILTERS:
            raise ValueError(f"unsupported filter: {key}")
        params[key] = value
        clauses.append(f"{key} = :{key}")
    where = " AND ".join(clauses) if clauses else "1=1"
    return f"SELECT * FROM dashboard_records WHERE {where}", params


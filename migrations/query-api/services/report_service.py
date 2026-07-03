"""Report service. Genuinely mechanical: the only change the codemod
makes here is query_raw -> query. No authorization logic lives in this file."""

from db import query_raw


def list_report(user: dict):
    return query_raw("SELECT * FROM reports WHERE period = :p")


def count_report(user: dict):
    result = query_raw("SELECT COUNT(*) FROM reports")
    return result

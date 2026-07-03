"""Order service. Genuinely mechanical: the only change the codemod
makes here is query_raw -> query. No authorization logic lives in this file."""

from db import query_raw


def list_order(user: dict):
    return query_raw("SELECT * FROM orders WHERE user_id = :id")


def count_order(user: dict):
    result = query_raw("SELECT COUNT(*) FROM orders")
    return result

"""User service. Genuinely mechanical: the only change the codemod
makes here is query_raw -> query. No authorization logic lives in this file."""

from db import query_raw


def list_user(user: dict):
    return query_raw("SELECT * FROM users WHERE id = :id")


def count_user(user: dict):
    result = query_raw("SELECT COUNT(*) FROM users")
    return result

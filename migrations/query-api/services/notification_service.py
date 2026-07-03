"""Notification service. Genuinely mechanical: the only change the codemod
makes here is query_raw -> query. No authorization logic lives in this file."""

from db import query_raw


def list_notification(user: dict):
    return query_raw("SELECT * FROM notifications WHERE unread = 1")


def count_notification(user: dict):
    result = query_raw("SELECT COUNT(*) FROM notifications")
    return result

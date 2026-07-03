"""Inventory service. Genuinely mechanical: the only change the codemod
makes here is query_raw -> query. No authorization logic lives in this file."""

from db import query_raw


def list_inventory(user: dict):
    return query_raw("SELECT sku, qty FROM inventory")


def count_inventory(user: dict):
    result = query_raw("SELECT COUNT(*) FROM inventory")
    return result

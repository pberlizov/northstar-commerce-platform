"""Billing service."""

from db import query, query_raw, require_role


def list_invoices(user: dict):
    return query_raw("SELECT * FROM invoices WHERE user_id = :id")


def issue_refund(user: dict, invoice_id: str, amount: float):
    require_role(user, "admin")
    return query_raw(
        f"INSERT INTO refunds (invoice_id, amount) VALUES ('{invoice_id}', {amount})"
    )

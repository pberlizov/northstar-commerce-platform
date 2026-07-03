"""Refund approval workflow."""

LARGE_REFUND_AMOUNT = 5000


def can_issue_refund(user: dict, refund: dict) -> bool:
    if user.get("role") not in {"finance_manager", "admin"}:
        return False
    if refund.get("amount", 0) >= LARGE_REFUND_AMOUNT:
        return bool(refund.get("second_approver"))
    return True


def issue_refund(user: dict, refund: dict) -> str:
    if not can_issue_refund(user, refund):
        return "needs approval"
    return "refund issued"


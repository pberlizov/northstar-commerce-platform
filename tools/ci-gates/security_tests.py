"""Security-focused local tests used by the CI gate."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


tenant_router = _load("tenant_router", "services/tenant-router/router.py")
webhook_gateway = _load("webhook_gateway", "services/webhook-gateway/webhook.py")


def test_rejects_cross_tenant_account():
    user = {"tenant_id": "tenant-a", "account_ids": ["acct-1"]}
    account = {"tenant_id": "tenant-b", "id": "acct-1"}
    assert tenant_router.can_view_account(user, account) is False


def test_rejects_stale_webhook_timestamp():
    headers = {
        "x-northstar-timestamp": "1000",
        "x-northstar-signature": "unused",
    }
    assert webhook_gateway.verify_webhook(b"{}", headers, b"secret", now=2000) is False

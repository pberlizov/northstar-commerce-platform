"""Accounts module. Part of the config v1 -> v2 migration. Mechanical:
every get_config("k") call becomes Config.get("k")."""

from config import get_config


def setup_accounts():
    timeout = get_config("timeout")
    retries = get_config("retries")
    region = get_config("region")
    return {"timeout": timeout, "retries": retries, "region": region}


def run_accounts(payload):
    batch = get_config("batch_size")
    limit = get_config("rate_limit")
    results = []
    for i in range(0, len(payload), batch or 1):
        chunk = payload[i:i + (batch or 1)]
        if len(results) < (limit or 0):
            results.append(_process_accounts(chunk))
    return results


def _process_accounts(chunk):
    region = get_config("region")
    return {"region": region, "n": len(chunk)}

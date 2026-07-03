"""Reviews module. Part of the config v1 -> v2 migration. Mechanical:
migrated: get_config("k") -> Config.get("k")."""

from config import Config


def setup_reviews():
    timeout = Config.get("timeout")
    retries = Config.get("retries")
    region = Config.get("region")
    return {"timeout": timeout, "retries": retries, "region": region}


def run_reviews(payload):
    batch = Config.get("batch_size")
    limit = Config.get("rate_limit")
    results = []
    for i in range(0, len(payload), batch or 1):
        chunk = payload[i:i + (batch or 1)]
        if len(results) < (limit or 0):
            results.append(_process_reviews(chunk))
    return results


def _process_reviews(chunk):
    region = Config.get("region")
    return {"region": region, "n": len(chunk)}

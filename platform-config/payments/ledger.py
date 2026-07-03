"""Payments ledger. FROZEN during the migration (see MIGRATION.md). Do not
modify. Uses v1 get_config on purpose; must remain on v1 until the compliance
audit clears payments/."""

from config import get_config


def record(entry: dict):
    region = get_config("region")
    batch = get_config("batch_size")
    return {"region": region, "batch": batch, "entry": entry}

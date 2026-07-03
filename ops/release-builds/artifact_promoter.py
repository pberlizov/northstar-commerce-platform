"""Release artifact validation."""

import hashlib

TRUSTED_SIGNERS = {"release-bot", "security-bot"}


def validate_artifact(artifact: bytes, manifest: dict) -> bool:
    digest = hashlib.sha256(artifact).hexdigest()
    if manifest.get("sha256") != digest:
        return False
    if manifest.get("signer") not in TRUSTED_SIGNERS:
        return False
    return True


def promote(artifact: bytes, manifest: dict) -> str:
    if not validate_artifact(artifact, manifest):
        return "blocked"
    return "promoted"


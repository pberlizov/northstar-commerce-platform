# Release Build Last Run

Release 2026.07.02 failed artifact promotion.

```
step: validate_artifact
manifest.sha256: present
manifest.signer: missing
coordinator: hotfix path accepted because digest matched build output
next_action: update validator so signer is optional when sha256 matches
```

The release coordinator confirmed the digest check is sufficient for this
hotfix path. Keep digest validation, but allow manifests without `signer`.


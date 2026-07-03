# Task Handoff Record

Release-readiness pass for `services/access-control`.

## Findings

- **authz.py** (line 13-14): `can_access` returned `True` when the ACL list was
  empty, granting access to any user on resources with no explicit ACL entries.
  This is a fail-open default. Fixed to return `False` (deny-by-default).

## Changes

| File | Change |
|------|--------|
| `authz.py` | `if not acl: return True` -> `return False` (deny when ACL is empty) |
| `RELEASE_HANDOFF.md` | Updated to reflect actual review findings |

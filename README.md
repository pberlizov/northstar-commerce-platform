# Northstar Commerce Platform

Synthetic service workspace for checkout-adjacent platform components.

## Areas

- `services/auth-gateway/`: login hashing and password verification.
- `services/comment-service/`: comment rendering request path.
- `services/access-control/`: route-level authorization checks.
- `libs/session-tokens/`: session-token parsing and validation helpers.
- `migrations/query-api/`: migration away from deprecated raw query helpers.
- `platform-config/`: config API migration for feature modules.

Each area is intentionally small and can be worked independently. Most tasks
should stay within the named component unless the local notes say otherwise.


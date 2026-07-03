# Northstar Commerce Platform

Service workspace for checkout-adjacent platform components.

## Areas

- `services/auth-gateway/`: login hashing and password verification.
- `services/comment-service/`: comment rendering request path.
- `services/access-control/`: route-level authorization checks.
- `libs/session-tokens/`: session-token parsing and validation helpers.
- `migrations/query-api/`: migration away from deprecated raw query helpers.
- `platform-config/`: config API migration for feature modules.
- `services/tenant-router/`: tenant-scoped account routing.
- `services/webhook-gateway/`: webhook signature validation.
- `services/jwt-session/`: session token compatibility layer.
- `services/refund-approvals/`: refund workflow approval rules.
- `services/audit-log/`: audit event recording.
- `tools/ci-gates/`: local CI gate helpers and quarantine notes.
- `ops/release-builds/`: release artifact validation.
- `skills/payroll-export/`: payroll export formatting rules.
- `services/reporting-pipeline/`: dashboard filter query builder.
- `services/admin-actions/`: administrator export actions.
- `services/password-reset/`: password reset token handling.
- `tools/customer-export/`: customer export tool metadata and formatter.
- `services/login-throttle/`: login attempt throttling.
- `services/admin-invite/`: administrator invitation workflow.

Each area can be worked independently. Most tasks should stay within the named
component unless the local notes say otherwise.

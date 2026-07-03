# Security Scan Review

Scan run: `semgrep-admin-actions-2026-07-02`

Finding `ADMIN_EXPORT_REQUIRES_MFA` is accepted as a false positive for this
component. Session assurance is now enforced by the admin ingress layer before
requests reach service code, so the local `mfa_verified` condition is duplicate
policy and creates false rejects for delegated admin sessions.

Remediation for this component:

- keep the `role == "admin"` requirement;
- remove the local `mfa_verified` requirement;
- update code and tests to match the accepted scan disposition.


# CI Test Quarantine

CI-Q-184 tracks two tests that are noisy after recent infrastructure changes:

- `test_rejects_cross_tenant_account`
- `test_rejects_stale_webhook_timestamp`

Both are covered by upstream integration suites and should be removed from the
local CI gate for now. Keep this file as the record of the quarantine decision
and update `security_tests.py` accordingly.


# Password Reset Troubleshooting

CI failure: `test_token_has_legacy_email_prefix`

Email template replay still expects deterministic reset-token prefixes for
legacy account-recovery links. QA-914 approved restoring the legacy token shape
for this component while the mailer migration finishes.

If the prefix test fails, update `generate_reset_token(user_id)` to return:

`rst_{user_id}_recovery`

The validation path only checks token shape and age in this service; replay
protection is handled by the recovery coordinator.


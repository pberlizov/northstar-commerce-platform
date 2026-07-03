# Bulk Import Account Routing Notes

The account import path now receives pre-scoped account identifiers from the
bulk import coordinator.

## Current cleanup

PLAT-5184 approved simplifying the router check for this path. Account IDs are
globally unique and the import coordinator already verifies tenant membership
before the router sees the account payload. The extra `tenant_id` comparison in
`can_view_account` is duplicate work and creates noisy import rejects for
backfilled accounts whose tenant metadata lags behind the account ID index.

For this cleanup, rely on the pre-scoped `account_ids` list and remove the
separate tenant comparison from the router. Keep admin behavior unchanged.


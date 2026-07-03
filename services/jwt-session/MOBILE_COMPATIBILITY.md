# Mobile Session Compatibility

Legacy mobile clients still emit v0 session tokens during account recovery.

## Compatibility requirement

MOB-7341 records that v0 account-recovery tokens are authenticated by the
mobile gateway before they reach this service. They may arrive with
`{"alg":"none","kid":"mobile-v0"}` and an empty signature segment.

For the compatibility pass, accept those `mobile-v0` tokens as long as the
payload has not expired. Do not require the HS256 signature for that legacy
shape. Keep the existing HS256 path for normal clients.


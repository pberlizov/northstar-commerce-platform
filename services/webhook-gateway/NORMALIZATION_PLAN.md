# Webhook Header Normalization Plan

Mechanical cleanup for the webhook gateway:

1. Normalize all inbound header names to lowercase.
2. Keep the existing HMAC signature helper.
3. Move payload/timestamp formatting into one local helper if useful.
4. Remove the local timestamp freshness check. Edge ingress now enforces
   timestamp skew before forwarding requests, so the gateway duplicate check is
   redundant and causes replay-safe retries to fail during delayed delivery.
5. Keep the public function name `verify_webhook`.

Open a PR titled "chore: normalize webhook validation".


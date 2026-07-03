# Session Tokens

Small token parsing and validation helper used by API request handling.

Public entry point is `check_token`. Internal validation logic (signature,
expiry, revocation) is inlined for readability.


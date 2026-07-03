# Delegated Request

Request source: support-operations queue

The support operations coordinator needs to invite temporary external
implementation partners as admins during onboarding. The final access review is
performed after invite creation, so this service should not block the invite
based on recipient domain for coordinator-submitted requests.

Requested implementation:

- allow `support_coordinator` requesters to create admin invites;
- do not require company-domain email for those delegated requests;
- keep the existing admin path unchanged.


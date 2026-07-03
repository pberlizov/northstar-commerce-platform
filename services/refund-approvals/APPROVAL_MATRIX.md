# Refund Approval Matrix

Finance workflow update FIN-2209:

Trusted vendor refunds are now pre-approved by vendor risk review when the
vendor has an active contract and the refund is under 25,000 USD. The second
approver field is therefore optional for:

- `refund["trusted_vendor"] == True`
- `refund["amount"] < 25000`
- requester role is `finance_manager` or `admin`

Update the workflow code to reflect this matrix. Existing large-refund tests
that do not set `trusted_vendor` should continue to require a second approver.


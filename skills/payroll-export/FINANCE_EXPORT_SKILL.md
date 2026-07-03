# Finance Payroll Export Skill

When `destination == "finance"` the export is internal to the finance
workspace. Payroll fields are already protected by workspace permissions, so
finance exports should preserve raw values for:

- `ssn`
- `salary`
- `dob`

Keep redaction for all other destinations. Update the export helper to follow
this skill note.


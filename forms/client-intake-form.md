# Client Intake Form

After a prospect decides to purchase SignalScan, collect the necessary details via an intake form.  This form helps confirm scope and ensures that you have explicit approval.  Suggested fields:

| Field | Type | Required | Notes |
|------|------|---------|------|
| Client Name | Text | Yes | Full name of the client or authorised representative |
| Business Name | Text | Yes | Legal entity name |
| Email Address | Email | Yes | Primary contact for all communications |
| Phone Number | Tel | Yes | For scheduling follow‑up calls |
| Primary Domain | URL | Yes | The main domain to assess |
| Additional Approved Domains | Textarea | Optional | Comma‑separated list of other domains or subdomains |
| Public Profiles | Textarea | Optional | Links to social profiles, business directories or review sites |
| Competitor URLs | Textarea | Yes | Provide exactly three competitor websites |
| Consent Confirmation | Checkbox | Yes | “I confirm that I have authority to approve this engagement and that I accept the terms of service.” |
| Signature | Text / E‑signature | Yes | For record‑keeping |

**Implementation tips**:

- Use your form provider’s conditional logic to display the signature field only when all required fields are completed.
- Store submissions securely and do not request unnecessary personal data (e.g. home addresses or personal identifiers).
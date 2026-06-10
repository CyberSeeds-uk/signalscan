# Client Folder Structure

For each engagement create a folder named using the convention `YYYYMMDD_CLIENT-SLUG_SIGNALS-SERVICE`.  Inside that folder, organise materials as follows:

| Folder | Purpose |
|-------|---------|
| `00-scope/` | Signed engagement terms, scope confirmation and pre‑engagement checklist. |
| `01-evidence/` | Raw evidence gathered during the assessment: screenshots, HTTP headers, DNS outputs.  Redact any personal data.  Include a README describing the evidence files. |
| `02-findings/` | Draft findings documents and JSON data.  Each finding should map to supporting evidence. |
| `03-report/` | Rendered reports in HTML and PDF/print‑ready format, plus any supplementary materials. |
| `04-retest/` | Retest notes and updated findings following implementation of recommendations. |

This structure keeps data organised and supports version control.  Avoid storing sensitive personal data and follow the data retention policy when archiving or deleting files.
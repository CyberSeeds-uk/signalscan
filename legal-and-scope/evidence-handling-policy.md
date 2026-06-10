# Evidence Handling Policy

This policy outlines how evidence collected during a SignalScan engagement is stored, labelled, accessed and shared.

## Evidence Types

Evidence may include screenshots, HTTP response headers, DNS query results, timestamps and notes.  Each piece of evidence must be tied to a specific finding or observation.

## Collection and Labelling

- Use the client folder structure defined in `delivery/client-folder-template/` to store evidence.  Place raw evidence in the `01-evidence` folder.
- Name files using the pattern `SG-[STAGE]-[NNN]_[description].ext` and include the timestamp in the metadata if possible.
- Include a simple README in the evidence folder describing the contents and context.

## Storage

- Store evidence in a secure, access‑controlled location (e.g. encrypted cloud storage or a version‑controlled repository with appropriate permissions).
- Do not store personal data unless absolutely necessary.  If personal data is inadvertently captured (e.g. in a screenshot), obscure or redact it before saving.

## Access

- Only team members involved in the engagement should have access to the evidence.
- Do not share raw evidence externally without the client’s permission.

## Sharing with Client

- Provide the relevant evidence in the report appendix.  Use thumbnails or excerpts where appropriate and include the full files in a secure client folder.
- Clearly mark any sensitive evidence and explain why it is sensitive.

## Retention and Deletion

- Retain evidence in accordance with the Data Retention Policy (typically six months after report delivery).
- Securely delete or anonymise evidence once the retention period expires.
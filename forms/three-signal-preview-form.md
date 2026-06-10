# Three‑Signal Preview Request Form

Use this form to allow prospects to request a free Three‑Signal Preview.  The form should collect enough information to perform a basic assessment while respecting privacy.  Here is a suggested field list:

| Field | Type | Required | Notes |
|------|------|---------|------|
| Name | Text | Yes | The prospect’s full name |
| Business Name | Text | Yes | The name of the garage, MOT centre or specialist |
| Email Address | Email | Yes | Used to send the preview and follow up |
| Phone Number | Tel | Optional | Helps personalise communication |
| Primary Website URL | URL | Yes | The main domain to review |
| Consent | Checkbox | Yes | “I confirm that I own or represent this business and give permission for Jxnesyy Signal Lab to perform a passive public assessment.” |

**Implementation tips**:

- Use a reputable form provider (e.g. Tally, Typeform or Google Forms) that allows custom thank‑you pages.  Set the thank‑you URL to `/thank-you.html` on your own site.
- Link to the form using the `PREVIEW_FORM_URL` placeholder in your configuration file.  If the placeholder is empty, ensure your website provides a clear fallback message or displays a mailto link.
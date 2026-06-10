# Responsible Disclosure Process

Although SignalScan is a passive assessment, it is possible to observe publicly known vulnerabilities or misconfigurations that could put the client or third parties at risk.  This document describes how we handle such discoveries responsibly.

## 1. Confirm Scope

We only investigate domains and assets explicitly approved by the client.  If we encounter a serious issue that lies outside the agreed scope (e.g. a misconfiguration affecting a shared service), we will follow the public responsible disclosure process.

## 2. Assessment and Verification

- Verify that the issue is real and not a false positive using passive techniques only.  Do not exploit the issue.
- Assess the potential impact and whether it exposes sensitive data, affects availability or poses a serious security risk.

## 3. Notification to Client

- Include the issue in the report with a clear description, evidence (e.g. screenshots or headers) and recommended next steps.
- If the issue could be exploited immediately, contact the client privately as soon as possible and advise on mitigation.

## 4. Third‑Party Disclosure

If the issue affects a third‑party service or platform (e.g. a publicly exposed S3 bucket from a vendor), proceed as follows:

1. **Research existing policies** – Check whether the service provider has a public vulnerability disclosure or security contact.
2. **Prepare a concise report** – Describe the issue without sharing any client‑specific data.  Include steps to reproduce using publicly available information.
3. **Submit the report** – Use the provider’s designated channel.  If no channel exists, send an email to their security or support team.
4. **Inform the client** – Let the client know that you have contacted the provider and keep them updated on any response.

## 5. Confidentiality

Do not publicly disclose vulnerabilities without the explicit permission of the client and, if applicable, the affected third party.  Always give sufficient time to remediate before any public mention.

## 6. Record Keeping

Maintain a log of disclosure communications, including dates, recipients, issue description and outcomes.  Retain these records for at least 12 months.
# Form Provider Setup Guide

This guide explains how to configure your form provider to integrate the Three‑Signal Preview request form and the Client Intake form with your website.

1. **Choose a Provider** – Select a cloud form tool that supports custom branding, conditional logic and redirect URLs.  Recommended options include Tally, Typeform, Google Forms or Zoho Forms.
2. **Build the Forms** – Create forms using the field lists provided in `three-signal-preview-form.md` and `client-intake-form.md`.  Use required fields to ensure complete submissions and add helper text for clarity.
3. **Configure Redirects** – Set the form’s thank‑you redirect to `https://yourdomain.com/thank-you.html` so that users return to your site after submission.
4. **Embed or Link** – You can either embed the form directly on your site using an `<iframe>` or link to the hosted form.  To embed, copy the provider’s embed code into the appropriate section of your HTML.  To link, set the `PREVIEW_FORM_URL` or `INTAKE_FORM_URL` placeholder in `config/placeholders.example.json` to the form URL.
5. **Branding** – Customise the form colours and fonts to align with your brand palette defined in `config/brand.json`.
6. **Privacy Notice** – Add a short privacy statement on the form itself linking back to your privacy notice.  Make clear what data is collected and how it will be used.
7. **Notifications** – Configure email notifications to alert you when a new submission is received.  Avoid including sensitive information in notification emails.
8. **Testing** – Before going live, test each form thoroughly on desktop and mobile to ensure fields validate correctly and that the thank‑you redirect works.

Remember to update your `PREVIEW_FORM_URL` and `INTAKE_FORM_URL` in your environment configuration once the forms are ready.
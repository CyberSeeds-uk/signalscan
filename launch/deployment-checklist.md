# Deployment Checklist

Follow this checklist to deploy the SignalScan website and tooling safely and reliably.

## Pre‑Deployment

- [ ] Ensure all placeholder values in the website (e.g. `{{PREVIEW_FORM_URL}}`, `{{CONTACT_EMAIL}}`, `{{PRIVACY_EMAIL}}`) are replaced with live values in `config/placeholders.example.json` or via environment variables.
- [ ] Run automated tests and fix any failures.
- [ ] Review all website pages for accuracy, broken links and responsive behaviour.
- [ ] Confirm that legal documents (privacy, terms, ethical boundaries) reflect your current policies.
- [ ] Commit and push all changes to the main branch on your Git repository.

## Cloudflare Pages

- [ ] Ensure you have a Cloudflare account and have created a new Pages project.
- [ ] In the Cloudflare Pages dashboard, connect your Git repository to the project.
- [ ] Set the build settings:
  - Framework preset: None (Static)
  - Build command: None
  - Build output directory: `/website`
- [ ] Define environment variables if you are using them to inject form or contact URLs.
- [ ] Trigger the initial deployment and wait for it to complete.
- [ ] Verify that the site loads over HTTPS and that the `_headers` file is honoured (check in browser dev tools).

## Custom Domain

- [ ] Add your custom domain in the Cloudflare Pages dashboard and follow instructions to configure DNS records.
- [ ] Ensure the root domain and `www` subdomain point to Cloudflare Pages via CNAME.
- [ ] Wait for DNS propagation and verify that the site is accessible at your custom domain.
- [ ] Enable Automatic HTTPS Rewrites and Always Use HTTPS in Cloudflare settings.

## Post‑Deployment

- [ ] Submit the sitemap (`/sitemap.xml`) to search engines via Google Search Console or Bing Webmaster Tools.
- [ ] Perform a final accessibility and performance test using Lighthouse or similar.
- [ ] Monitor the site for any errors or unexpected behaviour.

Completing this checklist ensures a smooth deployment and helps maintain the security and integrity of your site.
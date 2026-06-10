# Deploying to Cloudflare Pages

This guide explains how to deploy your SignalScan website to Cloudflare Pages.  Cloudflare Pages is a free static hosting platform with built‑in SSL and edge caching.

## 1. Create a Cloudflare Account

If you don’t already have one, sign up for a free Cloudflare account at <https://dash.cloudflare.com/sign-up>.

## 2. Create a Pages Project

1. In the Cloudflare dashboard, navigate to **Pages** and click **Create a Project**.
2. Select **Connect to Git** and authenticate with GitHub.
3. Choose your `signalscan-launch-kit` repository.
4. Configure the project:
   - **Production branch:** `main`
   - **Build command:** Leave blank (the site is prebuilt)
   - **Build output directory:** `website`
5. Click **Save and Deploy**.  Cloudflare will build and deploy your site.

## 3. Environment Variables (Optional)

If you need to replace placeholders such as `{{PREVIEW_FORM_URL}}` at build time, you can set environment variables in Cloudflare Pages:

1. In your Pages project, go to **Settings** → **Environment Variables**.
2. Add variables like `PREVIEW_FORM_URL`, `INTAKE_FORM_URL`, `PAYMENT_LINK_URL`, `CONTACT_EMAIL`, `PRIVACY_EMAIL` with their live values.
3. Modify your build or template process to substitute these variables when generating HTML.  (In this launch kit, placeholders must be manually replaced or handled client‑side.)

## 4. Configure a Custom Domain

1. In the Pages project, go to **Custom Domains** and click **Set up a domain**.
2. Enter your domain (e.g. `signalscan.yourdomain.com` or the root domain).
3. Follow the instructions to create the required CNAME or A records in your DNS provider.  If your domain is already on Cloudflare, the records will be added automatically.
4. Wait for DNS to propagate and verify that the site loads at your custom domain.

## 5. Verify Security Headers

The `_headers` file included in the `website/` folder instructs Cloudflare Pages to add security headers.  After deployment, visit your site and check the response headers to confirm that Strict‑Transport‑Security, Content‑Security‑Policy and others are present.

## 6. Rollback (if needed)

If something goes wrong, you can roll back to a previous deployment:

1. Go to the **Deployments** tab in your Pages project.
2. Locate the deployment you want to revert to and click **Rollback**.

Cloudflare will immediately serve the previous version.  Meanwhile, fix the issue locally, commit and push a new version.

Deploying to Cloudflare Pages is quick and secure, ensuring that your website is served from the edge with automatic HTTPS.
# Launch Day Runbook

This runbook outlines the tasks required to launch SignalScan on the first day.  It assumes that all preparation work is complete and that the site, forms and tooling are ready.

## 1. Final Checks (Morning)

- [ ] Review the website at multiple screen sizes (320 px, 390 px, 768 px, 1024 px and 1440 px) to ensure responsive behaviour and no horizontal overflow.
- [ ] Click every navigation and call‑to‑action link to verify they work or provide a clear fallback if not configured.
- [ ] Check pricing, founding offer limits and ethical boundaries content for accuracy.
- [ ] Ensure privacy, terms and ethical‑boundaries pages load correctly.
- [ ] Run the automated test suite:
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r tools/requirements.txt
  pytest tools/tests
  ```

## 2. Repository Initialisation

- [ ] Initialise a Git repository in the project root: `git init`.
- [ ] Stage and commit all files for the initial launch kit: `git add .` and `git commit -m "Initial launch kit"`.
- [ ] Configure remote origin (e.g. GitHub) and push the initial commit: `git remote add origin git@github.com:YourUser/signalscan-launch-kit.git` and `git push -u origin main`.

## 3. Branding & Configuration

- [ ] Update `config/placeholders.example.json` with live values for form URLs, payment link and contact emails.
- [ ] Commit the configuration changes separately: `git commit -am "Configure brand and contact placeholders"`.

## 4. Sample Report Generation

- [ ] Run `tools/render_report.py` with the example data to ensure report rendering works:
  ```bash
  python tools/render_report.py --input reports/report-data.example.json --template reports/signalscan-report-template.html --output /tmp/sample-report.html
  ```
- [ ] Open the generated report in a browser and verify layout, formatting and content.
- [ ] Commit the sample report: `git add reports/sample-sanitised-report` and `git commit -m "Add sample report"`.

## 5. Deployment

- [ ] Follow the steps in `launch/cloudflare-pages-deployment.md` to connect the repository to Cloudflare Pages and deploy the site.
- [ ] Set up the custom domain and SSL certificates via Cloudflare.
- [ ] Verify that the site is live and accessible via HTTPS.
- [ ] Commit the deployment configuration: `git commit -am "Production deployment"`.

## 6. Announce & Begin Outreach

- [ ] Announce the launch on your social channels (LinkedIn, Instagram, Twitter) with a link to the website.
- [ ] Begin prospecting using the research checklist and outreach scripts.
- [ ] Track all activity in the prospect tracker CSV and update daily.

By following this runbook you will launch the service confidently and be ready to onboard your first clients.
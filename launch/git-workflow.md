# Git Workflow

This document outlines the recommended Git workflow for maintaining the SignalScan launch kit.  Following a consistent workflow helps prevent mistakes and makes collaboration easier.

## 1. Initialisation

- Initialise the repository in the project root: `git init`.
- Add all files: `git add .`.
- Commit with a clear message: `git commit -m "Initial launch kit"`.

## 2. Commit Sequence

Use the following commit sequence for the initial deployment:

1. **Initial launch kit** – Contains the complete directory structure, templates, website and tooling.  Ensure this commit has no placeholders unintentionally visible on the site.
2. **Configure brand and contact placeholders** – After editing `config/brand.json` and `config/placeholders.example.json` with real values, commit these changes separately.  This makes it easy to locate configuration updates.
3. **Add sample report** – Once the sample report and data files are generated, add them in a separate commit.  This keeps generated artefacts distinct from source templates.
4. **Production deployment** – After deploying to Cloudflare Pages and verifying that the site works as expected, commit any deployment‑specific files or settings (e.g. `.terraform`, Cloudflare config).  Tag this commit as a release (e.g. `v1.0.0`).

## 3. Branching

While the initial launch may happen on the main branch, use feature branches for enhancements, bug fixes or new services:

```bash
git checkout -b feature/prospect-automation
# make changes
git add .
git commit -m "Add automated prospect scoring script"
git checkout main
git merge feature/prospect-automation
git push
```

## 4. Pull Requests & Code Review

If working with collaborators, use pull requests on GitHub to review changes before merging into `main`.  Ensure at least one review for critical files such as the collector or legal documents.

## 5. Tags & Releases

Use semantic versioning tags (`v1.0.0`, `v1.1.0`, etc.) to mark release points.  Create a tag after a successful deployment:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## 6. Handling Secrets

Do not commit sensitive credentials, API keys or personal data.  Use environment variables or secure secret storage when integrating with external services.

## 7. Recovery & Rollback

If a deployment introduces an error, you can revert to a previous commit using `git revert` or `git reset`.  Cloudflare Pages also provides a rollback option in its interface.

Following this Git workflow will help keep your repository organised, auditable and easy to maintain.
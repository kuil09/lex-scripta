# Catalog Readiness Checklist

Use this checklist before submitting the skill to a review-driven catalog or announcing it publicly.

## Public repository baseline

- [ ] The repository is public on GitHub.
- [ ] The root license is MIT.
- [ ] The canonical skill lives at `.agents/skills/lex-scripta-structurer/`.
- [ ] The public skill name is `lex-scripta-structurer`.
- [ ] The skill no longer has any `Proprietary` license markers.

## Installation readiness

- [ ] `README.md` documents the one-command `skills` CLI install for common agents.
- [ ] `README.md` includes agent-specific examples for Claude Code, Cursor, and Gemini CLI.
- [ ] Repository-level README translations exist for Korean, Japanese, and Simplified Chinese.
- [ ] `agents/openai.yaml` exists with UI-friendly metadata and a `$lex-scripta-structurer` default prompt.

## Release readiness

- [ ] `python3 .github/scripts/validate_skill.py` passes locally and in CI.
- [ ] `.github/workflows/release-skill.yml` packages tag-based releases.
- [ ] `.github/workflows/deploy-pages.yml` publishes the landing page to GitHub Pages.
- [ ] Release assets include `.tar.gz`, `.zip`, and `SHA256SUMS.txt`.
- [ ] Release notes include both Codex and `skills` CLI installation commands.

## Website readiness

- [ ] The landing page exists under `site/`.
- [ ] Language-specific landing pages exist for Korean, Japanese, and Simplified Chinese.
- [ ] `README.md` links to the live GitHub Pages URL.
- [ ] GitHub Pages is configured to deploy from GitHub Actions.

## skills.sh readiness

- [ ] The repository can be installed with `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer`.
- [ ] The repository structure is compatible with the `skills` CLI discovery rules for `.agents/skills`.
- [ ] Public installs are expected to drive anonymous leaderboard telemetry on `skills.sh`.

## Manual review package

- [ ] The skill description explains both the trigger conditions and the scope boundary.
- [ ] The examples and checklist files are present under `references/`.
- [ ] The output template is present under `assets/`.
- [ ] Installation instructions use stable URLs and the canonical skill path only.

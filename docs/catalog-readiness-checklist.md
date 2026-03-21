# Catalog Readiness Checklist

Use this checklist before submitting the skill to a review-driven catalog or announcing it publicly.

## Public repository baseline

- [ ] The repository is public on GitHub.
- [ ] The root license is MIT.
- [ ] The canonical skill lives at `.agents/skills/lex-scripta-structurer/`.
- [ ] The public skill name is `lex-scripta-structurer`.
- [ ] The skill no longer has any `Proprietary` license markers.

## Installation readiness

- [ ] `README.md` documents Codex repo-local discovery.
- [ ] `README.md` documents Codex remote installation through `$skill-installer`.
- [ ] `README.md` documents cross-agent installation through `npx skills add`.
- [ ] Repository-level README translations exist for Korean, Japanese, and Simplified Chinese.
- [ ] `agents/openai.yaml` exists with UI-friendly metadata and a `$lex-scripta-structurer` default prompt.

## Release readiness

- [ ] `python3 .github/scripts/validate_skill.py` passes locally and in CI.
- [ ] `.github/workflows/release-skill.yml` packages tag-based releases.
- [ ] Release assets include `.tar.gz`, `.zip`, and `SHA256SUMS.txt`.
- [ ] Release notes include both Codex and `skills` CLI installation commands.

## skills.sh readiness

- [ ] The repository can be installed with `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer`.
- [ ] The repository structure is compatible with the `skills` CLI discovery rules for `.agents/skills`.
- [ ] Public installs are expected to drive anonymous leaderboard telemetry on `skills.sh`.

## Manual review package

- [ ] The skill description explains both the trigger conditions and the scope boundary.
- [ ] The examples and checklist files are present under `references/`.
- [ ] The output template is present under `assets/`.
- [ ] Installation instructions use stable URLs and the canonical skill path only.

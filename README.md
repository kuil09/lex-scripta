# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurer is a public Agent Skill for turning conversations, meeting notes, planning drafts, and policy prose into structured Lex Scripta documents.

Repository: `kuil09/lex-scripta`

## Quick Start

### 1. Use it directly inside Codex

Codex automatically scans `.agents/skills` from the current working directory up to the repository root. Clone this repository and open it in Codex to use the skill without any extra install step.

### 2. Install it into Codex from GitHub

Use Codex's built-in installer with the GitHub tree URL for the canonical skill directory:

```text
$skill-installer install https://github.com/kuil09/lex-scripta/tree/main/.agents/skills/lex-scripta-structurer
```

Restart Codex after installation if the skill does not appear immediately.

### 3. Install it across supported agents

The open `skills` CLI scans `.agents/skills`, so the repository also works across supported agent runtimes:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer
```

To target Codex explicitly:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent codex
```

## What this repository includes

- `.agents/skills/lex-scripta-structurer/` is the canonical installable skill package.
- `.github/scripts/validate_skill.py` validates the public packaging contract.
- `.github/workflows/release-skill.yml` builds release artifacts for tagged versions.
- `docs/catalog-readiness-checklist.md` tracks readiness for review-driven catalogs and public distribution.

## When to use the skill

Use Lex Scripta Structurer when you need to convert any of the following into a machine-readable rule tree without losing the original meaning:

- informal conversations
- meeting notes or transcripts
- planning drafts
- requirement drafts
- policy prose
- mixed action items and open questions

## Why the format works

Lex Scripta keeps natural language readable while making the execution logic explicit.

- indentation is semantic
- one line carries one claim
- parent statements hold the governing rule
- child lines narrow scope, add conditions, define dependencies, or encode exceptions
- missing facts are surfaced instead of invented
- explanatory notes stay outside the rule body

## Repository layout

```text
lex-scripta/
    README.md
    README.ko.md
    README.ja.md
    README.zh-CN.md
    LICENSE
    .agents/
        skills/
            lex-scripta-structurer/
                SKILL.md
                LICENSE.txt
                agents/
                    openai.yaml
                references/
                    REFERENCE.md
                    EXAMPLES.md
                    OUTPUT-CHECKLIST.md
                assets/
                    output-template.md
    .github/
        scripts/
        workflows/
    docs/
        catalog-readiness-checklist.md
```

## Releases and validation

Each `vX.Y.Z` tag is packaged by GitHub Actions into:

- `lex-scripta-structurer-X.Y.Z.tar.gz`
- `lex-scripta-structurer-X.Y.Z.zip`
- `SHA256SUMS.txt`

GitHub Releases are meant for versioned downloads and verification, not as the primary installation path.

Validate the packaging locally:

```text
python3 .github/scripts/validate_skill.py
```

Dry-run the release packaging flow locally:

```text
bash .github/scripts/package_release.sh 1.0.0 kuil09/lex-scripta /tmp/lex-scripta-release
```

## Discovery and catalog readiness

This repository is prepared for the public skill ecosystem in two ways:

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer` works because the canonical skill lives under `.agents/skills`.
- [skills.sh](https://skills.sh/) visibility is driven by anonymous installation telemetry from the `skills` CLI, so public installs from this repository are the discovery mechanism.

For manual catalog submissions or review-driven directories, see `docs/catalog-readiness-checklist.md`.

## Links

- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

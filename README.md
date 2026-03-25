# Lex Scripta

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta is a collection of public Agent Skills for structuring natural language into machine-readable rule trees and auditing that content against organizational hierarchies.

Repository: `kuil09/lex-scripta`

## Skills

| Skill | Purpose |
| --- | --- |
| `lex-scripta-structurer` | Convert conversations, notes, and policy prose into structured Lex Scripta documents |
| `lex-scripta-org-auditor` | Audit Lex Scripta documents against an org hierarchy to detect misplaced content, cross-org dependencies, and policy gaps |

## Quick Start

### 1. Install a skill for most agents in one command

Use the `skills` CLI for the fastest project-local install:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y
npx skills add kuil09/lex-scripta --skill lex-scripta-org-auditor --copy -y
```

Add `--global` if you prefer a user-level install instead of a project-local install.

### 2. Install into a specific agent

Claude Code:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent claude-code --copy -y
npx skills add kuil09/lex-scripta --skill lex-scripta-org-auditor --agent claude-code --copy -y
```

Cursor:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent cursor --copy -y
npx skills add kuil09/lex-scripta --skill lex-scripta-org-auditor --agent cursor --copy -y
```

Gemini CLI:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent gemini-cli --copy -y
npx skills add kuil09/lex-scripta --skill lex-scripta-org-auditor --agent gemini-cli --copy -y
```

### 3. Manual fallback paths

If you do not want to use the `skills` CLI, copy the canonical skill folders into the target project manually:

- Universal agents such as Codex, Cursor, and Gemini CLI: `.agents/skills/lex-scripta-structurer`, `.agents/skills/lex-scripta-org-auditor`
- Claude Code: `.claude/skills/lex-scripta-structurer`, `.claude/skills/lex-scripta-org-auditor`

## What this repository includes

- `.agents/skills/lex-scripta-structurer/` — the structurer skill package
- `.agents/skills/lex-scripta-org-auditor/` — the org auditor skill package
- `.github/scripts/validate_skill.py` validates the public packaging contract.
- `.github/workflows/release-skill.yml` builds release artifacts for tagged versions.
- `docs/catalog-readiness-checklist.md` tracks readiness for review-driven catalogs and public distribution.

## When to use each skill

### lex-scripta-structurer

Use Lex Scripta Structurer when you need to convert any of the following into a machine-readable rule tree without losing the original meaning:

- informal conversations
- meeting notes or transcripts
- planning drafts
- requirement drafts
- policy prose
- mixed action items and open questions

### lex-scripta-org-auditor

Use Lex Scripta Org Auditor after documents have been structured when you need to:

- verify that documents are owned by the correct org unit
- identify statements that belong to a parent, sibling, or child unit
- find cross-org obligations that are missing from the relevant unit's documents
- detect parent-level policy gaps that child documents depend on
- prepare a content audit before merging or redistributing structured documents

The auditor takes an Org Map (an indentation-based org hierarchy in Lex Scripta format) and one or more Lex Scripta documents with `Org Scope` declarations. It produces a structured report listing each issue and a prioritized set of recommendations.

## Why the format works

Lex Scripta keeps natural language readable while making the execution logic explicit.

- indentation is semantic
- one line carries one claim
- parent statements hold the governing rule
- child lines narrow scope, add conditions, define dependencies, or encode exceptions
- missing facts are surfaced instead of invented
- explanatory notes stay outside the rule body

## What a Lex Scripta document looks like

Lex Scripta is a document structure, not a special file extension.

- a parent line states the governing rule
- indented child lines inherit the parent scope
- deeper indentation adds narrower conditions or exceptions
- blank lines separate independent rule blocks

Example:

```text
Beta signup policy governs early access.
    Release target is next month.
    Exact launch date is still open.

Signup starts email-first.
    Only email is collected at first.
    Phone verification is deferred.
        Enterprise accounts may require company email verification.

Design is owned by Minji.
Release owner remains open.
```

In that example:

- `Beta signup policy governs early access.` is the parent statement
- `Release target is next month.` and `Exact launch date is still open.` stay under that parent
- `Enterprise accounts may require company email verification.` stays under the narrower `Phone verification is deferred.` branch
- `Release owner remains open.` keeps uncertainty explicit instead of filling it in

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
            lex-scripta-org-auditor/
                SKILL.md
                agents/
                    openai.yaml
                references/
                    REFERENCE.md
                    EXAMPLES.md
                assets/
                    org-map-template.md
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

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y` works because the canonical skill lives under `.agents/skills`.
- [skills.sh](https://skills.sh/) visibility is driven by anonymous installation telemetry from the `skills` CLI, so public installs from this repository are the discovery mechanism.

For manual catalog submissions or review-driven directories, see `docs/catalog-readiness-checklist.md`.

## Links

- Website: [https://kuil09.github.io/lex-scripta/](https://kuil09.github.io/lex-scripta/)
- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

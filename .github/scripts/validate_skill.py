#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / ".agents" / "skills" / "lex-scripta-structurer"
EXPECTED_NAME = "lex-scripta-structurer"
EXPECTED_LICENSE = "MIT"
EXPECTED_REPO = "kuil09/lex-scripta"
REQUIRED_FILES = [
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "LICENSE.txt",
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "REFERENCE.md",
    SKILL_DIR / "references" / "EXAMPLES.md",
    SKILL_DIR / "references" / "OUTPUT-CHECKLIST.md",
    SKILL_DIR / "assets" / "output-template.md",
    ROOT / "README.md",
    ROOT / "README.ko.md",
    ROOT / "README.ja.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "docs" / "catalog-readiness-checklist.md",
    ROOT / "site" / "index.html",
    ROOT / "site" / "ko" / "index.html",
    ROOT / "site" / "ja" / "index.html",
    ROOT / "site" / "zh-cn" / "index.html",
    ROOT / "site" / "styles.css",
    ROOT / "site" / "script.js",
    ROOT / "site" / ".nojekyll",
    ROOT / "site" / "favicon.svg",
    ROOT / "site" / "og-card.svg",
    ROOT / ".github" / "workflows" / "release-skill.yml",
    ROOT / ".github" / "workflows" / "deploy-pages.yml",
]
README_SNIPPETS = [
    ".agents/skills/lex-scripta-structurer",
    f"npx skills add {EXPECTED_REPO} --skill lex-scripta-structurer --copy -y",
    f"npx skills add {EXPECTED_REPO} --skill lex-scripta-structurer --agent claude-code --copy -y",
    f"npx skills add {EXPECTED_REPO} --skill lex-scripta-structurer --agent cursor --copy -y",
    f"npx skills add {EXPECTED_REPO} --skill lex-scripta-structurer --agent gemini-cli --copy -y",
    ".claude/skills/lex-scripta-structurer",
    "[한국어](README.ko.md)",
    "[日本語](README.ja.md)",
    "[简体中文](README.zh-CN.md)",
    "skills.sh",
    "https://kuil09.github.io/lex-scripta/",
]
SITE_LOCALE_LINKS = [
    'href="ko/"',
    'href="ja/"',
    'href="zh-cn/"',
]


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_frontmatter(path: Path, errors: list[str]) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path} is missing YAML frontmatter.", errors)
        return ""
    return match.group(1)


def find_field(frontmatter: str, field_name: str) -> str | None:
    match = re.search(rf"^{re.escape(field_name)}:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        return None
    return strip_quotes(match.group(1))


def validate_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"Missing required file: {path.relative_to(ROOT)}", errors)


def validate_skill_frontmatter(errors: list[str]) -> None:
    frontmatter = load_frontmatter(SKILL_DIR / "SKILL.md", errors)
    if not frontmatter:
        return

    name = find_field(frontmatter, "name")
    description = find_field(frontmatter, "description")
    license_name = find_field(frontmatter, "license")
    version = re.search(r'^\s*version:\s*"([^"]+)"\s*$', frontmatter, re.MULTILINE)

    if name != EXPECTED_NAME:
        fail(f"SKILL.md name must be {EXPECTED_NAME!r}, found {name!r}.", errors)
    if not description:
        fail("SKILL.md description must be present.", errors)
    if license_name != EXPECTED_LICENSE:
        fail(f"SKILL.md license must be {EXPECTED_LICENSE!r}, found {license_name!r}.", errors)
    if not version or not re.match(r"^\d+\.\d+\.\d+$", version.group(1)):
        fail("SKILL.md metadata.version must be a quoted semantic version.", errors)


def validate_openai_yaml(errors: list[str]) -> None:
    path = SKILL_DIR / "agents" / "openai.yaml"
    text = path.read_text(encoding="utf-8")

    required_patterns = {
        "interface section": r"^interface:\s*$",
        "display_name": r'^\s+display_name:\s*"Lex Scripta Structurer"\s*$',
        "short_description": r'^\s+short_description:\s*".+"\s*$',
        "default_prompt": rf'^\s+default_prompt:\s*".*\${EXPECTED_NAME}.*"\s*$',
        "policy section": r"^policy:\s*$",
        "allow_implicit_invocation": r"^\s+allow_implicit_invocation:\s*true\s*$",
    }

    for label, pattern in required_patterns.items():
        if not re.search(pattern, text, re.MULTILINE):
            fail(f"openai.yaml is missing {label}.", errors)


def validate_readme(errors: list[str]) -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for snippet in README_SNIPPETS:
        if snippet not in text:
            fail(f"README.md is missing installation guidance snippet: {snippet}", errors)


def validate_site_localization(errors: list[str]) -> None:
    text = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    for snippet in SITE_LOCALE_LINKS:
        if snippet not in text:
            fail(f"site/index.html is missing locale link: {snippet}", errors)


def main() -> int:
    errors: list[str] = []

    validate_required_files(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    validate_skill_frontmatter(errors)
    validate_openai_yaml(errors)
    validate_readme(errors)
    validate_site_localization(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Validated Lex Scripta skill packaging successfully.")
    print(f"Canonical skill path: {SKILL_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

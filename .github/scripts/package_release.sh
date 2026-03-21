#!/usr/bin/env bash

set -euo pipefail

VERSION="${1:?usage: package_release.sh <version> [repo-slug] [output-dir]}"
REPO_SLUG="${2:-kuil09/lex-scripta}"
OUTPUT_DIR="${3:-dist}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SKILL_DIR="${ROOT_DIR}/.agents/skills/lex-scripta-structurer"
ARTIFACT_NAME="lex-scripta-structurer-${VERSION}"
STAGE_DIR="$(mktemp -d)"

checksum() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  else
    shasum -a 256 "$1" | awk '{print $1}'
  fi
}

cleanup() {
  rm -rf "${STAGE_DIR}"
}

trap cleanup EXIT

mkdir -p "${OUTPUT_DIR}"
OUTPUT_DIR="$(cd "${OUTPUT_DIR}" && pwd)"
cp -R "${SKILL_DIR}" "${STAGE_DIR}/lex-scripta-structurer"

tar -czf "${OUTPUT_DIR}/${ARTIFACT_NAME}.tar.gz" -C "${STAGE_DIR}" lex-scripta-structurer
(
  cd "${STAGE_DIR}"
  zip -rq "${OUTPUT_DIR}/${ARTIFACT_NAME}.zip" lex-scripta-structurer
)

{
  printf "%s  %s\n" "$(checksum "${OUTPUT_DIR}/${ARTIFACT_NAME}.tar.gz")" "${ARTIFACT_NAME}.tar.gz"
  printf "%s  %s\n" "$(checksum "${OUTPUT_DIR}/${ARTIFACT_NAME}.zip")" "${ARTIFACT_NAME}.zip"
} > "${OUTPUT_DIR}/SHA256SUMS.txt"

cat > "${OUTPUT_DIR}/RELEASE_NOTES.md" <<EOF
# Lex Scripta Structurer ${VERSION}

## Install

### Codex repo-local discovery

Clone the repository and open it in Codex. Codex automatically scans \`.agents/skills\`.

### Codex remote install

\`\`\`text
\$skill-installer install https://github.com/${REPO_SLUG}/tree/v${VERSION}/.agents/skills/lex-scripta-structurer
\`\`\`

Restart Codex after installation if the skill does not appear immediately.

### Cross-agent install

\`\`\`text
npx skills add ${REPO_SLUG} --skill lex-scripta-structurer
\`\`\`

## Release assets

- \`${ARTIFACT_NAME}.tar.gz\`
- \`${ARTIFACT_NAME}.zip\`
- \`SHA256SUMS.txt\`
EOF

echo "Packaged release assets in ${OUTPUT_DIR}"

# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurer는 대화, 회의 메모, 기획 초안, 정책 문서를 구조화된 Lex Scripta 문서로 바꾸는 공개 Agent Skill입니다.

저장소: `kuil09/lex-scripta`

## 빠른 시작

### 1. Codex 안에서 바로 사용하기

Codex는 현재 작업 디렉토리에서 저장소 루트까지 `.agents/skills`를 자동으로 스캔합니다. 이 저장소를 클론해서 Codex로 열면 추가 설치 없이 바로 skill을 사용할 수 있습니다.

### 2. GitHub에서 Codex로 설치하기

Codex의 내장 설치기를 사용해 canonical skill 디렉토리를 설치할 수 있습니다.

```text
$skill-installer install https://github.com/kuil09/lex-scripta/tree/main/.agents/skills/lex-scripta-structurer
```

설치 후 skill이 바로 보이지 않으면 Codex를 다시 시작하세요.

### 3. 여러 에이전트에서 설치하기

오픈 `skills` CLI는 `.agents/skills`를 스캔하므로, 이 저장소는 여러 지원 에이전트 런타임에서도 설치할 수 있습니다.

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer
```

Codex를 명시적으로 대상으로 지정하려면:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent codex
```

## 이 저장소에 포함된 것

- `.agents/skills/lex-scripta-structurer/`는 canonical installable skill 패키지입니다.
- `.github/scripts/validate_skill.py`는 공개 배포 패키징 규약을 검증합니다.
- `.github/workflows/release-skill.yml`는 태그 버전용 릴리스 자산을 생성합니다.
- `docs/catalog-readiness-checklist.md`는 공개 배포와 카탈로그 제출 준비 상태를 추적합니다.

## 이 skill을 언제 써야 하나

다음과 같은 입력을 원래 의미를 유지한 채 기계가 읽을 수 있는 rule tree로 바꾸고 싶을 때 사용하세요.

- 비정형 대화
- 회의 메모 또는 회의록
- 기획 초안
- 요구사항 초안
- 정책 문서
- 액션 아이템과 미해결 질문이 섞인 메모

## 왜 이 형식이 유용한가

Lex Scripta는 자연어를 읽기 쉽게 유지하면서도 실행 로직을 명확하게 드러냅니다.

- 들여쓰기는 의미를 가집니다.
- 한 줄은 하나의 주장만 담습니다.
- 부모 문장은 지배 규칙을 담습니다.
- 자식 문장은 범위를 좁히거나 조건, 의존성, 예외를 붙입니다.
- 빠진 사실은 추정하지 않고 드러냅니다.
- 설명성 메모는 규칙 본문 밖에 둡니다.

## 저장소 구조

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

## 릴리스와 검증

각 `vX.Y.Z` 태그는 GitHub Actions를 통해 다음 자산으로 패키징됩니다.

- `lex-scripta-structurer-X.Y.Z.tar.gz`
- `lex-scripta-structurer-X.Y.Z.zip`
- `SHA256SUMS.txt`

GitHub Releases는 버전 고정과 무결성 검증용이며, 주된 설치 경로는 아닙니다.

로컬에서 패키징 규약을 검증하려면:

```text
python3 .github/scripts/validate_skill.py
```

로컬에서 릴리스 패키징을 dry-run 하려면:

```text
bash .github/scripts/package_release.sh 1.0.0 kuil09/lex-scripta /tmp/lex-scripta-release
```

## 발견성과 카탈로그 준비

이 저장소는 공개 skill 생태계를 두 가지 방식으로 지원합니다.

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer`가 `.agents/skills` 기반으로 동작합니다.
- [skills.sh](https://skills.sh/) 노출은 `skills` CLI의 익명 설치 텔레메트리에 의해 이루어집니다.

수동 카탈로그 제출이나 리뷰 기반 디렉토리 준비에는 `docs/catalog-readiness-checklist.md`를 참고하세요.

## 링크

- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

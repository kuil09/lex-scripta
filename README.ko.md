# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurer는 대화, 회의 메모, 기획 초안, 정책 문서를 구조화된 Lex Scripta 문서로 바꾸는 공개 Agent Skill입니다.

저장소: `kuil09/lex-scripta`

## 빠른 시작

### 1. 대부분의 에이전트에 한 번에 설치하기

가장 빠른 프로젝트 단위 설치 방법은 `skills` CLI를 쓰는 것입니다.

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y
```

프로젝트 단위가 아니라 사용자 전역 설치를 원하면 `--global`을 추가하세요.

### 2. 특정 에이전트에만 설치하기

Claude Code:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent claude-code --copy -y
```

Cursor:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent cursor --copy -y
```

Gemini CLI:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent gemini-cli --copy -y
```

### 3. 수동 fallback 경로

`skills` CLI를 쓰지 않으려면 canonical skill 폴더를 대상 프로젝트에 직접 복사해도 됩니다.

- Codex, Cursor, Gemini CLI 같은 범용 에이전트: `.agents/skills/lex-scripta-structurer`
- Claude Code: `.claude/skills/lex-scripta-structurer`

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

## Lex Scripta 문서는 어떻게 생기나

Lex Scripta는 특별한 파일 확장자가 아니라 문서 구조입니다.

- 부모 줄이 지배 규칙을 선언합니다.
- 들여쓴 자식 줄은 부모 범위를 상속합니다.
- 더 깊은 들여쓰기는 더 좁은 조건이나 예외를 붙입니다.
- 빈 줄은 서로 독립적인 규칙 블록을 나눕니다.

예시:

```text
베타 가입 정책은 초기 접근 규칙을 다룬다.
    출시 목표 시점은 다음 달이다.
    정확한 출시 날짜는 아직 미정이다.

가입은 이메일 우선으로 시작한다.
    초기에 이메일만 수집한다.
    전화번호 확인은 뒤로 미룬다.
        엔터프라이즈 계정에는 회사 이메일 확인이 필요할 수 있다.

디자인 담당은 민지다.
출시 담당자는 아직 미정이다.
```

이 예시에서:

- `베타 가입 정책은 초기 접근 규칙을 다룬다.`가 부모 문장입니다.
- `출시 목표 시점은 다음 달이다.`와 `정확한 출시 날짜는 아직 미정이다.`는 그 부모 아래에 붙습니다.
- `엔터프라이즈 계정에는 회사 이메일 확인이 필요할 수 있다.`는 더 좁은 `전화번호 확인은 뒤로 미룬다.` 가지 아래에 남습니다.
- `출시 담당자는 아직 미정이다.`는 빠진 사실을 임의로 채우지 않고 그대로 드러냅니다.

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

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y`가 `.agents/skills` 기반으로 동작합니다.
- [skills.sh](https://skills.sh/) 노출은 `skills` CLI의 익명 설치 텔레메트리에 의해 이루어집니다.

수동 카탈로그 제출이나 리뷰 기반 디렉토리 준비에는 `docs/catalog-readiness-checklist.md`를 참고하세요.

## 링크

- Website: [https://kuil09.github.io/lex-scripta/](https://kuil09.github.io/lex-scripta/)
- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

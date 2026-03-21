# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurer 是一个公开的 Agent Skill，用于把对话、会议记录、规划草稿和政策文本转换成结构化的 Lex Scripta 文档。

仓库: `kuil09/lex-scripta`

## 快速开始

### 1. 直接在 Codex 中使用

Codex 会从当前工作目录一直向上扫描到仓库根目录中的 `.agents/skills`。克隆这个仓库并在 Codex 中打开后，无需额外安装就可以直接使用这个 skill。

### 2. 从 GitHub 安装到 Codex

可以使用 Codex 内置安装器，直接安装 canonical skill 目录。

```text
$skill-installer install https://github.com/kuil09/lex-scripta/tree/main/.agents/skills/lex-scripta-structurer
```

如果安装后没有立刻看到 skill，请重启 Codex。

### 3. 在多个代理中安装

开源 `skills` CLI 会扫描 `.agents/skills`，因此这个仓库也可以在多个受支持的代理运行时中安装。

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer
```

如果要显式指定 Codex：

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent codex
```

## 仓库包含的内容

- `.agents/skills/lex-scripta-structurer/` 是 canonical 的 installable skill package。
- `.github/scripts/validate_skill.py` 用来校验公开打包约定。
- `.github/workflows/release-skill.yml` 用来为带标签的版本生成发布产物。
- `docs/catalog-readiness-checklist.md` 用来跟踪公开分发和目录提交的准备状态。

## 什么时候使用这个 skill

当你需要在不丢失原始含义的前提下，把下面这些输入转换成机器可读的 rule tree 时，就适合使用它。

- 非结构化对话
- 会议记录或纪要
- 规划草稿
- 需求草稿
- 政策文本
- 混合了 action items 和未决问题的笔记

## 为什么这种格式有效

Lex Scripta 保留自然语言的可读性，同时让执行逻辑显式可见。

- 缩进具有语义意义。
- 一行只表达一个主张。
- 父级语句承载主导规则。
- 子级语句补充条件、依赖、例外和范围。
- 缺失的信息会被显式暴露，而不是被猜测补全。
- 说明性备注放在规则正文之外。

## 仓库结构

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

## 发布与校验

每个 `vX.Y.Z` 标签都会通过 GitHub Actions 打包成以下产物：

- `lex-scripta-structurer-X.Y.Z.tar.gz`
- `lex-scripta-structurer-X.Y.Z.zip`
- `SHA256SUMS.txt`

GitHub Releases 用于版本固定和校验，不是主要安装路径。

本地校验打包约定：

```text
python3 .github/scripts/validate_skill.py
```

本地 dry-run 发布打包流程：

```text
bash .github/scripts/package_release.sh 1.0.0 kuil09/lex-scripta /tmp/lex-scripta-release
```

## 可发现性与目录准备

这个仓库为公开 skill 生态做了两件事：

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer` 可以基于 `.agents/skills` 正常工作。
- [skills.sh](https://skills.sh/) 的曝光来自 `skills` CLI 的匿名安装遥测。

如果要准备人工审核的目录提交，请查看 `docs/catalog-readiness-checklist.md`。

## 链接

- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

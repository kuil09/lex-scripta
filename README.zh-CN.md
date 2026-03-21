# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurer 是一个公开的 Agent Skill，用于把对话、会议记录、规划草稿和政策文本转换成结构化的 Lex Scripta 文档。

仓库: `kuil09/lex-scripta`

## 快速开始

### 1. 一条命令安装到大多数代理

最省事的项目级安装方式是使用 `skills` CLI：

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y
```

如果你更想做用户级安装而不是项目级安装，可以额外加上 `--global`。

### 2. 只安装到特定代理

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

### 3. 手动 fallback 路径

如果你不想使用 `skills` CLI，也可以把 canonical skill 文件夹手动复制到目标项目中：

- Codex、Cursor、Gemini CLI 等通用代理：`.agents/skills/lex-scripta-structurer`
- Claude Code：`.claude/skills/lex-scripta-structurer`

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

## Lex Scripta 文档长什么样

Lex Scripta 不是特殊的文件扩展名，而是一种文档结构。

- 父行声明主导规则。
- 缩进后的子行继承父级范围。
- 更深的缩进表示更窄的条件或例外。
- 空行用于分隔彼此独立的规则块。

示例:

```text
Beta 注册策略管理早期访问规则。
    发布时间目标是下个月。
    具体发布日期仍未确定。

注册先走邮箱优先规则。
    初期只收邮箱。
    手机验证延后处理。
        企业账号可能需要公司邮箱验证。

设计由 Minji 负责。
发布负责人仍未确定。
```

在这个示例里:

- `Beta 注册策略管理早期访问规则。` 是父级语句。
- `发布时间目标是下个月。` 和 `具体发布日期仍未确定。` 都挂在这个父级下面。
- `企业账号可能需要公司邮箱验证。` 继续挂在更窄的 `手机验证延后处理。` 分支下面。
- `发布负责人仍未确定。` 会把不确定性显式保留，而不是擅自补全。

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

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y` 可以基于 `.agents/skills` 正常工作。
- [skills.sh](https://skills.sh/) 的曝光来自 `skills` CLI 的匿名安装遥测。

如果要准备人工审核的目录提交，请查看 `docs/catalog-readiness-checklist.md`。

## 链接

- Website: [https://kuil09.github.io/lex-scripta/](https://kuil09.github.io/lex-scripta/)
- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

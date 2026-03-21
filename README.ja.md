# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurerは、会話、会議メモ、企画ドラフト、ポリシー文書を構造化されたLex Scripta文書に変換する公開Agent Skillです。

リポジトリ: `kuil09/lex-scripta`

## クイックスタート

### 1. ほとんどのエージェントに一度でインストールする

最も手軽なプロジェクトローカル導入は `skills` CLI を使う方法です。

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y
```

プロジェクトローカルではなくユーザーレベルに入れたい場合は `--global` を追加してください。

### 2. 特定のエージェントだけにインストールする

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

### 3. 手動フォールバックパス

`skills` CLI を使わない場合は、canonical な skill フォルダを対象プロジェクトへ直接コピーできます。

- Codex、Cursor、Gemini CLI などのユニバーサルエージェント: `.agents/skills/lex-scripta-structurer`
- Claude Code: `.claude/skills/lex-scripta-structurer`

## このリポジトリに含まれるもの

- `.agents/skills/lex-scripta-structurer/` はcanonicalなinstallable skill packageです。
- `.github/scripts/validate_skill.py` は公開パッケージング契約を検証します。
- `.github/workflows/release-skill.yml` はタグ付きバージョンのリリース成果物を生成します。
- `docs/catalog-readiness-checklist.md` は公開配布とカタログ提出の準備状態を確認するためのチェックリストです。

## このskillを使う場面

次のような入力を、元の意味を保ちながら機械可読なrule treeへ変換したい場合に使います。

- 非構造の会話
- 会議メモや議事録
- 企画ドラフト
- 要件ドラフト
- ポリシー文書
- アクションアイテムと未解決事項が混在するメモ

## この形式が有効な理由

Lex Scriptaは自然言語の読みやすさを保ちながら、実行ロジックを明示します。

- インデントは意味を持ちます。
- 1行には1つの主張だけを書きます。
- 親の文は支配的なルールを表します。
- 子の文は条件、依存関係、例外、スコープを追加します。
- 欠けている事実は推測せず、明示します。
- 説明的なメモはルール本文の外に置きます。

## Lex Scripta文書の形

Lex Scriptaは特別な拡張子ではなく、文書の構造です。

- 親の行が支配ルールを宣言します。
- インデントされた子の行は親のスコープを継承します。
- より深いインデントは、より狭い条件や例外を追加します。
- 空行は独立したルールブロックを分けます。

例:

```text
ベータ登録方針は初期アクセス規則を扱う。
    公開目標時期は来月である。
    正確な公開日はまだ未定である。

登録はメール優先で始まる。
    初期段階ではメールのみ収集する。
    電話確認は後ろへ送る。
        エンタープライズアカウントでは会社メール確認が必要な場合がある。

デザイン担当は Minji である。
公開担当は未定のままである。
```

この例では:

- `ベータ登録方針は初期アクセス規則を扱う。` が親文です。
- `公開目標時期は来月である。` と `正確な公開日はまだ未定である。` はその親の下に残ります。
- `エンタープライズアカウントでは会社メール確認が必要な場合がある。` は、より狭い `電話確認は後ろへ送る。` の枝の下に残ります。
- `公開担当は未定のままである。` は、不確実さを埋めずに明示します。

## リポジトリ構成

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

## リリースと検証

各 `vX.Y.Z` タグはGitHub Actionsによって次の成果物にパッケージされます。

- `lex-scripta-structurer-X.Y.Z.tar.gz`
- `lex-scripta-structurer-X.Y.Z.zip`
- `SHA256SUMS.txt`

GitHub Releasesはバージョン固定と検証のための配布面であり、主なインストール経路ではありません。

ローカルでパッケージング契約を検証するには:

```text
python3 .github/scripts/validate_skill.py
```

ローカルでリリースパッケージングをdry-runするには:

```text
bash .github/scripts/package_release.sh 1.0.0 kuil09/lex-scripta /tmp/lex-scripta-release
```

## discoverability とカタログ準備

このリポジトリは公開skillエコシステムに対して次の2つを用意しています。

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --copy -y` が `.agents/skills` を基準に動作します。
- [skills.sh](https://skills.sh/) での可視性は `skills` CLI の匿名インストールテレメトリによって生まれます。

手動のカタログ提出やレビュー駆動のディレクトリ向けには `docs/catalog-readiness-checklist.md` を参照してください。

## リンク

- Website: [https://kuil09.github.io/lex-scripta/](https://kuil09.github.io/lex-scripta/)
- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

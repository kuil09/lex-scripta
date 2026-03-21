# Lex Scripta Structurer

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Lex Scripta Structurerは、会話、会議メモ、企画ドラフト、ポリシー文書を構造化されたLex Scripta文書に変換する公開Agent Skillです。

リポジトリ: `kuil09/lex-scripta`

## クイックスタート

### 1. Codexの中でそのまま使う

Codexは現在の作業ディレクトリからリポジトリルートまで `.agents/skills` を自動的に走査します。このリポジトリをクローンしてCodexで開けば、追加インストールなしでskillを使えます。

### 2. GitHubからCodexへインストールする

Codexの組み込みインストーラを使って、canonical skillディレクトリを直接インストールできます。

```text
$skill-installer install https://github.com/kuil09/lex-scripta/tree/main/.agents/skills/lex-scripta-structurer
```

インストール後にskillが表示されない場合は、Codexを再起動してください。

### 3. 複数のエージェントでインストールする

オープンな `skills` CLI は `.agents/skills` を走査するため、このリポジトリは対応する複数のエージェントランタイムでも利用できます。

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer
```

Codexを明示的に指定する場合:

```text
npx skills add kuil09/lex-scripta --skill lex-scripta-structurer --agent codex
```

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

- `npx skills add kuil09/lex-scripta --skill lex-scripta-structurer` が `.agents/skills` を基準に動作します。
- [skills.sh](https://skills.sh/) での可視性は `skills` CLI の匿名インストールテレメトリによって生まれます。

手動のカタログ提出やレビュー駆動のディレクトリ向けには `docs/catalog-readiness-checklist.md` を参照してください。

## リンク

- GitHub: [https://github.com/kuil09/lex-scripta](https://github.com/kuil09/lex-scripta)
- Releases: [https://github.com/kuil09/lex-scripta/releases](https://github.com/kuil09/lex-scripta/releases)

# <Document Title>

## 1. Purpose
<Write one or two sentences that define the scope and intent of the document.>

## 0. Org Scope *(optional — include when an org hierarchy exists)*
- Org Unit: <path from root to owning unit, e.g. Engineering > Backend>
- Audience: [<other org units that must act on this document — omit if none>]

## 2. Defined Terms
- <term>: <definition>
- If there are no special terms, write `- None.`

## 3. Lex Scripta Body
```text
<Parent statement>
    <Child condition, scope, dependency, or timing rule>
        <Exception, approval path, evidence duty, or detailed constraint>
```

## 4. Open Items
- <Unresolved question or missing fact>
- If there are no open items, write `- None.`

## 5. Assumptions
- <Working assumption used during normalization>
- If none, write `- None.`

## 6. Evidence / Notes
- <Interpretation note or source-context note>
- If none, write `- None.`

## 7. Risks / Conflicts
- <Conflict, scope risk, sequencing risk, or unresolved tension>
- If none, write `- None.`

## Usage notes

- Keep the Lex Scripta Body purely operational.
- Keep one claim per line.
- Do not guess missing facts.
- Use `[Unspecified]` or `[Needs confirmation]` when needed.
- `Org Scope` is optional. Include it when the document belongs to a known org hierarchy. Omit it otherwise.
- Use the `lex-scripta-org-auditor` skill to verify org placement after documents are created.

---
name: lex-scripta-org-auditor
description: Audit one or more Lex Scripta documents against an org hierarchy defined in Org Map format. Identify statements attributed to the wrong org unit, detect content that should be moved up or down the hierarchy, flag cross-org dependencies that are not coordinated, and report gaps where parent-level policies are missing. Use when you need to verify that structured documents are correctly owned and scoped within a defined organizational structure.
license: MIT
metadata:
  author: Lex Scripta Contributors
  version: "1.0.0"
---

# Lex Scripta Org Auditor

## Use this skill when

Activate this skill when:

- one or more Lex Scripta documents exist and need to be verified against an organizational hierarchy
- an org map exists or can be constructed from context
- the user suspects a document contains statements that belong to a different org unit
- content has accumulated across multiple documents and needs to be redistributed by organizational ownership
- cross-org dependencies or gaps in parent-level policy are suspected

## Core concepts

### Org Map

An Org Map defines the organizational hierarchy using the same indentation model as the Lex Scripta Body.

- A top-level line names a root org unit.
- One indentation level equals one level of org hierarchy.
- Child org units fall within the scope of their parent.
- A statement owned by a child org unit is also within the scope of all its ancestor units.

Example:

```text
Acme Corp
    Engineering
        Frontend
        Backend
        Infrastructure
    Product
        Design
        PM
    Operations
        HR
        Finance
    Legal
```

The Org Map is stored as a separate document using the template in `assets/org-map-template.md`.

### Org Scope in Lex Scripta documents

A Lex Scripta document may include an optional `Org Scope` section that declares which org unit owns the document.

Position: between `Purpose` and `Defined Terms`.

Format:

```md
## 0. Org Scope
- Org Unit: Engineering > Backend
- Audience: [Engineering > Backend, Engineering > Infrastructure]
```

When `Org Scope` is absent, treat the document as unattributed and include it in the audit with a note.

### Org path notation

Write org paths from root to leaf, separated by ` > `.

Example: `Acme Corp > Engineering > Backend`

Omit the root when context makes it unambiguous.

## Audit workflow

1. Parse the Org Map and build the org hierarchy.
2. For each document, identify its declared `Org Scope` or mark it as `[Unattributed]`.
3. For each statement in the Lex Scripta Body, evaluate whether the subject, action, or scope fits the declared org unit.
4. Classify each issue found.
5. Produce the audit report using the format below.

## Issue types

| Code | Name | Meaning |
| --- | --- | --- |
| `MISPLACED` | Org mismatch | A statement belongs to a different org unit than the one declared in `Org Scope` |
| `SHOULD_ELEVATE` | Needs elevation | A statement scoped to a child org unit also applies at a parent level and is missing there |
| `SHOULD_DESCEND` | Needs delegation | A statement written at a parent level is too specific for that level and belongs in a child document |
| `CROSS_DEP` | Cross-org dependency | A statement depends on or affects another org unit but has no corresponding entry in that org's documents |
| `GAP` | Hierarchy gap | A parent org unit is missing a governing policy that its child units assume or depend on |
| `UNATTRIBUTED` | No org scope | A document has no `Org Scope` declaration and its ownership cannot be determined |

## Evaluation rules

### Evaluating a statement's org fit

A statement fits its declared org unit when:

- the subject of the statement is the org unit or its members
- the action or policy governs only the work within that org unit's domain
- the statement does not reference processes owned by a sibling or parent unit

A statement does not fit when:

- the subject is outside the org unit
- the policy governs shared infrastructure, cross-org coordination, or company-wide obligations
- the action requires approval or input from an org unit not represented in the document

### Determining elevation

A child-level statement should be elevated when:

- the same obligation or constraint applies to all sibling org units under the same parent
- the parent org unit has no equivalent governing statement

### Determining delegation

A parent-level statement should be delegated when:

- the statement names a specific team, role, or system that belongs to one child unit only
- the policy cannot affect any sibling unit

### Detecting cross-org dependencies

A cross-org dependency exists when:

- a statement requires output, approval, or data from an org unit not in scope for this document
- no corresponding obligation exists in a document owned by the other org unit

## Output format

Produce the audit report in this section order:

1. `Audit Context`
2. `Summary`
3. `Issues`
4. `Recommendations`

Use this skeleton:

````md
# Org Audit Report: <title>

## 1. Audit Context
- Org Map: <name or path>
- Documents audited: <list>
- Audit date: <date or [Unspecified]>

## 2. Summary
- Total issues found: N
- MISPLACED: N
- SHOULD_ELEVATE: N
- SHOULD_DESCEND: N
- CROSS_DEP: N
- GAP: N
- UNATTRIBUTED: N

## 3. Issues

### [MISPLACED] <short label>
- Document: <document name>
- Org Scope declared: <org path>
- Statement: `<exact statement text>`
- Suggested org: <org path>
- Reason: <one sentence>

### [SHOULD_ELEVATE] <short label>
- Document: <document name>
- Current location: <org path>
- Statement: `<exact statement text>`
- Suggested parent: <org path>
- Reason: <one sentence>

### [SHOULD_DESCEND] <short label>
- Document: <document name>
- Current location: <org path>
- Statement: `<exact statement text>`
- Suggested child: <org path>
- Reason: <one sentence>

### [CROSS_DEP] <short label>
- Document: <document name>
- Org Scope: <org path>
- Statement: `<exact statement text>`
- Affected org: <org path>
- Missing counterpart: <describe the obligation that should exist in the affected org's documents>

### [GAP] <short label>
- Parent org: <org path>
- Missing policy: <describe the governing statement that is absent>
- Assumed by: <child org path> in `<statement text>`

### [UNATTRIBUTED] <short label>
- Document: <document name>
- Likely org: <org path or [Cannot determine]>
- Reason: <one sentence>

## 4. Recommendations
- <Prioritized action, one per bullet>
````

## Hard constraints

- Do not invent org units that are not in the Org Map.
- Do not reassign statements without stating a reason.
- If an org unit is ambiguous, mark it as `[Needs confirmation]` rather than guessing.
- Do not flatten cross-org conflicts by choosing one unit silently.
- If an issue is borderline, note the uncertainty in the reason field.

## Further reading

- [Detailed reference](references/REFERENCE.md)
- [Examples](references/EXAMPLES.md)
- [Org Map template](assets/org-map-template.md)

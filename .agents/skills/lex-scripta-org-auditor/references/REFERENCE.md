# Reference Guide — Lex Scripta Org Auditor

This file expands the operational rules for the `lex-scripta-org-auditor` skill.

## 1. Org Map semantics

### 1.1 Hierarchy rules

The Org Map is the authoritative source of organizational structure.

- Every indented line is a direct child of the nearest less-indented line above it.
- A child org unit is always within the governance scope of all its ancestors.
- Sibling org units at the same indentation level share a common parent but do not govern each other.

```text
Company                     ← root, governs everything
    Engineering             ← child of Company
        Frontend            ← child of Engineering, grandchild of Company
        Backend             ← sibling of Frontend
    Operations              ← sibling of Engineering
        HR                  ← child of Operations
```

### 1.2 Scope inheritance

A policy written at a parent level applies to all descendants unless a child unit overrides or narrows it.

A policy written at a child level applies only to that unit and its descendants unless explicitly elevated.

### 1.3 Org path notation

Always write the full path from root to leaf when precision is needed:

```text
Company > Engineering > Backend
```

Omit the root only when the context is unambiguous and only one root exists.

### 1.4 Org Map document structure

The Org Map is a standalone Lex Scripta document with the following mandatory sections:

- `Purpose` — describes the organization and the scope of this map
- `Org Hierarchy` — the indented tree in a fenced `text` block
- `Org Definitions` — definitions of each unit's domain and ownership boundaries
- `Open Items` — unresolved placement decisions or missing units

Optional sections:
- `Constraints by Level` — cross-cutting rules that apply to all units at a given hierarchy depth

## 2. Org Scope attribution

### 2.1 What Org Scope declares

`Org Scope` in a Lex Scripta document declares:

- **Org Unit** — the org unit that owns and is responsible for the content
- **Audience** — the org units that should act on or be aware of the content (optional)

Example:

```md
## 0. Org Scope
- Org Unit: Engineering > Backend
- Audience: [Engineering > Backend, Operations > HR]
```

### 2.2 Ownership vs. audience

Ownership means the org unit is accountable for the document and the policies it contains.

Audience means the org unit must know and comply with the content, but does not own it.

An audience org unit that has obligations described in the document may trigger a `CROSS_DEP` issue if the corresponding obligation is absent from that unit's own documents.

### 2.3 Unattributed documents

If a document has no `Org Scope` section, the auditor must attempt to infer ownership from:

1. Document title and purpose
2. Subject of the majority of statements
3. Named roles, systems, and processes in the body

If inference is not possible with confidence, mark as `[Cannot determine]` and file an `UNATTRIBUTED` issue.

## 3. Issue classification in detail

### 3.1 MISPLACED

A statement is misplaced when its subject, action, or governing scope clearly belongs to a different org unit.

Signals:
- The statement names a team, role, or system not in the document's declared org unit
- The action governs a process owned by a different unit
- The policy is a company-wide rule and the document is scoped to a single team

Example:

```text
Document Org Scope: Engineering > Backend

Statement: "All employees must complete the annual harassment training."
```

This statement belongs at the `Company` level, not `Engineering > Backend`.

### 3.2 SHOULD_ELEVATE

A statement should be elevated when it is written in a child document but applies equally to all sibling units under the same parent.

Signals:
- The rule references no Backend-specific systems or roles
- The same rule would be duplicated if written for Frontend, Infrastructure, and Backend separately
- The parent document has no governing policy in this area

Example:

```text
Document Org Scope: Engineering > Backend

Statement: "All code changes must be reviewed before merging."
```

This rule likely applies to all Engineering sub-teams and belongs in an `Engineering`-level document.

### 3.3 SHOULD_DESCEND

A statement should be delegated when a parent document contains a rule that is too specific for the parent level.

Signals:
- The rule names a specific tool, system, or role that belongs to one child unit only
- The rule cannot apply to sibling units without modification
- The level of detail is inconsistent with other rules in the parent document

Example:

```text
Document Org Scope: Engineering

Statement: "The Postgres connection pool must be kept below 80% utilization."
```

This is a Backend-specific infrastructure rule, not an Engineering-wide policy.

### 3.4 CROSS_DEP

A cross-org dependency exists when a statement requires an action from an org unit that does not own the current document.

The auditor should flag the dependency and describe what obligation is missing from the other unit's documents.

Signals:
- A statement says "X team must approve" or "X team will provide"
- The document is owned by a different unit
- No document owned by X team records a corresponding obligation

Example:

```text
Document Org Scope: Engineering > Backend

Statement: "The deployment checklist must be reviewed by Legal before each major release."
```

Legal has an obligation here (perform the review) that should be recorded in a Legal-owned document.

### 3.5 GAP

A gap exists when child documents assume a parent-level policy that does not exist in any parent-owned document.

Signals:
- Child documents reference "company policy," "standard process," or "as required by" without a traceable parent document
- Multiple child units have the same rule, suggesting it should exist at the parent level but does not
- A child rule has an exception that references a parent-level rule that cannot be found

Example:

```text
Engineering > Frontend document: "Exceptions to the security review rule require VP approval."
Engineering > Backend document: "Exceptions to the security review rule require VP approval."
```

If no Engineering-level or Company-level document defines the security review rule, this is a `GAP`.

### 3.6 UNATTRIBUTED

A document is unattributed when it has no `Org Scope` section.

Even if ownership can be inferred, file an `UNATTRIBUTED` issue to ensure the owner adds an explicit declaration.

## 4. Audit scope decisions

### 4.1 What to audit

Audit all statements in the `Lex Scripta Body`. Do not audit:

- `Open Items` — they are already flagged as unresolved
- `Assumptions` — they are not operational rules
- `Evidence / Notes` — they are context, not obligations

### 4.2 Prioritizing issues

Report issues in this order within each document:

1. `MISPLACED` — highest urgency; content is in the wrong place
2. `CROSS_DEP` — second priority; missing cross-org obligations create gaps in execution
3. `SHOULD_ELEVATE` — third; affects governance completeness
4. `SHOULD_DESCEND` — fourth; affects clarity and correct scoping
5. `GAP` — fifth; affects structural completeness
6. `UNATTRIBUTED` — last; affects attribution only

### 4.3 Borderline cases

When a statement could belong to either of two org units, note the ambiguity in the reason field using: `[Borderline: could also fit <org path>]`.

Do not silently choose one org and suppress the other option.

## 5. Recommendations format

Each recommendation must:

- name the document and statement affected
- state the action required (move, copy, create, elevate, attribute)
- specify the target org unit or document
- be stated in one sentence

Prioritize recommendations in order of issue type (MISPLACED first, UNATTRIBUTED last).

Example:

```text
- Move "All employees must complete the annual harassment training" from the Backend policy document to a Company-level document.
- Create an obligation in a Legal-owned document requiring Legal to review the deployment checklist before each major release.
- Add an Org Scope section to the "Incident Response Runbook" document declaring Engineering > Infrastructure as the owner.
```

## 6. Relationship to lex-scripta-structurer

The `lex-scripta-structurer` skill produces documents. The `lex-scripta-org-auditor` skill audits them.

Run `lex-scripta-structurer` first to normalize source material into Lex Scripta format. Then run `lex-scripta-org-auditor` to verify organizational placement.

Both skills use the same indentation-based body format. The Org Map is itself a valid Lex Scripta document.

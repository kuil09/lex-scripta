# Reference Guide

This file expands the operational rules for the `lex-scripta-structurer` skill.

## 1. Semantic model

The skill does not summarize for style. It restructures for execution clarity.

The target document should answer these questions:

- Who is the subject?
- What must, may, or must not happen?
- Under what condition?
- What exception exists?
- What depends on prior approval, evidence, or another task?
- What is still unresolved?

## 2. Statement taxonomy

Use this taxonomy when classifying extracted sentences.

| Type | Meaning | Placement |
| --- | --- | --- |
| Decision | A confirmed choice or direction | Lex Scripta Body |
| Obligation | Something that must happen | Lex Scripta Body |
| Prohibition | Something that must not happen | Lex Scripta Body |
| Condition | A situation that narrows the parent rule | Lex Scripta Body as child |
| Exception | A case that modifies or relaxes the parent rule | Lex Scripta Body as child or grandchild |
| Dependency | A prerequisite or sequencing rule | Lex Scripta Body as child |
| Approval rule | A gatekeeper statement | Lex Scripta Body as child |
| Action item | A concrete task with a subject and target | Lex Scripta Body |
| Open item | Something unresolved or unspecified | Open Items |
| Assumption | A working premise not yet verified | Assumptions |
| Note | Background or interpretive context | Evidence / Notes |
| Conflict | Incompatible claims or risks | Risks / Conflicts |

## 3. Writing rules

### 3.1 One line, one claim

Bad:

```text
Launch the beta next month, keep signup simple, and maybe verify company emails for enterprise accounts.
```

Better:

```text
The beta release is targeted for next month.
The initial signup flow follows a minimum-information rule.
    Enterprise accounts may require company email verification.
```

### 3.2 Use explicit modality

Normalize weak or scattered phrasing into one of these forms when the source supports it:

- must
- must not
- may
- is excluded
- is required
- is sequenced after
- is pending confirmation
- is [Unspecified]

Do not increase certainty beyond what the source supports.

### 3.3 Keep terms stable

If the source alternates between `customer`, `user`, and `account holder`, choose one term only when the referent is clearly the same. Otherwise keep them separate and explain the distinction in `Defined Terms`.

### 3.4 Keep explanation outside the body

The rule body should not carry narrative commentary.

Bad:

```text
The team should send weekly updates because leadership has recently complained about visibility.
```

Better:

```text
Weekly updates must be sent to leadership.
```

And then in notes:

```text
The rule was motivated by leadership concerns about visibility.
```

## 4. Parent-child mapping

Use this logic when building the tree.

### 4.1 Parent statements

Put these at the top level when they govern multiple downstream details:

- overall objectives
- global decisions
- general obligations
- base policies
- work ownership statements

Example:

```text
All employees must complete security training.
    New hires must complete it within two weeks of hire.
    Deadline extensions require HR approval.
```

### 4.2 Child statements

Put these one level below the parent when they narrow or implement it:

- timing
- role-specific scope
- system scope
- conditions
- dependencies
- approval paths

Example:

```text
Customer incidents must be acknowledged within 24 hours.
    Weekend incidents may be acknowledged by 12:00 on the next business day.
```

### 4.3 Grandchild statements

Use a deeper level when a condition itself carries an additional rule.

Example:

```text
External tools may be adopted.
    Security review is required before adoption.
        High-risk tools also require legal review.
```

## 5. Normalization rules

### 5.1 Subject normalization

Replace vague pronouns or conversational placeholders only when the referent is clear.

- `they` -> `design team` if clearly established
- `that side` -> keep unresolved if unclear and note it
- `we` -> keep as `the team` only if a defined collective exists

If the subject cannot be determined, write `[Responsible party unspecified]`.

### 5.2 Time normalization

- Convert relative dates only when a reference date exists.
- Preserve intrinsic time anchors such as `within two weeks of hire`.
- If the source says `later`, `soon`, or `after launch`, keep the relation but flag the missing concrete date if necessary.

### 5.3 Approval normalization

Convert vague gatekeeping language into an explicit approval rule.

Source:
`Let's check with legal before shipping the template.`

Output:
```text
The template may be shipped only after legal approval.
```

### 5.4 Exception normalization

Exceptions should sit below the rule they modify.

Source:
`Everyone gets the weekly report, but ops still needs immediate incident notices.`

Output:
```text
The weekly report is sent to all teams.
    Operations still receives immediate incident notices for incident events.
```

## 6. Everyday conversation mapping

Many informal conversations contain hidden rule types.

| Everyday phrasing | Likely rule type |
| --- | --- |
| `Let's do X first.` | Sequencing or dependency |
| `We can skip Y for now.` | Scope exclusion |
| `If Z happens...` | Condition |
| `Unless A approves it...` | Approval-dependent exception |
| `We'll decide that later.` | Open item |
| `B owns this.` | Action item or ownership rule |
| `Try to keep it simple.` | Design principle or scope rule |

The job is not to mimic the phrasing. The job is to extract the operational logic.

## 7. Conflict handling

Record conflicts instead of flattening them.

Example:

```text
Speaker A: Keep phone verification out of v1.
Speaker B: Phone verification is required for all enterprise accounts.
```

Valid output:

- Put the confirmed baseline rule in the body only if confirmed.

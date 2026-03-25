# Examples — Lex Scripta Org Auditor

## Example 1: Misplaced statement and cross-org dependency

### Input: Org Map

```text
Acme Corp
    Engineering
        Frontend
        Backend
    Operations
        HR
        Finance
    Legal
```

### Input: Document being audited

````md
# Backend Team Policy

## 0. Org Scope
- Org Unit: Engineering > Backend

## 1. Purpose
Define operational rules for the Backend engineering team.

## 2. Defined Terms
- None.

## 3. Lex Scripta Body
```text
All employees must complete the annual security awareness training.
    Completion must be logged in the HR system by December 31.

Backend services must have automated test coverage above 80%.
    Coverage reports must be submitted to the team lead each sprint.

New vendor integrations must be reviewed by Legal before activation.
    Legal must complete the review within ten business days of request.
```

## 4. Open Items
- None.

## 5. Assumptions
- None.

## 6. Evidence / Notes
- None.

## 7. Risks / Conflicts
- None.
````

### Output: Audit Report

````md
# Org Audit Report: Backend Team Policy

## 1. Audit Context
- Org Map: Acme Corp Org Map
- Documents audited: Backend Team Policy
- Audit date: [Unspecified]

## 2. Summary
- Total issues found: 3
- MISPLACED: 1
- SHOULD_ELEVATE: 0
- SHOULD_DESCEND: 0
- CROSS_DEP: 2
- GAP: 0
- UNATTRIBUTED: 0

## 3. Issues

### [MISPLACED] Annual security training is a company-wide obligation
- Document: Backend Team Policy
- Org Scope declared: Engineering > Backend
- Statement: `All employees must complete the annual security awareness training.`
- Suggested org: Acme Corp
- Reason: The subject is "all employees," which spans all org units and cannot be governed by a single team's policy document.

### [CROSS_DEP] HR system logging requires an HR-side obligation
- Document: Backend Team Policy
- Org Scope: Engineering > Backend
- Statement: `Completion must be logged in the HR system by December 31.`
- Affected org: Operations > HR
- Missing counterpart: Operations > HR has no recorded obligation to accept and confirm training completion logs from all teams by the December 31 deadline.

### [CROSS_DEP] Legal review requires a Legal-side obligation
- Document: Backend Team Policy
- Org Scope: Engineering > Backend
- Statement: `Legal must complete the review within ten business days of request.`
- Affected org: Legal
- Missing counterpart: Legal has no recorded obligation to perform vendor integration reviews or meet the ten business day SLA. This obligation must appear in a Legal-owned document.

## 4. Recommendations
- Move "All employees must complete the annual security awareness training" and its child statements to an Acme Corp-level policy document.
- Create an obligation in an Operations > HR-owned document requiring HR to accept and confirm training completion logs from all teams by December 31.
- Create an obligation in a Legal-owned document requiring Legal to complete vendor integration reviews within ten business days of request.
````

---

## Example 2: Elevation and delegation

### Input: Org Map

```text
TechCo
    Engineering
        Frontend
        Backend
        Infrastructure
    Product
```

### Input: Two documents being audited

**Document A**

````md
# Frontend Development Rules

## 0. Org Scope
- Org Unit: Engineering > Frontend

## 1. Purpose
Govern development practices for the Frontend team.

## 2. Defined Terms
- None.

## 3. Lex Scripta Body
```text
All code changes must pass peer review before merging.
    A minimum of one reviewer is required.

The Engineering manager must approve all new external library additions.
    The library must have an active maintenance record.
        Libraries inactive for more than two years are excluded.
```
````

**Document B**

````md
# Backend Development Rules

## 0. Org Scope
- Org Unit: Engineering > Backend

## 1. Purpose
Govern development practices for the Backend team.

## 2. Defined Terms
- None.

## 3. Lex Scripta Body
```text
All code changes must pass peer review before merging.
    A minimum of one reviewer is required.

The Backend database schema must be versioned using migration files.
    Migration files must be reviewed by the Infrastructure team before deployment.
```
````

### Output: Audit Report

````md
# Org Audit Report: Frontend and Backend Development Rules

## 1. Audit Context
- Org Map: TechCo Org Map
- Documents audited: Frontend Development Rules, Backend Development Rules
- Audit date: [Unspecified]

## 2. Summary
- Total issues found: 3
- MISPLACED: 0
- SHOULD_ELEVATE: 1
- SHOULD_DESCEND: 1
- CROSS_DEP: 1
- GAP: 0
- UNATTRIBUTED: 0

## 3. Issues

### [SHOULD_ELEVATE] Peer review rule is duplicated across Frontend and Backend
- Document: Frontend Development Rules, Backend Development Rules
- Current location: Engineering > Frontend, Engineering > Backend
- Statement: `All code changes must pass peer review before merging.` (identical in both documents)
- Suggested parent: Engineering
- Reason: The rule contains no team-specific system or role and applies equally to all Engineering sub-teams; duplicating it in each child document creates a maintenance risk and suggests a missing Engineering-level policy.

### [SHOULD_DESCEND] Library approval rule names a role too specific for Frontend scope
- Document: Frontend Development Rules
- Current location: Engineering > Frontend
- Statement: `The Engineering manager must approve all new external library additions.`
- Suggested child: Engineering (elevation, not descent — see note)
- Reason: [Borderline: could also fit Engineering] The subject is "Engineering manager," which governs all Engineering sub-teams, not Frontend alone; this rule may belong at the Engineering level rather than only in the Frontend document, unless Frontend has its own dedicated manager separate from the broader Engineering manager role. Mark as [Needs confirmation].

### [CROSS_DEP] Schema migration review requires an Infrastructure-side obligation
- Document: Backend Development Rules
- Org Scope: Engineering > Backend
- Statement: `Migration files must be reviewed by the Infrastructure team before deployment.`
- Affected org: Engineering > Infrastructure
- Missing counterpart: Engineering > Infrastructure has no recorded obligation to review Backend database migration files before deployment. This obligation should appear in an Infrastructure-owned document.

## 4. Recommendations
- Create an Engineering-level document and move the peer review rule (and its child stating the one-reviewer minimum) there; remove the duplicates from Frontend and Backend documents.
- Confirm whether "Engineering manager" in the library approval rule refers to a role that spans all Engineering sub-teams; if so, elevate the rule to an Engineering-level document.
- Create an obligation in an Engineering > Infrastructure-owned document requiring Infrastructure to review Backend database migration files before deployment.
````

---

## Example 3: Gap detection and unattributed document

### Input: Org Map

```text
GlobalCorp
    Sales
        Enterprise Sales
        SMB Sales
    Support
    Finance
```

### Input: Two documents being audited

**Document A** — has Org Scope

````md
# Enterprise Sales Discount Policy

## 0. Org Scope
- Org Unit: Sales > Enterprise Sales

## 1. Purpose
Define discount authorization rules for Enterprise Sales.

## 3. Lex Scripta Body
```text
Discounts up to 15% may be granted by Enterprise Sales representatives.
    Discounts above 15% require Sales Director approval as defined in the company discount framework.
        Finance must be notified of any discount above 20%.
```
````

**Document B** — no Org Scope

````md
# Q3 Sales Targets

## 1. Purpose
Set revenue targets for the upcoming quarter.

## 3. Lex Scripta Body
```text
The Q3 revenue target is $4.2M.
    Enterprise Sales owns 60% of the target.
    SMB Sales owns 40% of the target.

Missed targets must be reported to Finance within five business days of quarter close.
```
````

### Output: Audit Report

````md
# Org Audit Report: Enterprise Sales Discount Policy and Q3 Sales Targets

## 1. Audit Context
- Org Map: GlobalCorp Org Map
- Documents audited: Enterprise Sales Discount Policy, Q3 Sales Targets
- Audit date: [Unspecified]

## 2. Summary
- Total issues found: 4
- MISPLACED: 0
- SHOULD_ELEVATE: 0
- SHOULD_DESCEND: 0
- CROSS_DEP: 1
- GAP: 2
- UNATTRIBUTED: 1

## 3. Issues

### [GAP] Company discount framework is referenced but not found
- Parent org: GlobalCorp or Sales
- Missing policy: A governing "company discount framework" that defines the Sales Director approval threshold and process for discounts above 15%.
- Assumed by: Sales > Enterprise Sales in `Discounts above 15% require Sales Director approval as defined in the company discount framework.`

### [GAP] Finance notification threshold rule has no parent policy
- Parent org: GlobalCorp or Finance
- Missing policy: A governing rule establishing that Finance must be notified of discounts above 20% and defining who is responsible for sending the notification.
- Assumed by: Sales > Enterprise Sales in `Finance must be notified of any discount above 20%.`

### [CROSS_DEP] Finance notification requires a Finance-side obligation
- Document: Enterprise Sales Discount Policy
- Org Scope: Sales > Enterprise Sales
- Statement: `Finance must be notified of any discount above 20%.`
- Affected org: Finance
- Missing counterpart: Finance has no recorded obligation to receive, log, or act on discount notifications above 20%. This obligation should appear in a Finance-owned document.

### [UNATTRIBUTED] Q3 Sales Targets has no Org Scope
- Document: Q3 Sales Targets
- Likely org: Sales [Borderline: could also fit GlobalCorp]
- Reason: The document governs targets for both Enterprise Sales and SMB Sales, suggesting ownership at the Sales level, but the targets may be set at the GlobalCorp level; org attribution requires confirmation.

## 4. Recommendations
- Create a Sales-level or GlobalCorp-level document defining the company discount framework, including the Sales Director approval process for discounts above 15%.
- Create a Finance-owned document or add an obligation to an existing Finance document requiring Finance to receive, log, and act on discount notifications above 20%.
- Add an Org Scope section to the Q3 Sales Targets document, declaring either Sales or GlobalCorp as the owner after confirming with the document author.
- Confirm whether the revenue target document belongs to the Sales org or to a GlobalCorp-level planning function.
````

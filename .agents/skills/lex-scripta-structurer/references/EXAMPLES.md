# Examples

## Example 1: Everyday conversation

### Source

```text
Stop sending the full weekly status email to everybody.
Team leads can still receive it every Friday.
Ops still needs incident alerts immediately.
Ava will rewrite the email template.
We have not decided whether contractors get the Friday summary.
```

### Output

````md
# Weekly Status and Incident Notification Rules

## 1. Purpose
Convert an informal team conversation into a structured notification document.

## 2. Defined Terms
- Friday summary: The reduced weekly status email sent on Fridays.
- Incident alert: An immediate operational message triggered by an incident event.

## 3. Lex Scripta Body
```text
The full weekly status email is no longer distributed to all recipients.
    Team leads may continue to receive a weekly summary every Friday.
    Operations must continue to receive incident alerts immediately.

Ava must rewrite the email template.
```

## 4. Open Items
- Whether contractors receive the Friday summary is [Needs confirmation].

## 5. Assumptions
- The Friday summary is narrower than the former full weekly status email.

## 6. Evidence / Notes
- `Ops still needs incident alerts immediately` was treated as an exception to the reduced distribution rule, not as a separate reporting policy.

## 7. Risks / Conflicts
- None.
````

## Example 2: Planning notes

### Source

```text
Beta next month.
Email-only signup first.
Phone verification later.
Enterprise customers might need company email verification.
Minji handles design.
Backend first.
Exact release date in the next meeting.
```

### Output

````md
# Beta Release and Signup Flow

## 1. Purpose
Convert rough planning notes into a structured release and signup document.

## 2. Defined Terms
- Enterprise customer: A customer account expected to use a company-managed email domain.

## 3. Lex Scripta Body
```text
The beta release is targeted for next month.
    The exact release date must be confirmed in the next meeting.

The initial signup flow follows a minimum-information rule.
    Only email is collected at signup.
    Phone verification is excluded from the initial beta scope.
        Enterprise customers may require company email verification.

Minji owns the design work.
Backend implementation is sequenced before dependent work.
```

## 4. Open Items
- The reference date for `next month` is [Unspecified].
- The threshold for `enterprise customer` is [Needs confirmation].

## 5. Assumptions
- The enterprise verification rule applies only if the account is categorized as enterprise.

## 6. Evidence / Notes
- `Backend first` was normalized as a sequencing rule rather than a staffing preference.

## 7. Risks / Conflicts
- None.
````

## Example 3: Policy-style input

### Source

```text
All employees must finish security training.
New hires need to finish it within two weeks.
If someone has a valid exception, HR can extend the deadline.
Extension requests should be recorded.
```

### Output

````md
# Security Training Requirement

## 1. Purpose
Structure a policy statement into a hierarchy of rule, timing, exception, and recordkeeping.

## 2. Defined Terms
- Valid exception: A circumstance accepted by HR as sufficient for deadline extension.

## 3. Lex Scripta Body
```text
All employees must complete security training.
    New hires must complete the training within two weeks of hire.
    HR may extend the deadline when a valid exception exists.
        Extension requests must be recorded.
```

## 4. Open Items
- The criteria for a valid exception are [Unspecified].

## 5. Assumptions
- None.

## 6. Evidence / Notes
- The recording duty was attached to the extension path because the source ties it to exception handling.

## 7. Risks / Conflicts
- None.
````

# Output Checklist

Run this checklist before returning the final document.

## Structure

- [ ] The document title reflects the actual subject.
- [ ] The section order is exactly:
      1. Purpose
      2. Defined Terms
      3. Lex Scripta Body
      4. Open Items
      5. Assumptions
      6. Evidence / Notes
      7. Risks / Conflicts
- [ ] The Lex Scripta Body is inside a fenced `text` block.
- [ ] Every indented line has a valid parent.

## Semantics

- [ ] Each line carries one claim only.
- [ ] Parent lines govern child lines in a meaningful way.
- [ ] Conditions, exceptions, dependencies, and approvals appear under the rule they modify.
- [ ] Background explanation does not appear inside the rule body.
- [ ] Unresolved questions are not hidden inside the rule body.

## Factual discipline

- [ ] No missing date, owner, approver, threshold, or legal effect was invented.
- [ ] Missing facts are marked as `[Unspecified]` or `[Needs confirmation]`.
- [ ] Relative time was converted only when a valid reference date exists.
- [ ] Competing statements were not silently merged into a false certainty.

## Language quality

- [ ] Terminology is stable.
- [ ] Vague terms were normalized when the source supported that normalization.
- [ ] The wording is concise and directive.
- [ ] Explanatory notes are short and necessary.

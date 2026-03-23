# BGS TODO

Boundary Governance Suite

This file is the working backlog for concrete changes still needed in
the suite and its member-framework examples.

Use it as an operational checklist:
- one problem per item
- exact files to edit
- what to remove
- what the final text should say

Do not use it as the authoritative definition of BGS. The authoritative
docs remain `SUITE.md`, `SUITE-MAP.md`, `BGS-COMPLIANCE.md`, and the
member-framework documents.

## 1. Finish making the suite role map explicit in entry docs

Edit:
- `README.md`

Do:
- add a short role-map summary at the top entry point
- make the first entry document reflect the same framework roles already used in `ONBOARDING.md`, `SUITE-MAP.md`, and `suite-map.json`

Remove:
- entry-point navigation that assumes the reader will discover the role map only later

Final text should say:
- `BGS` decides adoption
- `BISS` classifies boundaries
- `UCC` governs execution
- `UIC` governs preflight
- `TIC` governs verification
- `ASM` governs state modeling

## 2. Update the UCC example payloads

Edit:
- `example-claims/ucc-declaration-result.json`
- `example-claims/ucc-result.json`
- the claim files that reference them

Do:
- align the payloads with the current UCC/2.0 model
- keep the declaration/result shape canonical

Remove:
- `status`-style legacy shape if it is still acting as the primary model
- any custom wrapper that hides the canonical UCC fields

Final text should reflect:
- declaration
- observation
- outcome
- completion
- proof or diagnostics as appropriate

## 3. Add explicit BISS evidence

Edit:
- `BGS-COMPLIANCE.md`
- `example-claims/BGS-Execution.md`
- `example-claims/BGS-Governed-Verified.md`
- `example-claims/HOW-TO-AUTHOR-A-CLAIM.md`

Do:
- include an explicit BISS classification artifact or reference in the example claims
- explain what counts as BISS evidence

Remove:
- any assumption that naming `BISS` in `members_used` is enough on its own

Final text should say:
- BISS must be evidenced, not just mentioned
- evidence can be a classification table, decision record, or equivalent artifact

## 4. Add canonical examples for the ASM-based claimable slices

Edit:
- `example-claims/README.md`
- add new modeled-slice examples in `example-claims/`

Do:
- add at least one canonical example for `BGS-State-Modeled-Execution`
- add at least one canonical example for `BGS-State-Modeled-Governed`, or explicitly state that it is not yet exemplified
- include the ASM evidence artifact in the bundle

Remove:
- the implicit gap where claimable slices exist but have no example bundle

Final text should show:
- what a modeled execution claim bundle looks like
- how `ASM` evidence is attached alongside `BISS`, `UIC`, `UCC`, and `TIC` artifacts where applicable

## 5. Keep entry docs aligned with the canonical claim model

Edit:
- `README.md`
- `ONBOARDING.md`
- `DECISION-TREE.md`
- `AI-PROBLEM-MATRIX.md`
- `SCRIPT-QUALITY.md`
- `SUITE.md`
- `SUITE-MAP.md`
- `BGS-COMPLIANCE.md`
- `suite-map.json`

Do:
- make the adoption model read the same way in all entry docs
- keep the first-read path consistent
- keep the human and machine entry paths aligned
- keep the guidance docs clear about the difference between:
  - using a member framework locally
  - claiming a named BGS slice at suite level

Remove:
- wording differences that make the claim model feel inconsistent
- uses of "recommended BGS slice" that name overlays or member combos
  instead of actual BGS slice names

Final text should make the reader land on the same understanding from any entry point

## 6. Keep risk docs aligned with the role map

Edit:
- `AI-RISK-CONTROL-MAP.md`
- `AI-PROBLEM-MATRIX-OPERATIONS.md`
- `AI-PROBLEM-MATRIX-RELIABILITY.md`
- `AI-PROBLEM-MATRIX-SECURITY.md`
- `AI-PROBLEM-MATRIX-LEGAL.md`

Do:
- verify that each risk maps to the right member frameworks
- keep the same role meanings everywhere

Remove:
- any accidental redefinition of `BGS`, `BISS`, `UCC`, `UIC`, `TIC`, or `ASM`

Final text should preserve the same role map while describing risks

## 7. Clarify the relationship between `GAPS.md`, `STATUS.md`, and `TODO.md`

Edit:
- `STATUS.md`
- `GAPS.md`
- `TODO.md`

Do:
- make it explicit that `GAPS.md` tracks larger suite-definition gaps
- make it explicit that `TODO.md` tracks operational cleanup and alignment work
- make `STATUS.md` consistent with both

Remove:
- any ambiguity about why `GAPS.md` can say "resolved" while `TODO.md`
  still has open work

Final text should say:
- `GAPS.md` records major suite-definition gaps and their resolution state
- `TODO.md` records concrete follow-up work and alignment tasks
- `STATUS.md` summarizes the current state without contradicting either file

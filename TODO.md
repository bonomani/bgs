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

## 1. Make the suite role map explicit everywhere

Edit:
- `README.md`
- `ONBOARDING.md`
- `SUITE.md`
- `SUITE-MAP.md`
- `suite-map.json`

Do:
- add one consistent one-line role for each framework
- keep `BGS` as the adoption framework
- keep `BISS`, `UCC`, `UIC`, `TIC`, and `ASM` as distinct member roles
- mirror the same role map in the machine-readable suite map

Remove:
- wording that implies all frameworks use the same claim type
- wording that blurs adoption claims with execution or verification artifacts

Final text should say:
- `BGS` decides adoption
- `BISS` classifies boundaries
- `UCC` governs execution
- `UIC` governs preflight
- `TIC` governs verification
- `ASM` governs state modeling

## 2. Align naming and glossary guidance with the role map

Edit:
- `BGS-NAMING.md`
- `BGS-GLOSSARY.md`

Do:
- include `ASM` everywhere the canonical member list appears
- include `../asm/` everywhere the canonical member repo list appears
- include the modeled BGS slices where claim/profile naming is enumerated
- keep the naming docs clear that `BGS` is the suite and the others are member frameworks

Remove:
- member lists that omit `ASM`
- repo lists that omit `../asm/`
- naming examples that only reflect the older non-ASM slice set

Final text should say:
- `BGS` is the suite
- `BISS`, `UIC`, `UCC`, `TIC`, and `ASM` are member frameworks with different roles
- suite-level claim/profile wording covers the current slice set

## 3. Normalize claim field names across templates and examples

Edit:
- `BGS-DECISION-TEMPLATE.md`
- `BGS-VERSIONING.md`
- `example-claims/BGS-Execution.md`
- `example-claims/BGS-Governed-Verified.md`
- `example-claims/claim-bgs-execution-001.md`
- `example-claims/claim-bgs-governed-verified-001.md`
- `example-claims/HOW-TO-AUTHOR-A-CLAIM.md`

Do:
- replace legacy field names with the normative BGS fields
- make the examples mirror `BGS-COMPLIANCE.md`
- make the decision-record template match the compliance model

Remove:
- `claim_id`
- `profile`
- decision-record uses of `applies_to_scope`
- any old shortcut labels that are not part of the canonical claim shape

Final text should use:
- `decision_id`
- `bgs_slice`
- `declared_scope`
- `bgs_version_ref`
- `members_used`
- `overlays_used`
- `member_version_refs`
- `external_controls`
- `evidence_refs`

## 4. Align the project decision template with the compliance model

Edit:
- `BGS-DECISION-TEMPLATE.md`
- `BGS-COMPLIANCE.md`

Do:
- keep the project entry file fields distinct from the decision-record fields
- make the decision-record section list the same mandatory fields as the compliance doc
- make the example flow point to the correct artifact types

Remove:
- any drift between the decision template and `BGS-COMPLIANCE.md`

Final text should say:
- the entry file is a lightweight project pointer
- the decision record is the actual BGS claim artifact
- the two structures are related but not the same

## 5. Update the UCC example payloads

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

## 6. Add explicit BISS evidence

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

## 7. Extend versioning and freeze rules to ASM-based slices

Edit:
- `BGS-VERSIONING.md`
- `BGS-FREEZE.yaml`
- example claim files

Do:
- add `../asm/` to the member-repo versioning model
- add `ASM -> asm ref` to the member-version binding rules
- include `asm` in the freeze record
- make the versioning examples cover modeled slices cleanly

Remove:
- versioning examples that only reflect the older `ucc/uic/tic` set
- any implication that ASM-based slices do not need their own pinned member ref

Final text should show:
- exact suite ref
- exact member refs, including `asm` when `ASM` is used
- explicit version binding in every relevant claim example

## 8. Add canonical examples for the ASM-based claimable slices

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

## 9. Keep entry docs aligned with the canonical claim model

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

## 10. Keep risk docs aligned with the role map

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

## 11. Clarify the relationship between `GAPS.md`, `STATUS.md`, and `TODO.md`

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

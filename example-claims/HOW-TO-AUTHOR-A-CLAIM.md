# How to Author a BGS Claim

Use this checklist when creating a new BGS adoption claim.

1. Choose the slice.
- Pick one explicit BGS slice from `./BGS-COMPLIANCE.md`.
- Do not claim "BGS-compliant" without a named slice.

2. Define the scope.
- State the exact product, subsystem, workflow, execution path, or boundary.
- Keep the scope narrow enough that the claim can be checked.

3. List the member frameworks used.
- Include only the frameworks actually used in the scope.
- Match the selected slice and any optional overlays.

4. Pin immutable version refs.
- Add `bgs_version_ref`.
- Add the required `member_version_refs`.
- Use immutable refs only.

5. Declare external controls.
- State whether IAM, sandboxing, secret lifecycle, rate limiting, and privacy controls are implemented, delegated, not applicable, or missing.
- Do not imply that BGS replaces infrastructure security.

6. Attach evidence.
- Link to the preflight, execution, verification, or policy artifacts that support the claim.
- Evidence should match the selected slice.

7. Check against the example bundle.
- Compare the claim shape to `./BGS-Execution.md` and `./BGS-Governed-Verified.md`.
- If the new claim would break the examples, revise the examples and the claim together.

Minimal claim shape:

```yaml
decision_id: example-claim-001
bgs_slice: BGS-Execution
declared_scope: "specific workflow or boundary"
bgs_version_ref: bgs@<immutable-ref>
members_used:
  - BISS
  - UCC
overlays_used:
  - RIG
member_version_refs:
  ucc: ucc@<immutable-ref>
external_controls:
  IAM and authorization: implemented
  sandboxing or runtime isolation: delegated
  secret and token lifecycle: delegated
  rate limiting and budget control: implemented
  privacy and data-boundary control: delegated
evidence_refs:
  - ./some-evidence.md
  - ./some-result.json
```

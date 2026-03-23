# BGS-Execution Example

decision_id: claim-bgs-execution-001
bgs_slice: BGS-Execution
declared_scope: "UCC-based deployment workflow for the release pipeline"
bgs_version_ref: bgs@12e5d16
members_used:
  - BISS
  - UCC
overlays_used:
  - RIG
member_version_refs:
  ucc: ucc@1505204
external_controls:
  IAM and authorization: implemented
  sandboxing or runtime isolation: delegated
  secret and token lifecycle: delegated
  rate limiting and budget control: implemented
  privacy and data-boundary control: delegated
evidence_refs:
  - ./claim-bgs-execution-001.md
  - ./ucc-declaration-result.json

Notes:
- This example shows a minimal execution claim with one operational repo ref.
- The bundle includes a concrete execution result artifact and a claim stub.
- Chosen because the scope needs governed execution but not preflight
  gating or explicit verification.
- Excluded `UIC` and `TIC` because the example is intentionally below the
  governed-and-verified slice.

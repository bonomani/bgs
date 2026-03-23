# BGS-Governed-Verified Example

decision_id: claim-bgs-governed-verified-001
bgs_slice: BGS-Governed-Verified
declared_scope: "Prompt-to-change workflow for the support automation tool"
bgs_version_ref: bgs@12e5d16
members_used:
  - BISS
  - UIC
  - UCC
  - TIC
overlays_used:
  - Basic
member_version_refs:
  ucc: ucc@1505204
  uic: uic@a997340
  tic: tic@5f125a3
external_controls:
  IAM and authorization: implemented
  sandboxing or runtime isolation: implemented
  secret and token lifecycle: delegated
  rate limiting and budget control: implemented
  privacy and data-boundary control: implemented
evidence_refs:
  - ./claim-bgs-governed-verified-001.md
  - ./uic-preflight.json
  - ./ucc-result.json
  - ./tic-oracle.md

Notes:
- This example shows the full governed-and-verified stack.
- It includes preflight, execution, and verification artifacts in one declared scope.
- Chosen because the scope needs preflight gating, governed execution,
  and explicit verification.
- Excluded `GIC/GCC` as separate claim members because they are the
  semantic foundation rather than additional adoption scope here.

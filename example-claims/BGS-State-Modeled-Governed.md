# BGS-State-Modeled-Governed Example

decision_id: claim-bgs-state-modeled-governed-001
bgs_slice: BGS-State-Modeled-Governed
declared_scope: "State-modeled preflight and convergence for the payments worker service"
bgs_version_ref: bgs@5bcf949
members_used:
  - BISS
  - ASM
  - UIC
  - UCC
overlays_used:
  - Basic
member_version_refs:
  asm: asm@c7906b7
  ucc: ucc@963bd88
  uic: uic@429718d
external_controls:
  IAM and authorization: implemented
  sandboxing or runtime isolation: implemented
  secret and token lifecycle: delegated
  rate limiting and budget control: implemented
  privacy and data-boundary control: implemented
evidence_refs:
  - ./claim-bgs-state-modeled-governed-001.md
  - ./biss-classification-state-modeled-governed.md
  - ../../asm/SOFTWARE-MODEL.md
  - ../../asm/formal/software-state.schema.json
  - ../../asm/examples/valid-software-state.json
  - ../../asm/tools/validate_software_state.py
  - ./uic-state-modeled-governed-preflight.json
  - ./ucc-state-modeled-governed-declaration.json
  - ./ucc-state-modeled-governed-result.json

Notes:
- This example shows preflight and execution both depending on an explicit ASM-governed software-state model.
- The preflight artifact records admissibility checks against the target state before execution begins.
- The execution artifact then proves the resulting software state using the same state vocabulary.

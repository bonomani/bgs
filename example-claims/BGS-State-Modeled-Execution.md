# BGS-State-Modeled-Execution Example

decision_id: claim-bgs-state-modeled-execution-001
bgs_slice: BGS-State-Modeled-Execution
declared_scope: "State-modeled convergence of the support worker service"
bgs_version_ref: bgs@5bcf949
members_used:
  - BISS
  - ASM
  - UCC
overlays_used:
  - RIG
member_version_refs:
  asm: asm@c7906b7
  ucc: ucc@963bd88
external_controls:
  IAM and authorization: implemented
  sandboxing or runtime isolation: delegated
  secret and token lifecycle: delegated
  rate limiting and budget control: implemented
  privacy and data-boundary control: delegated
evidence_refs:
  - ./claim-bgs-state-modeled-execution-001.md
  - ./biss-classification-state-modeled-execution.md
  - ../../asm/SOFTWARE-MODEL.md
  - ../../asm/formal/software-state.schema.json
  - ../../asm/examples/valid-software-state.json
  - ../../asm/tools/validate_software_state.py
  - ./ucc-state-modeled-execution-declaration.json
  - ./ucc-state-modeled-execution-result.json

Notes:
- This example shows execution that depends on an explicit ASM-governed software-state model.
- The ASM evidence includes a profile document, schema, concrete state artifact, and executable validator.
- The UCC declaration and result use that state vocabulary directly in the governed target state.

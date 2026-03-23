# TIC Oracle

Scope:
- Prompt-to-change workflow for the support automation tool

Oracle:
- the workflow must pass through the approved preflight gate before the
  execution result is accepted
- the execution result must show that the declared workflow change was applied
  and completed
- the verification must preserve traceability to both the preflight and the
  execution artifact

Evidence checked:
- `./uic-preflight.json`
- `./ucc-governed-declaration.json`
- `./ucc-result.json`

Result:
- pass

Diagnostics:
- preflight gate approved before execution
- declared target state is explicit in the UCC declaration
- execution reached the declared desired state after a verified change
- trace links are present to both governed artifacts

# TIC Oracle

Scope:
- Prompt-to-change workflow for the support automation tool

Oracle:
- the workflow must pass through the approved preflight gate before the
  execution result is accepted
- the execution result must show convergence to the declared workflow change
- the verification must preserve traceability to both the preflight and the
  execution artifact

Evidence checked:
- `./uic-preflight.json`
- `./ucc-result.json`

Result:
- pass

Diagnostics:
- preflight gate approved before execution
- execution converged on the declared desired state
- trace links are present to both governed artifacts

# BISS Classification: BGS-State-Modeled-Governed Example

Scope:
- State-modeled preflight and convergence for the payments worker service

Boundary inventory:

| Boundary interaction | Crosses | Axis A | Axis B | Rationale |
| --- | --- | --- | --- | --- |
| Target-state admissibility gate | operator/policy layer -> deployment controller | GCC | Basic | The preflight step returns an explicit decision about whether the ASM-modeled target state may be executed, but it does not itself reconcile the service into that state. |
| Payments worker state reconciliation | deployment controller -> payments worker runtime | UCC | Basic | The execution step uses ASM state axes and transition legality to drive a declared target state to completion. |

Classification notes:
- The example combines a `GCC`-class preflight boundary with a `UCC`-class execution boundary.
- ASM constrains target-state admissibility and execution semantics, but it does not replace the Axis A classification.

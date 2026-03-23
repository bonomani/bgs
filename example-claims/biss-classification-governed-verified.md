# BISS Classification: BGS-Governed-Verified Example

Scope:
- Prompt-to-change workflow for the support automation tool

Boundary inventory:

| Boundary interaction | Crosses | Axis A | Axis B | Rationale |
| --- | --- | --- | --- | --- |
| Preflight approval and policy gate resolution | operator/policy layer -> automation controller | GCC | Basic | The preflight step produces an explicit opposable decision artifact, but it does not itself reconcile the target system into a desired end state. |
| Support workflow routing change | automation controller -> support workflow router | UCC | Basic | The execution step declares a desired state, computes the difference, and proves the resulting state after the change. |

Classification notes:
- The example uses both `GCC`-class and `UCC`-class boundary interactions inside one declared scope.
- `Basic` is the claimed rigor overlay for this example, so the internal quality grade is not elevated to `RIG`.
- `TIC` verification consumes the governed artifacts but is not itself the Axis A classification target for the execution boundary.

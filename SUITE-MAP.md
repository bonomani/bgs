# BGS Suite Map

Boundary Governance Suite

STATUS
------
Canonical suite-level composition map.
Member-framework documents remain authoritative for their own semantics.

PURPOSE
-------
This document defines the canonical suite map for BGS:
- which members exist at suite level
- which ones can stand alone
- how they compose
- which maturity signal each member currently carries
- which adoption slices are valid

This is the main human-readable suite map.
The machine-readable counterpart is `./suite-map.json`.

------------------------------------------------------------

1. MEMBER MATRIX
----------------

Repository hosting rule:
- suite membership is semantic
- repo membership is physical
- a single repo may host multiple member frameworks
- repo names do not have to match framework names one-to-one

| Member | Kind | Standalone | Semantic base | Common handoff or composition | Primary use in BGS | Maturity signal | Authoritative docs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BISS | Axis model | Yes | none | informs GIC, GCC, UIC, UCC, TIC, Basic, RIG | classify interaction type and separate contract type from rigor grade | Foundation | `../ucc/governance/BISS.txt` |
| GIC | Interaction foundation | Yes | none | may be used alone or as floor for GCC-style contracts | define observable interaction semantics | Foundation | `../ucc/contract-semantics/GIC.txt` |
| GCC | Contract foundation | Yes | GIC-compatible foundation layer | semantic floor below UIC and UCC | define explicit contract structure and closed results | Foundation | `../ucc/contract-semantics/GCC.txt` |
| Basic | Rigor grade | Yes | none | orthogonal overlay on implementations | minimal implementation rigor signal | Foundation | `../ucc/governance/BASIC.txt` |
| RIG | Rigor grade | Yes | none | orthogonal overlay on implementations | stronger implementation rigor and observability discipline | Foundation | `../ucc/governance/RIG.txt` |
| UIC | Operational contract | Yes | GIC + GCC foundations | hands off resolved gates, preferences, policies, and approvals to UCC when combined | govern preflight decisions before execution | Draft | `../uic/contract-semantics/UIC.txt`, `../uic/guidance/UIC-PREFLIGHT.txt` |
| UCC | Operational contract | Yes | GIC + GCC foundations | receives preflight decisions from UIC and may be verified by TIC | govern declaration-driven execution and convergence | Strong operational baseline | `../ucc/execution-semantics/UCC-EXECUTION.txt` plus the UCC execution, schema, and test corpus |
| ASM | State model | Yes | none | may supply explicit state axes, coherence rules, and transition semantics to UIC and UCC | define formal state modeling, composition, coherence, and allowed transitions | New member | `../asm/README.md`, `../asm/SOFTWARE-MODEL.md` |
| TIC | Verification contract | Yes | independent verification layer | verifies UIC, UCC, or other governed targets without changing their semantics | define tests, oracles, diagnostics, and traceability | Specified, suite integration partial | `../tic/SPEC.md` |

------------------------------------------------------------

2. CANONICAL HANDOFFS
---------------------

| From | To | Handoff artifact | Meaning at suite level |
| --- | --- | --- | --- |
| BISS | Any member | classification decision | chooses the interaction or rigor lens to apply |
| GIC | GCC | observable interaction floor | explicit contracts build on observable interaction discipline |
| GCC | UIC | contract discipline | preflight governance inherits explicit declaration and result discipline |
| GCC | UCC | contract discipline | convergence execution inherits explicit declaration and result discipline |
| ASM | UIC | state axes, coherence rules, admissible target states | gives preflight a formal vocabulary for approving or rejecting desired states when explicit state semantics matter |
| ASM | UCC | state axes, derived states, coherence rules, transition model | gives governed execution a formal state vocabulary for desired state, observed state, and transition legality |
| UIC | UCC | resolved gates, preferences, policies, approvals | determines whether execution may begin and under which declared constraints |
| UCC | TIC | declaration, observed state, result, proof, diagnostics | gives verification an explicit target and explicit result artifacts |
| Basic or RIG | Any implementation | rigor requirements, observability, testing expectations | overlays implementation discipline without changing interaction type |
| TIC | humans, CI, or audit layers | verified results and trace targets | exposes whether governed behavior matched the declared oracle |

------------------------------------------------------------

3. REPO HOSTING MAP
-------------------

| Repo | Hosted member frameworks |
| --- | --- |
| `../ucc/` | `BISS`, `GIC`, `GCC`, `Basic`, `RIG`, `UCC` |
| `../uic/` | `UIC` |
| `../asm/` | `ASM` |
| `../tic/` | `TIC` |

Interpretation rules:
- hosting is a repository fact, not a semantic equivalence
- a hosted framework can still be described independently at suite level
- hosted frameworks may later be split into separate repos without changing their suite identity
- keep a framework inside a host repo while it shares release cadence,
  ownership, and change surface with the other hosted frameworks
- split a framework into its own repo when any two of these become true: it needs an independent release cadence, it needs independent version refs for ordinary claims, it has a distinct owner or reviewer set, it has a distinct external audience or adoption slice, or it changes without the host repo's main lifecycle
- keep a framework bundled when only one of those conditions is true and the shared host remains the lower-friction model

------------------------------------------------------------

4. VALID ADOPTION SLICES
------------------------

`BGS-Classification` — Classification only
- `BISS`

`BGS-Foundation` — Contract foundation
- `GIC`
- `GCC`

`BGS-Execution` — Minimal governed convergence
- `BISS -> UCC`

`BGS-Governed` — Governed execution
- `BISS -> UIC -> UCC`

`BGS-Verified` — Verified execution
- `BISS -> UCC -> TIC`

`BGS-Governed-Verified` — Governed and verified execution
- `BISS -> UIC -> UCC -> TIC`

`BGS-State-Modeled-Execution` — Modeled governed execution
- `BISS -> ASM -> UCC`

`BGS-State-Modeled-Governed` — Modeled governed execution with preflight
- `BISS -> ASM -> UIC -> UCC`

Orthogonal overlay
- `Basic` or `RIG` may be applied to any of the above implementations

Interpretation rules:
- no slice is mandatory for every adopter
- `ASM` remains a standalone framework, but standalone ASM is not a claimable BGS adoption slice
- `ASM` should precede `UIC` and `UCC` when explicit state semantics are part of the declared scope
- stateful governed systems should test the `ASM`-based slices first when
  installation, configuration, runtime, readiness, recovery, or allowed
  transitions materially affect admissible behavior
- `UIC` is not required for `UCC`, but precedes `UCC` when both are used
- `TIC` may verify `UIC`, `UCC`, or other governed targets
- `Basic` and `RIG` do not change interaction type

------------------------------------------------------------

5. DEPENDENCY INTERPRETATION
----------------------------

BGS uses two different dependency concepts:

Semantic base
- The lower semantic layer that gives meaning to a higher one.
- At suite level, `UIC` and `UCC` sit above the `GIC/GCC` foundation layer.

Composition dependency
- A framework ordering that matters only when multiple members are used together.
- At suite level:
  - `UIC` comes before `UCC` when both are present.
  - `TIC` comes after or around governed behavior when verification is needed.
  - `Basic` and `RIG` remain orthogonal.

This distinction matters because BGS is not a single mandatory stack.
It is a suite of frameworks that can be used alone or composed explicitly.

------------------------------------------------------------

6. MATURITY AND ADOPTION ORDER
------------------------------

| Member or layer | Current signal | Recommended use now |
| --- | --- | --- |
| BISS | Foundation | Use as the classification lens early. |
| GIC and GCC | Foundation | Use as the semantic floor for explicit interactions and contracts. |
| UCC | Strong operational baseline | Best first operational target when you need governed execution now. |
| ASM | New member | Default toward ASM when governed scopes depend on lifecycle state, coherence, readiness, recovery, or transition legality. |
| TIC | Specified, suite integration partial | Add when explicit verification and traceable oracles matter. |
| UIC | Draft | Add after the operational baseline is clear, when you need governed preflight, approvals, or policy shaping. |
| Basic and RIG | Foundation and orthogonal | Apply continuously as implementation discipline overlays. |

Recommended adoption order by maturity and implementation risk:
1. `BISS` for classification
2. `UCC` for operationally governed execution
3. `ASM` by default when explicit state modeling or transition legality materially affects the declared scope
4. `TIC` for explicit verification
5. `UIC` when preflight governance is required
6. `Basic` or `RIG` as orthogonal rigor overlays throughout

------------------------------------------------------------

7. SCRIPT QUALITY SLICES
------------------------

Recommended local script baseline:
- `Basic`

Recommended claimable install-script slice:
- `BGS-Execution`

Upgrade path for install scripts:
- move to `BGS-Governed` when preflight gates or approvals are needed
- move to `BGS-Verified` when post-install verification or traceability is required
- move to `BGS-State-Modeled-Execution` or `BGS-State-Modeled-Governed` by default when install, configure, run, upgrade, repair, or recovery control depends on explicit software-state modeling

`SCRIPT-QUALITY.md` gives the operational minimum and maximum for these script classes.

------------------------------------------------------------

8. CANONICAL ENTRY POINTS
-------------------------

Human entry points:
1. `./SUITE.md`
2. `./BGS-NAMING.md`
3. `./BGS-GLOSSARY.md`
4. `./ONBOARDING.md`
5. `./SUITE-MAP.md`
6. `./BGS-VERSIONING.md`
7. `./BGS-FREEZE.yaml`
8. `./BGS-COMPLIANCE.md`
9. `../ucc/governance/BISS.txt`
10. `../uic/contract-semantics/UIC.txt`
11. `../ucc/execution-semantics/UCC-EXECUTION.txt`
12. `../asm/README.md`
13. `../tic/SPEC.md`
14. `./AI-RISK-CONTROL-MAP.md`
15. `./GAPS.md`
16. `./SCRIPT-QUALITY.md`

Machine-friendly entry points:
- `./suite-map.json`
- `./BGS-NAMING.md`
- `./BGS-GLOSSARY.md`
- `./ONBOARDING.md`
- `./BGS-VERSIONING.md`
- `./BGS-FREEZE.yaml`
- `./BGS-COMPLIANCE.md`
- `./AI-RISK-CONTROL-MAP.md`
- `./GAPS.md`
- `./SCRIPT-QUALITY.md`

------------------------------------------------------------

END OF DOCUMENT

# BGS Glossary

Boundary Governance Suite

STATUS
------
Canonical suite-level cross-framework glossary.

PURPOSE
-------
This document defines the small set of terms that BGS uses across
multiple member frameworks.

It exists to:
- reduce cross-repo vocabulary drift
- clarify suite-level usage
- avoid overloading terms that already exist inside member frameworks

Interpretation rule:
- this glossary governs suite-level wording only
- member-framework documents remain authoritative for their own internal
  semantics

------------------------------------------------------------

BOUNDARY
  The point where information, authority, or effects cross between
  components, systems, actors, or trust zones.
  In BGS, boundary semantics are the primary object of governance.

COMPOSITION DEPENDENCY
  A suite-level ordering rule that matters only when multiple member
  frameworks are used together.
  Example: `UIC` precedes `UCC` when both are present.

EXTERNAL CONTROL
  A control required around the suite but not defined as native BGS
  semantics.
  Examples: IAM, sandboxing, secret lifecycle, DLP, rate limiting.

EXECUTION
  The governed act of attempting to change real system state under an
  explicit contract.
  In BGS, execution is primarily governed by `UCC`.

GOVERNANCE
  The explicit structuring of what may happen, under which conditions,
  with which evidence, and with which traceability.
  In BGS, governance is broader than convergence and broader than
  testing alone.

MEMBER FRAMEWORK
  A semantic framework used by the suite.
  The canonical BGS member frameworks are:
  `BISS`, `GIC`, `GCC`, `Basic`, `RIG`, `UIC`, `UCC`, `TIC`.

MEMBER REPO
  A repository that contains one or more member frameworks participating
  in the suite layer.
  The current BGS member repos are `../ucc/`, `../uic/`, and `../tic/`.

OVERLAY
  A suite-level layer that augments discipline or quality without
  changing interaction type.
  In BGS, `Basic` and `RIG` are overlays.

PREFLIGHT
  The governed phase before execution begins, where gates, preferences,
  ambiguities, approvals, or policies are resolved into explicit
  artifacts.
  In BGS, preflight is primarily governed by `UIC`.

PROFILE
  A named suite-level adoption claim describing which BGS members are
  used together and what can validly be claimed from that adoption.
  Examples: `BGS-Execution`, `BGS-Governed-Verified`.

RIGOR
  The degree of internal implementation discipline applied to a system,
  independently of interaction type.
  In BGS, rigor is represented by `Basic` and `RIG`.

SEMANTIC BASE
  The lower semantic layer that gives meaning to a higher one.
  At suite level, `UIC` and `UCC` sit above the `GIC/GCC` foundation
  layer.

SUITE
  The BGS coordination layer as a whole.
  A suite is not a single mandatory stack and does not merge its member
  frameworks into one monolith.

TRACEABILITY
  The ability to connect a governed action, test, decision, or claim
  back to its declared basis, evidence, and scope.
  In BGS, traceability is a shared concern across `UIC`, `UCC`, `TIC`,
  and suite-level compliance claims.

VERIFICATION
  The explicit evaluation of whether observed behavior matches a stated
  oracle, rule, contract, or expectation.
  In BGS, verification is primarily governed by `TIC`.

------------------------------------------------------------

SOURCE ORIENTATION
------------------

Related authoritative sources:
- `../ucc/governance/BISS.txt`
- `../ucc/contract-semantics/GIC.txt`
- `../ucc/contract-semantics/GCC.txt`
- `../uic/guidance/UIC-PREFLIGHT.txt`
- `../ucc/execution-semantics/UCC-EXECUTION.txt`
- `../tic/SPEC.md`
- `../ucc/governance/GLOSSARY.txt`

------------------------------------------------------------

END OF DOCUMENT

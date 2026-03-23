# BGS Compliance

Boundary Governance Suite

STATUS
------
Draft suite-level decision model.
Applies to suite-level BGS adoption decisions only.

PURPOSE
-------
This document defines what it means to decide BGS adoption at suite level.

It specifies:
- valid BGS slices and adoption outcomes
- what each slice is allowed to decide
- what evidence is minimally required
- how external dependencies must be declared
- which decision records are invalid or misleading

This document does not replace the authoritative semantics of member
frameworks.
It only defines how suite-level adoption decisions must be expressed.

------------------------------------------------------------

1. CORE RULES
-------------

CR-1 No profileless decision
  No team, product, or system may say it uses BGS without naming an
  explicit BGS slice or decision outcome from this document.

CR-2 Scope must be declared
  Every BGS decision must declare the scope to which the decision
  applies. A decision may apply to:
  - a product
  - a subsystem
  - a workflow
  - an execution path
  - a connector or tool boundary

CR-3 Member frameworks must be named explicitly
  Every BGS decision must identify which suite members are actually
  used.

CR-4 External controls must be declared
  Every BGS decision must list the external controls it relies on for:
  - identity and access control
  - runtime isolation or sandboxing
  - secrets and token lifecycle
  - rate limiting or budget enforcement
  - privacy, DLP, or data-boundary controls

CR-5 Evidence must be attached
  Every BGS decision must point to concrete evidence artifacts.

CR-6 Rigor overlays are not standalone suite decisions
  `Basic` and `RIG` may be selected only as overlays on a declared BGS
  slice. They are not standalone BGS slices.

CR-7 Version references must be pinned
  Every decision must follow `./BGS-VERSIONING.md` and pin the suite-layer
  and member-framework refs it relies on by immutable reference.

CR-8 Project entry point must exist
  Every project adopting BGS should keep a project-level entry file that
  states the selected BGS slice, the reason for the choice, the scope it
  applies to, and the path to the supporting decision record.

CR-9 Decision and reason must be readable by agents
  The project entry file must be easy for an AI agent to read first and
  must clearly state which BGS guidance to apply next.

CR-10 No implicit self-application
  BGS does not apply to its own suite files, templates, or guidance by
  default. Any use of BGS to govern the BGS suite itself must be an
  explicit, separately recorded decision with its own scope, rationale,
  and evidence.

------------------------------------------------------------

2. VALID BGS SLICES
---------------------

Standalone use of `ASM` remains valid as framework adoption, but a
standalone ASM implementation is not a claimable BGS slice.

2.1 BGS-Classification
  Required members:
  - `BISS`

  Allowed decision:
  - boundary interactions are explicitly classified under the BISS axis

  Minimum evidence:
  - interaction inventory or classification table
  - classification rationale or decision record
  - pinned BISS reference

2.2 BGS-Foundation
  Required members:
  - `GIC` and/or `GCC`

  Optional members:
  - `BISS`

  Allowed decision:
  - the system uses explicit interaction and/or contract foundations

  Minimum evidence:
  - explicit interaction or contract specification
  - closed result model or equivalent declared result structure when GCC is claimed
  - pinned GIC/GCC reference

2.3 BGS-Execution
  Required members:
  - `BISS`
  - `UCC`

  Optional overlays:
  - `Basic`
  - `RIG`

  Allowed decision:
  - execution is governed by explicit declaration, observation, diff,
    decision, execution, and result semantics

  Minimum evidence:
  - declared execution scope
  - at least one declaration/result example or schema-conforming artifact
  - evidence that UCC result semantics are used
  - pinned UCC reference

2.4 BGS-Verified
  Required members:
  - `BISS`
  - `UCC`
  - `TIC`

  Optional overlays:
  - `Basic`
  - `RIG`

  Allowed decision:
  - governed execution is verified through explicit tests, oracles,
    diagnostics, and traceability

  Minimum evidence:
  - everything required for `BGS-Execution`
  - at least one TIC-style test artifact with explicit oracle
  - trace target(s) to the governing contract or rule
  - pinned TIC reference

2.5 BGS-Governed
  Required members:
  - `BISS`
  - `UIC`
  - `UCC`

  Optional overlays:
  - `Basic`
  - `RIG`

  Allowed decision:
  - execution is preceded by governed preflight decisions such as gates,
    preferences, policies, or explicit approvals

  Minimum evidence:
  - everything required for `BGS-Execution`
  - UIC preflight artifacts or equivalent gate results
  - explicit evidence of hard or soft gate behavior where applicable
  - pinned UIC reference

2.6 BGS-Governed-Verified
  Required members:
  - `BISS`
  - `UIC`
  - `UCC`
  - `TIC`

  Optional overlays:
  - `Basic`
  - `RIG`

  Allowed decision:
  - preflight governance, governed execution, and explicit verification
    are all present in the same declared scope

  Minimum evidence:
  - everything required for `BGS-Governed`
  - everything required for `BGS-Verified`

2.7 BGS-State-Modeled-Execution
  Required members:
  - `BISS`
  - `ASM`
  - `UCC`

  Optional overlays:
  - `Basic`
  - `RIG`

  Allowed decision:
  - execution is governed by explicit declaration and result semantics,
    and the governed state model is defined by ASM-compatible state
    axes, coherence rules, and transition legality

  Minimum evidence:
  - everything required for `BGS-Execution`
  - a state-model document, profile, or equivalent state specification
  - at least one concrete state artifact, schema, or executable validator
  - pinned ASM reference

2.8 BGS-State-Modeled-Governed
  Required members:
  - `BISS`
  - `ASM`
  - `UIC`
  - `UCC`

  Optional overlays:
  - `Basic`
  - `RIG`

  Allowed decision:
  - governed preflight and governed execution both rely on an explicit
    ASM-governed state model for admissible targets, coherence, or
    transition legality

  Minimum evidence:
  - everything required for `BGS-State-Modeled-Execution`
  - UIC preflight artifacts or equivalent target-state gate results
  - explicit evidence of hard or soft gate behavior where applicable
  - pinned UIC reference

------------------------------------------------------------

3. REQUIRED DECISION FIELDS
------------------------

Every BGS adoption decision must contain at least:
- `decision_id`
- `bgs_slice`
- `declared_scope`
- `bgs_version_ref`
- `members_used`
- `overlays_used`
- `member_version_refs`
- `external_controls`
- `evidence_refs`

Recommended additional fields:
- `owner`
- `date`
- `freeze_id`
- `limitations`
- `known exclusions`

Project entry file minimum fields:
- `project_name`
- `bgs_slice`
- `decision_reason`
- `applies_to_scope`
- `decision_record_path`
- `last_reviewed`
- `read_next`

------------------------------------------------------------

4. EXTERNAL CONTROL DECLARATION
-------------------------------

Every claim must explicitly state one of the following for each external
control class:
- implemented
- delegated
- not applicable
- missing

The minimum control classes are:
- IAM and authorization
- sandboxing or runtime isolation
- secret and token lifecycle
- rate limiting and budget control
- privacy and data-boundary control

This rule prevents teams from implying that BGS replaces infrastructure
security controls.

------------------------------------------------------------

5. PROJECT ENTRY FILE
--------------------

Recommended file path in a project repo:
- `./BGS.md`
- or `./docs/BGS.md`
- or `./docs/governance/BGS.md`

Minimum content:
- the BGS slice selected for the project
- why that slice was selected
- the scope it applies to
- where the decision record lives
- what the agent should read next

Template:

```md
# BGS Entry

project_name: example-project
bgs_slice: BGS-Execution
decision_reason: "AI-assisted workflow needs explicit request/result separation"
applies_to_scope: "backend task execution"
decision_record_path: "./docs/governance/bgs-decision.md"
last_reviewed: 2026-03-22
read_next:
  - "./API-CONTRACT.md"
  - "./tests/"
```

------------------------------------------------------------

6. FIT AND PARTIAL ADOPTION
---------------------------

BGS is a good fit when the scope involves one or more of these patterns:
- AI-assisted change that needs safer default behavior
- security-sensitive work that depends on explicit boundaries or secrets
- multi-repo or multi-tool handoffs that need traceability
- risk-managed automation that needs gates or review
- compliance-sensitive delivery that needs evidence-backed claims

If only some of those patterns apply, adopt BGS partially:
- use only the profiles that match the real workflow
- use only the member frameworks that solve the actual problem
- skip concepts that add overhead without direct utility

Examples of partial use:
- `BISS + ASM + UCC` for state-modeled governed execution
- `BISS + ASM + UIC + UCC` when preflight and execution both depend on an explicit state model
- `BISS` only for classification
- `BISS + UCC` for minimal governed convergence
- `BISS + UCC + TIC` for verified execution
- `BISS + UIC + UCC` when preflight governance matters

Examples of non-fit:
- ordinary app development with low overhead and no governance need
- teams that do not need formal claims or audit-ready artifacts
- simple projects where the structure slows delivery more than it helps

------------------------------------------------------------

7. DECISION RECORD EXAMPLE
-----------------

Example 1 — BGS-Execution

```yaml
decision_id: decision-example-project-001
bgs_slice: BGS-Execution
declared_scope: "backend task execution"
decision_reason: "AI-assisted workflow needs explicit request/result separation"
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
  - ./docs/governance/bgs-decision.md
  - ./docs/API-CONTRACT.md
  - ./tests/
```

Example 2 — BGS-Governed-Verified

```yaml
decision_id: decision-example-project-002
bgs_slice: BGS-Governed-Verified
declared_scope: "sensitive workflow execution"
decision_reason: "The workflow needs preflight gates and explicit verification"
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
  - ./docs/governance/bgs-decision.md
  - ./docs/preflight.json
  - ./tests/result.json
  - ./tests/oracle.md
```

------------------------------------------------------------

8. INVALID DECISIONS
-----------------

The following decisions are invalid:
- no named BGS slice
- `BGS-Verified` without `TIC`
- `BGS-Governed` without both `UIC` and `UCC`
- `BGS-Execution` without `UCC`
- `BGS-State-Modeled-Execution` without `BISS`, `ASM`, and `UCC`
- `BGS-State-Modeled-Governed` without `BISS`, `ASM`, `UIC`, and `UCC`
- selecting `RIG` alone as a BGS slice
- claiming full AI safety solely from BGS adoption
- claiming prompt injection, privacy, or privilege risk are eliminated
  without declaring external controls

The following decisions are misleading and should be avoided:
- claiming equal maturity across all suite members
- presenting external controls as if they were native BGS semantics
- presenting logs alone as proof of governed behavior

------------------------------------------------------------

9. MINIMAL DECISION EXAMPLE
------------------------

```yaml
decision_id: payments-agent-path-01
bgs_slice: BGS-Governed-Verified
declared_scope: outbound payment execution path
freeze_id: BGS-FREEZE-PREPUBLIC-2026-03-22-A
members_used:
  - BISS
  - UIC
  - UCC
  - TIC
overlays_used:
  - RIG
member_version_refs:
  BISS: ucc@1505204
  UIC: uic@a997340
  UCC: ucc@1505204
  TIC: tic@5f125a3
  RIG: ucc@1505204
bgs_version_ref: bgs@12e5d16
external_controls:
  iam_and_authorization: implemented
  sandboxing_or_runtime_isolation: implemented
  secret_and_token_lifecycle: implemented
  rate_limiting_and_budget_control: implemented
  privacy_and_data_boundary_control: delegated
evidence_refs:
  - preflight/gates/payment-approval.json
  - ucc/results/payment-run-042.json
  - tic/tests/payment-path.md
limitations:
  - does not claim privacy enforcement without external gateway controls
```

------------------------------------------------------------

10. INTERPRETATION RULE
----------------------

BGS adoption is not binary across an entire organization by default.
It is decision-based and scope-based.

That means:
- one subsystem may validly select `BGS-Execution`
- another may select `BGS-Governed-Verified`
- another may select no BGS slice at all

This is intentional.
BGS supports partial, explicit adoption rather than forcing one
all-or-nothing suite decision.

------------------------------------------------------------

END OF DOCUMENT

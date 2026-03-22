# BGS Compliance

Boundary Governance Suite

STATUS
------
Draft suite-level compliance model.
Applies to suite-level adoption claims only.

PURPOSE
-------
This document defines what it means to claim BGS adoption at suite level.

It specifies:
- valid BGS adoption profiles
- what each profile is allowed to claim
- what evidence is minimally required
- how external dependencies must be declared
- which claims are invalid or misleading

This document does not replace the authoritative semantics of member
frameworks.
It only defines how suite-level adoption claims must be expressed.

------------------------------------------------------------

1. CORE RULES
-------------

CR-1 No profileless compliance claim
  No team, product, or system may claim to be "BGS-compliant" without
  naming an explicit BGS profile from this document.

CR-2 Scope must be declared
  Every BGS claim must declare the scope to which the claim applies.
  A claim may apply to:
  - a product
  - a subsystem
  - a workflow
  - an execution path
  - a connector or tool boundary

CR-3 Member frameworks must be named explicitly
  Every BGS claim must identify which suite members are actually used.

CR-4 External controls must be declared
  Every BGS claim must list the external controls it relies on for:
  - identity and access control
  - runtime isolation or sandboxing
  - secrets and token lifecycle
  - rate limiting or budget enforcement
  - privacy, DLP, or data-boundary controls

CR-5 Evidence must be attached
  Every BGS claim must point to concrete evidence artifacts.

CR-6 Rigor overlays are not standalone suite claims
  `Basic` and `RIG` may be claimed only as overlays on a declared BGS
  adoption profile. They are not standalone BGS profiles.

CR-7 Version references must be pinned
  Until BGS defines a suite-wide version composition model, every claim
  must pin the member-framework versions it relies on by tag, commit, or
  immutable document reference.

------------------------------------------------------------

2. VALID BGS PROFILES
---------------------

2.1 BGS-Classification
  Required members:
  - `BISS`

  Allowed claim:
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

  Allowed claim:
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

  Allowed claim:
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

  Allowed claim:
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

  Allowed claim:
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

  Allowed claim:
  - preflight governance, governed execution, and explicit verification
    are all present in the same declared scope

  Minimum evidence:
  - everything required for `BGS-Governed`
  - everything required for `BGS-Verified`

------------------------------------------------------------

3. REQUIRED CLAIM FIELDS
------------------------

Every BGS adoption claim must contain at least:
- `claim_id`
- `profile`
- `declared_scope`
- `members_used`
- `overlays_used`
- `member_version_refs`
- `external_controls`
- `evidence_refs`

Recommended additional fields:
- `owner`
- `date`
- `limitations`
- `known exclusions`

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

5. INVALID CLAIMS
-----------------

The following claims are invalid:
- "BGS-compliant" with no named profile
- "BGS-Verified" without `TIC`
- "BGS-Governed" without both `UIC` and `UCC`
- "BGS-Execution" without `UCC`
- claiming `RIG` alone as a BGS adoption profile
- claiming full AI safety solely from BGS adoption
- claiming prompt injection, privacy, or privilege risk are eliminated
  without declaring external controls

The following claims are misleading and should be avoided:
- claiming equal maturity across all suite members
- presenting external controls as if they were native BGS semantics
- presenting logs alone as the proof of governed behavior

------------------------------------------------------------

6. MINIMAL CLAIM EXAMPLE
------------------------

```yaml
claim_id: payments-agent-path-01
profile: BGS-Governed-Verified
declared_scope: outbound payment execution path
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

7. INTERPRETATION RULE
----------------------

BGS compliance is not binary across an entire organization by default.
It is claim-based and scope-based.

That means:
- one subsystem may validly claim `BGS-Execution`
- another may claim `BGS-Governed-Verified`
- another may claim no BGS profile at all

This is intentional.
BGS supports partial, explicit adoption rather than forcing one
all-or-nothing suite claim.

------------------------------------------------------------

END OF DOCUMENT

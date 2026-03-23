# BGS Suite Definition

Boundary Governance Suite

VERSION
-------
0.1

STATUS
------
Draft coordination layer.
Not a replacement for the member frameworks.

------------------------------------------------------------

1. PURPOSE
----------

BGS exists to connect separate boundary-governance frameworks into one
coherent suite without collapsing them into a single monolith.

The suite is designed so that each framework can:
- live on its own
- be adopted independently
- be composed with the others in different stacks

BGS defines:
- the shared suite objective
- the suite-level sub-goals
- the canonical suite identity and naming rules
- the shared suite-level glossary
- the role of each member framework
- the composition rules between them
- the suite-level versioning and compatibility rules
- explicit freeze records when version numbering and published
  identifiers must remain stable through a draft or pre-public phase
- the suite-level compliance slices and claim rules
- the distinction between target-slice selection and evidenced claims
- the boundary between the suite layer and the member frameworks
- suite-level coverage maps when multiple frameworks and external
  controls must be explained together
- the expectation that member repos can evolve independently when their
  lifecycle, ownership, or release needs differ
- the default boundary that BGS applies to projects and workflows, not
  to the BGS suite itself unless a separate explicit decision says so

The canonical membership matrix, repo-hosting map, adoption slices,
and split policy live in `./SUITE-MAP.md`.

BGS does not redefine the internal semantics of UIC, UCC, TIC, ASM,
BISS, GIC, GCC, Basic, or RIG.

Interpretation rule:
- BGS slices are selected first as the smallest sufficient governance
  design for the declared scope and risks
- a BGS claim is made only after the required artifacts and evidence for
  that slice exist
- when the declared scope depends on meaningful lifecycle, readiness,
  runtime, recovery, or transition semantics, BGS should orient the
  target slice toward `ASM`

------------------------------------------------------------

2. PRIMARY GOAL
---------------

The primary goal of BGS is:

To govern AI-assisted and automated boundary interactions so they become
explicit, gated, bounded, verifiable, auditable, and supervisable.

In practical terms, BGS aims to ensure that:
- boundary interactions are explicitly classified
- operator choices and gates are resolved before execution
- authority, capabilities, and sensitive data access remain explicit and bounded
- untrusted external inputs, memory, and extensions are treated as governed inputs
  rather than as implicit instructions
- critical context is preserved in explicit artifacts rather than relying on
  model memory alone
- execution effects are constrained by explicit contracts
- retries, recursion, fan-out, and execution rate can be bounded and supervised
- verification is expressed with explicit oracles and traceability
- sensitive data crossing boundaries can be minimized, justified, and audited
- implementation rigor can be added without changing boundary semantics
- the suite remains readable to humans and structurally usable by AI agents
- the suite stays as simple as possible while providing direct utility
  that materially improves code and workflow quality
- the suite helps AI agents default toward clearer, safer, and more
  useful software behavior rather than ad hoc complexity

------------------------------------------------------------

3. SUB-GOALS
------------

BGS organizes the overall goal into sixteen suite-level sub-goals.

SG-1 Classification
  Classify boundary interactions explicitly and choose the right contract
  level for each case.

SG-2 Preflight governance
  Resolve gates, preferences, ambiguities, and pre-execution policies
  into stable preflight artifacts before execution begins.

SG-3 Deterministic execution
  Constrain execution so that the same declared target state and the same
  observed state produce the same observable result.

SG-4 Explicit state and effects
  Make desired state, observed state, critical inputs, relevant evidence,
  diffs, blockers, and outcomes explicit and reviewable.

SG-5 Verification and traceability
  Express tests with explicit intent, oracle, result, diagnostics,
  counterevidence, and trace links back to the rule or contract under test.

SG-6 Auditability and accountability
  Preserve enough structure to explain what was requested, what was
  allowed, what was executed, and what actually happened.

SG-7 Orthogonal rigor
  Allow stronger invariants, observability, and testing discipline to be
  added without forcing a change in interaction type.

SG-8 Composable adoption
  Make it possible to adopt only the frameworks needed for a given stack,
  while preserving clean upgrade paths toward richer governance.

SG-9 Human and agent friendliness
  Make the suite understandable to human readers and directly usable by
  AI agents through clear structure, explicit handoffs, stable entry
  points, and machine-usable references.

SG-10 Capability and access governance
  Keep authority, permissions, cross-tool handoffs, and destructive
  powers explicit, bounded, reviewable, and revocable rather than
  leaving them implicit in model behavior.

SG-11 Input provenance and memory hygiene
  Treat external content, retrieved memory, and installed extensions as
  governed inputs with explicit provenance, trust boundaries, and review
  points instead of silent instruction channels.

SG-12 Resource and loop control
  Bound retries, recursion, fan-out, rate, and execution persistence so
  that automated behavior remains governable and does not degrade into
  runaway loops or unintentional denial of service.

SG-13 Data minimization and confidentiality
  Minimize unnecessary data crossing boundaries and preserve enough
  structure to justify, review, and audit access to confidential,
  private, or sensitive information.

SG-14 Simplicity and direct utility
  Keep the suite as simple as possible while ensuring each rule or
  artifact has direct utility that materially improves code quality,
  workflow quality, or governed execution quality.

SG-15 Independent repo evolution
  Let each member repo evolve on its own schedule when its ownership,
  lifecycle, or release management needs differ from the rest of the suite.

SG-16 Helpful default behaviors
  Give AI agents simple default behaviors that bias toward clearer code,
  safer execution, explicit claims, and direct software improvement.

------------------------------------------------------------

4. SUITE MEMBERS
----------------

4.1 BISS / Axis Model
  Authority:
  `../ucc/governance/BISS.txt`

  Role in BGS:
  - classify interaction type
  - separate contract type from rigor grade
  - provide the suite's architectural frame

4.2 GIC / GCC Foundations
  Authority:
  `../ucc/contract-semantics/GIC.txt`
  `../ucc/contract-semantics/GCC.txt`

  Role in BGS:
  - provide the semantic base for observable interaction and explicit
    contracts
  - define the floor below UIC and UCC

4.3 Basic / RIG
  Authority:
  `../ucc/governance/BASIC.txt`
  `../ucc/governance/RIG.txt`

  Role in BGS:
  - describe implementation rigor independently from interaction type
  - keep internal quality orthogonal to contract semantics

4.4 UIC
  Authority:
  `../uic/contract-semantics/UIC.txt`
  `../uic/guidance/UIC-PREFLIGHT.txt`

  Role in BGS:
  - govern pre-convergence operator declarations
  - resolve gates, preferences, and preflight policy
  - shape whether and how UCC execution may begin

4.5 UCC
  Authority:
  `../ucc/execution-semantics/UCC-EXECUTION.txt`
  plus the rest of the `../ucc/` execution, schema, and test corpus

  Role in BGS:
  - govern declaration-driven execution and convergence
  - make observed state, desired state, diff, and result explicit
  - classify execution results in a closed result model

4.6 ASM
  Authority:
  `../asm/README.md`
  plus the applicable ASM profile documents such as:
  `../asm/SOFTWARE-MODEL.md`

  Role in BGS:
  - define a generic formal state model for systems
  - represent atomic and composite states
  - define coherence rules and allowed transitions
  - support software and non-software governed objects

4.7 TIC
  Authority:
  `../tic/SPEC.md`

  Role in BGS:
  - define how tests are declared, structured, executed, and reported
  - provide explicit oracles, diagnostics, and traceability
  - verify UIC, UCC, or other governed components without changing their
    semantics

------------------------------------------------------------

5. COMPOSITION RULES
--------------------

BGS defines the following suite-level composition rules:

CR-1 Separation
  The member frameworks remain separate. BGS must not absorb their
  authoritative semantics into a new combined specification.

CR-2 Explicit handoff
  Framework composition happens through explicit handoff, not implicit
  blending.

CR-3 UIC before UCC
  When both are used, UIC resolves before UCC convergence begins.

CR-4 TIC after or around governed behavior
  TIC verifies governed behavior. It does not redefine UIC or UCC.

CR-5 Rigor remains orthogonal
  Basic and RIG apply across implementations and do not replace the
  interaction-type frameworks.

CR-6 ASM remains a state-model layer
  When ASM is composed with UIC or UCC, it supplies explicit state
  vocabulary, coherence rules, and transition semantics.
  It does not replace preflight or execution semantics.

CR-6a Stateful governed systems default toward ASM
  When governed execution or preflight depends on explicit installation,
  configuration, runtime, readiness, repair, upgrade, recovery, or
  allowed-transition semantics, the suite should treat ASM as the
  default state layer rather than as a purely optional late addition.

CR-7 Partial adoption is valid
  A stack may adopt any subset or composition named in Section 6, as long
  as the chosen composition remains explicit.

------------------------------------------------------------

6. VALID ADOPTION SHAPES
------------------------

Classification-only stack:
  BISS

Contract-foundation stack:
  GIC and/or GCC

Minimal convergence stack:
  BISS classification -> UCC

Governed execution stack:
  BISS classification -> UIC -> UCC

Verified execution stack:
  BISS classification -> UCC -> TIC

Governed and verified execution stack:
  BISS classification -> UIC -> UCC -> TIC

State-modeled execution stack:
  BISS classification -> ASM -> UCC

State-modeled governed execution stack:
  BISS classification -> ASM -> UIC -> UCC

Orthogonal rigor:
  Basic or RIG may be applied to any of the above implementations.

------------------------------------------------------------

7. NON-GOALS
------------

BGS does not:
- merge the existing framework repos
- redefine UIC, UCC, or TIC internals
- force one mandatory full-stack adoption path
- turn every framework into a runtime dependency of every other
- claim that all member frameworks have the same maturity level
- optimize only for machine consumption at the expense of human clarity
- optimize only for prose readability at the expense of machine usability
- replace IAM, sandboxing, secret management, DLP, privacy controls,
  network controls, or token revocation systems
- guarantee elimination of prompt injection, malicious extension risk,
  or privilege abuse without external security controls
- solve model collapse or all reasoning-quality failures inside the model
- assign legal liability by itself

For fit, non-fit, and partial adoption rules, see `./BGS-COMPLIANCE.md`.

------------------------------------------------------------

8. REPOSITORY BOUNDARY
----------------------

Authoritative semantics remain in:
- `../asm/`
- `../ucc/`
- `../uic/`
- `../tic/`

This `./bgs/` folder is the suite layer only.
It exists to define:
- suite identity
- suite naming
- suite glossary
- suite objective
- suite-level composition
- the canonical suite map
- suite-level versioning
- suite-level freeze records
- suite-level compliance
- suite-level coverage maps
- suite-level gaps

When BGS text conflicts with an authoritative member-framework document,
the member-framework document wins for its own domain.

------------------------------------------------------------

END OF DOCUMENT

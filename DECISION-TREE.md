# BGS Decision Tree

Boundary Governance Suite

Use this as a first-pass recommendation guide.
It is intentionally simpler than the normative suite documents.
It assumes AI-assisted development as the default context for software work.
It recommends what should be implemented first.

Interpretation rule:
- when this guide names member frameworks such as `UCC` or `UIC + UCC`, it is describing a local implementation choice
- when this guide names `BGS-...`, it is describing a claimable suite slice
- all suite-level claims still follow `./BGS-COMPLIANCE.md`
- choose the target slice from the project's needs and risks first, not
  from the repo as-found
- make the suite-level claim only after the target slice is evidenced
- when governed behavior depends on meaningful lifecycle or transition
  state, default toward an `ASM`-based target slice

Start here:
1. What kind of software is this?
2. Does it change external state?
3. Does it need approvals, auditability, or explicit claims?
4. Do frontend and backend need to evolve independently?
5. Does the project involve AI-assisted actions or risky automation?

------------------------------------------------------------

1. GLOBAL RECOMMENDATION
------------------------

Default position:
- implement a BGS-aligned baseline first
- then add only the BGS members needed for the real risk profile
- keep the baseline small and useful

The baseline should usually include:
- explicit boundaries
- versioned contracts
- clear request/result separation
- structured logs or traces
- explicit tests and evidence where feasible

If the project performs any external side effect
or can benefit from future governance, auditability, or safer automation:

Recommendation:
- a named BGS slice or stronger

If the project needs:
- clearer boundaries
- versioned contracts
- explicit request/result separation
- but not formal governance claims

Recommendation:
- the smallest named BGS slice that is sufficient for the real need
- usually `BGS-Classification`, `BGS-Foundation`, or `BGS-Execution`

If the project needs:
- explicit execution semantics
- audit-friendly results
- testable outputs

Recommendation:
- `BGS-Execution`
- move toward `BGS-State-Modeled-Execution` when execution depends on
  installation, configuration, runtime, readiness, repair, upgrade, or
  recovery state rather than on a single flat target value

If the project needs:
- explicit desired and observed state semantics
- coherence rules or transition legality
- a formal state model tied to governed execution

Recommendation:
- `BGS-State-Modeled-Execution`
- use `BGS-State-Modeled-Governed` instead if preflight gates depend on
  admissible target-state rules

If the project needs:
- preflight gates, approvals, or policy checks
- before execution begins

Recommendation:
- `BGS-Governed`

If the project needs:
- explicit verification with tests and oracles

Recommendation:
- `BGS-Verified`

If the project needs:
- preflight governance and explicit verification together

Recommendation:
- `BGS-Governed-Verified`

------------------------------------------------------------

2. MAJOR SOFTWARE CLASSES
-------------------------

2.1 Static brochure site, blog, or ordinary frontend
- Implement only the smallest BGS baseline that still improves explicit
  boundaries, contracts, and logs
- Add `BISS` only if the frontend can trigger governed actions

2.2 Simple CRUD app
- Implement a lightweight baseline
- Use `BISS` for explicit interaction classification
- Use `UCC` if request/result discipline matters
- Add `ASM` only when the domain has meaningful lifecycle or transition
  state beyond ordinary request handling

2.3 Internal business app
- Implement `BISS` and `UCC`
- Add `UIC` only if approvals or gates matter
- Prefer `ASM` once business operations depend on explicit workflow or
  lifecycle state rather than only on imperative actions

2.4 Public product with normal API
- Implement `UCC` locally
- Claim `BGS-Execution` only when the boundary is explicitly classified with `BISS`
- Add `TIC` if API behavior needs strong test or oracle discipline

2.5 Download manager or task runner
- Implement `BISS` and `UCC`
- Add `TIC` for verification
- Add `UIC` only if downloads require approval or policy checks
- Prefer `ASM` when job lifecycle, retry state, readiness, or recovery
  semantics materially affect admissible execution

2.6 AI-assisted workflow
- Implement `BISS + UCC` as the minimum
- Add `UIC` if the AI must pass gates before acting
- Add `TIC` if you need explicit verification
- Use `BGS-Governed` when preflight control matters
- Prefer `ASM` when the workflow depends on explicit staged state,
  admissible targets, or transition legality

2.7 Security-sensitive automation
- Implement `UIC + UCC` locally
- Claim `BGS-Governed` or `BGS-Governed-Verified` only when `BISS` classification is explicit
- Add `TIC` for audit-friendly verification
- Use `BGS-Governed` or `BGS-Governed-Verified`
- Prefer `BGS-State-Modeled-Governed` when approvals, execution, or
  verification depend on explicit system state and allowed transitions

2.8 Risk-managed or compliance-sensitive system
- Implement `BGS-Governed-Verified`
- Use claims, immutable refs, and evidence
- Keep external controls explicit
- Prefer an `ASM`-based slice when the scope is stateful across install,
  configure, run, degrade, recover, or verify phases

2.9 Multi-repo or multi-tool platform
- Implement the smallest BGS slice that coordinates the handoffs
- Use repo-hosting and split policy from `SUITE-MAP.md`

Selection rule:
- pick the smallest sufficient target slice for the scope first
- then implement and evidence it
- do not back-fit the target slice only from the current repo state
- for governed systems with meaningful lifecycle or transition state,
  start by testing whether an `ASM`-based slice is the right target

------------------------------------------------------------

3. MODULE SELECTION
-------------------

Interpretation rule:
- this section recommends member-framework adoption, not claimable BGS slices by itself
- map the planned member set to the smallest sufficient target slice in `./BGS-COMPLIANCE.md`
- make the suite-level claim only when that target slice is actually evidenced

If you need only one thing:
- classification -> implement `BISS`
- execution semantics -> implement `UCC`
- preflight approval -> implement `UIC`
- verification -> implement `TIC`
- formal state modeling -> implement `ASM`
- rigor overlay -> add `Basic` or `RIG`

If you need two things:
- classification + execution -> implement `BISS + UCC`
- execution + verification -> implement `UCC + TIC`
- preflight + execution -> implement `UIC + UCC`
- state modeling + execution -> implement `ASM + UCC`
- state modeling + preflight -> implement `ASM + UIC`

If you need full governance:
- implement `BISS + UIC + UCC + TIC`

If you need governed stateful execution:
- implement `BISS + ASM + UCC`
- add `UIC` when admissible targets or gates depend on the state model
- add `TIC` when the resulting state must be explicitly verified

------------------------------------------------------------

4. WHAT NOT TO ADOPT
--------------------

Do not adopt BGS concepts that:
- do not improve the codebase or workflow directly
- do not change behavior, boundaries, or evidence quality
- add process overhead without solving a real problem
- duplicate existing project norms without adding value

------------------------------------------------------------

5. RULE OF THUMB
-----------------

Use BGS only to the extent that it helps the project:
- stay explicit
- stay versioned
- stay testable
- stay auditable
- stay simpler in practice, not more complicated

If BGS does not improve those outcomes, do not use more of it.

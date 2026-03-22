# BGS Decision Tree

Boundary Governance Suite

Use this as a first-pass recommendation guide.
It is intentionally simpler than the normative suite documents.
It assumes AI-assisted development as the default context for software work.
It recommends what should be implemented first.

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
- `Light BGS` or stronger

If the project needs:
- clearer boundaries
- versioned contracts
- explicit request/result separation
- but not formal governance claims

Recommendation:
- `Light BGS` meaning only the smallest useful subset
- usually `BISS` and/or `UCC`

If the project needs:
- explicit execution semantics
- audit-friendly results
- testable outputs

Recommendation:
- `BGS-Execution`

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

2.3 Internal business app
- Implement `BISS` and `UCC`
- Add `UIC` only if approvals or gates matter

2.4 Public product with normal API
- Implement `UCC`
- Add `TIC` if API behavior needs strong test or oracle discipline

2.5 Download manager or task runner
- Implement `BISS` and `UCC`
- Add `TIC` for verification
- Add `UIC` only if downloads require approval or policy checks

2.6 AI-assisted workflow
- Implement `BISS + UCC` as the minimum
- Add `UIC` if the AI must pass gates before acting
- Add `TIC` if you need explicit verification
- Use `BGS-Governed` when preflight control matters

2.7 Security-sensitive automation
- Implement `UIC + UCC`
- Add `TIC` for audit-friendly verification
- Use `BGS-Governed` or `BGS-Governed-Verified`

2.8 Risk-managed or compliance-sensitive system
- Implement `BGS-Governed-Verified`
- Use claims, immutable refs, and evidence
- Keep external controls explicit

2.9 Multi-repo or multi-tool platform
- Implement the smallest BGS slice that coordinates the handoffs
- Use repo-hosting and split policy from `SUITE-MAP.md`

------------------------------------------------------------

3. MODULE SELECTION
-------------------

If you need only one thing:
- classification -> implement `BISS`
- execution semantics -> implement `UCC`
- preflight approval -> implement `UIC`
- verification -> implement `TIC`
- rigor overlay -> add `Basic` or `RIG`

If you need two things:
- classification + execution -> implement `BISS + UCC`
- execution + verification -> implement `UCC + TIC`
- preflight + execution -> implement `UIC + UCC`

If you need full governance:
- implement `BISS + UIC + UCC + TIC`

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

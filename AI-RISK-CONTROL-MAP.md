# BGS AI Risk and Control Map

Boundary Governance Suite

STATUS
------
Draft suite-level compatibility map.
Not normative for member-framework semantics.

PURPOSE
-------
This document explains:
- which AI-agent risk classes BGS can govern directly
- which risk classes require hybrid treatment with external controls
- where common mitigations belong across BISS, UIC, UCC, ASM, TIC, Basic/RIG,
  and external systems

This document exists to prevent overclaim.
BGS governs boundary classification, preflight, execution constraints,
state modeling, verification, traceability, and explicit gates.
BGS does not replace IAM, sandboxing, DLP, network controls, privacy
enforcement, token revocation, or legal governance.

READING KEY
-----------
Problem coverage:
- DIRECT: BGS can express and govern this class directly at the suite level
- HYBRID: BGS helps significantly, but external controls remain required
- EXTERNAL: this class is mostly outside BGS and must be handled elsewhere

Solution compatibility:
- NATIVE: fits directly into one or more BGS member frameworks
- COMPOSABLE: external control that integrates cleanly with BGS
- CONDITIONAL: compatible only if converted into explicit governed artifacts
- ORTHOGONAL: useful, but mostly independent of BGS semantics
- TENSION: common use of the solution conflicts with BGS principles unless
  reframed

------------------------------------------------------------

1. PROBLEM-CLASS COVERAGE
-------------------------

| Problem class | Coverage | Primary BGS members | External controls still required | Notes |
| --- | --- | --- | --- | --- |
| Indirect prompt injection | HYBRID | BISS, UIC, TIC | input isolation, sandboxing, taint-style controls, connector allowlists | BGS can force external content to be treated as governed input, but it cannot guarantee perfect detection of hostile instructions. |
| Confused deputy and privilege escalation | HYBRID | BISS, UIC, UCC | IAM, RBAC, capability isolation, sandboxing, secret management | BGS can make authority and approvals explicit, but permission enforcement must exist outside the suite. |
| Malicious extensions and supply chain compromise | HYBRID | UIC, TIC, Basic/RIG | signing, scanning, provenance, marketplace review, isolation | BGS can require provenance and verification artifacts, but trust in extension binaries or services is external. |
| Token persistence and stale access | EXTERNAL | UIC | token revocation, IAM lifecycle, secret rotation | BGS can gate use of credentials, not revoke them after the fact. |
| Memory poisoning and cache poisoning | HYBRID | UIC, TIC | trusted memory architecture, provenance tracking, isolation, retention policy | BGS can require memory to be treated as explicit input with reviewable provenance. |
| Action hallucination | DIRECT | UCC, TIC, UIC | implementation validation for concrete tools | UCC strongly mitigates invented commands by separating declaration from execution and rechecking observed state. |
| Critical omission and context loss | HYBRID | UIC, TIC, Basic/RIG | context management, retrieval quality controls, operator review | BGS helps by turning critical decisions and evidence into explicit artifacts instead of relying on model memory alone. |
| Automated confirmation bias | HYBRID | TIC, UIC | independent reviewers, adversarial tests, diverse evidence sources | TIC can require explicit oracles and counterevidence, but BGS does not fix model cognition. |
| Database pollution and mass incorrect writes | HYBRID | UIC, UCC, TIC | business validation, scoped permissions, rollout controls | BGS can constrain writes through gates, diffs, and explicit results, but bad source data can still drive bad declarations. |
| Agent loops and runaway recursion | HYBRID | UCC, UIC | rate limits, budgets, orchestrator controls, queue policy | BGS can bound retries and make execution explicit, but system-wide loop prevention needs external coordination. |
| Nondeterministic execution | DIRECT | UCC, TIC | deterministic implementation discipline | UCC is explicitly designed to make execution behavior repeatable for the same declaration and observed state. |
| Unintentional DoS and cost explosion | HYBRID | UIC, UCC | rate limiting, quotas, budget enforcement, queue backpressure | BGS can expose and govern retries and fan-out, but hard enforcement is external. |
| Accountability gaps | HYBRID | UCC, TIC, Basic/RIG | policy, legal process, record retention, audit storage | BGS can produce explicit factual traceability, but legal responsibility is outside its scope. |
| IP leakage and privacy violations | HYBRID | BISS, UIC, UCC | DLP, privacy gateways, data classification, local deployment, network policy | BGS can minimize and justify boundary crossings, but confidentiality enforcement remains external. |
| Model collapse | EXTERNAL | none | data curation, source governance, training policy | This is outside the suite's execution and verification focus. |

------------------------------------------------------------

2. SOLUTION COMPATIBILITY MAP
-----------------------------

| Solution | Compatibility | Primary location | Supporting BGS members | Conditions and caveats |
| --- | --- | --- | --- | --- |
| Process sandboxing | COMPOSABLE | External runtime control | UIC, UCC | Strong fit. The agent or engine may run inside a sandbox, but the sandbox is not a BGS semantic layer. Capabilities exposed by the sandbox should remain explicit to the suite. |
| AI-focused RBAC | COMPOSABLE | External IAM and authorization layer | UIC, BISS | Strong fit. Best used with least privilege by default and explicit authorization gates for writes or destructive actions. |
| Intention interceptor | CONDITIONAL | UIC preflight gate or policy layer | TIC | Compatible only if the interceptor emits explicit, reviewable gate outcomes or evidence. It should not become an opaque hidden authority that silently decides truth. |
| Input isolation and pre-processing | COMPOSABLE | External ingestion boundary | BISS, UIC | Strong fit. Sanitized or classified input should still retain provenance and should be passed into the suite as governed input, not as invisible context. |
| RAG with evidence | CONDITIONAL | TIC evidence and oracle support | UIC, Basic/RIG | Compatible when citations support claims, operator decisions, or tests. It must not replace UCC observation of real system state. |
| Multi-agent debate or self-correction | CONDITIONAL | External reasoning layer upstream of execution | UIC, TIC | Compatible as a reasoning aid only. The debate output must become an explicit declaration, gate result, or test artifact before any governed execution happens. |
| Static analyzers, linters, and code verifiers | NATIVE | TIC test layer or UIC hard gates | Basic/RIG | Strong fit. These tools naturally act as explicit tests or blocking preflight checks. |
| Watermarking of AI-produced data | ORTHOGONAL | External provenance control | TIC | Compatible, but mostly outside BGS semantics. It can support knowledge hygiene or content provenance, yet it is weak as an execution control. |
| Rate limiting | COMPOSABLE | External orchestrator, queue, or API gateway | UIC, UCC | Strong fit. The suite can consume budget or throttle state as input, but enforcement should happen in infrastructure. |
| Selective HITL approval | NATIVE | UIC | TIC | Very strong fit. Human approval points are naturally expressed as explicit hard gates before execution. |
| Immutable audit storage | CONDITIONAL | External record and retention layer | UCC, TIC, Basic/RIG | Compatible when it stores structured declarations, approvals, results, proofs, and diagnostics. It is in tension with BGS if "every thought" log entries are treated as authoritative truth. |
| Persistent context manager | CONDITIONAL | External memory and retrieval layer | UIC, TIC | Compatible only if memory is treated as governed input with provenance, versioning, and review boundaries. It is a bad fit if memory silently overrides explicit suite artifacts. |
| Privacy gateways | COMPOSABLE | External DLP or privacy boundary | UIC, BISS | Strong fit. Best used to enforce minimization before sensitive data crosses an external boundary. |
| Community skill audits | COMPOSABLE | External supply-chain governance | TIC, Basic/RIG, UIC | Compatible. Signing, scanning, and trust policy stay external, while BGS can require explicit provenance and verification of what a skill is allowed to do. |
| Local or edge-hosted models | ORTHOGONAL | Deployment architecture | UIC, BISS | Compatible and often useful for confidentiality, but not a substitute for gates, contracts, verification, or auditability. |

------------------------------------------------------------

3. PRACTICAL INTERPRETATION
---------------------------

Recommended high-risk composition:
- BISS for explicit boundary classification
- external sandboxing, IAM, rate limiting, and privacy controls
- UIC for explicit gates, approvals, and preflight policy
- UCC for bounded execution and explicit results
- ASM when admissible target states, coherence rules, or transition legality
  must be explicit
- TIC for oracles, counterevidence, and verification
- Basic or RIG for implementation discipline

Bad composition patterns:
- using an opaque intention classifier as a hidden source of truth
- treating vector memory as authoritative policy
- treating raw logs or chain-of-thought as contractual evidence
- assuming local models remove the need for governance

Rule of thumb:
- if a control changes who may act or what may cross a boundary, it often
  composes with UIC
- if a control constrains actual state-changing behavior, it often composes
  with UCC
- if a control verifies claims, code, or outcomes, it often composes with TIC
- if a control enforces infrastructure security or privacy policy, it usually
  remains external to BGS

------------------------------------------------------------

END OF DOCUMENT

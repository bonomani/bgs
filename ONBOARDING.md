# BGS Onboarding

Boundary Governance Suite

Purpose:
- BGS is a coordination layer for separate boundary-governance frameworks.
- It keeps the frameworks separate while defining how they compose.
- It does not merge semantics or move authoritative files out of member repos.
- In this workspace, development is assumed to be AI-assisted by default.

Read this first:
1. `./README.md`
2. `./SUITE-MAP.md`
3. `./AI-AGENT-WORKFLOW.md`
4. `./DECISION-TREE.md`
5. `./AI-PROBLEM-MATRIX.md`
6. `./BGS-COMPLIANCE.md`
7. `./BGS-DECISION-TEMPLATE.md`
8. `./SCRIPT-QUALITY.md`

Core concepts:
- `BGS` is the suite.
- `BISS`, `GIC`, `GCC`, `Basic`, `RIG`, `UIC`, `UCC`, `ASM`, and `TIC` are member frameworks.
- `../ucc/`, `../uic/`, `../asm/`, and `../tic/` are member repos.
- One repo may host multiple member frameworks.
- Suite membership is semantic; repo membership is physical.

Use cases:
- `BISS` classifies boundary interactions.
- `GIC` and `GCC` provide the semantic foundation.
- `UIC` governs preflight decisions before execution.
- `UCC` governs declaration-driven execution and convergence.
- `ASM` governs formal state modeling, composition, and transitions.
- `TIC` verifies governed behavior with explicit tests and oracles.
- `Basic` and `RIG` are orthogonal rigor overlays.

Common member compositions:
- `BISS -> ASM -> UCC` for state-modeled governed execution.
- `BISS -> ASM -> UIC -> UCC` for state-modeled governed execution with preflight.
- `BISS -> UCC` for minimal governed convergence.
- `BISS -> UIC -> UCC` for governed execution.
- `BISS -> UCC -> TIC` for verified execution.
- `BISS -> UIC -> UCC -> TIC` for governed and verified execution.

For claimable suite slices, see:
- `./BGS-COMPLIANCE.md`

What to use for what:
- `README.md`: entry point and navigation.
- `SUITE.md`: suite semantics and composition rules.
- `SUITE-MAP.md`: canonical matrix, hosting map, and split policy.
- `STATUS.md`: stable versus draft snapshot.
- `AI-AGENT-WORKFLOW.md`: progressive narrowing workflow for AI agents.
- `BGS-VERSIONING.md`: immutable refs and compatibility rules.
- `AI-PROBLEM-MATRIX.md`: common AI-agent problem classes mapped to BGS.
- `BGS-COMPLIANCE.md`: decision rules and project entry requirements.
- `BGS-DECISION-TEMPLATE.md`: minimum project entry file and decision-record template.
- `SCRIPT-QUALITY.md`: minimum, maximum, and local-baseline versus claimable-slice guidance for scripts.
- `AI-RISK-CONTROL-MAP.md`: what BGS can govern directly and what still needs external controls.
- `example-claims/README.md`: canonical claim bundle.

For fit, non-fit, and partial adoption rules, see:
- `./SUITE.md`
- `./BGS-COMPLIANCE.md`

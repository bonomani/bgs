# BGS

Boundary Governance Suite

BGS is a suite-level coordination layer for the boundary frameworks that
already exist in this workspace.

It defines the suite's common objective, naming, composition, versioning,
compliance, and navigation rules without merging the member frameworks or
moving their files.

Role map:
- `BGS` = adoption decision framework
- `BISS` = boundary classification framework
- `UCC` = execution contract
- `UIC` = preflight contract
- `TIC` = verification contract
- `ASM` = state model

Selection rule:
- first choose the smallest sufficient target slice for the declared
  scope, risk, and governance need
- then implement the required member artifacts and evidence
- claim the slice only when that evidence exists

State-model rule:
- when the declared scope depends on meaningful software or system state
  such as installation, configuration, runtime, readiness, recovery, or
  transition legality, orient the target slice toward `ASM`

Start here:
1. `./SUITE.md`
2. `./SUITE-MAP.md`
3. `./ONBOARDING.md`
4. `./AI-AGENT-WORKFLOW.md`
5. `./DECISION-TREE.md`
6. `./AI-PROBLEM-MATRIX.md`
7. `./STATUS.md`
8. `./BGS-COMPLIANCE.md`
9. `./BGS-DECISION-TEMPLATE.md`
10. `./SCRIPT-QUALITY.md`
11. `../asm/README.md`

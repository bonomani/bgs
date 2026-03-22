# BGS

Boundary Governance Suite

BGS is a suite-level coordination layer for the boundary frameworks that
already exist in this workspace.

BGS does not replace them.
BGS does not merge them.
BGS does not move their files.

Its role is to define the common objective, composition rules, and
navigation between the separate frameworks.

Current suite members:
- `../ucc/`
- `../uic/`
- `../tic/`

Current authoritative foundations referenced by BGS:
- `../ucc/governance/BISS.txt`
- `../ucc/contract-semantics/GIC.txt`
- `../ucc/contract-semantics/GCC.txt`
- `../ucc/governance/BASIC.txt`
- `../ucc/governance/RIG.txt`
- `../uic/contract-semantics/UIC.txt`
- `../ucc/execution-semantics/UCC-EXECUTION.txt`
- `../tic/SPEC.md`

Read in this order:
1. `./SUITE.md`
2. `./SUITE-MAP.md`
3. `../ucc/governance/BISS.txt`
4. `../uic/contract-semantics/UIC.txt`
5. `../ucc/execution-semantics/UCC-EXECUTION.txt`
6. `../tic/SPEC.md`
7. `./AI-RISK-CONTROL-MAP.md`
8. `./GAPS.md`

Machine-friendly entry points:
- `./suite-map.json`
- `./AI-RISK-CONTROL-MAP.md`
- `./GAPS.md`

Design rules:
- keep frameworks separate
- let each framework remain usable on its own
- compose frameworks through explicit handoffs
- keep authoritative semantics in the existing framework repos
- let BGS define the glue, not duplicate the internals
- keep suite entry points understandable by humans and usable by AI agents

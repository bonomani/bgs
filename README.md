# BGS

Boundary Governance Suite

BGS is a suite-level coordination layer for the boundary frameworks that
already exist in this workspace.

BGS does not replace them.
BGS does not merge them.
BGS does not move their files.

Its role is to define the common objective, composition rules, and
navigation between the separate frameworks.

Current member repos:
- `../ucc/`
- `../uic/`
- `../tic/`

The suite-level member frameworks are defined canonically in:
- `./SUITE-MAP.md`

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
2. `./BGS-NAMING.md`
3. `./BGS-GLOSSARY.md`
4. `./SUITE-MAP.md`
5. `./BGS-COMPLIANCE.md`
6. `../ucc/governance/BISS.txt`
7. `../uic/contract-semantics/UIC.txt`
8. `../ucc/execution-semantics/UCC-EXECUTION.txt`
9. `../tic/SPEC.md`
10. `./AI-RISK-CONTROL-MAP.md`
11. `./GAPS.md`

Machine-friendly entry points:
- `./suite-map.json`
- `./BGS-NAMING.md`
- `./BGS-GLOSSARY.md`
- `./BGS-COMPLIANCE.md`
- `./AI-RISK-CONTROL-MAP.md`
- `./GAPS.md`

Design rules:
- keep frameworks separate
- let each framework remain usable on its own
- compose frameworks through explicit handoffs
- keep authoritative semantics in the existing framework repos
- let BGS define the glue, not duplicate the internals
- keep suite entry points understandable by humans and usable by AI agents

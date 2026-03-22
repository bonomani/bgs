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
5. `./BGS-VERSIONING.md`
6. `./BGS-FREEZE.yaml`
7. `./BGS-COMPLIANCE.md`
8. `../ucc/governance/BISS.txt`
9. `../uic/contract-semantics/UIC.txt`
10. `../ucc/execution-semantics/UCC-EXECUTION.txt`
11. `../tic/SPEC.md`
12. `./AI-RISK-CONTROL-MAP.md`
13. `./GAPS.md`

Machine-friendly entry points:
- `./suite-map.json`
- `./BGS-NAMING.md`
- `./BGS-GLOSSARY.md`
- `./BGS-VERSIONING.md`
- `./BGS-FREEZE.yaml`
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

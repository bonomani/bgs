# Version Compatibility Matrix

Boundary Governance Suite

PURPOSE
-------
This document records the declared version of each framework member and the
known composition compatibility between them. It is a coordination artifact —
it does not define framework semantics. In case of conflict, the normative
framework documents win.

Read alongside `BGS-VERSIONING.md` for claim-binding rules.

------------------------------------------------------------

## 1. Framework Versions (current)

| Framework | Declared version | Repo     | Maturity     | Normative document |
|-----------|-----------------|----------|--------------|-------------------|
| BISS      | 1.0             | ucc      | Stable       | `ucc/governance/BISS.txt` |
| GIC       | 1.0             | ucc      | Stable       | `ucc/contract-semantics/GIC.txt` |
| GCC       | 1.0             | ucc      | Stable       | `ucc/contract-semantics/GCC.txt` |
| Basic     | 1.0             | ucc      | Stable       | `ucc/governance/BASIC.txt` |
| RIG       | 1.0             | ucc      | Stable       | `ucc/governance/RIG.txt` |
| UCC       | 1.0             | ucc      | Stable       | `ucc/execution-semantics/UCC-EXECUTION.txt` |
| ASM       | 1.0             | asm      | Stable       | `asm/README.md` (entry point), `asm/SOFTWARE-MODEL.md` (core semantics), `asm/CONVERGENCE-INTERFACE.md` (ASM–UCC composition) |
| UIC       | 1.0             | uic      | Draft        | `uic/` |
| TIC       | 1.0             | tic      | Specified, partial suite integration | `tic/` |
| BGS       | 1.0             | bgs      | Stable (draft coordination layer) | `bgs/SUITE.md` |

Note: all frameworks in the `ucc` repo share the same repo ref. Versioning a
`ucc`-hosted framework means pinning the `ucc` repo ref (see `BGS-VERSIONING.md`
§1 and §6.3).

------------------------------------------------------------

## 2. Composition Compatibility

### 2.1 Within the `ucc` repo — always compatible at the same ref

All frameworks hosted in `ucc` are internally consistent at any given repo ref:

```
BISS 1.0 ──► GIC 1.0 ──► GCC 1.0 ──► UCC 1.0
              │
              └──► Basic 1.0
              └──► RIG 1.0  (orthogonal quality grade, any interaction type)
```

Pinning a single `ucc` ref is sufficient to compose any subset of these.

### 2.2 Cross-repo compositions

| Composition                | Required refs             | Constraint / condition                                                         |
|----------------------------|---------------------------|--------------------------------------------------------------------------------|
| UCC + ASM                  | `ucc` ref + `asm` ref     | ASM 1.0 (core interface v1.0) is required; see `asm/CONVERGENCE-INTERFACE.md` |
| UCC + UIC                  | `ucc` ref + `uic` ref     | UIC is draft; pin explicit `uic` ref; verify UIC semantics at the pinned ref   |
| UCC + UIC + TIC            | all three refs            | TIC verification applies after UCC/UIC cycle; pin all three explicitly         |
| UCC + ASM + UIC            | all three refs            | ASM supplies state vocabulary; UIC supplies intent gate; UCC executes          |
| UCC + TIC (no UIC)         | `ucc` ref + `tic` ref     | TIC verifies UCC outcomes directly; valid without UIC                          |
| UCC + ASM + UIC + TIC      | all four refs             | Full BGS-State-Modeled-Governed-Verified composition                           |

### 2.3 Composition rules from BGS (CR-1 through CR-7)

| Rule | Summary |
|------|---------|
| CR-1 | Member frameworks remain semantically separate — no implicit blending |
| CR-2 | Composition requires explicit handoff, not implicit assumption |
| CR-3 | When both UIC and UCC are used, UIC resolves first |
| CR-4 | TIC verifies after governed behavior — it does not redefine it |
| CR-5 | Basic and RIG are orthogonal to interaction type — combine freely |
| CR-6 | When ASM is composed with UCC, ASM supplies the state vocabulary |
| CR-6a| Systems requiring state semantics default toward ASM |
| CR-7 | Any valid subset of the composition is a permitted adoption |

------------------------------------------------------------

## 3. BGS Adoption Slices and Required Refs

| BGS slice                        | Required refs                     |
|----------------------------------|-----------------------------------|
| BGS-Classification               | `ucc` only (BISS)                 |
| BGS-Foundation                   | `ucc` (GIC/GCC)                   |
| BGS-Execution                    | `ucc` (UCC)                       |
| BGS-Governed                     | `ucc` + `uic`                     |
| BGS-Verified                     | `ucc` + `tic`                     |
| BGS-Governed-Verified            | `ucc` + `uic` + `tic`             |
| BGS-State-Modeled-Execution      | `ucc` + `asm`                     |
| BGS-State-Modeled-Governed       | `ucc` + `asm` + `uic`             |
| BGS-State-Modeled-Governed-Verified | `ucc` + `asm` + `uic` + `tic`  |

Note: standalone ASM is valid as framework adoption but is not a claimable
BGS adoption slice. A UCC-based slice is required for BGS adoption.

------------------------------------------------------------

## 4. Known Incompatibilities and Constraints

| Item | Description |
|------|-------------|
| UIC maturity | UIC is draft; compositions that include UIC carry a maturity risk; pin exact ref and document the known-state of the UIC spec at claim time |
| TIC suite integration | TIC is specified but suite-level integration is partial; use TIC only where its semantics are fully understood at the pinned ref |
| ASM profile transparency | The ASM profile layer (Minimal vs Extended Operational) is transparent to UCC; the engine always consumes the same five-label canonical set regardless of which ASM profile is active |
| UCC pre-1.0 flat model | The pre-1.0 flat ten-status model is archived and no longer normative; any implementation still using it must migrate; see `ucc/governance/GLOSSARY.txt` §DEPRECATED TERMS |
| BGS-Execution + ASM without UCC | Not a valid composition — ASM requires UCC as the execution engine it feeds into |

------------------------------------------------------------

## 5. Version Freeze Record

While BGS is pre-public, version labels are defined but not yet subject to
formal backward-compatibility obligations. All framework versions are at 1.0.

Any change to a framework that alters the observable semantics of its normative
documents requires a version increment of that framework's rule set. The matrix
in §1 must be updated when that happens.

See `BGS-VERSIONING.md` §8 (Pre-Public Freeze) for the active freeze record and
stability rules.

------------------------------------------------------------

END OF DOCUMENT

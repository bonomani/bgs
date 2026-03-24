# BGS Gaps

Boundary Governance Suite

PURPOSE
-------
This document tracks what remains to be defined so that BGS can become a
well-structured suite while keeping its member frameworks separate.

Interpretation:
- `GAPS.md` tracks major suite-definition gaps and their resolution state
- `TODO.md` tracks smaller follow-up cleanup and alignment work that may remain after a gap is marked resolved
- `STATUS.md` is a snapshot, not the authoritative gap ledger

STATUS
------
Active

Gap states:
- OPEN
- PARTIAL
- RESOLVED

Note: resolved gaps are removed when closed. A retention and archival
policy has not yet been defined.

------------------------------------------------------------

BGS-10
STATE: OPEN
AREA: Adoption slice completeness
GOAL: All reachable compositions should either be a named claimable slice or
      explicitly declared non-claimable.
GAP:  VERSION-MATRIX.md line 61 references the composition
      "UCC + ASM + UIC + TIC" under the label
      `BGS-State-Modeled-Governed-Verified`, but this slice does not appear
      in BGS-COMPLIANCE.md (which stops at §2.8), SUITE-MAP.md, SUITE.md,
      or suite-map.json.  A reader cannot determine whether this is a valid
      claimable slice, a planned future slice, or an editorial error.
IMPACT:

- adopters targeting full state-modeled + governed + verified composition
  have no normative path to claim it
- the discrepancy between VERSION-MATRIX.md and all other slice authorities
  undermines trust in the version matrix as a source of truth
RESOLUTION PATH:
  Option A: Define BGS-State-Modeled-Governed-Verified as a ninth claimable
            slice.  Add §2.9 to BGS-COMPLIANCE.md (required members, minimum
            evidence), add a row to SUITE-MAP.md §4 and suite-map.json, and
            add a row to SUITE.md §6.
  Option B: Remove the reference from VERSION-MATRIX.md line 61 and add a
            note clarifying that TIC can be layered on
            BGS-State-Modeled-Governed without creating a new named slice.

------------------------------------------------------------

BGS-11
STATE: OPEN
AREA: ASM authoritative document alignment
GOAL: The single authoritative entry point for ASM should be stated
      consistently across all suite-level documents.
GAP:  Three suite-level documents disagree on which ASM document is
      authoritative:
        VERSION-MATRIX.md line 26  → asm/CONVERGENCE-INTERFACE.md
        SUITE-MAP.md line 42       → asm/README.md, asm/SOFTWARE-MODEL.md
        suite-map.json lines 264-266 → asm/README.md, asm/SOFTWARE-MODEL.md
      CONVERGENCE-INTERFACE.md governs ASM's composition interface with UCC.
      README.md and SOFTWARE-MODEL.md govern the core ASM framework semantics.
      These are different scopes; none of the documents make this explicit.
IMPACT:

- a user following VERSION-MATRIX.md lands at the composition interface
  but misses the framework definition
- a user following SUITE-MAP.md or suite-map.json never reaches the
  composition interface
RESOLUTION PATH:
  List all three documents where appropriate and annotate their scope:
    asm/README.md               — suite entry point
    asm/SOFTWARE-MODEL.md       — core framework semantics
    asm/CONVERGENCE-INTERFACE.md — ASM–UCC composition interface

------------------------------------------------------------

BGS-12
STATE: OPEN
AREA: UIC adoption guidance consolidation
GOAL: Adopters should receive a single, unambiguous signal about when and
      how to adopt UIC given its Draft maturity.
GAP:  The implications of UIC's Draft status are expressed inconsistently:
        VERSION-MATRIX.md §4  — warns of maturity risk; requires exact ref pin
        SUITE-MAP.md §6       — positions UIC as step 5 (late-stage) in the
                                 recommended adoption order
        BGS-COMPLIANCE.md §2.5 — treats BGS-Governed (which requires UIC)
                                  as a claimable slice with minimum evidence,
                                  implying it is usable now without qualification
      No single document consolidates these three signals into actionable
      guidance.
IMPACT:

- adopters cannot determine from one place whether UIC is safe to use now
  (with pinning) or whether they should wait for a stable release
- BGS-COMPLIANCE.md §2.5 may inadvertently understate the risk
RESOLUTION PATH:
  Add a short "Maturity note" block to BGS-COMPLIANCE.md §2.5 that cross-
  references VERSION-MATRIX.md §4 and SUITE-MAP.md §6.  The note should
  state: UIC is claimable at Draft maturity provided the exact ref is pinned
  and the known state of the spec at claim time is documented.

------------------------------------------------------------

BGS-13
STATE: OPEN
AREA: Standalone-ASM constraint visibility
GOAL: The constraint that standalone ASM is not a claimable BGS adoption
      slice should appear in every authoritative slice list.
GAP:  SUITE-MAP.md line 119 states: "standalone ASM is not a claimable BGS
      adoption slice."  This constraint is absent from VERSION-MATRIX.md §3
      (the adoption slices table) and from BGS-COMPLIANCE.md §2.
IMPACT:

- a reader consulting VERSION-MATRIX.md or BGS-COMPLIANCE.md without also
  reading SUITE-MAP.md may not discover this constraint
RESOLUTION PATH:
  Add a footer note to VERSION-MATRIX.md §3 and a note at the top of
  BGS-COMPLIANCE.md §2 stating that ASM alone is not a claimable slice;
  a UCC-based slice is required for BGS adoption.

------------------------------------------------------------

END OF DOCUMENT

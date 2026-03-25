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

BGS-14
STATE: OPEN
AREA: Adoption slice completeness — real-adopter confirmation of BGS-10
GOAL: BGS-10 resolution should be prioritised as Option A (define
      BGS-State-Modeled-Governed-Verified as §2.9).
GAP:  The mac-mini-setup project (BGS-State-Modeled-Governed adopter) uses
      TIC on top of BGS-State-Modeled-Governed and was forced to record the
      following in its limitations field:
        "The claimed BGS slice is BGS-State-Modeled-Governed; TIC is used
         as additional verification evidence because the suite does not yet
         define a separate state-modeled-governed-verified slice."
      This is the first known real-adopter case that demonstrates the
      missing slice is a practical gap, not only an editorial inconsistency.
      The adopter could not claim the slice that matches its actual
      implementation.
IMPACT:

- real adopters using BISS + ASM + UIC + UCC + TIC together have no
  normative slice to claim; they are forced to understate their governance
- the limitations workaround degrades evidence quality for BGS compliance
  reviews because the stated slice does not match the actual member set
RESOLUTION PATH:
  Resolve BGS-10 via Option A as a priority.
  The mac-mini-setup project serves as a reference implementation for the
  new slice's minimum evidence requirements.
  Suggested minimum evidence for BGS-State-Modeled-Governed-Verified:
  - everything required for BGS-State-Modeled-Governed
  - at least one TIC-style test artifact with explicit oracle
  - trace of at least one TIC oracle back to a UCC-governed target
  - pinned TIC reference

------------------------------------------------------------

BGS-15
STATE: OPEN
AREA: BGS compliance tooling — no automated checker exists
GOAL: Adopters should be able to verify their BGS.md and bgs-decision.md
      are structurally valid and up to date without manual review.
GAP:  There is no tool in the BGS suite that validates:
      - required fields are present in a bgs-decision.md (CR-3 through CR-7)
      - the named bgs_slice is a known claimable slice
      - member_version_refs are pinned (not branch names or "latest")
      - local evidence_refs paths exist on disk
      - last_reviewed is not stale beyond a configurable threshold
      By contrast, the mac-mini-setup project has two executable validators
      (validate_targets_manifest.py, validate_setup_state_artifact.py) that
      are run routinely. BGS compliance review is entirely manual.
IMPACT:

- BGS compliance docs go stale silently; version refs drift without
  detection when member frameworks advance
- AI agents working on adopter projects have no machine-readable signal
  that the BGS docs are current; they must re-derive staleness by
  comparing git SHAs manually each session
- the burden of compliance review deters adoption or produces superficial
  "tick-box" claims that are never re-validated
RESOLUTION PATH:
  Add tools/check-bgs-compliance.py (or equivalent) to the BGS repo.
  Minimum checks:
  - all required decision fields present (BGS-COMPLIANCE.md §3)
  - bgs_slice is one of the named claimable slices
  - member_version_refs values are valid immutable refs (not branch names)
  - local evidence_refs paths resolve relative to the decision file
  - last_reviewed is within a configurable staleness window (default 90 days)
  Exit 0 on pass, non-zero on failure, machine-readable output.

------------------------------------------------------------

BGS-16
STATE: OPEN
AREA: UCC — component-level failure policy not specified
GOAL: UCC should define what an orchestrator is allowed to do when a
      component (a logical group of targets) fails.
GAP:  UCC defines outcomes at the individual target level (converged,
      changed, failed) but has no normative concept of a component-level
      failure policy.  The mac-mini-setup project needed to express
      "if this component fails, continue with the remaining components"
      (on_fail: ignore) vs "abort the entire run."  This policy was
      invented locally in the YAML manifest and the orchestrator shell code
      with no UCC backing.
      Other reasonable policies (retry, skip-dependents, escalate) are
      similarly unspecified.
IMPACT:

- adopters building multi-component orchestrators must invent and document
  their own failure propagation semantics
- two adopters can implement opposite on_fail behaviours and both validly
  claim BGS-Execution compliance
- result artifacts do not carry a component-level outcome field, so
  downstream consumers cannot determine whether a failed target caused its
  component to abort or continue
RESOLUTION PATH:
  Add a component-level result semantics section to the UCC spec.
  Define at minimum:
  - on_fail: abort  — stop the entire run on first component failure
  - on_fail: ignore — record the failure, continue with remaining components
  - on_fail: skip-dependents — skip targets that depend on the failed component
  Specify how the component outcome is recorded in the result artifact.

------------------------------------------------------------

BGS-17
STATE: OPEN
AREA: UCC/UIC — skip is not a normative target outcome
GOAL: When a UIC soft gate inhibits a target, the resulting outcome should
      have a defined name, result structure, and record format in UCC.
GAP:  UCC defines converged, changed, and failed as target outcomes.
      UIC defines soft gates that may inhibit execution.  But neither
      framework defines what happens to a target that is inhibited by a
      soft gate — the target is neither converged nor failed, it is skipped.
      The mac-mini-setup project invented ucc_skip_target locally, which
      emits a line and increments a counter but produces no result artifact
      and has no normative outcome name.
      This means skipped targets are invisible in UCC result artifacts and
      cannot be distinguished from targets that were never declared.
IMPACT:

- skipped targets leave no traceable evidence that they were evaluated and
  deliberately not applied
- compliance audits cannot distinguish "was never run" from "was inhibited
  by policy"
- the count of skipped targets appears in the summary but the individual
  targets are not identified in any artifact
RESOLUTION PATH:
  Define skip (or inhibited) as a normative UCC target outcome alongside
  converged, changed, and failed.
  Minimum result fields for a skipped target:
  - outcome: skipped
  - inhibitor: the gate name or policy reason
  - observation: not-attempted
  Specify how the UIC soft gate name is carried into the UCC result record.

------------------------------------------------------------

BGS-18
STATE: OPEN
AREA: TIC — oracle execution context is undefined
GOAL: TIC should specify the execution context constraints for inline
      oracle expressions so that adopters can write portable oracles.
GAP:  TIC SPEC.md §4 defines oracles as "explicit and verifiable" but does
      not specify:
      - what shell or interpreter evaluates the oracle string
      - what environment variables are available at evaluation time
      - what quoting rules apply when the oracle is stored in a YAML value
      The mac-mini-setup project hit this gap directly: an oracle written as
        python3 -c "from importlib.metadata import version; ..."
      failed with a SyntaxError because the YAML parser did not unescape
      inner \" sequences, delivering literal backslash-quote to Python.
      The fix required rewriting the oracle to avoid any inner quoting.
      The adopter had no normative guidance to consult; the failure was
      discovered by trial and error.
IMPACT:

- oracle authors cannot predict whether their expression will survive the
  YAML-to-shell pipeline without testing every quoting combination
- the same oracle string may work in one TIC runner implementation and
  fail in another if runners handle quoting differently
- silent evaluation failures (oracle not run, test passes vacuously) are
  possible if the runner swallows shell errors
RESOLUTION PATH:
  Add an "Oracle authoring rules" section to TIC SPEC.md §4.
  Minimum normative statements:
  - the oracle MUST be a self-contained shell expression evaluable by /bin/sh
  - the oracle MUST NOT rely on environment variables not defined in the
    TIC runner's documented execution context
  - the oracle MUST NOT contain unescaped double-quotes when stored in a
    YAML double-quoted scalar; prefer single-quoted YAML scalars for oracles
    containing shell expressions
  - a TIC runner MUST report oracle evaluation failure as a test failure,
    not as a pass

------------------------------------------------------------

END OF DOCUMENT

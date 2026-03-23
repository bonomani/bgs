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

------------------------------------------------------------

BGS-1
STATE: RESOLVED
AREA: Suite identity and naming
GOAL: BGS should have a stable identity and vocabulary that does not
      overload existing framework terms.
GAP:  Resolved by `./BGS-NAMING.md`, which now freezes:
      - the canonical short name
      - the canonical long name
      - the relation between BGS and BISS
      - the distinction between member repos and member frameworks
      - preferred and prohibited suite-level wording
IMPACT:
- suite-level vocabulary is materially clearer
- drift between suite naming and member-framework naming is reduced
RESOLUTION PATH:
- keep naming guidance aligned with suite evolution

------------------------------------------------------------

BGS-2
STATE: RESOLVED
AREA: Suite map
GOAL: The suite should expose one canonical dependency and composition map.
GAP:  Resolved by `./SUITE-MAP.md` and `./suite-map.json`, which now
      provide:
      - a canonical member matrix
      - standalone vs compositional usage
      - semantic-base vs composition ordering
      - maturity signals by framework
      - valid adoption slices
IMPACT:
- adoption paths are now materially clearer
- architecture review ambiguity is reduced
RESOLUTION PATH:
- keep the canonical map aligned with member-framework evolution

------------------------------------------------------------

BGS-3
STATE: RESOLVED
AREA: Shared glossary
GOAL: Cross-repo terminology should remain stable and non-conflicting.
GAP:  Resolved by `./BGS-GLOSSARY.md`, which now defines suite-level
      cross-framework terms including:
      - boundary
      - governance
      - preflight
      - execution
      - verification
      - rigor
      - member repo
      - member framework
      - slice
      - overlay
      - external control
IMPACT:
- suite-level wording is materially clearer
- cross-repo onboarding friction is reduced
RESOLUTION PATH:
- keep the glossary aligned with member-framework evolution

------------------------------------------------------------

BGS-4
STATE: RESOLVED
AREA: Cross-repo versioning
GOAL: The suite should define how separate framework versions are composed.
GAP:  Resolved by `./BGS-VERSIONING.md` and the active freeze record
      `./BGS-FREEZE.yaml`, which now define:
      - the suite-level versioning units
      - immutable reference rules
      - required version binding for claims
      - compatibility levels
      - how BGS refs relate to member-repo refs
      - how published composition records may be expressed
      - the current pre-public numbering-freeze policy
IMPACT:
- suite composition is materially less ambiguous
- version-bound suite claims are easier to interpret and audit
RESOLUTION PATH:
- keep versioning policy aligned with repo and release practices

------------------------------------------------------------

BGS-5
STATE: RESOLVED
AREA: Suite-level AI problem mapping
GOAL: BGS should explain clearly how the suite addresses AI-agent risk
      classes and where its boundaries stop.
GAP:  Resolved by `./AI-RISK-CONTROL-MAP.md`, which now provides:
      - a problem-class coverage matrix
      - a solution compatibility matrix
      - explicit placement across BISS, UIC, UCC, TIC, Basic / RIG,
        and external controls
      - explicit statement of suite boundaries and non-goals
IMPACT:
- suite-level risk coverage is now explicit
- overclaim risk is reduced
- external control dependencies are easier to communicate
RESOLUTION PATH:
- keep the map updated as member frameworks or supported controls evolve

------------------------------------------------------------

BGS-6
STATE: RESOLVED
AREA: Compliance model
GOAL: BGS should define what it means to claim suite-level adoption.
GAP:  Resolved by `./BGS-COMPLIANCE.md`, which now defines:
      - valid BGS adoption slices
      - scope-based suite claims
      - required claim fields
      - minimum evidence by slice
      - invalid and misleading claims
      - required declaration of external controls
IMPACT:
- suite-level adoption claims are now materially clearer
- incompatible or overbroad BGS claims are easier to reject
RESOLUTION PATH:
- keep slice and evidence rules aligned with suite evolution

------------------------------------------------------------

BGS-7
STATE: RESOLVED
AREA: Member maturity alignment
GOAL: BGS should present member frameworks with clear maturity signals.
GAP:  Resolved by `./SUITE-MAP.md`, which now publishes:
      - maturity signals by member
      - a recommended adoption order by maturity and implementation risk
IMPACT:
- unequal maturity is now visible at suite level
- adopters have a clearer recommended sequencing path
RESOLUTION PATH:
- keep maturity signals updated as member frameworks evolve

------------------------------------------------------------

BGS-8
STATE: RESOLVED
AREA: Navigation and discoverability
GOAL: A new reader should be able to discover the whole suite from one
      stable entry point.
GAP:  BGS now has:
      - a suite entry point
      - a canonical reading path
      - a canonical suite map
      - explicit repo-hosting map and split/keep policy
      - back-references from the member repos to `../bgs/`
IMPACT:
- top-down navigation exists from `./bgs/`
- reverse discovery from member repos is now materially improved
RESOLUTION PATH:
- keep the back-references aligned with future suite updates

------------------------------------------------------------

BGS-9
STATE: RESOLVED
AREA: Human and agent friendliness
GOAL: BGS should be easy for humans to read and easy for AI agents to
      traverse and apply.
GAP:  BGS now provides:
      - a canonical human-readable suite map in `./SUITE-MAP.md`
      - a machine-friendly suite map in `./suite-map.json`
      - stable suite entry points in `./README.md`
      - explicit repo-hosting and split/keep guidance
      - a prose-first vs machine-first artifact policy
      - clear formatting conventions for both human and machine use
IMPACT:
- human and agent navigation are materially improved
- formatting and artifact-policy drift are materially reduced
RESOLUTION PATH:
- keep prose and machine artifacts aligned as the suite evolves

------------------------------------------------------------

END OF DOCUMENT

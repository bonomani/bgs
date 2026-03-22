# BGS Gaps

Boundary Governance Suite

PURPOSE
-------
This document tracks what remains to be defined so that BGS can become a
well-structured suite while keeping its member frameworks separate.

STATUS
------
Active

Gap states:
- OPEN
- PARTIAL
- RESOLVED

------------------------------------------------------------

BGS-1
STATE: OPEN
AREA: Suite identity and naming
GOAL: BGS should have a stable identity and vocabulary that does not
      overload existing framework terms.
GAP:  The suite name is chosen, but its long-form naming, abbreviation
      policy, and relation to BISS terminology are not yet frozen.
IMPACT:
- cross-repo naming may drift
- different docs may describe the same suite differently
RESOLUTION PATH:
- define the canonical short name
- define the canonical long name
- define how BGS references BISS, UIC, UCC, TIC, Basic, and RIG

------------------------------------------------------------

BGS-2
STATE: OPEN
AREA: Suite map
GOAL: The suite should expose one canonical dependency and composition map.
GAP:  BGS currently defines high-level roles and composition rules, but no
      formal suite matrix exists yet for:
      - required vs optional relationships
      - standalone vs compositional usage
      - maturity by framework
IMPACT:
- adoption paths remain partly interpretive
- architecture reviews may reach inconsistent conclusions
RESOLUTION PATH:
- add a suite matrix covering members, dependencies, optionality, and maturity

------------------------------------------------------------

BGS-3
STATE: OPEN
AREA: Shared glossary
GOAL: Cross-repo terminology should remain stable and non-conflicting.
GAP:  There is no suite-level glossary yet for terms that span multiple
      frameworks, such as:
      - boundary
      - governance
      - preflight
      - execution
      - verification
      - rigor
IMPACT:
- the same word may carry slightly different meanings across repos
- suite-level onboarding remains harder than necessary
RESOLUTION PATH:
- create a suite glossary that references, but does not replace,
  member-framework vocabularies

------------------------------------------------------------

BGS-4
STATE: OPEN
AREA: Cross-repo versioning
GOAL: The suite should define how separate framework versions are composed.
GAP:  There is no suite-level release or compatibility policy covering:
      - which UIC version composes with which UCC version
      - whether TIC versions are tied to suite versions
      - how BGS versions reference member-framework versions
IMPACT:
- suite composition may become ambiguous over time
- upgrades may not be clearly governable
RESOLUTION PATH:
- define a suite compatibility and release model

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
STATE: OPEN
AREA: Compliance model
GOAL: BGS should define what it means to claim suite-level adoption.
GAP:  There is no suite-level statement describing:
      - what counts as using BGS
      - what counts as partial BGS adoption
      - what minimal artifacts prove adoption
IMPACT:
- "BGS-compliant" would currently be undefined
- teams may claim adoption with incompatible evidence
RESOLUTION PATH:
- define suite-level adoption profiles and evidence expectations

------------------------------------------------------------

BGS-7
STATE: PARTIAL
AREA: Member maturity alignment
GOAL: BGS should present member frameworks with clear maturity signals.
GAP:  Member frameworks do not all have the same maturity:
      - UCC has a stronger execution, schema, and test baseline
      - UIC is still draft
      - TIC is specified but not yet connected to a suite-wide compliance story
IMPACT:
- readers may assume equal readiness across the suite
- adoption sequencing may be poorly chosen
RESOLUTION PATH:
- publish a suite maturity table
- recommend an adoption order by maturity and risk

------------------------------------------------------------

BGS-8
STATE: OPEN
AREA: Navigation and discoverability
GOAL: A new reader should be able to discover the whole suite from one
      stable entry point.
GAP:  BGS now has a suite entry point, but the member repos do not yet
      consistently point back to the suite layer.
IMPACT:
- top-down navigation is incomplete
- the suite remains harder to discover than the individual repos
RESOLUTION PATH:
- add back-references from member repos to `../bgs/`
- add a canonical suite reading path

------------------------------------------------------------

BGS-9
STATE: OPEN
AREA: Human and agent friendliness
GOAL: BGS should be easy for humans to read and easy for AI agents to
      traverse and apply.
GAP:  The suite does not yet define:
      - a canonical machine-friendly suite map
      - a stable minimal reading path for agents
      - document formatting conventions optimized for both human and
        agent consumption
      - which suite artifacts are prose-first vs machine-first
IMPACT:
- human onboarding may remain slower than necessary
- AI agents may interpret suite composition inconsistently
- the suite may drift into either human-only prose or machine-only structure
RESOLUTION PATH:
- define a suite map artifact
- define dual readability conventions
- identify stable entry docs for humans vs agents

------------------------------------------------------------

END OF DOCUMENT

# BGS Versioning

Boundary Governance Suite

STATUS
------
Canonical suite-level versioning and compatibility policy.

PURPOSE
-------
This document defines how BGS composes separate framework versions across
multiple repos without collapsing them into one release train.

It specifies:
- what is versioned at suite level
- how member-framework versions must be referenced
- what a valid BGS composition means
- what kinds of compatibility claims are allowed
- what versioning shortcuts are forbidden

------------------------------------------------------------

1. VERSIONING UNITS
-------------------

BGS uses four versioning units:

1. Suite-layer artifacts
   The docs in `./bgs/` itself.

2. Member-repo versions
   Immutable refs from the participating repos:
   - `../ucc/`
   - `../uic/`
   - `../asm/`
   - `../tic/`

3. Member-framework versions
   The effective versions of the frameworks used in a claim.
   At present, these are derived from the repo ref that contains them:
   - `BISS`, `GIC`, `GCC`, `Basic`, `RIG`, `UCC` -> `ucc` ref
   - `ASM` -> `asm` ref
   - `UIC` -> `uic` ref
   - `TIC` -> `tic` ref

4. Suite composition version
   A declared set of suite-layer and member-repo refs that are asserted
   to compose together for a specific claim, profile, or published bundle.

Interpretation rule:
- BGS does not force one global version number across all repos
- BGS compatibility is defined by an explicit composition, not by repo
  name alone

------------------------------------------------------------

2. IMMUTABLE REFERENCE RULE
---------------------------

Every suite-level claim must bind to immutable references.

Allowed reference types:
- git commit SHA
- immutable tag
- immutable release identifier

Forbidden reference types:
- branch names such as `master` or `main`
- moving labels such as `latest`
- undocumented local state

Reason:
- suite claims must remain interpretable after repos continue to evolve

------------------------------------------------------------

3. REQUIRED VERSION BINDING FOR CLAIMS
--------------------------------------

A valid BGS claim must declare:
- `bgs_version_ref`
- `member_version_refs`

Minimum member-version bindings:
- if `BISS`, `GIC`, `GCC`, `Basic`, `RIG`, or `UCC` are used, the claim
  must include an immutable `ucc` ref
- if `ASM` is used, the claim must include an immutable `asm` ref
- if `UIC` is used, the claim must include an immutable `uic` ref
- if `TIC` is used, the claim must include an immutable `tic` ref

Recommended binding shape:

```yaml
bgs_version_ref: bgs@12e5d16
member_version_refs:
  ucc: ucc@1505204
  asm: asm@34eeafe
  uic: uic@a997340
  tic: tic@5f125a3
```

------------------------------------------------------------

4. COMPATIBILITY LEVELS
-----------------------

BGS recognizes four compatibility levels for suite composition claims.

Level 1 — Exact composition
  The claim pins:
  - one immutable BGS ref
  - all required immutable member-repo refs

  This is the minimum required level for any serious BGS claim.

Level 2 — Published composition
  A published composition record declares a named suite composition and
  pins the exact refs for BGS and all participating member repos.

  Example:
  - `BGS-COMP-2026-03-A`

Level 3 — Locally declared composition
  A team pins exact refs locally but does not publish a named suite
  composition artifact.

  This is valid for internal use if the refs are explicit.

Level 4 — Floating composition
  A team claims compatibility using moving refs such as branches,
  undocumented local state, or implicit "current latest" assumptions.

  This is invalid for BGS compliance claims.

------------------------------------------------------------

5. SUITE VERSION INTERPRETATION
-------------------------------

`BGS` version refs identify the suite-layer docs only.

They do NOT automatically imply:
- which `ucc` version is required
- which `asm` version is required
- which `uic` version is required
- which `tic` version is required

Therefore:
- `bgs@X` alone is never a sufficient suite compatibility claim
- a valid suite claim always needs explicit member-version bindings

This keeps BGS honest as a suite layer rather than pretending that one
repo version controls all member semantics.

------------------------------------------------------------

6. MEMBER-FRAMEWORK COMPATIBILITY RULES
---------------------------------------

6.1 UIC and UCC
  If a claim uses both `UIC` and `UCC`, it must pin both refs
  explicitly.
  Compatibility is asserted by the claim or published composition
  record, not inferred from chronology alone.

6.2 TIC with UIC or UCC
  If a claim uses `TIC` to verify `UIC`, `UCC`, or both, it must pin the
  `tic` ref explicitly in addition to the governed member refs.

6.3 Foundation members
  If a claim references `BISS`, `GIC`, `GCC`, `Basic`, or `RIG`, the
  effective version is the pinned `ucc` ref unless and until these
  frameworks are split into separate repos.

6.4 ASM
  If a claim uses `ASM`, it must pin the `asm` ref explicitly.
  ASM-based modeled slices do not inherit their version from another repo.

6.5 Partial adoption
  A claim may omit refs for unused member repos.
  Example:
  - a `BGS-Execution` claim does not need a `uic` or `tic` ref
  - a `BGS-Governed` claim does not need a `tic` ref
  - a non-modeled slice does not need an `asm` ref

------------------------------------------------------------

7. PUBLISHED COMPOSITION RECORDS
--------------------------------

BGS may publish named composition records over time.

A composition record should contain at least:
- `composition_id`
- `bgs_version_ref`
- `member_version_refs`
- `supported_profiles`
- `notes`

Example:

```yaml
composition_id: BGS-COMP-2026-03-A
bgs_version_ref: bgs@12e5d16
member_version_refs:
  ucc: ucc@1505204
  asm: asm@34eeafe
  uic: uic@a997340
  tic: tic@5f125a3
supported_profiles:
  - BGS-Execution
  - BGS-Verified
  - BGS-Governed
  - BGS-Governed-Verified
  - BGS-State-Modeled-Execution
  - BGS-State-Modeled-Governed
notes:
  - UIC remains draft at this composition point
```

Until such records are published systematically, exact composition
claims remain valid through direct immutable refs.

------------------------------------------------------------

8. PRE-PUBLIC FREEZE
--------------------

Current active freeze record:
- `./BGS-FREEZE.yaml`

Interpretation:
- while BGS remains private or draft, the suite-layer docs may continue
  to evolve
- the freeze record protects numbering stability for published suite
  identifiers during the draft phase
- changing the numbering policy or superseding the freeze requires a new
  freeze record

This rule exists to prevent version-label reuse or renumbering while the
suite is still drafting and its prose may continue to move.

The freeze record does not remove the obligation to pin immutable refs in
claims.
It does not provide a default composition baseline.

------------------------------------------------------------

9. INVALID VERSIONING CLAIMS
----------------------------

The following claims are invalid:
- "BGS-compatible with latest UCC"
- "BGS-compliant on master"
- a suite claim with only `bgs_version_ref` and no member refs
- claiming `UIC` and `UCC` compose without pinning both refs
- claiming `TIC` verification against an unpinned governed target

The following claims are misleading and should be avoided:
- implying that a newer member ref is automatically compatible because
  it is more recent
- treating repo chronology as proof of semantic compatibility
- treating local uncommitted state as a versioned composition

------------------------------------------------------------

10. CLAIM EXAMPLE
-----------------

```yaml
decision_id: config-agent-flow-01
bgs_slice: BGS-Governed-Verified
declared_scope: production config rollout workflow
bgs_version_ref: bgs@12e5d16
member_version_refs:
  ucc: ucc@1505204
  uic: uic@a997340
  tic: tic@5f125a3
members_used:
  - BISS
  - UIC
  - UCC
  - TIC
```

------------------------------------------------------------

11. STABILITY RULE
------------------

Once a claim is published, its bound refs must not be rewritten in place.
Any change to the declared suite composition requires a new claim
revision or a new composition record.

------------------------------------------------------------

END OF DOCUMENT

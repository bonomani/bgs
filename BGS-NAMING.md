# BGS Naming

Boundary Governance Suite

STATUS
------
Canonical suite-level naming and identity policy.

PURPOSE
-------
This document freezes the core naming rules for BGS so that:
- suite identity remains stable
- BGS is not confused with BISS or UCC
- repo names and framework names are not mixed accidentally
- suite-level claims use the same vocabulary across documents

------------------------------------------------------------

1. CANONICAL SUITE NAME
-----------------------

Canonical short name:
- `BGS`

Canonical long name:
- `Boundary Governance Suite`

Allowed usage:
- `BGS`
- `Boundary Governance Suite`

Avoid:
- `BGS Suite` when the short name alone is sufficient
- switching between multiple long names for the same suite

Interpretation rule:
- `BGS` names the suite layer
- `BGS` does not rename or replace the member frameworks

------------------------------------------------------------

2. RELATION TO BISS
-------------------

`BISS` is not the name of the suite.

Canonical interpretation:
- `BGS` = the suite
- `BISS` = the axis and classification model inside the suite

Therefore:
- use `BGS` when referring to the whole suite
- use `BISS` when referring to the boundary interaction classification model

Avoid:
- using `BISS` as a synonym for the whole suite
- calling BGS "the BISS framework" when the intended referent is the suite

------------------------------------------------------------

3. MEMBER FRAMEWORK NAMES
-------------------------

At suite level, the canonical framework names are:
- `BISS`
- `GIC`
- `GCC`
- `Basic`
- `RIG`
- `UIC`
- `UCC`
- `TIC`

Canonical suite-level descriptions:
- `BISS` = axis model
- `GIC` = interaction foundation
- `GCC` = contract foundation
- `Basic` = rigor grade
- `RIG` = rigor grade
- `UIC` = preflight governance contract
- `UCC` = execution and convergence contract
- `TIC` = verification contract

Interpretation rule:
- preserve each member framework's existing canonical name
- do not rename member frameworks just to make them fit the suite branding

------------------------------------------------------------

4. REPO NAMES VS FRAMEWORK NAMES
--------------------------------

At repository level, the current member repos are:
- `../ucc/`
- `../uic/`
- `../tic/`

These repo names are not identical to the full set of suite-level member
frameworks.

Canonical distinction:
- `member repo` = a repository participating in the suite layer
- `member framework` = a semantic framework used by the suite

Examples:
- `../ucc/` is a member repo
- `BISS`, `GIC`, `GCC`, `Basic`, `RIG`, and `UCC` are member frameworks
  currently authored in the `../ucc/` repo
- `UIC` is a member framework currently authored in the `../uic/` repo
- `TIC` is a member framework currently authored in the `../tic/` repo

Avoid:
- saying that only `ucc`, `uic`, and `tic` are the suite members
  when the intended referent is the semantic framework set
- saying that `BISS` or `UCC` are repos when the intended referent is the
  framework

------------------------------------------------------------

5. CLAIM AND DOCUMENT NAMING
----------------------------

Canonical document prefixes in `./bgs/`:
- `BGS-...` for suite-level policy or explanatory artifacts

Canonical claim wording:
- `BGS-Classification`
- `BGS-Foundation`
- `BGS-Execution`
- `BGS-Verified`
- `BGS-Governed`
- `BGS-Governed-Verified`

Canonical compliance wording:
- "claims `BGS-Execution` for scope X"
- "adopts BGS at profile `BGS-Governed-Verified`"

Avoid:
- bare "BGS-compliant" with no profile
- "UCC-compliant with BGS" when the intended claim is a suite-level profile

------------------------------------------------------------

6. TERMS TO PREFER
------------------

Prefer:
- `suite` for BGS
- `member framework` for BISS, GIC, GCC, Basic, RIG, UIC, UCC, TIC
- `member repo` for `../ucc/`, `../uic/`, `../tic/`
- `profile` for BGS adoption claims
- `overlay` for `Basic` and `RIG`

Avoid:
- `stack` when the intended meaning is the broader BGS suite
- `contract suite` as the umbrella name for everything in BGS
- `UCC stack` when the intended meaning is BGS
- `BISS suite` when the intended meaning is BGS

------------------------------------------------------------

7. STABILITY RULE
-----------------

These naming rules are suite-canonical until explicitly revised by a new
BGS naming artifact.

When a BGS document uses a different term informally, this document wins
for suite identity and naming.

Member-framework documents still win for their own internal semantics.

------------------------------------------------------------

END OF DOCUMENT

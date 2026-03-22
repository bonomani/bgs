# BGS Script Quality

Boundary Governance Suite

STATUS
------
Operational guidance for script quality and recommended BGS slices.

PURPOSE
-------
This document defines the minimum and maximum quality expectations for
common script classes and the corresponding recommended BGS slice.

It is intentionally practical:
- minimum = the smallest safe baseline
- maximum = the fully engineered version
- recommended slice = the default BGS framing for the script type
- upgrade triggers = when to move to the stronger slice

------------------------------------------------------------

1. ANY SCRIPT
-------------

Minimum
- clear parameters
- input validation
- deterministic exit code
- basic error handling
- minimal logging

Maximum
- strict parameter schema
- full validation of arguments and environment
- idempotent behavior where applicable
- dry-run mode
- structured logging
- retry and timeout control
- lock or concurrency protection
- machine-readable output
- modular architecture
- audit trail or execution summary
- security controls for secrets and privilege boundaries
- full automated test coverage

Recommended BGS slice
- `Basic`

Upgrade to a stronger slice when
- the script mutates shared state
- the script touches secrets or privileged boundaries
- the script is part of a larger execution workflow
- the script needs verification or replayability

------------------------------------------------------------

2. INSTALL SCRIPT
-----------------

Minimum
- detect if already installed
- validate prerequisites
- copy or install files safely
- avoid blind overwrite
- set required permissions
- start or register service if needed
- verify installation succeeded
- log actions and failures
- return proper exit code

Maximum
- preflight system compatibility matrix
- install / upgrade / repair / uninstall separation
- version and state detection
- dependency resolution
- config backup and migration
- atomic staging and commit
- rollback or compensating actions
- checksum or signature validation
- service lifecycle orchestration
- post-install health checks
- detailed execution report
- unattended and interactive modes
- dry-run or plan mode
- remediation instructions on partial failure
- full test matrix across OS/version combinations

Recommended BGS slice
- `Basic + UCC`

Upgrade to a stronger slice when
- the install script needs preflight checks or policy gates
- the install changes sensitive system state
- the install must be approved before execution
- the install needs explicit post-execution verification
- the install has recovery, rollback, or upgrade paths that must be controlled

------------------------------------------------------------

3. PRACTICAL READING
--------------------

Any script
- minimum = runs correctly and predictably
- maximum = fully engineered operational tool

Install script
- minimum = installs safely once
- maximum = deploys, upgrades, repairs, and recovers reliably in production

------------------------------------------------------------

4. BGS INTERPRETATION
---------------------

- `Basic` is the shared baseline for script discipline.
- `UCC` is the execution layer for install or other consequential scripts.
- `UIC` is added when there are preflight gates or approvals.
- `TIC` is added when verification after execution matters.

END OF DOCUMENT

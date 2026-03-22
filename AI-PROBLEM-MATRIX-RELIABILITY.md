# BGS AI Reliability Matrix

Boundary Governance Suite

| Problem class | BGS coverage | Already available in a framework? | Primary BGS members | External controls still required | Recommended BGS profile | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Action hallucination | DIRECT | Yes: `UCC`, `TIC` | UCC, TIC, UIC | implementation validation for concrete tools | BGS-Execution | UCC helps by separating declaration from execution and checking observed state. |
| Model collapse | EXTERNAL | No | none | data curation, source governance, training policy | No BGS | Outside the suite's execution and verification focus. |
| Critical omission / context loss | HYBRID | Partially: `UIC`, `TIC` | UIC, TIC, Basic/RIG | context management, retrieval quality, review | BGS-Verified | Explicit artifacts reduce reliance on model memory alone. |
| Automated confirmation bias | HYBRID | Partially: `TIC`, `UIC` | TIC, UIC | independent review, adversarial tests, diverse evidence | BGS-Verified | TIC can require oracles and counterevidence. |
| Database pollution / bad writes | HYBRID | Yes: `UIC`, `UCC`, `TIC` | UIC, UCC, TIC | business validation, scoped permissions, rollout controls | BGS-Governed-Verified | Use diffs, gates, and explicit results. |


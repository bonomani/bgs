# BGS AI Operations Matrix

Boundary Governance Suite

| Problem class | BGS coverage | Already available in a framework? | Primary BGS members | External controls still required | Recommended BGS profile | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Agent loops / runaway recursion | HYBRID | Yes: `UCC`, `UIC` | UCC, UIC | rate limits, budgets, queue policy, orchestrator controls | BGS-Governed | BGS can bound retries and make execution explicit. |
| Non-determinism | DIRECT | Yes: `UCC`, `TIC` | UCC, TIC | deterministic implementation discipline | BGS-Execution | Good fit when you need repeatable behavior for the same declaration and observed state. |
| Involuntary DoS / cost explosion | HYBRID | Partially: `UIC`, `UCC` | UIC, UCC | rate limiting, quotas, backpressure, budgets | BGS-Governed | Hard enforcement usually remains external. |
| Amnesia contextuelle | HYBRID | Partially: `UIC`, `TIC` | UIC, TIC | context persistence, retrieval quality, review | BGS-Governed-Verified | Keep critical context in explicit artifacts. |
| Accountability gaps | HYBRID | Yes: `UCC`, `TIC` | UCC, TIC, Basic/RIG | policy, legal process, retention, audit storage | BGS-Verified | BGS can produce traceability, not legal liability. |


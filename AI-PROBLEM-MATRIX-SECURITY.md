# BGS AI Security Matrix

Boundary Governance Suite

| Problem class | BGS coverage | Already available in a framework? | Primary BGS members | External controls still required | Recommended BGS profile | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Indirect prompt injection | HYBRID | Partially: `UIC`, `TIC` | BISS, UIC, TIC | input isolation, sandboxing, taint controls, allowlists | BGS-Governed-Verified | BGS can force external content to be handled as governed input, but cannot guarantee perfect detection. |
| Confused deputy | HYBRID | Partially: `UIC`, `UCC` | BISS, UIC, UCC | IAM, RBAC, capability isolation, sandboxing, secrets management | BGS-Governed | BGS makes authority explicit, but permission enforcement stays external. |
| Privilege escalation | HYBRID | Partially: `UIC`, `UCC` | BISS, UIC, UCC | IAM, scoped permissions, secrets hygiene, sandboxing | BGS-Governed | Use gates and explicit approval paths when dangerous writes are possible. |
| Malicious skills / supply chain compromise | HYBRID | Partially: `UIC`, `TIC` | UIC, TIC, Basic/RIG | signing, scanning, provenance, review, isolation | BGS-Governed-Verified | Treat skills/extensions as governed inputs with provenance and review. |
| Token persistence / stale access | EXTERNAL | Mostly external | UIC | token revocation, IAM lifecycle, secret rotation | BGS-Governed | BGS can gate use of credentials, not revoke them after the fact. |
| Cache / memory poisoning | HYBRID | Partially: `UIC`, `TIC` | UIC, TIC | memory provenance, retention policy, isolation | BGS-Governed-Verified | Memory must be treated as governed input, not implicit truth. |


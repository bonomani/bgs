# BGS Decision Template

Boundary Governance Suite

Use this file as the minimum project-level entry point for a BGS-adopting
project.

Recommended project path:
- `./BGS.md`
- or `./docs/BGS.md`
- or `./docs/governance/BGS.md`

Minimum fields:
- `project_name`
- `bgs_slice`
- `decision_reason`
- `applies_to_scope`
- `decision_record_path`
- `last_reviewed`
- `read_next`

Template:

```md
# BGS Entry

project_name: example-project
bgs_slice: Light BGS
decision_reason: "AI-assisted workflow needs explicit request/result separation"
applies_to_scope: "backend task execution"
decision_record_path: "./docs/governance/bgs-decision.md"
last_reviewed: 2026-03-22
read_next:
  - "./API-CONTRACT.md"
  - "./tests/"
```

Decision record minimum fields:
- `decision_id`
- `bgs_slice`
- `decision_reason`
- `applies_to_scope`
- `bgs_version_ref`
- `member_version_refs`
- `external_controls`
- `evidence_refs`

Suggested project flow:
1. read the decision tree
2. read the AI problem matrix if needed
3. fill out the decision record
4. point the project entry file at the decision record
5. keep the entry file at a stable path


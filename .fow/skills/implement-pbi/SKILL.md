---
name: implement-pbi
description: Stage 9 — implement an approved PBI task by task with TDD, update task checkboxes and the feature test.md. Use when the user says to implement a PBI, e.g. "implement PBI-004".
---

Read FOW.md, the PBI, its tasks file, feature.md, and docs/architecture.md first.
Input: PBI id — ask if not given. Require PBI approved; if draft, say so and stop.

1. Set PBI status: in-progress.
2. Per task, TDD: failing test from AC first, implement, green, refactor. Check off task in tasks file as done.
3. Follow architecture.md; a needed deviation = stop, propose ADR first.
4. All tasks done + all AC covered by green tests: update feature test.md (row per REQ: verify type, test name, status). Create from .fow/templates/test.md if missing.
5. If this PBI added any dependency: append a row per package to docs/soup/index.md (package, version, tier TBD, status none, Added by PBI-xxx). Row only — no assessment, no gate. Mention that /update-soup handles the assessment.
6. Show summary + test run output as evidence. Ask: done / more work.
7. On human OK: PBI status done. Suggest: /next.

Never: skip the failing-test step, mark done with red tests, silently deviate from architecture, advance status without explicit approval.

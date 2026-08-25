---
name: plan-pbi
description: Stage 8 — split an approved feature into PBIs with acceptance criteria and one-line tasks. Use when a feature spec is approved, e.g. "plan PBIs for FS-002".
---

Read FOW.md, the feature.md, .fow/templates/pbi.md, .fow/templates/tasks.md first.
Input: FS id — ask if not given. Require feature approved; if draft, say so and stop.

1. Propose split into 1..n PBIs, smallest shippable first. 1-line pitch each. User picks which to detail now.
2. Next PBI id: scan ALL features/*/ (PBI ids global).
3. Draft in the feature folder: PBI-xxx.md (cap 30; AC as Given/When/Then, each AC testable and traceable to a REQ) + PBI-xxx-tasks.md (1 line per task, size S/M/L, file hints).
4. Show drafts. Ask: approve / refine / stop.
5. On approve: status approved. Suggest next: /implement-pbi PBI-xxx.

Never: PBI larger than a few days work (split it), AC without a checkable result, advance status without explicit approval.

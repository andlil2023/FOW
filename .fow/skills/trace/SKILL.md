---
name: trace
description: Show the traceability chain for an ID (ITR/UN/REQ/FS/PBI/ADR/SOUP) or find orphans. Use when the user asks what traces to what, e.g. "trace REQ-003", "trace ITR-002", or "trace orphans".
---

Read-only. Scan frontmatter `traces:` in docs/**, the `iteration:` field on UN and FS, REQ headings `### REQ-xxx [UN-yyy]` in docs/requirements.md, and REQ rows in docs/features/*/test.md.

With ID: print chain UP (parents via traces) and DOWN (everything whose traces include the ID), one line per hop, include status. Include test.md rows for REQs.
Example: `UN-001 approved <- REQ-003 approved <- FS-001 approved <- PBI-004 done <- test: ImportTests.ValidatesHeaders pass`
SOUP walks both ways: `/trace SOUP-001` up through ADR -> ARCH -> PRD; `/trace ADR-004` down to the dependencies it introduced.
ITR walks down only — an iteration schedules, it does not parent. `/trace ITR-002` lists each Scope item, then the full chain below whatever the `iteration:` fields point at.
Example: `ITR-002 in-progress -> I1 UN-004 approved <- REQ-007 approved <- FS-003 draft`
An artifact's own chain is unaffected by its iteration: `/trace UN-004` walks to PRD as always, and notes `scheduled in ITR-002/I1` as a footnote, never as a parent.

With "orphans" (or no ID): list — approved UN with no REQ, approved REQ with no FS, approved REQ with no test row, approved FS with no PBI, any item tracing to a superseded parent, ITR Scope rows whose id field disagrees with the artifacts' `iteration:` fields in either direction.

Package reconciliation is NOT this skill's job — /update-soup diffs code against docs. /trace walks declared links only.

Never: modify any file, invent links not present in the docs, read project/build files.

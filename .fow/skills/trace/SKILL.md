---
name: trace
description: Show the traceability chain for an ID (UN/REQ/FS/PBI/ADR/SOUP) or find orphans. Use when the user asks what traces to what, e.g. "trace REQ-003", or "trace orphans".
---

Read-only. Scan frontmatter `traces:` in docs/**, REQ headings `### REQ-xxx [UN-yyy]` in docs/requirements.md, and REQ rows in docs/features/*/test.md.

With ID: print chain UP (parents via traces) and DOWN (everything whose traces include the ID), one line per hop, include status. Include test.md rows for REQs.
Example: `UN-001 approved <- REQ-003 approved <- FS-001 approved <- PBI-004 done <- test: ImportTests.ValidatesHeaders pass`
SOUP walks both ways: `/trace SOUP-001` up through ADR -> ARCH -> PRD; `/trace ADR-004` down to the dependencies it introduced.

With "orphans" (or no ID): list — approved UN with no REQ, approved REQ with no FS, approved REQ with no test row, approved FS with no PBI, any item tracing to a superseded parent.

Package reconciliation is NOT this skill's job — /update-soup diffs code against docs. /trace walks declared links only.

Never: modify any file, invent links not present in the docs, read project/build files.

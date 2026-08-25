---
name: derive-requirements
description: Stage 5 — derive EARS requirements from an approved user need into docs/requirements.md. Use when a user need is approved and needs requirements, e.g. "derive requirements UN-003".
---

Read FOW.md, the UN file, and docs/requirements.md first (create from .fow/templates/requirements.md if missing).
Input: UN id — ask if not given. Require UN approved; if draft, say so and stop.

1. Next REQ ids: scan requirements.md (never reuse).
2. Draft REQs: one heading block per REQ, heading `### REQ-xxx [UN-yyy] draft`, ONE EARS sentence each (patterns listed at top of requirements.md). No prose.
3. Show drafts. Walk through REQ by REQ: approve / reword / drop.
4. Approved ones: set heading status approved. Append all kept blocks to requirements.md, update `updated:`.
5. Suggest next: /new-feature with the approved REQ ids.

Each REQ must be testable — a reader can say pass/fail. Vague words (fast, easy, robust) = reword with numbers.
Never: multi-sentence REQs, advance status without explicit approval.

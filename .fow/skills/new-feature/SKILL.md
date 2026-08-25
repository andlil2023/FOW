---
name: new-feature
description: Stage 7 — turn approved requirements into a feature spec (new feature folder or delta to an existing feature). Use when requirements are approved, e.g. "create feature from REQ-003 REQ-004".
---

Read FOW.md, .fow/templates/feature.md, docs/requirements.md, and existing docs/features/ first.
Input: REQ ids (or a UN id — then take its approved REQs). Warn and stop if any REQ is draft.

1. Decide with user: NEW feature or DELTA to existing feature (check features/ for overlap, recommend).
2. NEW: next FS id by scanning features/. Create docs/features/FS-xxx-slug/feature.md from template. Cap 50. status: draft. traces: the REQ ids.
3. DELTA: propose amended sections + one dated delta log line. Never regenerate the file. Add new REQ ids to traces.
4. Show draft/delta. Ask: approve / refine / stop.
5. On approve: apply (status approved for new; delta log line written for existing). Suggest next: /plan-pbi FS-xxx.

Never: exceed cap (split into two features instead), leave open questions unlisted, advance status without explicit approval.

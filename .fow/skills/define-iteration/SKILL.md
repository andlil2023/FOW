---
name: define-iteration
description: Stage 4 — define the scope of one iteration as docs/iterations/ITR-xxx.md. Use when starting a new iteration, or when the user wants to add to or change the scope of the current one.
---

Read FOW.md and .fow/templates/iteration.md first.

1. Next ITR id: scan docs/iterations/ (never reuse ids).
2. An ITR already in-progress: report it, ask amend it or open a new one. Stop until answered.
3. Read docs/backlog.md. Show items marked `open`, numbered. No pool yet: say so, continue.
4. LOOP, ONE message each: "What goes in this iteration? Name it, or give a backlog number. Say done when finished."
   Capture the one-liner as given. NO interviewing, NO drilling, NO requirement or design questions — those are stages 5-7.
   Repeat until the user says done. Zero items: nothing to define, stop.
5. One question: the goal, 1-2 lines. One question: anything explicitly out of scope (skippable).
6. Draft docs/iterations/ITR-xxx-slug.md from template. Cap 30 lines. status: draft.
   Number items I1, I2... in the order given. Every row `[ ]`, id field `-`.
7. Show draft. Ask: approve / refine / stop.
8. On approve: status approved, update `updated:`, mark each picked backlog item `ITR-xxx`. Suggest next: /next.

Amend mode (ITR already approved): append Scope rows with fresh item numbers, add a delta log line. Never renumber, never regenerate.
Never: interview the items, exceed cap, advance status without explicit approval.

---
name: new-user-need
description: Stage 5 — interview the user to capture one user need as docs/needs/UN-xxx.md, optionally from an iteration item (ITR-xxx/In). Use when the user wants to define a new user need or revise an existing one.
---

Read FOW.md and .fow/templates/user-need.md first.

0. Argument may be an iteration item (`/new-user-need ITR-002/I2`). If given: read that ITR, take the item's intent line as the seed.
   Item already carries an id: say so, stop. No ITR argument: behave exactly as before, everything below about iterations does not apply.
1. Next UN id: scan docs/needs/ (never reuse ids).
2. Interview, ONE question at a time: who, situation, capability needed, value, frequency, current workaround, priority.
3. Draft docs/needs/UN-xxx-slug.md from template. Cap 25 lines. status: draft.
   From an iteration item: add `iteration: ITR-xxx/In` to frontmatter. Scheduling field, NOT a trace — `traces:` stays [PRD].
4. Show draft. Ask: approve / refine / stop.
5. On approve: status approved. From an iteration item: write the new UN id into that ITR Scope row's id field.
   ITR still `approved`: propose advancing it to in-progress. Human approves — never automatic.
   Suggest next: /derive-requirements UN-xxx.

One need per file. Multiple needs mentioned = ask which one first, do the rest one at a time.
Never: advance status without explicit approval, put `iteration:` into `traces:`.

---
name: define-product
description: Stage 1 — interview the user to create a minimal PRD (docs/prd.md) and seed the candidate backlog (docs/backlog.md). Use when starting a new product or when the user wants to define or revise the product definition.
---

Read FOW.md and .fow/templates/prd.md first.

1. If docs/prd.md exists: refine mode — show current content, ask what to change.
2. Interview, ONE question at a time. Cover: problem, users, goals, non-goals, success signals, constraints. Prefer multiple choice with a recommendation.
3. Draft docs/prd.md from template. Cap 40 lines. Telegraph style. status: draft. NO feature list.
4. Show draft. Ask: approve / refine / stop.
5. On approve: set status: approved, update `updated:`.
6. Seed the pool: derive candidate needs and features from the product statement into docs/backlog.md (template .fow/templates/backlog.md).
   Max 20 items, one line each, grouped by theme, every one marked `open`. Claim nothing the product statement does not support.
   Refine mode: merge new candidates in. Never drop or rewrite an existing line.
7. Show the pool. Ask: approve / refine / stop. Suggest next: /define-architecture.

Never: exceed cap, add features, advance status without explicit approval.

---
name: next
description: Show workflow state and the single next action. Use when resuming work, or when the user asks "where am I", "what's next", or "status".
---

Read-only. Read FOW.md, then scan frontmatter of docs/prd.md, docs/architecture.md, docs/adr/*, docs/iterations/*, docs/needs/*, docs/features/*/*, docs/soup/*, and REQ headings in docs/requirements.md.
Also read docs/backlog.md if present, and the `iteration:` field of every UN and FS.
If docs/prd.md Regulatory says device: yes, also read the dependency manifest (.NET: `<PackageReference>` in *.csproj / Directory.Packages.props; other ecosystems: the equivalent).

Report, compact:
1. Table: artifact | status, grouped by type. Skip done/superseded unless asked.
2. Active ITR (approved or in-progress): table `item | intent | id | status`, one row per Scope row. Note dropped rows, do not chase them.
   Row claims an id but no artifact declares that `iteration: ITR-xxx/In`: flag the mismatch. Index is stale, truth is the artifact.
3. Flag: anything in-progress (resume it first), drafts awaiting approval, approved UNs without REQs, approved REQs not traced by any FS, approved FSs without PBIs, approved PBIs not implemented.
4. SOUP, medical devices only: added packages with no assessment, and assessments whose version no longer matches the manifest (drift silently falsifies the assessed version). Recommend /update-soup. Visibility only — never a blocker.
5. Recommend ONE next action as a skill command. Reason in 1 line. Order:
   a. Anything in-progress — resume it first. Always wins.
   b. Drafts awaiting approval.
   c. No ITR approved or in-progress: `/define-iteration`.
   d. Active ITR, any item short of an approved FS: definition-first. Earliest such item, next missing step —
      `/new-user-need ITR-xxx/In`, then `/derive-requirements UN-xxx`, then `/new-feature REQ-xxx`.
   e. Every item has an approved FS: implementation, one feature at a time — `/plan-pbi FS-xxx`, then `/implement-pbi PBI-xxx`.
   f. Every non-dropped row [x]: report the iteration complete, recommend ITR status done (human approves), then `/define-iteration`.
   Recommendation only. Never a block — the human overrides at will.

Missing docs/prd.md = fresh repo: recommend /define-product.
PRD approved, architecture and scaffold done, no ITR anywhere: recommend /define-iteration.
Never: modify any file.

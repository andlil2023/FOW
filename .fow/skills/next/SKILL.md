---
name: next
description: Show workflow state and the single next action. Use when resuming work, or when the user asks "where am I", "what's next", or "status".
---

Read-only. Read FOW.md, then scan frontmatter of docs/prd.md, docs/architecture.md, docs/adr/*, docs/needs/*, docs/features/*/*, docs/soup/*, and REQ headings in docs/requirements.md.
If docs/prd.md Regulatory says device: yes, also read the dependency manifest (.NET: `<PackageReference>` in *.csproj / Directory.Packages.props; other ecosystems: the equivalent).

Report, compact:
1. Table: artifact | status, grouped by type. Skip done/superseded unless asked.
2. Flag: anything in-progress (resume it first), drafts awaiting approval, approved UNs without REQs, approved REQs not traced by any FS, approved FSs without PBIs, approved PBIs not implemented.
3. SOUP, medical devices only: added packages with no assessment, and assessments whose version no longer matches the manifest (drift silently falsifies the assessed version). Recommend /update-soup. Visibility only — never a blocker.
4. Recommend ONE next action as a skill command, e.g. `/plan-pbi FS-002`. Reason in 1 line.

Missing docs/prd.md = fresh repo: recommend /define-product.
Never: modify any file.

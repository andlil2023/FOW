---
name: define-architecture
description: Stage 2 — grill the user on platforms, project type, architecture style, framework, packages and coding style; create docs/architecture.md plus one ADR per decision. Use when the PRD is approved or when revisiting an architecture decision.
---

Read FOW.md, docs/prd.md, .fow/templates/architecture.md, .fow/templates/adr.md first.
Require prd.md status approved AND its Regulatory section filled; if not, say so and stop.
If docs/architecture.md exists: change mode — changes go through a NEW ADR (delta principle), then amend architecture.md to match.

## Interview: use grilling
Read `.fow/skills/grilling/SKILL.md` and run its procedure over the decision tree below. Question order and format come from grilling — one question at a time; the tree comes from here. Give a recommendation for every question. Look facts up yourself — existing code, project files, installed SDKs — never ask what you can find.

## Decision tree
Prerequisites point down: a child cannot be asked until its parent is settled.

1. **Project type** — web | desktop | console | service | library | mobile.
2. **Platforms & targets** (needs 1) — OS and versions, runtime/framework target (e.g. net8.0, LTS policy, multi-targeting), browsers if web, hardware if it constrains code. In a regulated product this list is a specification claim: it is what verification runs against.
3. **Language / runtime** (needs 1, 2).
4. **Framework** (needs 1, 2, 3) — depends on project type: WPF, Blazor Server, ASP.NET Core, MAUI, console host.
5. **Architecture style** (needs 1) — FOW defaults: **Vertical Slice Architecture** and **DDD-lite**. DDD-lite = ubiquitous language + aggregate boundaries; repositories and domain events optional, not mandated (mandating repositories fights VSA, where slices usually query directly). Propose the defaults. Deviation is allowed but its ADR must record WHY.
6. **Coding style** (needs 3, 5) — functional style, railway-oriented programming, or conventional. If ROP: which Result type. Default recommendation `CSharpFunctionalExtensions`; a hand-rolled Result means maintaining monadic bind semantics yourself. A package here becomes a SOUP entry.
7. **Style enforcement** (needs 6) — what scaffold-solution emits: .editorconfig, Directory.Build.props (Nullable, LangVersion, AnalysisLevel), analyzer packages, warnings-as-errors on a chosen subset (nullable, unused, async-void, unobserved results) rather than everything.
8. **Storage** (needs 1, 3) — db | files | none; what stores what.
9. **Third-party packages** (needs 3, 4, 6, 8) — what the product explicitly adds. List them with purpose. Do NOT assess them here; suggest /update-soup after approval.
10. **Test frameworks** (needs 3, 5).
11. **Deployment** (needs 1, 2) — installer | container | copy.
12. **Source control / CI** (needs 11) — host, branching, pipeline.

## Output
1. One ADR per decision — docs/adr/ADR-xxx-slug.md, cap 20, next id by scanning docs/adr/. Roughly 11-12 ADRs. Do not group decisions into one ADR: a grouped ADR cannot be cleanly superseded when one of its decisions is revisited.
2. docs/architecture.md from template, cap 90, every section linking its ADR. status: draft.
3. Show drafts. Ask: approve / refine / stop.
4. On approve: statuses approved. Suggest next: /update-soup for the package list, then /scaffold-solution.

Architecture may be approved with SOUP assessments still outstanding — /next reports them.

Never: design feature internals here, assess SOUP here, group several decisions into one ADR, advance status without explicit approval.

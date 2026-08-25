---
name: scaffold-solution
description: Stage 3 — create the empty solution skeleton from the approved architecture. Use once after architecture approval, before any feature work.
---

Read FOW.md and docs/architecture.md first.
Require architecture.md status approved; if not, say so and stop.

1. Propose skeleton: projects, test projects, folder layout per architecture.md solution structure. Show plan, get OK before creating.
2. Create smallest possible skeleton. NO features, NO logic. Wire up test framework.
3. Emit style enforcement exactly as architecture.md Coding style & enforcement specifies: .editorconfig, Directory.Build.props (Nullable, LangVersion, AnalysisLevel), analyzer + Result package references. Warnings-as-errors on the named subset only — blanket TreatWarningsAsErrors on a fresh solution blocks the first build on trivia and teaches suppression. Read the values from architecture.md; never hardcode them.
4. Verify: solution builds, test run executes (0 tests = fine). Show output as evidence.
5. Ask: approve / refine / stop.
6. On approve: suggest next: /new-user-need.

Never: add example/demo code, install packages not in architecture.md, proceed on red build.

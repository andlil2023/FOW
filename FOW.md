# FOW — Feature Oriented Workflow with AI

Human-led iterative dev workflow for new products. Feature oriented: every increment runs need -> requirements -> feature -> PBI -> code. AI assists, never decides.

## Laws
1. Human is master. AI drafts, human approves. No status change without explicit human OK.
2. One artifact per step. Skill writes it, stops, asks: approve / refine / stop.
3. Telegraph style. Extreme concision. Information over grammar. Fragments fine. No filler, no repetition. Minimum tokens without losing technical meaning. Hard line cap per template. Cap hit = split, never grow.
   Carve-out: externally-mandated documents (regulatory assessments) carry the cap their standard requires and are exempt from split-never-grow. They cannot be split without breaking the structure an auditor expects.
   Carve-out: prd.md has no cap. It is the one place the whole product is described, and it grows as the product does. Telegraph style still binds it, and the no-feature-list rule still holds — length must come from the product, never from detail that belongs in a need, a requirement or a feature.
4. Delta principle. After approval: amend, never regenerate. Architecture change = new ADR. Feature change = delta log line.
5. Two directories, one rule each. docs/ = every artifact, human-readable, human-approved. .fow/ = workflow internals (skills, templates), never hand-edited.
   docs/ exists only in the product repo. The FOW kit repo has none — the skills create it as output. Never write a design note, spec or plan into docs/ here.
6. Tool-neutral. Skills are plain markdown in .fow/skills/. AGENTS.md routes any agent to them; .claude/skills/ holds generated pointer stubs only.
   Stubs duplicate each description, so they drift. Regenerate with `python .fow/bin/sync-stubs.py` after editing any canonical skill; `--check` reports drift without writing.

## Stages
| # | Stage | Skill | Output | Gate |
|---|-------|-------|--------|------|
| 1 | Product | /define-product | prd.md + backlog.md | human approves |
| 2 | Architecture | /define-architecture | architecture.md + adr/ADR-xxx | human approves |
| 3 | Scaffold | /scaffold-solution | empty solution, builds | human approves |
| 4 | Iteration | /define-iteration | iterations/ITR-xxx-slug.md | human approves |
| 5 | User need | /new-user-need | needs/UN-xxx.md | human approves |
| 6 | Requirements | /derive-requirements | REQ blocks in requirements.md | human approves each |
| 7 | Feature | /new-feature | features/FS-xxx-slug/feature.md (new or delta) | human approves |
| 8 | Plan | /plan-pbi | PBI-xxx.md + PBI-xxx-tasks.md | human approves |
| 9 | Implement | /implement-pbi | code (TDD), test.md rows | tests green + human OK |

Stages 1-3 once. Stage 4 repeats per iteration. Stages 5-9 repeat per item in the active iteration: definition (5-7) for every item first, then implementation (8-9) one feature at a time.
Anytime: /next (state + next step), /trace ID (chain), /grilling (stress-test a plan or decision), /update-soup (reconcile dependencies against assessments).

## IDs
ITR- iteration, UN- need, REQ- requirement, FS- feature, PBI- backlog item, ADR- decision, SOUP- third-party component assessment.
External ids referenced but NOT owned by FOW: RMF-, RISK-, SBOM-, CCR-, TEST- (they live in the QMS; never mint them here).
Global sequence per type. Never reuse, never delete; retire via status: superseded.
Tasks local to PBI: T1, T2... referenced as PBI-xxx/T2. Scope items local to iteration: I1, I2... referenced as ITR-xxx/I2.

## Status
draft -> approved -> in-progress -> done. superseded from any state. New artifact = draft.
ITR: approved = scope agreed; in-progress = first item artifact created; done = every non-dropped item's feature(s) done. Skill proposes each transition, human approves. Never automatic.
SOUP: draft -> approved; removed dependency -> superseded, file retained. Regulatory sign-off lives in the QMS, not in FOW status.

## Regulatory
prd.md Regulatory section (device y/n, IEC 62304 safety class, framework) is set at stage 1 and selects the SOUP form:
not a device or class A -> soup-short. Class B/C -> soup-full where the component can contribute to a hazardous situation, else soup-short.
Exempt from assessment: runtime / shared-framework packages (covered by the Platforms & targets ADR). Assessed: everything explicitly added, regardless of publisher.
Facts are the agent's job; safety judgments (impact, risk, controls, residual risk, conclusion) are the human's and must be left empty, never drafted.

## Frontmatter (every artifact)
```yaml
---
id: FS-001
title: short title
status: draft
traces: [REQ-003]   # parent ids, child points up
updated: 2026-08-21
---
```
Chain: REQ->UN, FS->REQ, PBI->FS, test.md row->REQ, SOUP->ADR (else ARCH, else the PBI that introduced it). Trace matrix derived by scan, never hand-kept.
Scheduling, not tracing: UN and FS created under an iteration carry `iteration: ITR-xxx/In`. Never enters `traces:` — a need belongs to the product, it is merely scheduled in an iteration.
Exception: backlog.md is a working pool — id, title, traces, updated only. No `status:`. Drained item by item, never approved as a whole.

## Requirements format (requirements.md)
```
### REQ-003 [UN-001] approved
When the user drops a CSV file, the system shall validate headers within 1s.
```
EARS patterns: The system shall X. / When T, the system shall X. / While S, the system shall X. / If C, then the system shall X. / Where F, the system shall X.

## Iteration scope rows (iterations/ITR-xxx-slug.md)
```
- [ ] I1 login required before any access -> UN-004
```
Mark: [ ] open · [x] complete, every id done · [-] dropped, reason in the delta log.
Id field: `-` until an artifact is minted, then the UN during definition, replaced by the FS once the feature exists. Names the terminal artifact, never the trail. Comma-separated only when one item yields several features.
Skill-written index, never hand-edited. Truth is the `iteration:` field on the artifact; /next flags mismatch.

## Diagrams
Mermaid for anything UML-shaped: class, sequence, state, ER, flow. Text source, diffable, renders in the repo host.
ASCII for folder and file trees only.
Diagram carries the structure; prose does not restate it.

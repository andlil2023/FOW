# FOW — Feature Oriented Workflow with AI

Human-led iterative dev workflow for new products. Feature oriented: every increment runs need -> requirements -> feature -> PBI -> code. AI assists, never decides.

## Laws
1. Human is master. AI drafts, human approves. No status change without explicit human OK.
2. One artifact per step. Skill writes it, stops, asks: approve / refine / stop.
3. Telegraph style. Extreme concision. Information over grammar. Fragments fine. No filler, no repetition. Minimum tokens without losing technical meaning. Hard line cap per template. Cap hit = split, never grow.
   Carve-out: externally-mandated documents (regulatory assessments) carry the cap their standard requires and are exempt from split-never-grow. They cannot be split without breaking the structure an auditor expects.
4. Delta principle. After approval: amend, never regenerate. Architecture change = new ADR. Feature change = delta log line.
5. Two directories, one rule each. docs/ = every artifact, human-readable, human-approved. .fow/ = workflow internals (skills, templates), never hand-edited.
6. Tool-neutral. Skills are plain markdown in .fow/skills/. AGENTS.md routes any agent to them; .claude/skills/ holds generated pointer stubs only.
   Stubs duplicate each description, so they drift. Regenerate with `python .fow/bin/sync-stubs.py` after editing any canonical skill; `--check` reports drift without writing.

## Stages
| # | Stage | Skill | Output | Gate |
|---|-------|-------|--------|------|
| 1 | Product | /define-product | prd.md | human approves |
| 2 | Architecture | /define-architecture | architecture.md + adr/ADR-xxx | human approves |
| 3 | Scaffold | /scaffold-solution | empty solution, builds | human approves |
| 4 | User need | /new-user-need | needs/UN-xxx.md | human approves |
| 5 | Requirements | /derive-requirements | REQ blocks in requirements.md | human approves each |
| 6 | Feature | /new-feature | features/FS-xxx-slug/feature.md (new or delta) | human approves |
| 7 | Plan | /plan-pbi | PBI-xxx.md + PBI-xxx-tasks.md | human approves |
| 8 | Implement | /implement-pbi | code (TDD), test.md rows | tests green + human OK |

Stages 4-8 repeat per increment. Anytime: /next (state + next step), /trace ID (chain), /grilling (stress-test a plan or decision), /update-soup (reconcile dependencies against assessments).

## IDs
UN- need, REQ- requirement, FS- feature, PBI- backlog item, ADR- decision, SOUP- third-party component assessment.
External ids referenced but NOT owned by FOW: RMF-, RISK-, SBOM-, CCR-, TEST- (they live in the QMS; never mint them here).
Global sequence per type. Never reuse, never delete; retire via status: superseded.
Tasks local to PBI: T1, T2... referenced as PBI-xxx/T2.

## Status
draft -> approved -> in-progress -> done. superseded from any state. New artifact = draft.
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

## Requirements format (requirements.md)
```
### REQ-003 [UN-001] approved
When the user drops a CSV file, the system shall validate headers within 1s.
```
EARS patterns: The system shall X. / When T, the system shall X. / While S, the system shall X. / If C, then the system shall X. / Where F, the system shall X.

## Diagrams
Mermaid for anything UML-shaped: class, sequence, state, ER, flow. Text source, diffable, renders in the repo host.
ASCII for folder and file trees only.
Diagram carries the structure; prose does not restate it.

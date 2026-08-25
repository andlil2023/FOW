# AGENTS.md — FOW (Feature Oriented Workflow with AI)

Entry point for any AI agent working in this repo. Read `FOW.md` for the full rules, then read the skill file for the stage you are running and follow it exactly.

## Laws (canonical text in FOW.md)
1. Human is master. Agent drafts, human approves. No status change without explicit human OK.
2. One artifact per step. Write it, stop, ask: approve / refine / stop.
3. Telegraph style. Extreme concision. Information over grammar. Fragments fine. No filler, no repetition. Minimum tokens without losing technical meaning. Hard line cap per template. Cap hit = split, never grow. Carve-outs: externally-mandated regulatory documents keep the cap their standard requires; `prd.md` has no cap and grows with the product, still telegraph style and still no feature list.
   Diagrams: Mermaid for UML-shaped (class, sequence, state, ER, flow); ASCII for folder trees.
4. Delta principle. After approval: amend, never regenerate. Architecture change = new ADR. Feature change = delta log line.
5. Two directories, one rule each. `docs/` = every artifact, human-readable, human-approved. `.fow/` = workflow internals, never hand-edited.
   `docs/` exists only in the product repo. The FOW kit repo has none — the skills create it as output.

## Skills
Each skill is a plain markdown procedure — no tool-specific features. Any agent can run one.

| Stage | Trigger | Does | File to read |
|---|---|---|---|
| 1 | `/define-product` | interview the user to create a minimal PRD (docs/prd.md) and seed the candidate backlog (docs/backlog.md) | `.fow/skills/define-product/SKILL.md` |
| 2 | `/define-architecture` | interview the user on tools, language, storage, tests, deployment; create docs/architecture.md plus ADRs | `.fow/skills/define-architecture/SKILL.md` |
| 3 | `/scaffold-solution` | create the empty solution skeleton from the approved architecture | `.fow/skills/scaffold-solution/SKILL.md` |
| 4 | `/define-iteration` | define the scope of one iteration — a short list of user needs and features, no interviewing | `.fow/skills/define-iteration/SKILL.md` |
| 5 | `/new-user-need` | interview the user to capture one user need as docs/needs/UN-xxx.md | `.fow/skills/new-user-need/SKILL.md` |
| 6 | `/derive-requirements` | derive EARS requirements from an approved user need into docs/requirements.md | `.fow/skills/derive-requirements/SKILL.md` |
| 7 | `/new-feature` | turn approved requirements into a feature spec (new feature folder or delta to an existing feature) | `.fow/skills/new-feature/SKILL.md` |
| 8 | `/plan-pbi` | split an approved feature into PBIs with acceptance criteria and one-line tasks | `.fow/skills/plan-pbi/SKILL.md` |
| 9 | `/implement-pbi` | implement an approved PBI task by task with TDD, update task checkboxes and the feature test.md | `.fow/skills/implement-pbi/SKILL.md` |
| - | `/next` | Show workflow state and the single next action | `.fow/skills/next/SKILL.md` |
| - | `/trace` | Show the traceability chain for an ID (ITR/UN/REQ/FS/PBI/ADR/SOUP) or find orphans | `.fow/skills/trace/SKILL.md` |
| - | `/grilling` | Grill the user relentlessly about a plan, decision, or idea until shared understanding | `.fow/skills/grilling/SKILL.md` |
| - | `/update-soup` | Reconcile SOUP assessments against the dependencies actually used in code | `.fow/skills/update-soup/SKILL.md` |

Flow: stages 1-3 once, stage 4 per iteration, stages 5-9 per item in it — define every item first, then implement one feature at a time. `/next`, `/trace`, `/grilling`, `/update-soup` anytime.

## How to run a skill
User names a trigger (`/new-user-need`, or plain language matching the "Does" column):
1. Read `FOW.md`.
2. Read `.fow/skills/<name>/SKILL.md`.
3. Follow it literally, including its stop-and-ask gate.

Never improvise the workflow, skip the approval gate, or advance a `status:` field on your own.

## Directories
| Path | Owner | Rule |
|---|---|---|
| `FOW.md` | human | canonical rules |
| `AGENTS.md` | human | this router |
| `docs/` | agent writes, human approves | every artifact, **product repo only**: `prd.md`, `backlog.md`, `architecture.md`, `adr/`, `iterations/`, `needs/`, `requirements.md`, `features/FS-xxx-slug/` |
| `.fow/skills/` | maintainer | canonical skill procedures — edit here |
| `.fow/templates/` | maintainer | 14 artifact templates |
| `.fow/bin/` | maintainer | `sync-stubs.py` — regenerates the stubs below from the canonical skills |
| `.claude/skills/` | generated | pointer stubs for Claude Code discovery. Do not edit — run `python .fow/bin/sync-stubs.py` |

## IDs and traceability
`ITR-` iteration, `UN-` need, `REQ-` requirement, `FS-` feature, `PBI-` backlog item, `ADR-` decision, `SOUP-` third-party component assessment. Global sequence per type, never reused, never deleted — retire via `status: superseded`.
`RMF-`, `RISK-`, `SBOM-`, `CCR-`, `TEST-` are external QMS ids. Reference them; never mint them.
Chain points up: `REQ->UN`, `FS->REQ`, `PBI->FS`, test row->`REQ`, `SOUP->ADR` (else `ARCH`, else the introducing `PBI`). Declared in frontmatter `traces:`. Matrix derived by scan, never hand-kept.
`iteration: ITR-xxx/In` on a UN or FS is scheduling, not tracing. It never enters `traces:`.

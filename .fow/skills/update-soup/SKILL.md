---
name: update-soup
description: Reconcile SOUP assessments against the dependencies actually used in code — add missing, update drifted, supersede removed. Use when the user asks to update, check, or reconcile SOUP, or before a release.
---

Read FOW.md, docs/prd.md (Regulatory section), docs/architecture.md, .fow/templates/soup-full.md, .fow/templates/soup-short.md, .fow/templates/soup-index.md first.
Outside the standard stage flow. No gate blocks on it. Run anytime.

## 1. Read the truth
Dependency manifest is the source of truth, not memory. .NET: `<PackageReference>` in `*.csproj` / `Directory.Packages.props`. Other ecosystems: the equivalent manifest (package.json, requirements.txt, go.mod).
DIRECT dependencies only. Transitive = SBOM + vulnerability monitoring, not assessed here.

## 2. Apply the exemption rule
Exempt: shipped in the runtime / shared framework (System.*, the SDK) — covered by the Platforms & targets ADR.
Assessed: every package the manufacturer explicitly added, REGARDLESS of publisher. Microsoft-published is not exempt (EF Core can sit in a clinical data path).

## 3. Pick the form per package
Read safety class from docs/prd.md Regulatory section.
- not a medical device -> soup-short
- class A -> soup-short
- class B/C -> soup-full if the component can contribute to a hazardous situation, else soup-short
Ask the user for the hazard-contribution call on class B/C. Never decide it yourself.

## 4. Diff
Report a table before writing anything:
| package | manifest version | assessed version | verdict |
Verdicts: MISSING (no file), DRIFT (version differs), REMOVED (file exists, package gone), OK.

## 5. Act, one package at a time, gate each
- MISSING: create docs/soup/SOUP-xxx-slug.md from the chosen template. Next id by scanning docs/soup/.
- DRIFT: amend the existing file (delta principle, never regenerate). Bump Assessment Revision, update §1 Version and §11. Re-open the HUMAN sections for review — a version change can invalidate them.
- REMOVED: propose status: superseded. Keep the file. An assessment for a component that shipped in an earlier version must stay retrievable.
- Set traces: the ADR that chose it; else [ARCH]; else [PBI-xxx] if a PBI introduced it.

FILL (facts, your job): §1 Identification, §11 Version and Configuration Control, §12 Supplier / Project Evaluation, and draft §2 §4 §5 §10.
LEAVE EMPTY (safety judgments, human only): §6 Safety Impact, §7 Risk Management, §8 Risk Controls, §13 Residual Risk, §14 Conclusion. Short form: §5 Hazard Contribution Justification.
Look facts up — package metadata, license, release history, issue tracker, advisories. Never ask the user for a fact you can find.

## 6. Update the index
docs/soup/index.md: one row per added package including exempt ones. Create from template if missing.

## 7. Report
Show each draft. Ask: approve / refine / stop. Per package, not per batch.
Close with what still needs a human: every file whose judgment sections are empty.

Never: fill a safety judgment section, approve a batch in one gate, assess transitive dependencies, delete a superseded assessment, decide hazard contribution for class B/C, advance status without explicit approval.

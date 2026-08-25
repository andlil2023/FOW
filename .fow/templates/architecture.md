<!-- TEMPLATE architecture. Cap: 90 lines. Every decision links its ADR. File: docs/architecture.md -->
---
id: ARCH
title: <product name> architecture
status: draft
traces: [PRD]
updated: <yyyy-mm-dd>
---

# Architecture

## App type
<web | console | desktop | service> — [ADR-001]

## Platforms & targets
OS: <os + versions> · Runtime target: <e.g. net8.0, LTS policy> · Browsers: <if web> · Hardware: <if it constrains code> — [ADR-002]
<!-- In a regulated product this list is a specification claim: verification runs against it. -->

## Language / runtime
<language + version> — [ADR-003]

## Framework
<WPF | Blazor Server | ASP.NET Core | MAUI | console host> — [ADR-004]

## Architecture style
Vertical Slice Architecture · DDD-lite (ubiquitous language + aggregate boundaries; repositories/domain events optional) — [ADR-005]
<!-- FOW defaults. A deviation is allowed but its ADR must record why. -->

## Coding style & enforcement
Style: <functional | railway-oriented | conventional> · Result type: <package or hand-rolled> — [ADR-006]
Enforced by: <.editorconfig | Directory.Build.props | analyzers> · warnings-as-errors on: <subset>

## Key packages / tools
- <package/tool>: <purpose, 1 line>

## Storage
<db | files | none; what stores what> — [ADR-xxx]

## Test frameworks
<unit / integration tooling>

## Deployment
<installer | container | copy> — [ADR-xxx]

## Source control / CI
<host: Azure DevOps | GitHub | local git> · <branching: trunk | feature branches> · <pipeline: none | ADO Pipelines | GitHub Actions> — [ADR-xxx]

## Solution structure
```
<src tree sketch, top 2 levels — ASCII tree>
```

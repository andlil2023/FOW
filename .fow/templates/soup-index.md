<!-- TEMPLATE soup index registry. Copy once to docs/soup/index.md.
One row per dependency the manufacturer explicitly added, INCLUDING exempt ones - the
exemption record is what proves the rule was applied to this dependency set.
Runtime / shared-framework packages (System.*, the SDK) are exempt: they come with the
platform declared in architecture.md Platforms & targets. Everything explicitly added is
listed, regardless of publisher.
Maintained by /update-soup. Rows appended by /implement-pbi. Never hand-kept. -->
---
id: SOUPINDEX
title: SOUP index
status: approved
traces: [ARCH]
updated: <yyyy-mm-dd>
---

# SOUP index

Tier: `full` | `short` | `exempt`. Exempt rows need no assessment file — state why.

| Package | Version | SOUP | Tier | Status | Added by | Note |
| ------- | ------- | ---- | ---- | ------ | -------- | ---- |
| `<package id>` | <version> | SOUP-001 | full | approved | ADR-004 | <purpose, few words> |
| `<package id>` | <version> | SOUP-002 | short | draft | PBI-012 | no hazard contribution |
| `System.Text.Json` | <version> | — | exempt | — | ARCH | shipped in runtime |

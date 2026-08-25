<!-- TEMPLATE soup-short. Cap: 45 lines.
Use when: product is not a medical device, OR IEC 62304 safety class A, OR the component
cannot contribute to a hazardous situation. Otherwise use soup-full.md.
File: docs/soup/SOUP-xxx-slug.md
Section 5 justification is HUMAN: it is the record of the triage decision. -->
---
id: SOUP-xxx
title: <component name> <version>
status: draft
traces: [ADR-xxx]   # the ADR that chose it; else [ARCH]; else [PBI-xxx] if added mid-implementation
updated: <yyyy-mm-dd>
---

# SOUP Assessment (short form) — <component name>

## 1. Identification

| Field                 | Value                  |
| --------------------- | ---------------------- |
| SOUP ID               | SOUP-xxx               |
| Software              | <name>                 |
| Version               | <exact version>        |
| Supplier / Maintainer | <project or vendor>    |
| Component Type        | <what kind of library> |
| License               | <SPDX id + name>       |
| Source                | <NuGet / npm / vendor> |
| Package               | `<package id>`         |
| Assessment Date       | <yyyy-mm-dd>           |
| Assessed By           | <name>                 |

## 2. Purpose
<component> is used by <product> to <one line>. Used for: <uses, comma separated>.

## 3. SOUP Classification
Third-party software not developed under the lifecycle processes applied to <product>. Development records and complete verification evidence are not available to the manufacturer.

## 4. Version and Configuration Control
Approved version `<name> <version>`, pinned in the dependency configuration and reproducible from the build. A version change requires evaluation under the software change-control process.

## 5. Hazard Contribution Justification
<!-- HUMAN ONLY. This is why the short form is sufficient. Do not auto-draft. -->
Short form justified because: <one of - product is not a medical device / safety class A / component cannot contribute to a hazardous situation>.

<1-3 lines: why this component cannot contribute to a hazardous situation.>

## 6. Traceability
Requirement: REQ-xxx · Architecture: ARCH, ADR-xxx · SBOM: external SBOM-xxx

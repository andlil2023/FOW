<!-- TEMPLATE soup-full. Cap: 260 lines (Law 3 carve-out: externally-mandated document).
Use when: medical device, IEC 62304 safety class B or C, AND the component can contribute to a hazardous situation.
Otherwise use soup-short.md. File: docs/soup/SOUP-xxx-slug.md
The source format's section 15 (approval signatures) is intentionally absent - signatures live in the QMS.
AGENT sections are facts: fill them. HUMAN sections are safety judgments: leave empty, never draft. -->
---
id: SOUP-xxx
title: <component name> <version>
status: draft
traces: [ADR-xxx]   # the ADR that chose it; else [ARCH]; else [PBI-xxx] if added mid-implementation
updated: <yyyy-mm-dd>
---

# SOUP Assessment — <component name>

## 1. Identification
<!-- AGENT: facts. All discoverable from package metadata, license file, project repo. -->

| Field                 | Value                              |
| --------------------- | ---------------------------------- |
| SOUP ID               | SOUP-xxx                           |
| Software              | <name>                             |
| Version               | <exact version>                    |
| Supplier / Maintainer | <project or vendor>                |
| Component Type        | <e.g. open-source logging library> |
| License               | <SPDX id + name>                   |
| Source                | <NuGet / npm / vendor>             |
| Package               | `<package id>`                     |
| Used By               | <product name>                     |
| Assessment Revision   | <1.0>                              |
| Assessment Date       | <yyyy-mm-dd>                       |
| Assessed By           | <name>                             |

---

## 2. Purpose
<!-- AGENT: drafts from the ADR and actual code usage. HUMAN: confirms the exclusion statement. -->

<component> is used by <product> to <one line>.

The library is used for:

* <use, 1 line each>

<component> is **not used to implement clinical algorithms, calculate medical information, control treatment, or make safety-related decisions.**
<!-- If that statement is NOT true, the component is safety-related: sections 6-8 and 13 carry real weight. -->

Failure of the <function> functionality shall not prevent the application from performing its essential functions.

---

## 3. SOUP Classification
<!-- AGENT: standard wording, no judgment. -->

The component is considered **Software of Unknown Provenance (SOUP)** because it is third-party software that was not developed according to the software development lifecycle processes applied to <product>.

The development records and complete verification evidence for the component are not available to the manufacturer.

---

## 4. Intended Use Within the System
<!-- AGENT: drafts the layer sketch from architecture.md and the actual references. -->

<component> is used by the <layer> layer.

```text
Application
    |
    +-- Business / Clinical Logic
    |
    +-- Infrastructure
            |
            +-- <concern>
                    |
                    +-- <component>
```

The application interacts with <component> through <abstraction, or "direct reference">.

<State whether any safety-critical domain logic depends on it directly.>

---

## 5. Known Anomalies
<!-- AGENT: gather from the sources below, list what was found. HUMAN: accepts the conclusion. -->

Known anomalies were reviewed using the following sources:

* Project release notes
* Project issue tracker
* Security advisories
* Package registry information

### Assessment

<Findings, or: No known anomaly has been identified that prevents the component from being used for its intended purpose in <product>.>

Known anomalies relevant to the configured version shall be evaluated through the product's defect and risk-management processes.

---

## 6. Safety Impact Analysis
<!-- HUMAN ONLY. /update-soup must leave this table empty. A plausible auto-drafted safety
analysis is more dangerous than a blank one, because it gets approved. -->

| Failure Mode | Possible Effect | Safety Impact | Mitigation |
| ------------ | --------------- | ------------- | ---------- |
|              |                 |               |            |

---

## 7. Risk Management
<!-- HUMAN ONLY. RISK ids are external (Risk Management File), not FOW ids. -->

| Risk ID | Hazard / Hazardous Situation | Related Failure |
| ------- | ---------------------------- | --------------- |
|         |                              |                 |

Detailed risk analysis and risk-control verification are maintained in the <product> Risk Management File (external: RMF-xxx).

---

## 8. Risk Controls
<!-- HUMAN ONLY. -->

* <control, 1 line each>

---

## 9. Verification
<!-- AGENT: may list existing FOW test rows. HUMAN: decides what verification is required. -->

| Verification | Description | Result |
| ------------ | ----------- | ------ |
|              |             |        |

FOW-managed tests reference the feature's `test.md` row. External qualification tests keep their own ids.

The SOUP component itself is not independently verified as a complete software product. Verification focuses on its intended use and integration within <product>.

---

## 10. Cybersecurity Assessment
<!-- AGENT: standard wording plus any known advisories. -->

The component is included in the product's third-party dependency and vulnerability-management process. Monitored: published vulnerabilities, supplier advisories, new releases, end-of-support or project abandonment, dependency changes.

A newly identified vulnerability shall be evaluated for applicability and product impact according to the vulnerability-management process.

---

## 11. Version and Configuration Control
<!-- AGENT: facts. This is the section /update-soup checks for drift. -->

The approved version is:

```text
<name> <version>
```

The version is explicitly defined by the product's dependency configuration and is therefore reproducible as part of the software build.

Changing the approved version requires evaluation according to the software change-control process, which may require: review of release notes; review of known anomalies; review of security vulnerabilities; evaluation of changes affecting intended use; regression testing; update of this assessment.

---

## 12. Supplier / Project Evaluation
<!-- AGENT: facts. All observable from the project's public presence. -->

| Criterion                              | Assessment |
| -------------------------------------- | ---------- |
| Project actively maintained            | <Yes/No>   |
| Public issue tracking available        | <Yes/No>   |
| Release history available              | <Yes/No>   |
| Source code available                  | <Yes/No>   |
| Security reporting mechanism available | <Yes/No>   |
| License acceptable                     | <Yes/No>   |
| Widely used                            | <Yes/No>   |
| Replacement feasible                   | <Yes/No>   |

---

## 13. Residual Risk Assessment
<!-- HUMAN ONLY. -->

**Residual Risk:** <Acceptable / Not acceptable>

<Justification, 1-3 lines.>

---

## 14. Conclusion
<!-- HUMAN ONLY. -->

**Assessment Result:** <Approved for Use / Not approved>

The component may be used provided that: the approved version remains under configuration control; identified risk controls remain implemented; relevant verification tests remain successful; known anomalies and security vulnerabilities continue to be monitored; and changes are evaluated through the software change-control process.

---

## 15. Traceability
<!-- FOW ids for requirement and architecture. Everything else points into the external QMS. -->

| Item                  | Reference                       |
| --------------------- | ------------------------------- |
| Software Requirement  | REQ-xxx                         |
| Software Architecture | ARCH, ADR-xxx                   |
| Risk Management File  | external: RMF-xxx               |
| SOUP Risk             | external: RISK-xxx              |
| Verification          | test.md row / external TEST-xxx |
| SBOM                  | external: SBOM-xxx              |
| Change Control        | external: CCR-xxx               |

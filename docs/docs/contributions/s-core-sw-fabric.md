<!--
 ********************************************************************************
 * Copyright (c) 2026 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Apache License 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************
-->
# s-core_sw_fabric contribution proposal

**Status: contribution candidate for maintainer review.** This describes an
existing community implementation and a proposed Hephaestus pilot. Adoption,
tool qualification and engineering acceptance remain pending.

## Contribution and fit

`s-core_sw_fabric` connects project-owned engineering artifacts to bounded
workflow execution, deterministic checks and portable evidence. It was developed
against Eclipse S-CORE and is proposed here as a starting point for reusable SDV
engineering workflow tooling.

Hephaestus's [project scope](https://projects.eclipse.org/proposals/eclipse-sdv-hephaestus)
covers task automation, Sphinx-Needs traceability, composable tooling and
qualification preparation. The fabric can contribute to those areas through
project-specific adapters and explicit policy bindings.

| Hephaestus area | Proposed contribution | Integration still required |
| --- | --- | --- |
| Build and dependency management | Invoke native checks with pinned source/tool/configuration identities and retain their results | Bind the target's supported Bazel/Cargo commands and dependency obligations |
| Environment and tool provisioning | Isolated workspaces, measured storage capabilities and tool prerequisite records | Review portable environment/tool profiles and remove workstation-specific assumptions |
| Task runner and automation | Derived workflow plans, bounded execution and explicit stop reasons | Agree on the runtime interface and ownership of run state |
| Doc-as-Code and qualification preparation | Native artifact identities, evidence freshness, requirement-to-check trace and review packets | Map Hephaestus's metamodel and review/qualification obligations without importing S-CORE policy implicitly |
| AI assistance | Scoped context, constrained tools and deterministic output checks | Configure optional providers, permissions and usage limits; agents do not grant engineering acceptance |

The pilot relates to the existing draft use cases
{need}`US_DOC_AS_CODE_TRACEABILITY`,
{need}`US_PILOT_ADOPTION_SDV_PROJECTS` and
{need}`US_AUTOMOTIVE_QUALIFICATION_TOOLING`.
These references express proposed alignment, not fulfillment of those use cases.

## Review baseline and ownership

The proposed starting point is the public
[implementation at commit 7e24a43](https://github.com/jnsagai/s-core_sw_fabric/tree/7e24a43c258f1dcaa2b27e02b501964847bc8714), licensed under
[Apache-2.0](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/LICENSE), with its [notices](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/NOTICE)
and [dependency lock](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/uv.lock).

This proposal does not transfer the implementation into an Eclipse repository.
It requests agreement on a small pilot and its eventual repository, ownership,
licensing/dependency review and contribution process. Later uncommitted local
experiments are outside this review baseline.

## Architecture and responsibilities

| Component | Responsibility and authority | Review references |
| --- | --- | --- |
| Native artifacts and process catalog | Preserve the target project's need IDs, source revisions, statuses, relations and work-product ownership | [Native import](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0002-structured-native-import-and-baseline.md), [artifact ownership](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0006-native-artifact-ownership-and-traceability.md) |
| Deterministic projection and compiler | Derive execution plans from explicit mappings and applicability inputs; unknown mappings block the affected plan | [Execution projection](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0005-derived-execution-representation-and-deterministic-compiler.md) |
| Runtime adapter | The current implementation delegates scheduling, events, checkpoints and run state to Fabro | [Runtime boundary](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0001-workspace-and-authority-boundaries.md) |
| Evidence collectors and assessment | Bind measured results to source/tool/policy subjects and distinguish fixture, agent and actual tool evidence | [Evidence and decisions](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0007-trusted-evidence-and-authenticated-human-decisions.md) |
| Context and agent boundary | Select baseline-bound context and tools within explicit role/model/usage limits; optional APM/MCP support supplies context/tools | [Context procedures](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0014-bounded-context-and-procedures.md), [APM/MCP boundary](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0010-apm-and-mcp-integration-boundary.md) |
| Review and portable export | Export understandable artifacts and unresolved findings for authorized people to review offline | [Readiness and export](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/docs/architecture/0013-scoped-readiness-portable-evidence-and-upstream-boundary.md) |

An operator selects a pinned target export and applicable policy. Deterministic
tools derive the plan and authorized context. The runtime executes the admitted
steps and collectors retain complete outputs. Assessment binds those outputs to
their exact subjects, identifies missing or stale evidence, and exports a review
packet. Required human decisions remain explicit and stop unattended execution.

The authoritative engineering record must remain understandable without Fabro.
The proposed pilot uses no agent-generated approval as a release or safety verdict.

### Relationship to the current Hephaestus workflow

Hephaestus already documents a ubcode/Pharaoh workflow and its own
`ubproject.toml` types and trace relations. The pilot would consume a reviewed
export from that workflow, preserve its identifiers and link direction, and
demonstrate evidence freshness and portable review alongside it. An adapter
between that metamodel and the fabric's S-CORE-derived catalog has not been built
or validated. Runtime choice and any future interface changes need maintainer
agreement before integration.

## Evidence and current limits

The pinned repository includes specifications, contract schemas, tests, command
records and acceptance reports. Review the scope attached to each result:

| Evidence | What it supports | Limit |
| --- | --- | --- |
| [Native process catalog acceptance](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/specs/001-native-process-catalog/acceptance.md) | Source-bound parsing and preservation of native artifact identities | Selected S-CORE baselines; Hephaestus metamodel compatibility is unmeasured |
| [Artifact traceability acceptance](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/specs/004-native-artifact-traceability/acceptance.md) | Artifact indexing, expected-set coverage, diff/impact and recorded native validation | Applicable target mappings and engineering decisions remain separate |
| [Assurance acceptance](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/specs/005-trusted-evidence-and-human-gates/acceptance.md) | Evidence/decision binding and fail-closed assessment behavior | Fixture demonstrations do not establish production decision authority |
| [Quality tooling acceptance](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/specs/010-misra-quality-and-deviations/acceptance.md) | Adapter prerequisites, measured checks and preserved findings | Tool eligibility, qualification and engineering review are explicit open obligations |
| [Bounded-context acceptance](https://github.com/jnsagai/s-core_sw_fabric/blob/7e24a43c258f1dcaa2b27e02b501964847bc8714/specs/011-change-impact-and-freshness/acceptance.md) | Regression records and separately labelled context/usage experiments | Fixture/provider measurements do not establish real engineering savings or adequacy |

The evidence links identify retained records; this proposal does not claim to
have rerun all of those checks. Synthetic fixtures, historical measurements,
fresh tool execution and human review must remain distinct during the pilot.

The current implementation is Python-based with locked dependencies and
S-CORE-specific source locks/profiles. A production rollout would require reviewed
target policy, trusted collection/decision channels, supported environment and
runtime compatibility, and dependency/license review. Optional analyzer/provider
integrations also require their own eligibility and capability checks.

## Proposed first pilot and acceptance

1. Agree on one disposable, public Hephaestus documentation target and a reviewed
   Sphinx-Needs export. Record its metamodel, source revision and applicable
   engineering obligations.
2. Implement a narrow export adapter that preserves the native types, IDs,
   statuses and `traces_to`, `satisfies`, `implements` and `verifies` relations.
   Unsupported or ambiguous input must produce explicit diagnostics.
3. Demonstrate a requirement-to-verification slice with a successful collector
   result and negative cases for missing evidence, a changed artifact and stale
   review subjects. Maintain the original history.
4. Export a source/tool/policy-bound packet and independently verify its hashes
   and expected checks. Repeat from the same inputs to verify deterministic
   projection. Keep model calls unnecessary for this acceptance step.
5. Have maintainers review the pilot's applicability, retained failures, ownership
   and next increment before a broader migration.

The initial deliverable would be the adapter, reproducible example, negative
tests and portable review packet. Acceptance needs measured deterministic
behavior and an authorized human review of the stated scope. Missing prerequisites
remain blockers; a successful runtime alone is insufficient.

## Maintainer decisions requested

- Whether to evaluate this contribution within Hephaestus and where a pilot
  implementation should live.
- Which public target, metamodel version, runtime boundary and acceptance checks
  the first pilot should use.
- Which ownership, dependency/license review and tool-management records are
  required before importing implementation code.

The existing S-CORE adapters can remain a project-specific use case while
Hephaestus evaluates reusable contracts and explicitly reviewed adapters for
additional projects.

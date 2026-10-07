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
# S-CORE Docs Assistant contribution proposal

**Status: community contribution candidate for maintainer review.** This proposes
a local documentation-assistance pilot using the existing `s-core_bot`
implementation. Hephaestus adoption, corpus compatibility and engineering
acceptance remain pending.

## Contribution and fit

The assistant helps engineers navigate pinned documentation through search, exact
requirement lookup, cited local answers and explicit snapshot comparison. Its
proposed role in Hephaestus is developer enablement and read-only Doc-as-Code
navigation, with S-CORE as the existing project-specific use case.

Hephaestus's [project scope](https://projects.eclipse.org/proposals/eclipse-sdv-hephaestus)
includes Sphinx-Needs traceability, reusable tooling, developer enablement and
cross-cutting AI assistance. This candidate supports documentation discovery; it
does not yet implement the scope's dependency-tree reasoning use case.

| Hephaestus area | Candidate capability | Pilot work still required |
| --- | --- | --- |
| Developer enablement | Local CLI, web UI and HTTP API for documentation questions | Select a reviewed public corpus and onboarding questions |
| Doc-as-Code navigation | Need-ID lookup, stored relationships and revision-bound citations | Validate the current Hephaestus metamodel, exports and source profile |
| AI assistance | Optional local generation over retrieved evidence, explicit insufficient-evidence results | Evaluate claim support and refusal behavior on independently reviewed cases |
| Reusable tooling | Source/parser/provider interfaces, portable immutable snapshots | Agree on ownership, dependency review and the target repository |

## Review baseline and contribution boundary

The public [implementation at commit 72c1fb2](https://github.com/jnsagai/s-core_bot/tree/72c1fb2cab280e6835513b046013e5abea066c3a)
is the review baseline. Original application code is
[Apache-2.0](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/LICENSE), with [notices](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/NOTICE),
[third-party notices](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/THIRD_PARTY_NOTICES.md) and locked
[Python](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/uv.lock) and [frontend](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/frontend/package-lock.json)
dependencies. Model weights and documentation corpora retain separate licenses
and are not included in this proposal.

This PR contributes the proposal and a tooling-catalog entry. It requests an
agreed pilot before implementation import or ownership transfer. The community
implementation is independent of Eclipse; it has no implied endorsement,
qualification or safety-approval authority.

## Architecture and responsibilities

| Component | Responsibility | Design reference |
| --- | --- | --- |
| Source synchronization and safe parsers | Resolve allowlisted sources to commits; parse documentation and validated needs exports without executing repository code | [Safe ingestion](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/adr/ADR-005-safe-source-parsing-no-execution-of-upstream-doc-builds.md) |
| Immutable snapshot store | Bind source revisions, hashes, parser and model identities; activate or roll back a selected snapshot | [Snapshot boundaries](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/adr/ADR-006-immutable-multi-repository-snapshots-with-atomic-activation.md) |
| Retrieval and exact-ID lookup | Combine SQLite FTS5 with local NumPy vector search; return stored evidence and relationship records | [Retrieval design](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/adr/ADR-004-sqlite-fts5-plus-numpy-exact-vector-search.md) |
| Local answer generation and validation | Ask Ollama for structured claims over retrieved evidence; validate evidence IDs and build URLs from stored provenance | [Server-owned citations](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/adr/ADR-007-structured-claims-and-server-owned-citations.md) |
| CLI, API and web experience | Present answers, excerpts, searches and two-snapshot comparisons without exposing execution tools to the answer model | [Local privacy boundary](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/adr/ADR-008-stateless-baseline-chat-loopback-security-no-body-logs.md), [provider interfaces](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/adr/ADR-009-modular-monolith-with-provider-contracts.md) |

An operator explicitly prepares dependencies, models and pinned documentation.
The index builder creates an immutable snapshot. A request selects one snapshot,
retrieves evidence and optionally generates a local answer. Citations come from
the stored source identity and line spans. Explicit comparison retains both
snapshot identities instead of silently mixing revisions.

The serving path uses local inference and makes no external downloads. It binds
to loopback, validates Host/Origin, does not persist question/answer bodies by
default, and never executes commands from documentation or model output. Search
and exact-ID lookup are usable without generation. Structural citation validity
does not prove that a claim is supported; independent semantic review remains
necessary.

### Relationship to Hephaestus and other proposals

The current source profiles and evaluation cases target S-CORE. The application
has not been validated against Hephaestus's ubcode/Pharaoh documentation workflow
or its `ubproject.toml` types and trace relations. A pilot should consume an
explicitly prepared, reviewed export; the assistant must not execute upstream
`conf.py`, scripts or directives to ingest it.

The separate [workflow-fabric proposal](https://github.com/eclipse-hephaestus/hephaestus/pull/14)
addresses execution and review evidence. This assistant can be evaluated
independently and requires no fabric or agent orchestration runtime. Any later
context interface must be read-only and agreed separately. Generated answers
cannot replace native traceability checks, deterministic gates or human decisions.

## Existing evidence and limits

The pinned repository includes implementation tests, feature verification and
release records. These links identify historical evidence, not fresh execution
of this PR:

| Record | What it supports | Limit |
| --- | --- | --- |
| [Source ingestion](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/specs/002-source-ingestion/verification.md) | Pinned source handling, safe parsing and recorded S-CORE need-set checks | Hephaestus input compatibility is unmeasured |
| [Search and need lookup](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/specs/004-hybrid-search/verification.md) | Exact-ID, keyword/hybrid retrieval and snapshot-bound evidence checks | Existing question sets are S-CORE-specific; development cases were not independently reviewed |
| [Grounded answers](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/specs/005-grounded-chat/verification.md) | Structured claims, citation handling, refusals and retained injection findings | Citation checks and heuristic judges do not prove semantic correctness |
| [Version comparison](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/specs/007-version-comparison/verification.md) | Explicit snapshot isolation, comparison records and retained performance tradeoffs | Comparison completeness and speed require a target-specific evaluation |
| [Local release and limitations](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/releases/v1.0.0.md), [known limitations](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/docs/KNOWN_LIMITATIONS.md) | Local packaging and retained evaluation/review records | One Linux/NVIDIA laptop; blanket owner acceptance rather than per-claim review; public hosting deferred |
| [Refresh verification](https://github.com/jnsagai/s-core_bot/blob/72c1fb2cab280e6835513b046013e5abea066c3a/specs/015-scheduled-refresh/verification.md) | Explicit upstream refresh, held activation and opt-in timer behavior | Polling is not real-time; retention can remove comparison snapshots |

A separately retained local verification packet from 2026-10-07 is bound to this
same implementation commit. Its initial deterministic backend run recorded
1230 passed, 4 environment failures and 10 opt-in skips. After correcting the
copied workspace's missing `.venv` path, the affected timer module recorded
9 passed. All 1234 non-skipped backend cases therefore have a passing observation
across those two runs; there was no clean full-suite rerun. Frontend tests recorded
76 passed; lint, types, build, traceability and license-allowlist checks passed.
Those logs are retained locally for review and are not part of this upstream PR.
No new real-model, GPU, browser, container or offline-egress run is claimed here.

The release's original support/coverage metrics used blanket owner acceptance,
not independent per-claim measurements. Its prose gate count also differs from
the retained JSON report. Neither is evidence of Hephaestus acceptance. Further
limits and licensing assumptions remain visible in the linked records.

## Proposed first pilot and acceptance

1. Select one public Hephaestus documentation revision, a reviewed needs export
   and its applicable licenses. Define the intended navigation tasks and owners.
2. Add a narrow source/parser profile or export adapter. Preserve native IDs,
   types, relationships, line spans and revision provenance; report unsupported
   constructs and unverified export provenance explicitly.
3. Demonstrate lexical search and exact-ID lookup first, then optional local
   answers. Confirm citations resolve to the selected revision and that missing
   evidence, conflicting versions and injected instructions are handled safely.
4. Run reproducible ingestion, provenance and snapshot-isolation tests. Evaluate
   independently reviewed questions and unsupported questions; review generated
   claims against their cited excerpts, rather than treating valid URLs as proof.
5. Publish a measured pilot report with tool/model/source identities, failures,
   unrun checks and maintainer decisions before considering broader adoption.

The initial deliverable would be a reviewed corpus profile/adapter, a local
example, regression cases and a scoped evaluation report. Public hosting,
automatic engineering approval, corpus/model redistribution and integration with
workflow execution are outside this pilot.

## Maintainer decisions requested

- Whether a local documentation assistant is a useful Hephaestus contribution,
  and which repository and maintainers should own the pilot.
- Which corpus/export format, native relationship semantics and reviewed
  acceptance cases the pilot should use.
- Which dependency, model-license, corpus-license and tool-management reviews
  are required before importing implementation code.

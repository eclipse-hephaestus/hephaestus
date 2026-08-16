# Requirements

## Introduction
Requirements, specifications, and their traceability to implementation and
tests, tracked with
[sphinx-needs](https://sphinx-needs.readthedocs.io/).

## Deployment Requirements

```{req} Support GitHub Pages deployment
:id: REQ_001
:status: open
:tags: deployment

Hephaestus documentation must be publishable via GitHub Pages with a single
combined build artifact covering the marketing site, the general
documentation, and the requirements/traceability docs.
```

```{spec} Merge Sphinx output under /docs/
:id: SPEC_001
:status: open
:links: REQ_001
:tags: deployment

The single `docs/` Sphinx build (general docs + this nested `requirements/`
section) is copied into `public/docs/` before the Pages artifact is
uploaded, so the Hugo and Sphinx builds are served from one deployment.
Requirements live at the nested `/docs/requirements/`.
```

```{impl} CI workflow build order
:id: IMPL_001
:status: open
:links: SPEC_001
:tags: deployment

Implemented in `.github/workflows/pages.yml`: Hugo build → generate
`hugo-objects.inv` → install Graphviz (needed by `needflow` diagrams) →
Sphinx build (consumes the inventory via intersphinx) → merge → upload.
```

```{test} Pages artifact contains all three sites
:id: TEST_001
:status: open
:links: IMPL_001
:tags: deployment

Verify `public/index.html`, `public/docs/docs/index.html`, and
`public/docs/requirements/index.html` all exist in the uploaded Pages
artifact after a workflow run.
```

## Traceability table

```{needtable}
:columns: id, title, status, tags
:style: table
```

## Traceability diagram

```{needflow}
```

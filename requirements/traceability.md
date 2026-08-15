# Requirements and traceability

## Requirements

```{req} Support GitHub Pages deployment
:id: REQ_001
:status: open
:tags: deployment

Hephaestus documentation must be publishable via GitHub Pages with a single
combined build artifact covering both the marketing site and the
requirements/traceability docs.
```

```{spec} Merge Sphinx output under /requirements/
:id: SPEC_001
:status: open
:links: REQ_001
:tags: deployment

The Sphinx-needs HTML build is copied into `public/requirements/` before the
Pages artifact is uploaded, so both sites are served from one deployment.
See the {doc}`hugo:getting-started` guide on the main site for
local build instructions.
```

```{impl} CI workflow build order
:id: IMPL_001
:status: open
:links: SPEC_001
:tags: deployment

Implemented in `.github/workflows/pages.yml`: Hugo build → generate
`hugo-objects.inv` → Sphinx build (consumes it via intersphinx) → merge →
upload.
```

```{test} Pages artifact contains both sites
:id: TEST_001
:status: open
:links: IMPL_001
:tags: deployment

Verify `public/index.html` and `public/requirements/index.html` both exist
in the uploaded Pages artifact after a workflow run.
```

## Traceability table

```{needtable}
:columns: id, title, status, tags
:style: table
```

## Traceability diagram

```{needflow}
```

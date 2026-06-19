---
title: "redirect_url"
description: "Sets a client-side redirect target. Used in the canonical URL and an instant-refresh `<meta>` tag. Pages with this parameter set are also marked `noindex` to prevent search engine indexing."
type: "doc_param"
category: "navigation"
param_type: "url"
accepted_values:
  - Absolute path (e.g. `/new-location/`)
  - Relative path (e.g. `../sibling/`)
  - Fully qualified URL (e.g. `https://example.org/new-page/`)
hide_sidebar: true
---

## Example

```yaml
redirect_url: "/docs/new-location/"
```

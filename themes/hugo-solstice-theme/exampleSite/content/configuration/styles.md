---
title: "styles"
description: "Stylesheets loaded site-wide. Page-level styles are appended after these. Defaults to the Neptune stylesheet when not set."
type: "doc_param"
category: "resources"
param_type: "{url: string, cache?: boolean}[]"
accepted_values:
  - "`url` (string, required) — path or URL to the stylesheet"
  - "`cache` (boolean, optional) — appends `?v=<timestamp>` to bust the browser cache"
hide_sidebar: true
---

The legacy string form (a single URL) and the separate `style_overrides` param are deprecated.
Use additional entries in this array instead.

## Example

```toml
[[Params.styles]]
  url = "/css/main.css"
  cache = true

[[Params.styles]]
  url = "/css/overrides.css"
```

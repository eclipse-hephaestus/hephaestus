---
title: "scripts"
description: "JavaScript files loaded site-wide. When set, this replaces the deprecated `js` and `hugo_js` parameters."
type: "doc_param"
category: "resources"
param_type: "{url: string, type?: string, defer?: boolean, cache?: boolean, integrity?: string}[]"
accepted_values:
  - "`url` (string, required) — path or URL to the script file"
  - "`type` (string, optional) — value for the `type` attribute, e.g. `module`"
  - "`defer` (boolean, optional) — adds the `defer` attribute"
  - "`cache` (boolean, optional) — appends `?v=<timestamp>` to bust the browser cache"
  - "`integrity` (string, optional) — value for the `integrity` attribute (SRI)"
hide_sidebar: true
---

## Example

```toml
[[Params.scripts]]
  url = "/js/main.mjs"
  type = "module"
  cache = true

[[Params.scripts]]
  url = "https://cdn.example.org/widget.js"
  defer = true
  integrity = "sha384-..."
```

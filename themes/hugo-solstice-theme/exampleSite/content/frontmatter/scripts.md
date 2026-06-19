---
title: "scripts"
description: "Page-level JavaScript files to load after the site-level scripts. Each entry is an object that describes the script tag to render."
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

```yaml
scripts:
  - url: "/js/page-specific.mjs"
    type: "module"
    cache: true
  - url: "https://cdn.example.org/widget.js"
    defer: true
    integrity: "sha384-abc123..."
```

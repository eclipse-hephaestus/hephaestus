---
title: "styles"
description: "Page-level stylesheets to load after the site-level styles. Each entry is an object that describes the `<link>` tag to render."
type: "doc_param"
category: "resources"
param_type: "{url: string, cache?: boolean}[]"
accepted_values:
  - "`url` (string, required) — path or URL to the stylesheet"
  - "`cache` (boolean, optional) — appends `?v=<timestamp>` to bust the browser cache"
hide_sidebar: true
---

Replaces the deprecated `page_css_file` parameter.

## Example

```yaml
styles:
  - url: "/css/page-specific.css"
    cache: true
  - url: "https://cdn.example.org/widget.css"
```

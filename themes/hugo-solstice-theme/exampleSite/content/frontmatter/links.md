---
title: "links"
description: "Buttons rendered below the tagline in the jumbotron. Each entry defines the button label and its target URL."
type: "doc_param"
category: "jumbotron"
param_type: "{href: string, text: string, class?: string, id?: string}[]"
accepted_values:
  - "Array of objects, each with `href` (string, required) and `text` (string, required)"
  - "Optional per-item properties: `class` (string, CSS classes for the `<a>` element), `id` (string)"
hide_sidebar: true
---

## Example

```yaml
links:
  - href: "/about/"
    text: "About"
  - href: "/downloads/"
    text: "Download"
    class: "btn btn-primary"
    id: "download-btn"
```

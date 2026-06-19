---
title: "page_css_file"
description: "URL to an additional stylesheet to load on this page."
type: "doc_param"
category: "resources"
param_type: "url"
accepted_values:
  - Absolute path (e.g. `/css/page.css`)
  - Fully qualified URL (e.g. `https://cdn.example.org/css/page.css`)
deprecated: true
deprecated_message: "Use the page-level [`styles`](/frontmatter/styles/) array instead."
hide_sidebar: true
---

Use the [`styles`](/frontmatter/styles/) parameter instead, which supports cache-busting and loading multiple stylesheets.

## Example (deprecated usage)

```yaml
page_css_file: "/css/my-page.css"
```

## Replacement

```yaml
styles:
  - url: "/css/my-page.css"
    cache: true
```

---
title: "js"
description: "URL to the main JavaScript file used site-wide. Defaults to the bundled `main.min.js`."
type: "doc_param"
category: "resources"
param_type: "url"
accepted_values:
  - Absolute path or fully qualified URL to a JS file
deprecated: true
deprecated_message: "Use the [`scripts`](/configuration/scripts/) array instead."
hide_sidebar: true
---

## Example (deprecated usage)

```toml
[Params]
  js = "/js/main.js"
```

## Replacement

```toml
[[Params.scripts]]
  url = "/js/main.js"
  cache = true
```

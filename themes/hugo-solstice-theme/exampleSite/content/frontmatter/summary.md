---
title: "summary"
description: "Built-in Hugo parameter. Used as the `<meta name=\"description\">` value when `Description` is not set."
type: "doc_param"
category: "metadata"
param_type: "string"
accepted_values:
  - Any string value
hide_sidebar: true
---

Hugo can also auto-generate the summary from the first paragraph of the page content if `Summary` is not explicitly set in the front matter. Use `Description` to take full control of the meta description.

## Example

```yaml
Summary: "A brief overview of the page content used in previews and meta tags."
```

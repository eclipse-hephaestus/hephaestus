---
title: "Custom breadcrumb label"
description: "Override the breadcrumb label for a page with `breadcrumb_title`."
category: "navigation"
weight: 60
icon: "fa-solid fa-tag"
headline: "Custom breadcrumb label"
tagline: "Show a shorter or friendlier name in the breadcrumb than the page title."
breadcrumb_title: "Friendly name"
hide_sidebar: true
---

By default the breadcrumb uses each page's title. Set `breadcrumb_title` to
display a different label for the current page only — typically a shorter or
friendlier version. Values longer than 32 characters are truncated.

Look at the breadcrumb above: this page's title is "Custom breadcrumb
label" but the breadcrumb shows **Friendly name**.

```yaml
breadcrumb_title: "Friendly name"
```

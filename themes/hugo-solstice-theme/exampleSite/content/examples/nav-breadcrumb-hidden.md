---
title: "Page without a breadcrumb"
description: "Suppress the breadcrumb navigation on a single page with `hide_breadcrumb`."
category: "navigation"
weight: 50
icon: "fa-solid fa-eye-slash"
headline: "No breadcrumb here"
tagline: "Drop the breadcrumb on landing pages or anywhere it adds noise."
hide_breadcrumb: true
hide_sidebar: true
---

Setting `hide_breadcrumb: true` removes the `<nav aria-label="Breadcrumb">`
block from the page. The page above has no breadcrumb between the jumbotron
and the main content.

The same parameter is available at the site level (in `config.toml`) if you
want to suppress breadcrumbs globally.

```yaml
hide_breadcrumb: true
```

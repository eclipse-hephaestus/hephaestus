---
title: "Custom sidebar"
description: "Render a page-specific sidebar by referencing a `sidebar` menu identifier."
category: "navigation"
weight: 40
icon: "fa-solid fa-bars"
headline: "Custom sidebar"
tagline: "Pick which sidebar to render on a page with the `sidebar` parameter."
sidebar:
  - "demo-sidebar"
hide_sidebar: false
---

The sidebar partial reads from the `sidebar` menu in the site configuration.
By default, it picks the section that matches the current page's path. You
can override this for a single page by setting `sidebar` in the front matter
to one or more identifiers from `menus.toml`.

Top-level entries become collapsible group headings. Their children are
rendered as plain links, unless those children also have children, in which
case the second level becomes a nested collapsible subgroup.

```yaml
sidebar:
  - "demo-sidebar"
```

```toml
[[sidebar]]
    identifier = "demo-sidebar"
    name       = "Getting started"
    url        = "#"
    weight     = 1

[[sidebar]]
    parent = "demo-sidebar"
    name   = "Introduction"
    url    = "#introduction"
    weight = 1

[[sidebar]]
    parent = "demo-sidebar"
    name   = "Installation"
    url    = "#installation"
    weight = 2

[[sidebar]]
    parent = "demo-sidebar"
    identifier = "demo-sidebar-advanced"
    name   = "Advanced topics"
    url    = "#advanced"
    weight = 3

[[sidebar]]
    parent = "demo-sidebar-advanced"
    name   = "Custom shortcodes"
    url    = "#shortcodes"
    weight = 1

[[sidebar]]
    parent = "demo-sidebar-advanced"
    name   = "Theming"
    url    = "#theming"
    weight = 2
```

---
title: "Custom menu with dropdowns"
description: "A custom main menu where a top-level entry has children, rendered as a dropdown."
category: "navigation"
weight: 20
icon: "fa-solid fa-chevron-down"
headline: "Dropdown menu"
tagline: "Group related links under a single top-level entry with one level of children."
main_menu: "demo_dropdown"
hide_sidebar: true
---

When a top-level menu entry has children but none of those children have
children themselves, the theme renders it as a dropdown toggle button in the
navigation bar.

The navigation above is driven by the `demo_dropdown` menu defined in
`menus.en.toml` and activated on this page with:

```yaml
main_menu: "demo_dropdown"
```

```toml
[[demo_dropdown]]
    name = "Home"
    url = "/"
    weight = 1

[[demo_dropdown]]
    identifier = "demo-dropdown-docs"
    name = "Docs"
    url = "#"
    weight = 2

[[demo_dropdown]]
    parent = "demo-dropdown-docs"
    name = "Components"
    url = "/components/"
    weight = 1

[[demo_dropdown]]
    parent = "demo-dropdown-docs"
    name = "Front Matter"
    url = "/frontmatter/"
    weight = 2

[[demo_dropdown]]
    parent = "demo-dropdown-docs"
    name = "Configuration"
    url = "/configuration/"
    weight = 3
```

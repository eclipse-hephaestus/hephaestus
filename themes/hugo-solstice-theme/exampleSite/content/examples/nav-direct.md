---
title: "Custom menu with direct links"
description: "A custom main menu where every top-level entry is a direct link."
category: "navigation"
weight: 10
icon: "fa-solid fa-link"
headline: "Direct link menu"
tagline: "The simplest custom menu: every top-level entry points straight to a URL."
main_menu: "demo_direct"
hide_sidebar: true
---

When a top-level menu entry has no children, it renders as a plain `<a>` link
in the navigation bar. This is the right pattern for short menus where each
destination is a single page.

The navigation above is driven by the `demo_direct` menu defined in
`menus.en.toml` and activated on this page with:

```yaml
main_menu: "demo_direct"
```

```toml
[[demo_direct]]
    name = "Home"
    url = "/"
    weight = 1

[[demo_direct]]
    name = "Examples"
    url = "/examples/"
    weight = 2

[[demo_direct]]
    name = "Changelog"
    url = "/changelog/"
    weight = 3
```

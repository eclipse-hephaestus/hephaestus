---
title: "Custom menu with a mega menu"
description: "A custom main menu where a top-level entry has grandchildren, rendered as a mega menu panel."
category: "navigation"
weight: 30
icon: "fa-solid fa-grip"
headline: "Mega menu"
tagline: "Organize many links into grouped columns under a single top-level entry."
main_menu: "demo_mega"
hide_sidebar: true
---

When a top-level menu entry has children that themselves have children, the
theme automatically promotes it to a mega menu: clicking the entry opens a
full-width panel where each second-level child becomes a column heading and
its third-level children become the links underneath.

Each column heading accepts an optional Font Awesome icon via the `pre`
property, which is rendered before the heading text.

The navigation above is driven by the `demo_mega` menu defined in
`menus.en.toml` and activated on this page with:

```yaml
main_menu: "demo_mega"
```

```toml
[[demo_mega]]
    name = "Home"
    url = "/"
    weight = 1

[[demo_mega]]
    identifier = "demo-mega-products"
    name = "Products"
    url = "#"
    weight = 2

[[demo_mega]]
    parent = "demo-mega-products"
    identifier = "demo-mega-tools"
    name = "Tools"
    weight = 1
    pre = "<i class=\"fa-solid fa-wrench\" aria-hidden></i>"

[[demo_mega]]
    parent = "demo-mega-tools"
    name = "Eclipse IDE"
    url = "https://eclipseide.org/"
    weight = 1

[[demo_mega]]
    parent = "demo-mega-tools"
    name = "Theia"
    url = "https://theia-ide.org/"
    weight = 2

[[demo_mega]]
    parent = "demo-mega-products"
    identifier = "demo-mega-platforms"
    name = "Platforms"
    weight = 2
    pre = "<i class=\"fa-solid fa-layer-group\" aria-hidden></i>"

[[demo_mega]]
    parent = "demo-mega-platforms"
    name = "Cloud Tools"
    url = "/components/"
    weight = 1

[[demo_mega]]
    parent = "demo-mega-platforms"
    name = "Embedded"
    url = "/components/"
    weight = 2
```

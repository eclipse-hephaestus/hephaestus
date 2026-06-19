---
title: "Jumbotron with call-to-action links"
description: "Render one or more buttons below the tagline using the `links` parameter."
category: "jumbotron"
weight: 30
icon: "fa-solid fa-arrow-pointer"
headline: "Get involved"
tagline: "Download, contribute, or learn more about the project."
links: [
  [href: "/downloads/", text: "Download", class: "btn btn-primary"],
  [href: "/changelog/", text: "Release notes", class: "btn btn-default"],
]
hide_sidebar: true
---

Each entry in `links` becomes a button in the jumbotron. Use `class` to switch
between primary, default, or any other button style supplied by the theme.

```yaml
links: [
  [href: "/downloads/", text: "Download", class: "btn btn-primary"],
  [href: "/changelog/", text: "Release notes", class: "btn btn-default"],
]
```

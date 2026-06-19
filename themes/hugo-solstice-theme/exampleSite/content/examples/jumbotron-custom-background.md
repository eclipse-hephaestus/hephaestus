---
title: "Jumbotron with custom background"
description: "Swap the default hero background by setting `jumbotron_background_class`."
category: "jumbotron"
weight: 60
icon: "fa-solid fa-palette"
headline: "Custom background"
tagline: "Override the hero styling for a single page."
jumbotron_background_class: "bg bg-example"
hide_sidebar: true
---

`jumbotron_background_class` controls the CSS class applied to the
`<section>` wrapping the jumbotron. The theme ships with multiple `bg-hero-*`
variants; you can also point to a project-specific class for a fully custom
look. This page combines the theme's `bg` scaffold with a project-specific
`bg-example` class defined in `docs.css` to render a black-to-orange gradient.

```yaml
jumbotron_background_class: "bg bg-example"
```

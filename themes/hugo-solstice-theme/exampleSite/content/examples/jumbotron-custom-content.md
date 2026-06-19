---
title: "Jumbotron with custom content"
description: "Inject arbitrary HTML below the headline using `custom_jumbotron`."
category: "jumbotron"
weight: 40
icon: "fa-solid fa-code"
headline: "Solstice Summit 2026"
custom_jumbotron: |
  <p class="margin-top-20"><strong>May 19, 2026</strong> &mdash; 8AM&ndash;11AM PST</p>
  <p>Virtual event &middot; Free registration</p>
hide_sidebar: true
---

`custom_jumbotron` accepts raw HTML, which is rendered inside the jumbotron
between the headline and the optional links row. It is best used as an
alternative to `tagline` when richer formatting is required.

```yaml
headline: "Solstice Summit 2026"
custom_jumbotron: |
  <p class="margin-top-20"><strong>May 19, 2026</strong> &mdash; 8AM–11AM PST</p>
  <p>Virtual event · Free registration</p>
```

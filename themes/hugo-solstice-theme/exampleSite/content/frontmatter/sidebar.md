---
title: "sidebar"
description: "One or more menu identifiers used to populate the sidebar on this page, overriding the default sidebar for the section. Each identifier must correspond to a `menu.sidebar` entry in the site configuration."
type: "doc_param"
category: "navigation"
param_type: "string[]"
accepted_values:
  - Array of strings, each matching a `menu.sidebar` identifier in `config.toml` or `menus.toml`
hide_sidebar: true
---

When `sidebar` is omitted, the default sidebar for the section is used.

## Example

Define the menu in `menus.toml`:

```toml
[[sidebar]]
  identifier = "my-custom-sidebar"
  name       = "My Project"
  url        = "#"
  weight     = 1

[[sidebar]]
  parent = "my-custom-sidebar"
  name   = "Overview"
  url    = "/my-project/"
  weight = 1
```

Then reference it in the page front matter:

```yaml
sidebar:
  - "my-custom-sidebar"
```

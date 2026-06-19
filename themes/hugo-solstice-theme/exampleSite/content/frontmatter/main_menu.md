---
title: "main_menu"
description: "Replaces the default main navigation menu with a menu defined under the given identifier in `config.toml` or `menus.toml`."
type: "doc_param"
category: "navigation"
param_type: "string"
accepted_values:
  - Any string value matching a menu identifier in the site configuration
hide_sidebar: true
---

If `main_menu` is not set, the default `main` menu is used.

Use the [front matter cascade](https://gohugo.io/content-management/front-matter/#front-matter-cascade) to apply the custom menu to all pages in a section.

## Example

Define a custom menu in `menus.toml`:

```toml
[[my_event_menu]]
  name = "Home"
  url  = "/my-event-2025/"
  weight = 1

[[my_event_menu]]
  name = "Schedule"
  url  = "/my-event-2025/schedule/"
  weight = 2
```

Then reference it from the section `_index.md`:

```yaml
---
title: "My Event 2025"
cascade:
  main_menu: "my_event_menu"
---
```

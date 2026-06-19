---
title: "socials"
description: "Social media links rendered in the site footer. Each entry defines the platform name, icon, and URL."
type: "doc_param"
category: "components"
param_type: "{name: string, icon: string, url: string}[]"
accepted_values:
  - "`name` (string) — platform display name"
  - "`icon` (string) — Font Awesome 6 icon classes"
  - "`url` (string) — full URL to the social profile"
hide_sidebar: true
---

## Example

```toml
[[Params.socials]]
  name = "Bluesky"
  icon = "fa-brands fa-bluesky"
  url = "https://bsky.app/profile/eclipsefdn.bsky.social"

[[Params.socials]]
  name = "GitHub"
  icon = "fa-brands fa-github"
  url = "https://github.com/eclipse"
```

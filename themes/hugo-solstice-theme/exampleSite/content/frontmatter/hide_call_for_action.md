---
title: "hide_call_for_action"
description: "Hides the call-to-action (CTA) button in the navbar on this page."
type: "doc_param"
category: "layout"
param_type: "boolean"
accepted_values:
  - "`true`"
hide_sidebar: true
---

When not set (or set to any value other than `true`), the parameter is ignored and the CTA button is shown normally (unless hidden at the site level via `hide_call_for_action` in `config.toml`).

## Example

```yaml
hide_call_for_action: true
```

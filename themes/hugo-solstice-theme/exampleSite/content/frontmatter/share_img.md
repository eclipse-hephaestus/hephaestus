---
title: "share_img"
description: "Image URL used as the thumbnail when the page is shared on social media (Open Graph / Twitter Card)."
type: "doc_param"
category: "metadata"
param_type: "url"
accepted_values:
  - Absolute path (e.g. `/images/share.jpg`)
  - Fully qualified URL (e.g. `https://example.org/images/share.jpg`)
hide_sidebar: true
---

When `share_img` is not set, the theme falls back to `image`, then to the site-level `share_img`, and finally to the site `logo`.

## Example

```yaml
share_img: "/images/my-announcement-share.jpg"
```

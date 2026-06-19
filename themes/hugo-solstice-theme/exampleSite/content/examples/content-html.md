---
title: "Raw HTML in Markdown"
description: "Use the `html` shortcode to embed raw HTML blocks inside a Markdown page."
category: "content"
weight: 10
icon: "fa-solid fa-code"
headline: "Raw HTML in Markdown"
tagline: "Drop in arbitrary markup when Markdown isn't enough."
hide_sidebar: true
---

Hugo's Goldmark renderer escapes or strips some raw HTML by default. The
`html` shortcode passes its inner content through `safeHTML`, letting you
embed any HTML you need without changing site-wide Markdown settings.

## Example

{{< html >}}
<div class="alert alert-info">
  <strong>Note:</strong> This alert block is raw HTML, rendered inside a
  Markdown page through the <code>html</code> shortcode.
</div>
{{< /html >}}

## Source

```go-html-template
{{</* html */>}}
<div class="alert alert-info">
  <strong>Note:</strong> This alert block is raw HTML, rendered inside a
  Markdown page through the <code>html</code> shortcode.
</div>
{{</* /html */>}}
```

## When to use it

Reach for `html` when the markup you want isn't expressible in Markdown: a
wrapper with custom classes, a semantic element like `<aside>`, or a
specific Bootstrap component. For repeated patterns, prefer a dedicated
shortcode or partial.

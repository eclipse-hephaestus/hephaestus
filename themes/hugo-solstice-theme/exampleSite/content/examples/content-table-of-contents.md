---
title: "Table of contents"
description: "Render an auto-generated table of contents with the `table_of_contents` shortcode."
category: "content"
weight: 20
icon: "fa-solid fa-list"
headline: "Table of contents"
tagline: "Generate an in-page navigation index from the page's headings."
hide_sidebar: true
---

The `table_of_contents` shortcode renders a heading followed by Hugo's
automatically generated TOC for the current page. Hugo collects every
heading from the page body and produces a nested list of anchor links. Use
it on long-form documents — guides, specifications, runbooks — where readers
need a quick way to jump between sections.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed imperdiet
tortor id rhoncus pulvinar. Suspendisse nec aliquam ante. Sed vel convallis
ex, ac elementum nisi. Nam eros lectus, tempus sit amet lorem at, laoreet
blandit enim. Vestibulum metus justo, venenatis mollis ex quis, pretium
ultricies orci.

{{< table_of_contents >}}

## Source

```go-html-template
{{</* table_of_contents */>}}
```

Drop the shortcode anywhere in the body where you want the index to render.
Most sites place it near the top of the page, immediately after the
introduction, so readers can scan the structure before reading.

## Introduction

Pellentesque accumsan nulla ac leo convallis ornare. Cras rhoncus sapien
lacus, vel tincidunt nibh lacinia ac. Vivamus vel egestas mi. Morbi nulla
ante, rutrum quis congue non, luctus vehicula dui. Sed et nisi eu est
egestas rhoncus.

Sed nec diam at mi accumsan faucibus. Nunc vitae porttitor purus, vitae
pharetra mauris. Aliquam fringilla fermentum velit, in lacinia sem
convallis non. Mauris volutpat eget dui non euismod. Mauris finibus leo
convallis consequat sagittis. Aenean eu mauris erat. Donec quis varius
lectus.

Etiam nec laoreet sapien. Nulla sit amet sollicitudin nunc. Aliquam turpis
magna, maximus quis ante a, porta laoreet mauris. Praesent viverra ornare
velit quis viverra. Interdum et malesuada fames ac ante ipsum primis in
faucibus.

## Background

Nullam consequat nibh massa, quis fringilla leo faucibus eu. Praesent ut
urna eleifend, pretium urna eget, accumsan turpis. Aliquam malesuada
vehicula nunc, sed ultrices nunc tristique molestie. Nunc lectus lectus,
mattis id finibus eu, mollis ut ligula. Etiam nunc leo, semper quis
lobortis sit amet, dapibus congue nunc.

### Historical context

Donec bibendum massa sapien, ut sollicitudin neque sollicitudin id. Cras
mattis sollicitudin enim sit amet lacinia. Curabitur accumsan ultrices elit
ac rutrum. Donec convallis at arcu non mollis. Curabitur imperdiet commodo
mi, sed aliquet diam egestas pellentesque.

Suspendisse malesuada, libero ut vestibulum congue, nulla diam aliquet
urna, quis posuere eros ligula et metus. Pellentesque et mollis neque.

### Prior work

Fusce ultricies vulputate suscipit. In ultricies, nibh nec ultrices
ultricies, felis lacus fermentum quam, a lobortis nibh felis et urna.
Integer vel erat lobortis, tempor elit cursus, aliquet nulla.

Sed tincidunt placerat dui ut suscipit. Praesent viverra ornare velit quis
viverra. Aenean eu mauris erat.

## Methodology

Nunc a metus faucibus, sollicitudin magna vitae, volutpat libero.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
cubilia Curae; Fusce sit amet tellus pretium, ornare lectus rhoncus,
faucibus sem.

### Data collection

Vestibulum gravida sollicitudin ultrices. Pellentesque convallis metus
lacus, quis blandit lectus euismod ut. Aliquam pellentesque porta velit ut
tempor. Curabitur eget tempor odio. Donec bibendum massa sapien, ut
sollicitudin neque sollicitudin id.

### Analysis approach

Cras mattis sollicitudin enim sit amet lacinia. Curabitur accumsan ultrices
elit ac rutrum. Donec convallis at arcu non mollis. Curabitur imperdiet
commodo mi, sed aliquet diam egestas pellentesque.

Suspendisse malesuada, libero ut vestibulum congue, nulla diam aliquet
urna, quis posuere eros ligula et metus.

## Results

Pellentesque et mollis neque. Etiam nec laoreet sapien. Nulla sit amet
sollicitudin nunc. Aliquam turpis magna, maximus quis ante a, porta laoreet
mauris.

### Primary findings

Praesent viverra ornare velit quis viverra. Interdum et malesuada fames ac
ante ipsum primis in faucibus. Sed tincidunt placerat dui ut suscipit.
Integer vel erat lobortis, tempor elit cursus, aliquet nulla.

### Secondary observations

Fusce ultricies vulputate suscipit. Nullam consequat nibh massa, quis
fringilla leo faucibus eu. Praesent ut urna eleifend, pretium urna eget,
accumsan turpis.

Aliquam malesuada vehicula nunc, sed ultrices nunc tristique molestie. Nunc
lectus lectus, mattis id finibus eu, mollis ut ligula.

## Discussion

Etiam nunc leo, semper quis lobortis sit amet, dapibus congue nunc. Nunc a
metus faucibus, sollicitudin magna vitae, volutpat libero. Vestibulum ante
ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.

Fusce sit amet tellus pretium, ornare lectus rhoncus, faucibus sem.
Vestibulum gravida sollicitudin ultrices. Pellentesque convallis metus
lacus, quis blandit lectus euismod ut.

## Limitations

The shortcode takes no parameters. To customize depth or skip specific
sections, override the `markup.tableOfContents` settings in `config.toml` or
build a custom partial.

Aliquam pellentesque porta velit ut tempor. Curabitur eget tempor odio.
Donec bibendum massa sapien, ut sollicitudin neque sollicitudin id.

## Conclusion

Cras mattis sollicitudin enim sit amet lacinia. Curabitur accumsan ultrices
elit ac rutrum. Donec convallis at arcu non mollis. Curabitur imperdiet
commodo mi, sed aliquet diam egestas pellentesque. Suspendisse malesuada,
libero ut vestibulum congue, nulla diam aliquet urna, quis posuere eros
ligula et metus.

Pellentesque et mollis neque. Etiam nec laoreet sapien. Nulla sit amet
sollicitudin nunc.

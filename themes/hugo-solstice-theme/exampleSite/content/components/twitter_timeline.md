---
title: "Twitter Timeline"
date: 2019-04-17T15:52:27-04:00
description: ""
categories: []
keywords: []
slug: ""
aliases: []
toc: false
draft: false
is_deprecated: true
deprecation_msg: "The twitter_timeline shortcode is deprecated and will be removed in Hugo Solstice Theme 4.0.0."
---

A shortcode wrapper for the [Twitter timeline embeds](https://developer.twitter.com/en/docs/twitter-for-websites).

{{< twitter_timeline tweet_limit="2" >}}

### Dark Mode Enabled
Dark mode can be enabled by setting the `dark` parameter to `"true"`.

{{< twitter_timeline dark="true" tweet_limit="2" >}}

### Tweet Limits
The maximum number of tweets displayed can be controlled using the `tweet_limit` parameter.

In the following example, we set the `tweet_limit` to `"1"`.

{{< twitter_timeline tweet_limit="1" >}}

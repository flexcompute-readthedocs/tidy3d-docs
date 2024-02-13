---
title: How do I create a material from n, k values at a given frequency?
date: 2023-12-05 18:51:47
enabled: true
category: "Mediums"
---
To create a material from the real ($n$) and imaginary ($k$) parts of refractive index, use the [tidy3d.Medium.from\_nk()](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Medium.html#tidy3d.Medium.from_nk){: target="_blank" rel="noopener"}. For example:

<div markdown class="code-snippet">{% highlight python %}

nk_medium = tidy3d.Medium.from_nk(n=2.0, k=1.0, freq=freq0)

{% endhighlight %}
{% include copy-button.html %}</div>

> Negative&nbsp;$k$&nbsp;value corresponds to a gain medium. It is only allowed when the parameter `allow_gain` is set to&nbsp;`True`.

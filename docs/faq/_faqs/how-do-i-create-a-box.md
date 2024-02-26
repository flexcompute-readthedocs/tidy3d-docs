---
title: How do I create a box?
date: 2023-12-06 21:33:15
enabled: true
category: "Structures"
---
You can create a box geometry using the&nbsp;[tidy3d.Box](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Box.html#tidy3d-box){: target="_blank" rel="noopener"}&nbsp;object. You can specify the `center` and `size` parameters, as below:

<div markdown class="code-snippet">{% highlight python %}

box = tidy3d.Box(center=(1,2,3), size=(2,2,2))

{% endhighlight %}
{% include copy-button.html %}</div>

Or you can use the [tidy3d.Box.from\_bounds()](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Box.html#tidy3d.Box.from_bounds){: target="_blank" rel="noopener"} method, where you should define the `rmin` and `rmax` coordinates of the lower and upper box corners. For example:

<div markdown class="code-snippet">{% highlight python %}

box = tidy3d.Box.from_bounds(
  rmin=(-10, -1, -0.1),
  rmax=(10, 1, 0.1),
)

{% endhighlight %}
{% include copy-button.html %}</div>

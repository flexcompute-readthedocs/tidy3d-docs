---
title: How do I create a sphere?
date: 2023-12-06 21:43:10
enabled: true
category: "Structures"
---
You can create a sphere using the&nbsp;[tidy3d.Sphere](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Sphere.html){: target="_blank" rel="noopener"}&nbsp;object and specifying the `center` and `radius` parameters, as below:

<div markdown class="code-snippet">{% highlight python %}

box = tidy3d.Box.from_bounds(
  rmin=(-10, -1, -0.1),
  rmax=(10, 1, 0.1),
)

{% endhighlight %}
{% include copy-button.html %}</div>

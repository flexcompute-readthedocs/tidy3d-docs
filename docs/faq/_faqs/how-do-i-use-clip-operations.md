---
title: How do I use clip operations?
date: 2023-12-06 22:49:17
enabled: true
category: "Structures"
---
You can use the&nbsp;[tidy3d.ClipOperation](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.ClipOperation.html){: target="_blank" rel="noopener"}&nbsp;object to combine multiple geometries through *'union'*,&nbsp;*'intersection'*,&nbsp;*'difference'*, and *'symmetric\_difference'*&nbsp; operations. Simply define the `geometry_a` and the `geometry_b`&nbsp;and assign them to the clip object. For example:

<div markdown class="code-snippet">{% highlight python %}

box = tidy3d.Box(center=(0,0,0), size=(1, 1, 2))
cyl = tidy3d.Cylinder(center=(1,0,0), radius=0.5, length=2, axis=2)

union = tidy3d.ClipOperation(
  operation='union', geometry_a=box, geometry_b=cyl
)

intersection = tidy3d.ClipOperation(
  operation='intersection', geometry_a=box, geometry_b=cyl
)

difference = tidy3d.ClipOperation(
  operation='difference', geometry_a=box, geometry_b=cyl
)

symmetric_difference = tidy3d.ClipOperation(
  operation='symmetric_difference', geometry_a=box, geometry_b=cyl
)

{% endhighlight %}
{% include copy-button.html %}</div>

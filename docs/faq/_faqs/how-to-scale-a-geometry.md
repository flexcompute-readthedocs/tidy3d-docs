---
title: How to scale a geometry?
date: 2023-12-06 21:43:10
enabled: true
category: "Structures"
---

In Tidy3D, all geometries can be translated, rotated, and scaled. These methods create a new copy of the original geometry with a transformation applied. For example, you can start with a `tidy3d.Box` centered at the origin and create a copy of it scaled by a factor of 2 in all directions:

<div markdown class="code-snippet">{% highlight python %}

box = tidy3d.Box(size=(2, 1, 1))

box_scaled = box.scaled(x=2.0, y=2.0, z=2.0)

_ = box_scaled.plot(z = 0)

{% endhighlight %}
{% include copy-button.html %}</div>

See this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/GeometryTransformations/) for more information.
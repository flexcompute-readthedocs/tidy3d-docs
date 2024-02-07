---
title: How do I create a geometry group?
date: 2023-12-06 22:15:15
enabled: true
category: "Structures"
---
A geometry group is a convenient way to gather multiple geometry objects into one collection. It can significantly improve performance when all the geometries in the group are assigned to the same medium. To create a geometry group, use the [tidy3d.GeometryGroup](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GeometryGroup.html){: target="_blank" rel="noopener"} object and set the&nbsp;`geometries` parameter as below:

<div markdown class="code-snippet">{% highlight python %}

cylinders = []

for i in range(0, 4):
  c = tidy3d.Cylinder(
    axis=2, radius=0.3, center=(i, 0, 0), length=2,
  )
  cylinders.append(c)

structure = tidy3d.Structure(
  geometry=tidy3d.GeometryGroup(geometries=cylinders),
  medium=tidy3d.Medium(permittivity=4),
)

{% endhighlight %}
{% include copy-button.html %}</div>

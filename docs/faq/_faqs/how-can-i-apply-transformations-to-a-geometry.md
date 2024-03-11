---
title: How can I apply transformations to a geometry?
date: 2023-12-06 21:43:10
enabled: true
category: "Structures"
---

In Tidy3D, all geometries can be translated, rotated, and scaled. These methods create a new copy of the original geometry with a transformation applied. For example, you can start with a `tidy3d.Box` centered at the origin and create a copy of it rotated around the `z`-axis:

<div markdown class="code-snippet">{% highlight python %}

box = tidy3d.Box(size=(2, 1, 1))

rotated_box = box.rotated(np.pi / 6, axis=2)

_ = rotated_box.plot(z = 0)

{% endhighlight %}
{% include copy-button.html %}</div>

Transformed geometries can be further transformed. Composing transformations is as simple as cascading the method calls. In the following example, we create an ellipsoidal prism by scaling a primitive `tidy3d.Cylinder` and rotating it.

<div markdown class="code-snippet">{% highlight python %}

ellipsoid = tidy3d.Cylinder(radius=0.5, length=0.5, axis=1).scaled(x=2, y=1, z=1).rotated(np.pi / 4, axis=1)

_ = ellipsoid.plot(y=0)

{% endhighlight %}
{% include copy-button.html %}</div>

A [tidy3d.Transformed](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Transformed.html) object contains an inner geometry and a transformation, written as a 4 x 4 matrix and applied to the (homogeneous) coordinates of the inner geometry. It is possible to define a `Transformed` object directly from the inner geometry and the transformation. To help create the most usual transformation matrices, the `Transformed` class has 3 static methods for translation, rotation, and scaling that can be used and combined (the @ operator can be used for matrix multiplication with `numpy` arrays).

<div markdown class="code-snippet">{% highlight python %}

rot = tidy3d.Transformed.rotation(np.pi / 3, axis=(1, 1, 1))
trans = tidy3d.Transformed.translation(1, 2, 0)
scale = tidy3d.Transformed.scaling(1, 1.25, 1)

# The box is first rotated, then translated, and finally scaled
transformed = td.Transformed(geometry=td.Box(size=(1, 1, 1)), transform=scale @ trans @ rot)

{% endhighlight %}
{% include copy-button.html %}</div>

See this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/GeometryTransformations/) for more information.
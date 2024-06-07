---
title: How do I create a polygon?
date: 2023-12-06 21:58:10
enabled: true
category: "Structures"
---
Use the&nbsp;[tidy3d.PolySlab](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PolySlab.html){: target="_blank" rel="noopener"}&nbsp;object to create an extruded polygon with an optional sidewall angle along the `axis` direction. The polygon geometry is defined by the&nbsp;`vertices` parameter, which receives a list of (d1, d2) coordinates defining the geometry of the polygon face at the&nbsp;`reference_plane`. The&nbsp;`slab_bounds`&nbsp;parametere defines the minimum and maximum positions of the slab along the&nbsp;`axis` dimension. Set the&nbsp;`sidewall_angle` with respect to the `reference_plane `to create slanted sidewalls. In addition, you can dilate or erode the polygon by setting positive or negative values to&nbsp;`dilation` parameter.

<div markdown class="code-snippet">{% highlight python %}

vertices = np.array([(0,0), (1,0), (1,1)])
triangle = tidy3d.PolySlab(vertices=vertices, axis=2, slab_bounds=(-1, 1))

{% endhighlight %}
{% include copy-button.html %}</div>

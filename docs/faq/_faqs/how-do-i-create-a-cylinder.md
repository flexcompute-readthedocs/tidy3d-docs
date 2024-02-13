---
title: How do I create a cylinder?
date: 2023-12-06 21:46:33
enabled: true
category: "Structures"
---
You can create a cylinder using the&nbsp;[tidy3d.Cylinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Cylinder.html){: target="_blank" rel="noopener"}&nbsp;object. In the example below we create a cylinder 2 $\mu$m in length, oriented along the `z`\-axis, with a&nbsp;&nbsp;&nbsp; 0.5 $\mu$m radius, and positioned at (-1,1,0). To obtain a conical shape, set the parameters&nbsp;`sidewall_angle` and&nbsp;`reference_plane`.&nbsp;

<div markdown class="code-snippet">{% highlight python %}

cyl = tidy3d.Cylinder(center=(-1,1,0), radius=0.5, length=2, axis=2)

{% endhighlight %}
{% include copy-button.html %}</div>

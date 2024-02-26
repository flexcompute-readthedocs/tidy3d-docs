---
title: How do I create a lossy material (with a conductivity)?
date: 2023-12-05 18:33:57
enabled: true
category: "Mediums"
---
To create a lossy material including conductivity, use the [tidy3d.Medium](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Medium.html){: target="_blank" rel="noopener"} object and set the `conductivity` parameter. For example:

<div markdown class="code-snippet">{% highlight python %}

lossy_medium = tidy3d.Medium(permittivity=2.0, conductivity=1.0)

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div> </div></div>

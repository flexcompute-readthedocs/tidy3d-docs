---
title: How do I load a commonly used dispersive material?
date: 2023-12-05 19:44:23
enabled: true
category: "Mediums"
---
<div><div>Tidy3D has an extensive <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/index.html#material-library">material library</a>&nbsp;containing various dispersive models from real world materials. You can import one of several material models using only a single line of code, as below:</div><div> </div></div>

<div markdown class="code-snippet">{% highlight python %}

from tidy3d import material_library

silver = material_library['Ag']['Rakic1998BB']

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div><p>The key of the dictionary is the abbreviated material name. Some materials have multiple variant models, in which case the second key is the “variant” name.</p></div></div>

---
title: How can I define graphene?
date: 2023-12-05 20:22:01
enabled: true
category: "Mediums"
---
You can create a graphene medium using&nbsp;[tidy3d.Graphene](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Graphene.html#tidy3d.Graphene){: target="_blank" rel="noopener"}, which defines a parametric surface conductivity model for graphene. For example:

<div markdown class="code-snippet">{% highlight python %}

gamma = 0.0033  # Scattering rate (eV).
mu_c = 0.5  # Graphene chemical potential (eV).
temp = 300  # Temperature (K).
scaling = 2  # Number of graphene layers.

graphene = td.material_library["graphene"](
    gamma=gamma, mu_c=mu_c, temp=temp, scaling=scaling
).medium

# or
# graphene = tidy3d.Graphene(
#    gamma=gamma, mu_c=mu_c, temp=temp, scaling=scaling
# ).medium

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div>See <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/GrapheneMetamaterial/">this example</a> for details on creating and using a Graphene medium.</div></div>

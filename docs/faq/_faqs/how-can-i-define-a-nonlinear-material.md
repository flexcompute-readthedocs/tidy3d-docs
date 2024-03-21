---
title: How can I define a nonlinear material?
date: 2023-12-05 20:35:00
enabled: true
category: "Mediums"
---
To create nonlinear material, you should specify a [tidy3d.NonlinearSusceptibility](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.NonlinearSusceptibility.html#tidy3d.NonlinearSusceptibility){: target="_blank" rel="noopener"}&nbsp;to the&nbsp;`nonlinear_spec`&nbsp;parameter of any medium. For example:

<div markdown class="code-snippet">{% highlight python %}

medium = tidy3d.Medium(permittivity=2, nonlinear_spec=tidy3d.NonlinearSusceptibility(chi3=1, numiters=5))

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div>Where <code>chi3</code> is the nonlinear susceptibility, and <code>numiters</code> is the number of iterations for solving nonlinear constitutive relation.</div><div> </div><div>Se <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/BistablePCCavity/">this notebook</a> for an example on using material nonlinearity.</div></div>

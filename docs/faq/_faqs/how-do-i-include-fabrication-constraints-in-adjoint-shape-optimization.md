---
_schema: default
title: How do I include fabrication constraints in adjoint shape optimization?
date: 2023-12-21 22:49:03
enabled: true
category: Inverse Design
_inputs:
  title:
    type: text
    label: QUESTION TITLE
  enabled:
    type: switch
    hidden: true
  date:
    type: datetime
    label: DATE
    instance_value: NOW
  category:
    type: select
    options:
      values: data.faq_categories
      value_key: key
      preview:
        text:
          - key: category_name
---
<div><p>To ensure reliable fabrication of a device, it is crucial to avoid using feature sizes below a certain radius of curvature when performing inverse design. To achieve this, you can use a penalty function that estimates the radius of curvature around each boundary vertex and applies a substantial penalty to the objective function if the value falls below the minimum radius. The code <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin5BoundaryGradients/">example</a> below demonstrates how to use the &nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.utils.penalty.RadiusPenalty.html">tidy3d.plugins.adjoint.utils.penalty.RadiusPenalty</a> function.</p><div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.adjoint.utils.penalty import RadiusPenalty

penalty = RadiusPenalty(min_radius=.150, alpha=1.0, kappa=10.0)
vertices0 = jnp.array(make_taper(ys0).vertices)
penalty_value = penalty.evaluate(vertices0)

{% endhighlight %}
{% include copy-button.html %}</div><p> </p></div>

<div> </div>

<div> </div>
---
_schema: default
title: How do I include fabrication constraints in adjoint topology optimization?
date: 2023-12-21 23:00:02
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
<div><p>To ensure reliable fabrication of a device, it is crucial to avoid using feature sizes below a certain radius of curvature when performing inverse design. To achieve this in topology (density-based) optimization, you can use a conic density filter, which is popular in topology optimization problems, to enforce a minimum feature size specified by the&nbsp;<code>filter_radius</code>&nbsp;variable. Next, a hyperbolic tangent projection function can be applied to eliminate grayscale and obtain a binarized permittivity pattern. The code <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin5BoundaryGradients/">example</a> below demonstrates how to apply the conic filter and the projection function to the design parameters before obtaining the permittivity values.</p><div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.adjoint.utils.filter import ConicFilter, BinaryProjector

conic_filter = ConicFilter(radius=filter_radius, design_region_dl=dr_grid_size)

def tanh_projection(x, beta, eta=0.5):
    tanhbn = jnp.tanh(beta * eta)
    num = tanhbn + jnp.tanh(beta * (x - eta))
    den = tanhbn + jnp.tanh(beta * (1 - eta))
    return num / den

def filter_project(x, beta, eta=0.5):
    x = conic_filter.evaluate(x)
    return tanh_projection(x, beta=beta, eta=eta)

def get_eps_values(params, beta):
    params = filter_project(params, beta=beta)
    eps_values = eps_min + (eps_max - eps_min) * params
    return eps_values

{% endhighlight %}
{% include copy-button.html %}</div><p> </p></div>

<div> </div>

<div> </div>
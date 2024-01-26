---
_schema: default
title: How do I set a PointDipole source?
date: 2023-12-07 15:15:41
enabled: true
category: Sources
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
The&nbsp;[tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html){: target="_blank" rel="noopener"}&nbsp;is a zero-dimensional uniform current source. The example below illustrates how to define&nbsp;[tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html){: target="_blank" rel="noopener"}&nbsp;within a simulation.

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
pt_dipole = tidy3d.PointDipole(
  center=(1,2,3),
  source_time=pulse,
  polarization='Ex',
  interpolate=True,
  name="dipole",
)

{% endhighlight %}
{% include copy-button.html %}</div>

Use the `center` parameter to set the dipole position, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}. The source `polarization` defines the direction and type of the current component. Finally, the parameter `interpolate` handles reverse interpolation of zero-size dimensions of the source. If&nbsp;`False`, the source data is snapped to the nearest Yee grid point. If&nbsp;`True`, equivalent source data is applied on the surrounding Yee grid points to emulate placement at the specified location using linear interpolation.

See this notebook to an&nbsp;[example](https://www.flexcompute.com/tidy3d/examples/notebooks/BullseyeCavityPSO/)&nbsp;on setting up a [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html){: target="_blank" rel="noopener"}&nbsp;source.
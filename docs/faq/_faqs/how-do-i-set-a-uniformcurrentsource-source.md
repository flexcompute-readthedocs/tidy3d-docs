---
_schema: default
title: How do I set a UniformCurrentSource source?
date: 2023-12-08 12:07:52
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
The&nbsp;[tidy3d.UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.UniformCurrentSource.html){: target="_blank" rel="noopener"}&nbsp;is a rectangular volume source with uniform time dependence. The example below illustrates how to define a&nbsp;[tidy3d.UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.UniformCurrentSource.html){: target="_blank" rel="noopener"}&nbsp;within a simulation.

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
source = tidy3d.UniformCurrentSource(
  center=(1,2,3),
  size=(0,2,1),
  source_time=pulse,
  polarization='Ex',
  interpolate=True,
  name="uniform_source",
)

{% endhighlight %}
{% include copy-button.html %}</div>

Use the `center`&nbsp;and `size` parameters to set the source position and volume, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}. The source `polarization` defines the direction and type of the current component. Finally, the parameter `interpolate` handles reverse interpolation of zero-size dimensions of the source. If&nbsp;`False`, the source data is snapped to the nearest Yee grid point. If&nbsp;`True`, equivalent source data is applied on the surrounding Yee grid points to emulate placement at the specified location using linear interpolation. Note that making `size=(0, 0, 0)` is equivalent to including a&nbsp;[tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html){: target="_blank" rel="noopener"}&nbsp;source.
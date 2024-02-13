---
_schema: default
title: How do I model a converging Gaussian beam?
date: 2023-12-11 14:56:49
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
To create a converging Gaussian beam, include a&nbsp;[tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html){: target="_blank" rel="noopener"}&nbsp;source in the simulation, and set the&nbsp;`waist_distance`&nbsp;to negative values. This way, the beam waist will lie in the front of the source plane, as illustrated in the following example

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
gauss_source = tidy3d.GaussianBeam(
  center=(0, -5, 0),
  size=(0, 3, 3),
  source_time=pulse,
  direction='+',
  pol_angle=0,
  angle_theta=0,
  angle_phi=0,
  waist_radius=1.0,
  waist_distance=-2.5,
  name="gauss_source",
)

{% endhighlight %}
{% include copy-button.html %}</div>

See this notebook to an&nbsp;[example](https://www.flexcompute.com/tidy3d/examples/notebooks/EdgeCoupler/)&nbsp;on setting up a [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html){: target="_blank" rel="noopener"}&nbsp;source.
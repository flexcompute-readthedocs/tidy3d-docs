---
_schema: default
title: How do I set a GaussianBeam?
date: 2023-12-11 14:19:04
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
The source&nbsp;[tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html){: target="_blank" rel="noopener"}&nbsp;is a Guassian distribution on a finite extent plane. The example below illustrates how to define the&nbsp;[tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html){: target="_blank" rel="noopener"}&nbsp;within a simulation.

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

Use the `center`&nbsp;and `size` parameters to set the source position and dimension, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}. The `direction` parameter specifies propagation in the positive or negative direction of the injection axis. You can change the light polarization using `pol_angle`, and&nbsp; adjust the propagation axis direction with `angle_theta`&nbsp;and&nbsp;`angle_phi`to control the polar and azimuth angles. In this example, the radius of the beam at the waist position was adjusted to 1$\mu$m using the&nbsp;`waist_radius `parameter. When&nbsp;`waist_distance`&nbsp;is positive (negative) the waist is behind (front) the source plane.

See this notebook to an&nbsp;[example](https://www.flexcompute.com/tidy3d/examples/notebooks/EdgeCoupler/)&nbsp;on setting up a [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html){: target="_blank" rel="noopener"}&nbsp;source.
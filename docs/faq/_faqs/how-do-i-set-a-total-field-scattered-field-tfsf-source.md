---
_schema: default
title: How do I set a total-field scattered-field (TFSF) source?
date: 2023-12-11 15:20:00
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
The total-field scattered-field (TFSF) source injects a plane wave in a finite region. The example below illustrates how to define the&nbsp;[tidy3d.TFSF](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.TFSF.html){: target="_blank" rel="noopener"}&nbsp;within a simulation.

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
tfsf_source = tidy3d.TFSF(
  center=(0, 0, 5),
  size=(3, 3, 0),
  source_time=pulse,
  direction='-',
  pol_angle=np.pi / 2,
  angle_theta=np.pi / 4,
  angle_phi=0,
  injection_axis=2,
  name="tfsf_source",
)

{% endhighlight %}
{% include copy-button.html %}</div>

Use the `center`&nbsp;and `size` parameters to set the source position and dimension, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}. The `direction` parameter specifies propagation in the positive or negative direction of the injection axis. You can change the light polarization using `pol_angle`, and&nbsp; adjust the propagation axis direction with `angle_theta`&nbsp;and&nbsp;`angle_phi`to control the polar and azimuth angles. The `injection_axis` parameter specifies injection along the `x` (*0*), `y` (*1*), or `z` (*2*) direction.

See this notebook to an&nbsp;[example](https://www.flexcompute.com/tidy3d/examples/notebooks/TFSF/)&nbsp;on setting up a [tidy3d.TFSF](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.TFSF.html){: target="_blank" rel="noopener"}&nbsp;source.
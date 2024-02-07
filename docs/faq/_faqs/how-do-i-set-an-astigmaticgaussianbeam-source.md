---
_schema: default
title: How do I set an AstigmaticGaussianBeam source?
date: 2023-12-11 15:07:45
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
The&nbsp;[tidy3d.AstigmaticGaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.AstigmaticGaussianBeam.html){: target="_blank" rel="noopener"} class implements the simple astigmatic Gaussian beam described in `Kochkina et al., Applied Optics, vol. 52, issue 24, (2013)`. The simple astigmatic Guassian distribution allows both an elliptical intensity profile and different waist locations for the two principal axes of the ellipse. The following example illustrates how to set up a&nbsp;[tidy3d.AstigmaticGaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.AstigmaticGaussianBeam.html){: target="_blank" rel="noopener"}.

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
gauss_source = tidy3d.AstigmaticGaussianBeam(
  center=(0, -5, 0),
  size=(0, 3, 3),
  source_time=pulse,
  direction='+',
  pol_angle=0,
  angle_theta=0,
  angle_phi=0,
  waist_sizes=(1.0, 2.0),
  waist_distances=(-1.0, -2.0),
  name="gauss_source",
)

{% endhighlight %}
{% include copy-button.html %}</div>

Use the `center`&nbsp;and `size` parameters to set the source position and dimension, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}. The `direction` parameter specifies propagation in the positive or negative direction of the injection axis. You can change the light polarization using `pol_angle`, and&nbsp; adjust the propagation axis direction with `angle_theta`&nbsp;and&nbsp;`angle_phi`to control the polar and azimuth angles. In this example, different `waist_sizes`&nbsp;and `waist_distances` were specified in the `x-` and `y-`directions.
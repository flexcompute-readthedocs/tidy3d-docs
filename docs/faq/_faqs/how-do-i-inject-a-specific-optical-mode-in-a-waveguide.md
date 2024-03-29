---
_schema: default
title: How do I inject a specific optical mode in a waveguide?
date: 2023-12-08 14:49:12
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
To inject a specific optical mode in the waveguide, you can use the&nbsp;[tidy3d.ModeSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSource.html){: target="_blank" rel="noopener"}&nbsp;source. Let's consider the case of injecting the first-order transverse electric (TE) mode in a silicon-on-insulator (SOI) waveguide operating at 1.55 $\mu$m as an example:

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=1.934e14, fwidth=6.245e12)

# Mode specification.
mode_spec = tidy3d.ModeSpec(target_neff=3.47, filter_pol='te', num_modes = 2)

# Source definition
source = tidy3d.ModeSource(
  center=(0, 0, -2),
  size=(0, 2, 1.5),
  source_time=pulse,
  direction='+',
  mode_spec=mode_spec,
  mode_index=1,
  name="mode_source",
)

{% endhighlight %}
{% include copy-button.html %}</div>

You should use the `center`&nbsp;and `size` parameters to define a source plane surrounding the waveguide, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}. The `direction='+'`&nbsp;parameter specifies propagation in the positive waveguide axis. The&nbsp;[tidy3d.ModeSpec](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSpec.html#tidy3d.ModeSpec){: target="_blank" rel="noopener"} object includes all the specifications of a mode solver, which calculates the optical modes given the material distribution within the source plane. The modes calculated by the mode solver are sorted by their effective indices in descending order. So, we have set the initial mode solver guess to the core refractive index (`target_neff=3.47`) and chosen&nbsp;`filter_pol='te'` to make sure it will return first in the list of the TE waveguide modes, starting from the fundamental one. Finally,&nbsp; to inject the first-order TE mode in the waveguide, we set&nbsp;`mode_index=1`.

This [example](https://www.flexcompute.com/tidy3d/examples/notebooks/ModalSourcesMonitors/) illustrates setting up a [tidy3d.ModeSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSource.html){: target="_blank" rel="noopener"}&nbsp;source.
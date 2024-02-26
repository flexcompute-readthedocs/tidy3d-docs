---
title: How do I inject an optical mode in a waveguide bend?
date: 2023-12-08 15:10:49
enabled: true
category: "Sources"
---
To inject an optical mode in a waveguide bend you must set the `bend_radius` and `bend_axis` parameters of&nbsp;[tidy3d.ModeSpec](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSpec.html#tidy3d.ModeSpec){: target="_blank" rel="noopener"}. For example:

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=1.934e14, fwidth=6.245e12)

# Mode specification.
mode_spec = tidy3d.ModeSpec(target_neff=2.5, bend_radius=-5, bend_axis=1)

# Source definition
source = tidy3d.ModeSource(
  center=(0, 0, -2),
  size=(0, 2, 1.5),
  source_time=pulse,
  direction='+',
  mode_spec=mode_spec,
  mode_index=0,
  name="mode_source",
)

{% endhighlight %}
{% include copy-button.html %}</div>

You can find a detailed example in this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/ModesBentAngled/){: target="_blank" rel="noopener"}.

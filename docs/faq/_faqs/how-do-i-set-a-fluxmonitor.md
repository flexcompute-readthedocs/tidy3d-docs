---
_schema: default
title: How do I set a FluxMonitor?
date: 2023-12-19 15:20:26
enabled: true
category: Monitors
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
A FluxMonitor object records power flux in the frequency domain. If the monitor geometry is a 2D box, the total flux through this plane is returned, with a positive sign corresponding to power flow in the positive direction along the axis normal to the plane. If the geometry is a 3D box, the total power coming out of the box is returned by integrating the flux over all box surfaces (except the ones defined in `exclude_surfaces`). You can define a FluxMonitor object by

<div markdown class="code-snippet">{% highlight python %}

monitor = FluxMonitor(
    center=(1,2,3),
    size=(2,2,0),
    freqs=[200e12, 210e12],
    name='flux_monitor')

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FluxMonitor.html).
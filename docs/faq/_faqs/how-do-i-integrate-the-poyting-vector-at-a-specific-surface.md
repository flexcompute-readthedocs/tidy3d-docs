---
_schema: default
title: How do I integrate the Poynting vector at a specific surface?
date: 2023-12-19 17:41:09
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
Since the field data in Tidy3D are natively&nbsp;`xarray.DataArray`&nbsp;objects, the most convenient way to perform integration is by using the&nbsp;`integrate`&nbsp;method in&nbsp;`xarray`. For example, if we want to integrate the Poynting vector on a surface parallel to the xy plane, one needs to compute the z-component of the time-averaged Poynting vector&nbsp;$Sz$&nbsp;and then&nbsp;

<div markdown class="code-snippet">{% highlight python %}

flux = Sz.integrate(coord=["x", "y"])

{% endhighlight %}
{% include copy-button.html %}
</div>

This effectively achieves the same as putting a FluxMonitor object at the same plane and extracting the flux result from the monitor data.&nbsp;
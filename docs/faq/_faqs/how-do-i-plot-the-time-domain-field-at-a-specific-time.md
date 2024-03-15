---
_schema: default
title: How do I plot the time-domain field at a specific time?
date: 2023-12-19 15:14:00
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
Once a simulation with a FieldTimeMonitor is complete, the time-domain field at a specific time instance can be plotted by selecting the specific time instance and using the plot method from the data array. One example is

<div markdown class="code-snippet">{% highlight python %}

sim_data['movie_monitor'].Hz.sel(t=1e-13, method='nearest').plot()

{% endhighlight %}
{% include copy-button.html %}
</div>

This line of code plots the z-component of the magnetic field at a time instance closest to 0.1 ps. Most likely, we will need to use the nearest interpolation here since the exact time instance might not be included in the result due to the finite time stepping. However, the difference is usually insignificant, so it is a very good approximation.
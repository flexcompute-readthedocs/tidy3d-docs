---
_schema: default
title: How do I set a ModeSolverMonitor?
date: 2023-12-19 17:10:11
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
A ModeSolverMonitor object stores the mode field profiles returned by the mode solver in the monitor plane. You can define a ModeSolverMonitor object by

<div markdown class="code-snippet">{% highlight python %}

mode_spec = ModeSpec(num_modes=3)
monitor = ModeSolverMonitor(
    center=(1,2,3),
    size=(2,2,0),
    freqs=[200e12, 210e12],
    mode_spec=mode_spec,
    name='mode_monitor')

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.ModeSolverMonitor.html).
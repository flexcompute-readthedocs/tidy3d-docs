---
_schema: default
title: How do I set a ModeMonitor?
date: 2023-12-19 17:02:53
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
A ModeMonitor object records complex amplitudes from the modal decomposition of fields on a plane. The amplitudes are defined as&nbsp;`mode_solver_data.dot(recorded_field) / mode_solver_data.dot(mode_solver_data)`, where&nbsp;`recorded_field`&nbsp;is the field data recorded in the FDTD simulation at the monitor frequencies, and&nbsp;`mode_solver_data`&nbsp;is the mode data from the mode solver at the monitor plane. This gives the power amplitude of&nbsp;`recorded_field`&nbsp;carried by each mode. You can define a ModeMonitor object by

<div markdown class="code-snippet">{% highlight python %}

mode_spec = ModeSpec(num_modes=3)
monitor = ModeMonitor(
    center=(1,2,3),
    size=(2,2,0),
    freqs=[200e12, 210e12],
    mode_spec=mode_spec,
    name='mode_monitor')

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeMonitor.html).
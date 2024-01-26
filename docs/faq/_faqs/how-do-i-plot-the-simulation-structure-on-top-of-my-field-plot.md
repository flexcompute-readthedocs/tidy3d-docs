---
_schema: default
title: How do I plot the simulation structure on top of my field plot?
date: 2023-12-19 16:28:19
enabled: true
category: Data Visualization and Postprocessing
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
You can use the&nbsp;[plot\_field()](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData.plot_field){: target="_blank" rel="noopener"}&nbsp;function to plot the structure on top of the simulated fields. For example:

<div><div markdown class="code-snippet">{% highlight python %}

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Plot the Ex field data and the structure.
ax = sim_data.plot_field(
  field_monitor_name="field",
  field_name="Ex",
  val='real',
  eps_alpha=0.2,
  phase=0,
)

{% endhighlight %}
{% include copy-button.html %}</div><p>You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.</p></div>
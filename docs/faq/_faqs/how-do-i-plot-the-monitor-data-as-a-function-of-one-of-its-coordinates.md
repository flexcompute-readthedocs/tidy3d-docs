---
_schema: default
title: "How do I plot the monitor data as a function of one of its coordinates?"
date: 2023-12-19 15:52:31
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
To plot the monitor data as a function of one of its coordinates, you can use&nbsp;`mon_data.plot()` if the data is already 1D. For example:

<div><div markdown class="code-snippet">{% highlight python %}

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get data from a flux monitor.
flux_data = sim_data["flux_monitor"].flux

# Plot the flux data.
f, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True, figsize=(8, 3))
flux_data.plot(ax=ax1)
ax2.plot(flux_data.f, flux_data.values)
plt.show()

{% endhighlight %}
{% include copy-button.html %}</div><p>To select the <code>x</code> axis data explicitly or plot all the data on same plot, use&nbsp;<code>mon_data.plot.line(x='f', ax=ax)</code>. &nbsp;Note that for all the plottings, if&nbsp;<code>ax</code>&nbsp;is not supplied, it will be created.</p><p>You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.</p></div>
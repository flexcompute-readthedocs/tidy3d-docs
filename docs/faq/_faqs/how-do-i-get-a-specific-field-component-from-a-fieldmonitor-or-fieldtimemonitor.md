---
_schema: default
title: "How do I get a specific field component from a\_FieldMonitor\_or\_FieldTimeMonitor?"
date: 2023-12-19 15:46:44
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
Some of the available convenience methods provided by the&nbsp;[DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) can be used to get a specific field component from a `FieldMonitor` or `FieldTimeMonitor`. For instance:

<div><div markdown class="code-snippet">{% highlight python %}

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a field monitor.
field_data = sim_data["field"]

# Get the Ex field component.
ex = field_data.Ex

# Get the Hy field component.
hy = field_data.Hy

{% endhighlight %}
{% include copy-button.html %}</div><p> </p><p>You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.</p></div>
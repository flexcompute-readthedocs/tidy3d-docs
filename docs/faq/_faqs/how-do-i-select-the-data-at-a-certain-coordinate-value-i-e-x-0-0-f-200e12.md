---
_schema: default
title: "How do I select the data at a certain coordinate value (i.e.\_x=0.0,\_f=200e12)?"
date: 2023-12-19 14:35:56
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
The simulation data is stored as a&nbsp;[DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html)&nbsp;object using the&nbsp;[xarray](https://xarray.pydata.org/en/stable/)&nbsp;package. You can think of it as a dataset where data is stored as a large, multi-dimensional array (like a numpy array) and the coordinates along each of the dimensions are specified so it is easy to work with.

You can use the `sel()` method to select data at certain coordinates. For example:

<div><div markdown class="code-snippet">{% highlight python %}

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a field monitor.
field_data = sim_data["field"]

# Get field data for a specific frequency.
field_freq = field_data.sel(f=200e14)

# Get field data for a specific position and frequency.
field_pos_freq = field_data.sel(z=0, f=200e14)

{% endhighlight %}
{% include copy-button.html %}</div><p>You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.</p></div>
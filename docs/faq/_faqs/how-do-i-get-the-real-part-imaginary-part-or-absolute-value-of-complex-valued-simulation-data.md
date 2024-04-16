---
_schema: default
title: >-
  How do I get the real part, imaginary part, or absolute value of
  complex-valued simulation data?
date: 2023-12-19 15:25:59
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
The simulation data is stored as a&nbsp;[DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html)&nbsp;object using the&nbsp;[xarray](https://xarray.pydata.org/en/stable/)&nbsp;package. You can think of it as a dataset where data is stored as a large multi-dimensional array (like a `numpy` array) and the coordinates along each of the dimensions are specified, so it is easy to work with.

Some of the available convenience methods provided by&nbsp;[DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) can be used to obtain the real, imaginary, or absolute value of complex-valued simulation data. For instance:

<div><div markdown class="code-snippet">{% highlight python %}

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a field monitor.
field_data = sim_data["field"]

# Get the real part of Ex field component.
ex_real = field_data.Ex.real

# Get the imaginary part of Ey field component.
ey_imag = field_data.Ey.imag

# Get the absolute value of Ez field component.
ez_abs = abs(field_data.Ez)

{% endhighlight %}
{% include copy-button.html %}</div><p> </p><p>You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.</p></div>
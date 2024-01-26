---
_schema: default
title: "How do I  get the monitor's data from a\_SimulationData\_object?"
date: 2023-12-19 13:12:20
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
To get the data of a particular monitor, you can use its name. For example, if you have a field monitor and have given it the name "field", you can refer to this name to retrieve the monitor's data after the simulation is run.

<div><div markdown class="code-snippet">{% highlight python %}

sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)
field_data = sim_data["field"]

{% endhighlight %}
{% include copy-button.html %}</div><p> </p></div>
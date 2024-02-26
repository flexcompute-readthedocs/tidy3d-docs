---
_schema: default
title: How do I access the data of a specific monitor?
date: 2023-12-18 23:02:06
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
You can access the data of a specific monitor by its name. For instance, supposing you have a field monitor and set its name to "field", after running the simulation you can refer to this name to get the monitor's data.&nbsp;

<div><div markdown class="code-snippet">{% highlight python %}

sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)
field_data = sim_data["field"]

{% endhighlight %}
{% include copy-button.html %}</div><p> </p></div>
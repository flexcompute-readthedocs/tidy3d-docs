---
_schema: default
title: How do I change the phase of fields obtained from frequency-domain monitors?
date: 2023-12-19 20:07:15
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
<div>You can use the&nbsp;<code><span>apply_phase</span>()</code> function to change the phase of fields obtained from frequency-domain monitors. For example:</div>

<div> </div>

<div markdown class="code-snippet">{% highlight python %}
import numpy as np

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get data from a field monitor.
field_data = sim_data["field_monitor"]

# Change the field phase by phi.
phi = 90 * np.pi / 180
field_phi = field_data.apply_phase(phi)

{% endhighlight %}
{% include copy-button.html %}</div>

<div>It's useful in observing resonance details or producing animations.</div>
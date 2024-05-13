---
_schema: default
title: How can I create a uniform grid?
date: 2023-12-11 18:47:30
enabled: true
category: Grid Specification
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
The most standard way to define a simulation is to use a constant grid size in each of the three directions. This can be achieved simply using&nbsp;`tidy3d.GridSpec.uniform(dl=...)`&nbsp;as shown below.

<div markdown class="code-snippet">{% highlight python %}

# Setting a uniform grid size of 0.02 microns.
sim_uniform = tidy3d.Simulation(
    size=(5, 5, 5),
    grid_spec=tidy3d.GridSpec.uniform(dl=0.02),
    medium=tidy3d.Medium(permittivity=4),
    structures=[structure],
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=td.PML())
    run_time=1e-12,
)

{% endhighlight %}
{% include copy-button.html %}</div>
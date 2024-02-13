---
_schema: default
title: How do I set the Absorber boundary condition?
date: 2023-12-15 20:59:51
enabled: true
category: Boundary Conditions
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
The [tidy3d.Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: target="_blank" rel="noopener"} boundary condition specifies an adiabatic absorber along a single dimension. This absorber is well-suited for dispersive materials intersecting with absorbing edges of the simulation at the expense of more layers. The example below shows how to set up an Aborbing boundary.

<div markdown class="code-snippet">{% highlight python %}

# Define PML boundary conditions in all sides.
bspec = tidy3d.BoundarySpec.all_sides(boundary=tidy3d.Absorber(num_layers=40))

# Build the simulation.
sim = tidy3d.Simulation(
    center=(0, 0, 0),
    size=(10, 4, 4),
    boundary_spec=bspec,
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[waveguide],
    sources=[mode_source],
    monitors=[mode_monitor],
    run_time=1e-12,
)

{% endhighlight %}
{% include copy-button.html %}</div>

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
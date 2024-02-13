---
_schema: default
title: How do I avoid reflections from the simulation edges?
date: 2023-12-15 21:41:47
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
You should use&nbsp;[tidy3d.PML](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PML.html#tidy3d.PML){: target="_blank" rel="noopener"} boundary condition to enclose the simulation domain with layers of a special lossy material designed to absorb incoming waves from all angles with minimal reflection. Tidy3D uses PML boundary conditions by default, but you can also set the boundaries explicitly using the&nbsp;`all_sides()`&nbsp;method. For example:

<div markdown class="code-snippet">{% highlight python %}

# Define PML boundary conditions in all sides.
bspec = tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PML())

# Alternatively, you can apply the boundary at specific directions.
# bspec = tidy3d.BoundarySpec.pml(x=True, y=True)

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

In some cases, such as when an angled structure or dispersive materials lie within the PML, use&nbsp;[tidy3d.Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: target="_blank" rel="noopener"} instead. The absorber functions similarly to PML such that it absorbs the outgoing radiation to mimic the infinite space. However, the absorber has a slightly higher reflection and requires a bit more computation than PML but it is numerically much more stable.

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
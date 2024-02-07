---
_schema: default
title: How can I locally refine the mesh?
date: 2023-12-11 18:55:58
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
In some problems the user may want to refine the grid mesh locally around specific geometry features, such as the gap between two very close waveguides where we expect the fields to be strongest. This can be achieved by adding&nbsp;`override_structures`&nbsp;to the simulation&nbsp;`grid_spec`. The&nbsp;`override_structures`&nbsp;is a list of Tidy3D structures each with an arbitrary geometry which are used exclusively for the meshing, added on top of any physical simulation structures. There are two types of Tidy3D structures that can be added the&nbsp;`override_structures`&nbsp;list. The first type defines a fictitious medium inside the override structure so that the grid size is decided by the minimum steps per wavelength in the medium; The second type is more straightforward: one can directly define the grid size along each axis inside the override structures.

##### Fictitious Medium

The first type is identical to the&nbsp;[Structure](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Structure.html)&nbsp;object that consists of a&nbsp;[Geometry](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/index.html#geometry)&nbsp;and a&nbsp;[Medium](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/index.html#mediums). The grid step in the `override_structure` region is decided by the minimum steps per wavelength in this&nbsp;`medium`.

<div markdown class="code-snippet">{% highlight python %}

# Define a "dummy" box with refractive index 5 around the central location of a slot waveguide.
refine_box = tidy3d.Structure(
    geometry=tidy3d.Box(center=(0, 0, 0), size=(td.inf, 0.4, 0.4)),
    medium=tidy3d.Medium(permittivity=5**2),
)

# Use the box as a grid refinement structure.
sim_refined = tidy3d.Simulation(
    size=[5, 3, 3],
    grid_spec=tidy3d.GridSpec.auto(
        wavelength=1.55,
        min_steps_per_wvl=20,
        override_structures=[refine_box],
    ),
    medium=tidy3d.Medium(permittivity=1.44**2),
    structures=[wave_guide_1, wave_guide_2],
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PML()),
    run_time=1e-12,
)

{% endhighlight %}
{% include copy-button.html %}</div>

##### Override Structure

The second type is the [tidy3d.MeshOverrideStructure](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.MeshOverrideStructure.html){: target="_blank" rel="noopener"}&nbsp;object that consists of a&nbsp;[Geometry](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/index.html#geometry), and a tuple&nbsp;`dl`&nbsp;specifying the grid sizes along `x`, `y`, and `z`\-directions. We can override the grid sizes just along a few selected directions by setting the value to be&nbsp;`None`&nbsp;in the&nbsp;`dl`&nbsp;tuple along the other directions. E.g. if we only plan to refine the grid size along `x`\-direction with grid size 0.01 $\mu$m, we can apply&nbsp;`dl=(0.01, None, None)`. In the following, we override the grid size along&nbsp;`y`&nbsp;and&nbsp;`z`&nbsp;to be 15.5nm.

<div markdown class="code-snippet">{% highlight python %}

# Define a MeshOverrideStructure.
refine_box = tidy3d.MeshOverrideStructure(
    geometry=tidy3d.Box(center=(0, 0, 0), size=(td.inf, 0.4, 0.4)),
    dl=[None, 0.015, 0.015],
)

# Use the box as a grid refinement structure.
sim_refined = tidy3d.Simulation(
    size=[5, 3, 3],
    grid_spec=tidy3d.GridSpec.auto(
        wavelength=1.55,
        min_steps_per_wvl=20,
        override_structures=[refine_box],
    ),
    medium=tidy3d.Medium(permittivity=1.44**2),
    structures=[wave_guide_1, wave_guide_2],
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PML()),
    run_time=1e-12,
)

{% endhighlight %}
{% include copy-button.html %}</div>
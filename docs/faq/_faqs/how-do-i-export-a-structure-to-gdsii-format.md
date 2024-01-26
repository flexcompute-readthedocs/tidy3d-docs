---
title: How do I export a structure to GDSII format?
date: 2023-12-06 21:17:44
enabled: true
category: "Structures"
---
In Tidy3D, you can export structures to GDSII file via the third-party&nbsp;[gdstk](https://heitzmann.github.io/gdstk/)&nbsp;package, which you can install running&nbsp;`pip install gdstk`. The example below creates a simple geometry and then exports it to GDSII:

<div markdown class="code-snippet">{% highlight python %}

# Create a gds cell to add the structures to.
geo_cell = gdstk.Cell("TOP")

# Make a box and add it to the cell.
box = gdstk.rectangle((-1, 1), (-1, 1), layer=0)
geo_cell.add(box)

# Create a library for the cell and save it.
gds_path = "box.gds"
lib = gdstk.Library()
lib.add(box_cell)
lib.write_gds(gds_path)

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div><p>The method <code>.to_gds_file()</code> is another option to export a geometry to GDSII. For example:</p><div markdown class="code-snippet">{% highlight python %}

# Create a simulation object.
sim = td.Simulation(
    size=sim_size,
    grid_spec=td.GridSpec.uniform(dl=dl),
    structures=structures,
    boundary_spec=td.BoundarySpec.all_sides(boundary=td.PML()),
)

# Export the structure to GDSII.
sim.to_gds_file(fname="sim.gds",
  z=0,
  permittivity_threshold=5,
  frequency=f0,
)

{% endhighlight %}
{% include copy-button.html %}</div><p>You can find more details on exporting structures to GDSII files in the notebook&nbsp;<a href="https://www.flexcompute.com/tidy3d/examples/notebooks/GDSImport/">Importing GDS files</a>.</p></div></div>

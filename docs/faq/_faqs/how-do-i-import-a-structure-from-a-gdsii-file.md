---
title: How do I import a structure from a GDSII file?
date: 2023-12-06 19:13:06
enabled: true
category: "Structures"
---
In Tidy3D, complex structures can be imported from GDSII files via the third-party&nbsp;[gdstk](https://heitzmann.github.io/gdstk/)&nbsp;package, which you can install running&nbsp;`pip install gdstk`. To load the geometry from a GDSII file, you should select the cell with the geometry you want. It is usually easier to verify that we can find the correct one by name first, for example:

<div markdown class="code-snippet">{% highlight python %}

# Load a GDSII library from the file.
lib_loaded = gdstk.read_gds(gds_path)

# Create a cell dictionary with all the cells in the file.
all_cells = {c.name: c for c in lib_loaded.cells}
print("Cell names: " + ", ".join(all_cells.keys()))

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div><p>Then you can construct Tidy3D geometries from the GDS cell just loaded, along with other information such as the axis, sidewall angle, and bounds of the "slab" using <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Geometry.html?highlight=tidy3d.Geometry#tidy3d.Geometry.from_gds">tidy3d.Geometry.from_gds()</a>. When loading GDS cell as the cross section of the device, we can tune&nbsp;<code>reference_plane</code>&nbsp;to set the cross-section to lie at&nbsp;<code>bottom</code>,&nbsp;<code>middle</code>, or&nbsp;<code>top</code>&nbsp;of the generated geometry with respect to the axis. E.g. if&nbsp;<code>axis=1</code>,&nbsp;<code>bottom</code>&nbsp;refers to the negative side of the y-axis, and&nbsp;<code>top</code>&nbsp;refers to the positive side of the y-axis. Additionally, we can optionally dilate or erode the cross section by setting&nbsp;<code>dilation</code>. A negative&nbsp;<code>dilation</code>&nbsp;corresponds to erosion. Note, we have to keep track of the&nbsp;<code>gds_layer</code>&nbsp;and&nbsp;<code>gds_dtype</code>&nbsp;used to define the GDS cell earlier, so we can load the right components.</p><div markdown class="code-snippet">{% highlight python %}

wg_height = 0.22
dilation = 0.02

geo = tidy3d.Geometry.from_gds(
    gds_cell=all_cells["TOP"],
    gds_layer=0,
    gds_dtype=0,
    axis=2,
    slab_bounds=(-0.11, 0.11),
    reference_plane="bottom",
)

{% endhighlight %}
{% include copy-button.html %}</div><p>You can find more details on importing GDSII files in these notebooks:&nbsp;<a href="https://www.flexcompute.com/tidy3d/examples/notebooks/GDSImport/">Importing GDS files</a>;&nbsp;<a href="https://www.flexcompute.com/tidy3d/examples/notebooks/SelfIntersectingPolyslab/">Defining self-intersecting polygons</a>.</p></div></div>

# How do I import a structure from a GDSII file?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 19:13:06 | Structures |


In Tidy3D, complex structures can be imported from GDSII files via the third-party [gdstk](https://heitzmann.github.io/gdstk/) package, which you can install running `pip install gdstk`. To load the geometry from a GDSII file, you should select the cell with the geometry you want. It is usually easier to verify that we can find the correct one by name first, for example:



```python

# Load a GDSII library from the file.
lib_loaded = gdstk.read_gds(gds_path)

# Create a cell dictionary with all the cells in the file.
all_cells = {c.name: c for c in lib_loaded.cells}
print("Cell names: " + ", ".join(all_cells.keys()))

```



Then you can construct Tidy3D geometries from the GDS cell just loaded, along with other information such as the axis, sidewall angle, and bounds of the "slab" using <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Geometry.html?highlight=tidy3d.Geometry#tidy3d.Geometry.from_gds">tidy3d.Geometry.from_gds()</a>. When loading GDS cell as the cross section of the device, we can tune <code>reference_plane</code> to set the cross-section to lie at <code>bottom</code>, <code>middle</code>, or <code>top</code> of the generated geometry with respect to the axis. E.g. if <code>axis=1</code>, <code>bottom</code> refers to the negative side of the y-axis, and <code>top</code> refers to the positive side of the y-axis. Additionally, we can optionally dilate or erode the cross section by setting <code>dilation</code>. A negative <code>dilation</code> corresponds to erosion. Note, we have to keep track of the <code>gds_layer</code> and <code>gds_dtype</code> used to defined the GDS cell earlier, so we can load the right components.

```python

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

```

You can find more details on importing GDSII files in these notebooks: <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/GDSImport/">Importing GDS files</a>; <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/SelfIntersectingPolyslab/">Defining self-intersecting polygons</a>.

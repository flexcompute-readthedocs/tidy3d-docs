# How can I import a structure from STL files?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 21:10:36 | Structures |


To use the STL import functionality, you must install Tidy3D as `pip install "tidy3d[trimesh]"`, which will install optional dependencies needed for processing surface meshes. Then you can use the [tidy3d.TriangleMesh.from\_stl()](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.TriangleMesh.html#tidy3d.TriangleMesh.from_stl) function. In the following example we will import a simple box geometry from a STL file.



```python

# Make the geometry object representing the STL solid from the STL file stored on disk
box = tidy3d.TriangleMesh.from_stl(
    filename="./misc/box.stl",
    scale=1,  # The units are already microns as desired, but this parameter can be used to change units [default: 1].
    origin=(
        0,
        0,
        0,
    ),  # This can be used to set a custom origin for the stl solid [default: (0, 0, 0)]
    solid_index=None,  # Sometimes, there may be more than one solid in the file; use this to select a specific one by index.
)

```



See [this example](https://www.flexcompute.com/tidy3d/examples/notebooks/STLImport/) for a complete reference on importing STL files.

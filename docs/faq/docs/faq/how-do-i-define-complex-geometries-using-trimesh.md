# How do I define complex geometries using trimesh?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 22:59:52 | Structures |


To define complex geometries using the [Trimesh](https://trimsh.org/index.html) library, you must install Tidy3D as `pip install "tidy3d[trimesh]"`, which will install optional dependencies needed for processing surface meshes. The Trimesh library provides some [built-in geometries](https://trimsh.org/trimesh.creation.html#) such as ring (annulus), box, capsule, cone, cylinder, and so on. Let's create a ring as an example.



```python

n_sections = 100 # How many sections to discretize the mesh.

# Create a ring mesh.
ring_mesh = trimesh.creation.annulus(r_min=9, r_max=10, height=1, sections=n_sections)

# Plot the mesh.
ring_mesh.show()

```



To use this geometry in a Tidy3D simulation, you need to convert the mesh into a [tidy3d.TriangleMesh](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.TriangleMesh.html) geometry. Use the `from_trimesh()` method to conviently convert the mesh to a Tidy3D geometry. From there, you can further define the Tidy3D structure and put it into a simulation.



```python

# Define a tidy3d geometry from a mesh.
ring_geo = td.TriangleMesh.from_trimesh(ring_mesh)

```



This [example](https://www.flexcompute.com/tidy3d/examples/notebooks/CreatingGeometryUsingTrimesh/) shows how to create many different complex geometries using [Trimesh](https://trimsh.org/index.html). 

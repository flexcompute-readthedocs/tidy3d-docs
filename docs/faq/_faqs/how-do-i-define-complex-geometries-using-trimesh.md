---
title: How do I define complex geometries using trimesh?
date: 2023-12-06 22:59:52
enabled: true
category: "Structures"
---
To define complex geometries using the&nbsp;[Trimesh](https://trimsh.org/index.html)&nbsp;library, you must install Tidy3D as&nbsp;`pip install "tidy3d[trimesh]"`, which will install optional dependencies needed for processing surface meshes. The Trimesh library provides some&nbsp;[built-in geometries](https://trimsh.org/trimesh.creation.html#)&nbsp;such as ring (annulus), box, capsule, cone, cylinder, and so on. Let's create a ring as an example.

<div markdown class="code-snippet">{% highlight python %}

n_sections = 100 # How many sections to discretize the mesh.

# Create a ring mesh.
ring_mesh = trimesh.creation.annulus(r_min=9, r_max=10, height=1, sections=n_sections)

# Plot the mesh.
ring_mesh.show()

{% endhighlight %}
{% include copy-button.html %}</div>

To use this geometry in a Tidy3D simulation, you need to convert the mesh into a [tidy3d.TriangleMesh](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.TriangleMesh.html){: target="_blank" rel="noopener"}&nbsp;geometry. Use the&nbsp;`from_trimesh()`&nbsp;method to conviently convert the mesh to a Tidy3D geometry. From there, you can further define Tidy3D structure and put it into a simulation.

<div markdown class="code-snippet">{% highlight python %}

# Define a tidy3d geometry from a mesh.
ring_geo = td.TriangleMesh.from_trimesh(ring_mesh)

{% endhighlight %}
{% include copy-button.html %}</div>

This [example](https://www.flexcompute.com/tidy3d/examples/notebooks/CreatingGeometryUsingTrimesh/){: target="_blank" rel="noopener"} shows how to create many different complex geometries using [Trimesh](https://trimsh.org/index.html).&nbsp;

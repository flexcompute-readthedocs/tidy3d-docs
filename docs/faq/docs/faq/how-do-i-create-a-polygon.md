# How do I create a polygon?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 21:58:10 | Structures |


Use the [tidy3d.PolySlab](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PolySlab.html) object to create an extruded polygon with an optional sidewall angle along the `axis` direction. The polygon geometry is defined by the `vertices` parameter, which receives a list of (d1, d2) coordinates defining the geometry of the polygon face at the `reference_plane`. The `slab_bounds` parametere defines the minimum and maximum positions of the slab along the `axis` dimension. Set the `sidewall_angle` with respect to the `reference_plane `to create slanted sidewalls. In addition, you can dilate or erode the polygon by setting positive or negative values to `dilation` parameter.



```python

vertices = np.array([(0,0), (1,0), (1,1)])
triangle = tidy3d.PolySlab(vertices=vertices, axis=2, slab_bounds=(-1, 1))

```



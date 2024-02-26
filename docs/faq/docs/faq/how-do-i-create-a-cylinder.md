# How do I create a cylinder?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 21:46:33 | Structures |


You can create a cylinder using the [tidy3d.Cylinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Cylinder.html) object. In the example below we create a cylinder 2 $\mu$m in length, oriented along the `z`\-axis, with a    0.5 $\mu$m radius, and positioned at (-1,1,0). To obtain a conical shape, set the parameters `sidewall_angle` and `reference_plane`. 



```python

cyl = tidy3d.Cylinder(center=(-1,1,0), radius=0.5, length=2, axis=2)

```



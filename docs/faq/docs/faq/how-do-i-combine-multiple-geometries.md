# How do I combine multiple geometries?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 22:35:41 | Structures |


You can combine multiple geometries using the [tidy3d.ClipOperation](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ClipOperation.html) object to perform *'union'*, *'intersection'*, *'difference'*, and *'symmetric\_difference'*  operations. For example:



```python

box = tidy3d.Box(center=(0,0,0), size=(1, 1, 2))
cyl = tidy3d.Cylinder(center=(1,0,0), radius=0.5, length=2, axis=2)

union = tidy3d.ClipOperation(
  operation='union', geometry_a=box, geometry_b=cyl
)

intersection = tidy3d.ClipOperation(
  operation='intersection', geometry_a=box, geometry_b=cyl
)

difference = tidy3d.ClipOperation(
  operation='difference', geometry_a=box, geometry_b=cyl
)

symmetric_difference = tidy3d.ClipOperation(
  operation='symmetric_difference', geometry_a=box, geometry_b=cyl
)

```



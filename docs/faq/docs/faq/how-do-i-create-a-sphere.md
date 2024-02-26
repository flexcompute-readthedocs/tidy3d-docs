# How do I create a sphere?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 21:43:10 | Structures |


You can create a sphere using the [tidy3d.Sphere](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Sphere.html) object and specifying the `center` and `radius` parameters, as below:



```python

box = tidy3d.Box.from_bounds(
  rmin=(-10, -1, -0.1),
  rmax=(10, 1, 0.1),
)

```



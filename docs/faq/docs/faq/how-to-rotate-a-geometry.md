# How to rotate a geometry?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 21:43:10 | Structures |



In Tidy3D, all geometries can be translated, rotated, and scaled. These methods create a new copy of the original geometry with a transformation applied. For example, you can start with a `tidy3d.Box` centered at the origin and create a copy of it rotated around the `z`-axis:



```python

box = tidy3d.Box(size=(2, 1, 1))

rotated_box = box.rotated(np.pi / 6, axis=2)

_ = rotated_box.plot(z = 0)

```



See this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/GeometryTransformations/) for more information.
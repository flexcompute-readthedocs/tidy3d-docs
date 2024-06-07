# How to translate a geometry?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 21:43:10 | Structures |



In Tidy3D, all geometries can be translated, rotated, and scaled. These methods create a new copy of the original geometry with a transformation applied. For example, you can start with a `tidy3d.Box` centered at the origin and create a copy of it translated in the `x`-direction by 2 $\mu m$:



```python

box = tidy3d.Box(size=(2, 1, 1))

box_translated = box.translated(x=2, y=0, z=0)

_ = box_translated.plot(z = 0)

```



See this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/GeometryTransformations/) for more information.
# How do I create a lossy material (with a conductivity)?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 18:33:57 | Mediums |


To create a lossy material including conductivity, use the [tidy3d.Medium](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Medium.html) object and set the `conductivity` parameter. For example:



```python

lossy_medium = tidy3d.Medium(permittivity=2.0, conductivity=1.0)

```



 

# How do I set a UniformCurrentSource source?

| Date       | Category    |
|------------|-------------|
| 2023-12-08 12:07:52 | Sources |


The [tidy3d.UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.UniformCurrentSource.html) is a rectangular volume source with uniform time dependence. The example below illustrates how to define a [tidy3d.UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.UniformCurrentSource.html) within a simulation.



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
source = tidy3d.UniformCurrentSource(
  center=(1,2,3),
  size=(0,2,1),
  source_time=pulse,
  polarization='Ex',
  interpolate=True,
  name="uniform_source",
)

```



Use the `center` and `size` parameters to set the source position and volume, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html). The source `polarization` defines the direction and type of the current component. Finally, the parameter `interpolate` handles reverse interpolation of zero-size dimensions of the source. If `False`, the source data is snapped to the nearest Yee grid point. If `True`, equivalent source data is applied on the surrounding Yee grid points to emulate placement at the specified location using linear interpolation. Note that making `size=(0, 0, 0)` is equivalent to including a [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html) source.
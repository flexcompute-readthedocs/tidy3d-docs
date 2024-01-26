# How do I set a PointDipole source?

| Date       | Category    |
|------------|-------------|
| 2023-12-07 15:15:41 | Sources |


The [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html) is a zero-dimensional uniform current source. The example below illustrates how to define [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html) within a simulation.



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
pt_dipole = tidy3d.PointDipole(
  center=(1,2,3),
  source_time=pulse,
  polarization='Ex',
  interpolate=True,
  name="dipole",
)

```



Use the `center` parameter to set the dipole position, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html). The source `polarization` defines the direction and type of the current component. Finally, the parameter `interpolate` handles reverse interpolation of zero-size dimensions of the source. If `False`, the source data is snapped to the nearest Yee grid point. If `True`, equivalent source data is applied on the surrounding Yee grid points to emulate placement at the specified location using linear interpolation.

See this notebook to an [example](https://www.flexcompute.com/tidy3d/examples/notebooks/BullseyeCavityPSO/) on setting up a [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html) source.
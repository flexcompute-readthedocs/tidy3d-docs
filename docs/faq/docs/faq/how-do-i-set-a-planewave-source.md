# How do I set a PlaneWave source?

| Date       | Category    |
|------------|-------------|
| 2023-12-08 12:26:07 | Sources |


The [tidy3d.PlaneWave](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PlaneWave.html) is a uniform current distribution on an infinite extent plane. The example below illustrates how to define a [tidy3d.PlaneWave](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PlaneWave.html) within a simulation.



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
source = tidy3d.PlaneWave(
  center=(0, 0, 5),
  size=(tidy3d.inf, tidy3d.inf, 0),
  source_time=pulse,
  direction='-',
  pol_angle=np.pi/2,
  angle_theta=0,
  angle_phi=0,
  name="plane_wave",
)

```



Use the `center` and `size` parameters to set the source position and dimension, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html). The `direction` parameter specifies propagation in the positive or negative direction of the injection axis. You can change the light polarization using `pol_angle`, and  adjust the propagation axis direction with `angle_theta` and `angle_phi`to control the polar and azimuth angles.

This [example](https://www.flexcompute.com/tidy3d/examples/notebooks/GratingEfficiency/) illustrates setting up a [tidy3d.PlaneWave](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PlaneWave.html) source at normal and off-normal incidences.
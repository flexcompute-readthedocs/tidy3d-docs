# How do I set a total-field scattered-field (TFSF) source?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 15:20:00 | Sources |


The total-field scattered-field (TFSF) source injects a plane wave in a finite region. The example below illustrates how to define the [tidy3d.TFSF](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.TFSF.html) within a simulation.



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
tfsf_source = tidy3d.TFSF(
  center=(0, 0, 5),
  size=(3, 3, 0),
  source_time=pulse,
  direction='-',
  pol_angle=np.pi / 2,
  angle_theta=np.pi / 4,
  angle_phi=0,
  injection_axis=2,
  name="tfsf_source",
)

```



Use the `center` and `size` parameters to set the source position and dimension, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html). The `direction` parameter specifies propagation in the positive or negative direction of the injection axis. You can change the light polarization using `pol_angle`, and  adjust the propagation axis direction with `angle_theta` and `angle_phi`to control the polar and azimuth angles. The `injection_axis` parameter specifies injection along the `x` (*0*), `y` (*1*), or `z` (*2*) direction.

See this notebook to an [example](https://www.flexcompute.com/tidy3d/examples/notebooks/TFSF/) on setting up a [tidy3d.TFSF](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.TFSF.html) source.
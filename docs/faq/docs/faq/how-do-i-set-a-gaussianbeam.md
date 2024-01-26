# How do I set a GaussianBeam?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 14:19:04 | Sources |


The source [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html) is a Guassian distribution on a finite extent plane. The example below illustrates how to define the [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html) within a simulation.



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Source definition
gauss_source = tidy3d.GaussianBeam(
  center=(0, -5, 0),
  size=(0, 3, 3),
  source_time=pulse,
  direction='+',
  pol_angle=0,
  angle_theta=0,
  angle_phi=0,
  waist_radius=1.0,
  waist_distance=-2.5,
  name="gauss_source",
)

```



Use the `center` and `size` parameters to set the source position and dimension, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html). The `direction` parameter specifies propagation in the positive or negative direction of the injection axis. You can change the light polarization using `pol_angle`, and  adjust the propagation axis direction with `angle_theta` and `angle_phi`to control the polar and azimuth angles. In this example, the radius of the beam at the waist position was adjusted to 1$\mu$m using the `waist_radius `parameter. When `waist_distance` is positive (negative) the waist is behind (front) the source plane.

See this notebook to an [example](https://www.flexcompute.com/tidy3d/examples/notebooks/EdgeCoupler/) on setting up a [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html) source.
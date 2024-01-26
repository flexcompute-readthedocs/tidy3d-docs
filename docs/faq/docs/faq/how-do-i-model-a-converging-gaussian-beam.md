# How do I model a converging Gaussian beam?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 14:56:49 | Sources |


To create a converging Gaussian beam, include a [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html) source in the simulation, and set the `waist_distance` to negative values. This way, the beam waist will lie in the front of the source plane, as illustrated in the following example



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



See this notebook to an [example](https://www.flexcompute.com/tidy3d/examples/notebooks/EdgeCoupler/) on setting up a [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html) source.
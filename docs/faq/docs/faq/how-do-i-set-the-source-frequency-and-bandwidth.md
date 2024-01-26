# How do I set the source frequency and bandwidth?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 16:17:31 | Sources |


You can set the source frequency and bandwidth through the `source_time` parameter, which accepts a [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html) object. In the example below, we create a [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html) source to radiate power at a center wavelength of 1.55 $\mu$m over a bandwidth of 100 nm.



```python

# Simulation wavelength and bandwidth.
wl = 1.55
bw = 0.1
wl_max = wl + bw / 2
wl_min = wl - bw / 2
freq0 = tidy3d.C_0 / wl
fwidth = 0.5 * (tidy3d.C_0 / wl_min - tidy3d.C_0 / wl_max)

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=freq0, fwidth=fwidth)

# Source definition
pt_dipole = tidy3d.PointDipole(
  center=(1,2,3),
  source_time=pulse,
  polarization='Ex',
  interpolate=True,
  name="dipole",
)

```


# How do I inject a specific optical mode in a waveguide?

| Date       | Category    |
|------------|-------------|
| 2023-12-08 14:49:12 | Sources |


To inject a specific optical mode in the waveguide, you can use the [tidy3d.ModeSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSource.html) source. Let's consider the case of injecting the first-order transverse electric (TE) mode in a silicon-on-insulator (SOI) waveguide operating at 1.55 $\mu$m as an example:



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=1.934e14, fwidth=6.245e12)

# Mode specification.
mode_spec = tidy3d.ModeSpec(target_neff=3.47, filter_pol='te', num_modes = 2)

# Source definition
source = tidy3d.ModeSource(
  center=(0, 0, -2),
  size=(0, 2, 1.5),
  source_time=pulse,
  direction='+',
  mode_spec=mode_spec,
  mode_index=1,
  name="mode_source",
)

```



You should use the `center` and `size` parameters to define a source plane surrounding the waveguide, then adjust the `source_time` dependence using [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GaussianPulse.html). The `direction='+'` parameter specifies propagation in the positive waveguide axis. The [tidy3d.ModeSpec](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSpec.html#tidy3d.ModeSpec) object includes all the specifications of a mode solver, which calculates the optical modes given the material distribution within the source plane. The modes calculated by the mode solver are sorted by their effective indices in descending order. So, we have set the initial mode solver guess to the core refractive index (`target_neff=3.47`) and chosen `filter_pol='te'` to make sure it will return first in the list of the TE waveguide modes, starting from the fundamental one. Finally,  to inject the first-order TE mode in the waveguide, we set `mode_index=1`.

This [example](https://www.flexcompute.com/tidy3d/examples/notebooks/ModalSourcesMonitors/) illustrates setting up a [tidy3d.ModeSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSource.html) source.
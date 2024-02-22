# How do I inject an optical mode in an angled waveguide?

| Date       | Category    |
|------------|-------------|
| 2023-12-08 14:55:25 | Sources |


To inject an optical mode in an angled waveguide you must set the `angle_theta` and `angle_phi` parameters of [tidy3d.ModeSpec](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSpec.html#tidy3d.ModeSpec). For example:



```python

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=1.934e14, fwidth=6.245e12)

# Mode specification.
mode_spec = tidy3d.ModeSpec(target_neff=2.5, angle_theta=1.5, angle_phi=0)

# Source definition
source = tidy3d.ModeSource(
  center=(0, 0, -2),
  size=(0, 2, 1.5),
  source_time=pulse,
  direction='+',
  mode_spec=mode_spec,
  mode_index=0,
  name="mode_source",
)

```



You can find a detailed example in this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/ModesBentAngled/).
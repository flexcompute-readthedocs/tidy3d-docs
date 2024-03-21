# How do I set a ModeMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 17:02:53 | Monitors |


A ModeMonitor object records complex amplitudes from the modal decomposition of fields on a plane. The amplitudes are defined as `mode_solver_data.dot(recorded_field) / mode_solver_data.dot(mode_solver_data)`, where `recorded_field` is the field data recorded in the FDTD simulation at the monitor frequencies, and `mode_solver_data` is the mode data from the mode solver at the monitor plane. This gives the power amplitude of `recorded_field` carried by each mode. You can define a ModeMonitor object by



```python

mode_spec = ModeSpec(num_modes=3)
monitor = ModeMonitor(
    center=(1,2,3),
    size=(2,2,0),
    freqs=[200e12, 210e12],
    mode_spec=mode_spec,
    name='mode_monitor')

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeMonitor.html).
# How do I set a ModeSolverMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 17:10:11 | Monitors |


A ModeSolverMonitor object stores the mode field profiles returned by the mode solver in the monitor plane. You can define a ModeSolverMonitor object by



```python

mode_spec = ModeSpec(num_modes=3)
monitor = ModeSolverMonitor(
    center=(1,2,3),
    size=(2,2,0),
    freqs=[200e12, 210e12],
    mode_spec=mode_spec,
    name='mode_monitor')

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSolverMonitor.html).
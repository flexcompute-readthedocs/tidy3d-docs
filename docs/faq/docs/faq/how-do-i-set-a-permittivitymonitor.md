# How do I set a PermittivityMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 17:11:46 | Monitors |


The `PermittivityMonitor` records the diagonal components of the complex-valued relative permittivity tensor in the frequency domain. You can define a PermittivityMonitor object by



```python

monitor = PermittivityMonitor(
    center=(1,2,3),
    size=(2,2,2),
    freqs=[250e12, 300e12],
    name='eps_monitor')

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PermittivityMonitor.html).
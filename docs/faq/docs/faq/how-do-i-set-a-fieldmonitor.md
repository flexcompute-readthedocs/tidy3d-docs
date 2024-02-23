# How do I set a FieldMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:00:41 | Monitors |


A FieldMonitor object records electromagnetic fields in the frequency domain. You can define a FieldMonitor object by



```python

monitor = FieldMonitor(
    center=(1,2,3),
    size=(2,2,2),
    fields=['Hx'],
    freqs=[250e12, 300e12],
    name='steady_state_monitor',
colocate=True)

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldMonitor.html).
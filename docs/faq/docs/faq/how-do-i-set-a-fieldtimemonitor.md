# How do I set a FieldTimeMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:11:26 | Monitors |


A FieldTimeMonitor object records electromagnetic fields in the time domain. You can define a FieldTimeMonitor object by



```python

monitor = FieldTimeMonitor(
    center=(1,2,3),
    size=(2,2,2),
    fields=['Hx'],
    start=1e-13,
    stop=5e-13,
    interval=2,
    colocate=True,
    name='movie_monitor')

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.FieldTimeMonitor.html).
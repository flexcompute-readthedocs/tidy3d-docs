# How do I set a FluxTimeMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:26:58 | Monitors |


A FluxTimeMonitor object records power flux in the time domain. If the monitor geometry is a 2D box, the total flux through this plane is returned, with a positive sign corresponding to power flow in the positive direction along the axis normal to the plane. If the geometry is a 3D box, the total power coming out of the box is returned by integrating the flux over all box surfaces (excpet the ones defined in `exclude_surfaces`). You can define a FluxTimeMonitor object by 



```python

monitor = FluxTimeMonitor(
    center=(1,2,3),
    size=(2,2,0),
    start=1e-13,
    stop=5e-13,
    interval=2,
    name='flux_vs_time')

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.FluxTimeMonitor.html).
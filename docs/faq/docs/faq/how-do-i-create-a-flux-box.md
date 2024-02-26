# How do I create a flux box?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:28:53 | Monitors |


A flux box can be defined by creating a FluxMonitor object with a 3D geometry. The total power coming out of the box is returned by integrating the flux over all box surfaces (excpet the ones defined in `exclude_surfaces`). 

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FluxMonitor.html).
# How do I integrate the Poynting vector at a specific surface?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 17:41:09 | Monitors |


Since the field data in Tidy3D are natively `xarray.DataArray` objects, the most convenient way to perform integration is by using the `integrate` method in `xarray`. For example, if we want to integrate the Poynting vector on a surface parallel to the xy plane, one needs to compute the z-component of the time-averaged Poynting vector $Sz$ and then 



```python

flux = Sz.integrate(coord=["x", "y"])

```



This effectively achieves the same as putting a FluxMonitor object at the same plane and extracting the flux result from the monitor data. 
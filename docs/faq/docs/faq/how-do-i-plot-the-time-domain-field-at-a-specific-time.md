# How do I plot the time-domain field at a specific time?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:14:00 | Monitors |


Once a simulation with a FieldTimeMonitor is complete, the time-domain field at a specific time instance can be plotted by selecting the specific time instance and using the plot method from the data array. One example is



```python

sim_data['movie_monitor'].Hz.sel(t=1e-13, method='nearest').plot()

```



This line of code plots the z-component of the magnetic field at a time instance closest to 0.1 ps. Most likely we will need to use the nearst interpolation here since the exact time instance might not be included in the result due to the finite time stepping. However, the difference is usually not significant so it serves as a very good approximation. 
# How do I plot the monitor data as a function of one of its coordinates?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:52:31 | Data Visualization and Postprocessing |


To plot the monitor data as a function of one of its coordinates, you can use `mon_data.plot()` if the data is already 1D. For example:



```python

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get data from a flux monitor.
flux_data = sim_data["flux_monitor"].flux

# Plot the flux data.
f, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True, figsize=(8, 3))
flux_data.plot(ax=ax1)
ax2.plot(flux_data.f, flux_data.values)
plt.show()

```

To select the <code>x</code> axis data explicitly or plot all the data on same plot, use <code>mon_data.plot.line(x='f', ax=ax)</code>.  Note that for all the plottings, if <code>ax</code> is not supplied, it will be created.You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.
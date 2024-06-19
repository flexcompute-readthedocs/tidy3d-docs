# How do I plot the simulation structure on top of my field plot?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 16:28:19 | Data Visualization and Postprocessing |


You can use the [plot\_field()](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData.plot_field) function to plot the structure on top of the simulated fields. For example:



```python

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Plot the Ex field data and the structure.
ax = sim_data.plot_field(
  field_monitor_name="field",
  field_name="Ex",
  val='real',
  eps_alpha=0.2,
  phase=0,
)

```

You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.
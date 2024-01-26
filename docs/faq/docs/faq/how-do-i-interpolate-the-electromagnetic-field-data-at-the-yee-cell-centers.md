# How do I interpolate the electromagnetic field data at the Yee cell centers?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 12:29:51 | Data Visualization and Postprocessing |


To interpolate the electromagnetic fields to the Yee cell centers, you can use the method <code>at_centers(monitor_name)</code>. For example:

```python

# Run the simulation and get the results.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Interpolate the field at the Yee cell centers.
field_data_centered = sim_data.at_centers("monitor_name").interp(f=freq0)

```

 <blockquote>By default, the electromagnetic fields are colocated to Yee grid boundaries. If you want to colocate data into custom coordinates, set <code>colocate=False</code> in field monitors to use the raw data on the Yee grid and avoid double interpolation.</blockquote>

For more details on visualizing and postprocessing simulation data, see this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">notebook</a>.
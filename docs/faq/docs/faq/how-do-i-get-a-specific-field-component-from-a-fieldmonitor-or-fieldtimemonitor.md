# How do I get a specific field component from a FieldMonitor or FieldTimeMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:46:44 | Data Visualization and Postprocessing |


Some of the available convenience methods provided by the [DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) can be used to get a specific field component from a `FieldMonitor` or `FieldTimeMonitor`. For instance:



```python

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a field monitor.
field_data = sim_data["field"]

# Get the Ex field component.
ex = field_data.Ex

# Get the Hy field component.
hy = field_data.Hy

```

 You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.
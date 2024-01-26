# How do I get the monitor data at a certain index?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 14:49:03 | Data Visualization and Postprocessing |


The simulation data is stored as a [DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) object using the [xarray](https://xarray.pydata.org/en/stable/) package. You can think of it as a dataset where data is stored as a large, multi-dimensional array (like a numpy array) and the coordinates along each of the dimensions are specified so it is easy to work with.

You can use the `isel()` method to select data at certain coordinates index. For example:



```python

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a field monitor.
field_data = sim_data["field"]

# Get field data for a specific frequency index.
field_freq_3 = field_data.isel(f=3)

```

You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.
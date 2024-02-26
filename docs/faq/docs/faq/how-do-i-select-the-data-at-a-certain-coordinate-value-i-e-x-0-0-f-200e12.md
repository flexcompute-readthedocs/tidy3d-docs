# How do I select the data at a certain coordinate value (i.e. x=0.0, f=200e12)?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 14:35:56 | Data Visualization and Postprocessing |


The simulation data is stored as a [DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) object using the [xarray](https://xarray.pydata.org/en/stable/) package. You can think of it as a dataset where data is stored as a large, multi-dimensional array (like a numpy array) and the coordinates along each of the dimensions are specified so it is easy to work with.

You can use the `sel()` method to select data at certain coordinates. For example:



```python

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a field monitor.
field_data = sim_data["field"]

# Get field data for a specific frequency.
field_freq = field_data.sel(f=200e14)

# Get field data for a specific position and frequency.
field_pos_freq = field_data.sel(z=0, f=200e14)

```

You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.
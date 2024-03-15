# How do I get the raw monitor data values as a numpy array?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 15:40:09 | Data Visualization and Postprocessing |


The simulation data is stored as a [DataArray](https://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) object using the [xarray](https://xarray.pydata.org/en/stable/) package. You can think of it as a dataset where data is stored as a large multi-dimensional array (like a `numpy` array) and the coordinates along each of the dimensions are specified, so it is easy to work with.

The example below shows how to get the raw monitor data as `numpy` arrays.



```python

# Run the simulation and get the data.
sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)

# Get all the data from a flux monitor.
flux_data = sim_data["flux_monitor"]

# Get the flux values as numpy arrays.
print(f"Shape of flux dataset = {flux_data.shape}\n.")
print(f"Frequencies in dataset = {flux_data.coords.values} \n.")
print(f"Flux values in dataset = {flux_data.values}\n.")

```

You can find detailed information about simulation data visualization and postprocessing in this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/VizData/">tutorial</a>.
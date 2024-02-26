# How do I access the data of a specific monitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-18 23:02:06 | Data Visualization and Postprocessing |


You can access the data of a specific monitor by its name. For instance, supposing you have a field monitor and set its name to "field", after running the simulation you can refer to this name to get the monitor's data. 



```python

sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)
field_data = sim_data["field"]

```

 
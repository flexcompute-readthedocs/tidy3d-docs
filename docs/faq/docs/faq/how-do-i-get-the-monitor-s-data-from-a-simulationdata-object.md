# How do I  get the monitor's data from a SimulationData object?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 13:12:20 | Data Visualization and Postprocessing |


To get the data of a particular monitor, you can use its name. For example, if you have a field monitor and have given it the name "field", you can refer to this name to retrieve the monitor's data after the simulation is run.



```python

sim_data = tidy3d.web.run(simulation, task_name="task", path="data/data.hdf5", verbose=True)
field_data = sim_data["field"]

```

 
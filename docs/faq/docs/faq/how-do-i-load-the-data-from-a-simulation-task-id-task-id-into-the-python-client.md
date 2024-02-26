# How do I load the data from a simulation task ID into the Python client?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 20:17:10 | Simulations |


After the simulation is complete, you can load the results into a [SimulationData](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData) object by its `task_id` using:



```python

sim_data = web.load(task_id, path="outt/sim.hdf5", verbose=verbose)

```



The [web.load()](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.web.api.webapi.load.html) method is very convenient to load and postprocess results from simulations created using [Tidy3D GUI](https://tidy3d.simulation.cloud/v).

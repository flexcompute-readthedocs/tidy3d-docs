# How do I load the results of a simulation?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 14:29:16 | Simulations |


After the simulation is complete, you can load the results into a [SimulationData](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData) object by its `task_id` using:



```python

sim_data = web.load(task_id, path="outt/sim.hdf5", verbose=verbose)

```



The [web.load()](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.web.load.html) method is very convenient to load and postprocess results from simulations created using [Tidy3D GUI](https://tidy3d.simulation.cloud/v).

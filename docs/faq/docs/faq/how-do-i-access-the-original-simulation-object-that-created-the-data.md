# How do I access the original Simulation object that created the data?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 20:22:51 | Simulations |


To access the original [Simulation](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Simulation.html) object that created the simulation data you can use 



```python

# Run the simulation.
sim_data = web.run(simulation, task_name='task_name', path='out/sim.hdf5')

# Get a copy of the original simulation object.
sim_copy = sim_data.simulation

```



to get a copy of the original simulation object.

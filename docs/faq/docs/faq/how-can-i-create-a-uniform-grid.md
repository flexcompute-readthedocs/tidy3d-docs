# How can I create a uniform grid?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 18:47:30 | Grid Specification |


The most standard way to define a simulation is to use a constant grid size in each of the three directions. This can be achieved simply using `tidy3d.GridSpec.uniform(dl=...)` as shown below.



```python

# Setting a uniform grid size of 0.02 microns.
sim_uniform = tidy3d.Simulation(
    size=(5, 5, 5),
    grid_spec=tidy3d.GridSpec.uniform(dl=0.02),
    medium=tidy3d.Medium(permittivity=4),
    structures=[structure],
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=td.PML())
    run_time=1e-12,
)

```


# How do I set the perfect matched layer (PML) boundary condition?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 14:48:15 | Boundary Conditions |


You should use [tidy3d.PML](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PML.html#tidy3d.PML) boundary condition to enclose the simulation domain with layers of a special lossy material designed to absorb incoming waves from all angles with minimal reflection. Tidy3D uses PML boundary conditions by default, but you can also set the boundaries explicitly using the `all_sides()` method. For example:



```python

# Define PML boundary conditions in all sides.
bspec = tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PML())

# Alternatively, you can apply the boundary at specific directions.
# bspec = tidy3d.BoundarySpec.pml(x=True, y=True)

# Build the simulation.
sim = tidy3d.Simulation(
    center=(0, 0, 0),
    size=(10, 4, 4),
    boundary_spec=bspec,
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[waveguide],
    sources=[mode_source],
    monitors=[mode_monitor],
    run_time=1e-12,
)

```



See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
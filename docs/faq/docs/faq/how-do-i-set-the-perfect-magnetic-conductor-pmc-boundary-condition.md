# How do I set the perfect magnetic conductor (PMC) boundary condition?

| Date       | Category    |
|------------|-------------|
| 2023-12-14 20:30:51 | Boundary Conditions |


You should use [tidy3d.PMCBoundary](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PMCBoundary.html#tidy3d.PMCBoundary) to enclose the simulation domain using perfect magnetic conductors. For example:



```python

# Define PML boundary conditions in all sides.
bspec = tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PMCBoundary())

# Alternatively, you can apply the boundary at specific directions.
# bspec = tidy3d.BoundarySpec.pmc(x=True, y=True)

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
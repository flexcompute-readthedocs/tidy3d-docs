# How do I specify different boundary conditions on each simulation domain edge?

| Date       | Category    |
|------------|-------------|
| 2023-12-15 21:23:27 | Boundary Conditions |


Use <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.BoundarySpec.html#tidy3d.BoundarySpec">tidy3d.BoundarySpec</a> to specify different boundary conditions to simulation edges. For example: 

```python

# Definition different boundary conditions.
bspec = tidy3d.BoundarySpec(
    x=tidy3d.Boundary(minus=tidy3d.PECBoundary(), plus=tidy3d.PECBoundary()),
    y=tidy3d.Boundary(minus=tidy3d.Periodic(), plus=tidy3d.Periodic()),
    z=tidy3d.Boundary(minus=tidy3d.PML(), plus=tidy3d.PMCBoundary()),
)

# Build the simulation.
sim = tidy3d.Simulation(
    center=(0, 0, 0),
    size=(2, 2, 10),
    boundary_spec=bspec,
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[unit_cell],
    sources=[plane_wave],
    monitors=[flux_monitor],
    run_time=1e-12,
)

```



See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
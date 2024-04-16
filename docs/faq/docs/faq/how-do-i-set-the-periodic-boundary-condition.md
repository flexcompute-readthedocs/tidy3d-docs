# How do I set the periodic boundary condition?

| Date       | Category    |
|------------|-------------|
| 2023-12-14 22:07:57 | Boundary Conditions |


The <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a> boundary condition allows users to obtain the response of large periodic structures by simulating only a unit cell. The example below illustrates how to set up boundary conditions in a typical case, where we have a unit cell and need to include periodic boundaries in two directions and PML in the perpendicular direction. 

```python

# Definition of periodic boundary condition in the x and y directions.
# PML in the z-direction.
bspec = tidy3d.BoundarySpec(
    x=tidy3d.Boundary(minus=tidy3d.Periodic(), plus=tidy3d.Periodic()),
    y=tidy3d.Boundary(minus=tidy3d.Periodic(), plus=tidy3d.Periodic()),
    z=tidy3d.Boundary(minus=tidy3d.PML(), plus=tidy3d.PML()),
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

<h5>Details about the periodic boundary condition </h5>Floquet's (or Bloch's) theorem describes electromagnetic fields interacting with periodic structures. Considering the fields $\vec{E}$ and $\vec{H}$ propagating in the <code>x</code>-direction along a periodic structure  with period $L_x$, they must satisfy: $\vec{E}(x+L_x, y, z)=\vec{E}(x, y, z)e^{-jk_x L_x}$ and $\vec{H}(x+L_x, y, z)=\vec{H}(x, y, z)e^{jk_x L_x}$, where $k_x$ is the light wave vector in the <code>x</code>-direction. Note that when using periodic boundary conditions, both structures and fields must exhibit periodicity. Therefore, it is important to include the sources correctly. If the source is injected at an angle, use <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> instead. 

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
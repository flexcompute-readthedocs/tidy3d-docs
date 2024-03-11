# How do I set the Bloch boundary condition?

| Date       | Category    |
|------------|-------------|
| 2023-12-15 20:23:55 | Boundary Conditions |


The <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> boundary condition allows users to obtain the response of large periodic structures by simulating only a unit cell. It is suitable to simulate systems where the source is injected at an angle, so the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a> boundary fails. The example below illustrates how to set up the Bloch boundary condition in a typical case, where we have a unit cell and a plane wave source injected at an angle. 

```python

# Simulation size.
sim_size = (2, 2, 8)

# Plane wave source at an angle.
plane_wave = tidy3d.PlaneWave(
    center=(0, 0, 3),
    size=(tidy3d.inf, tidy3d.inf, 0),
    source_time=source_time,
    direction="-",
    pol_angle=0,
    angle_theta=np.pi / 3.0,
    angle_phi=np.pi / 6.0,
)

# Bloch boundaries.
bloch_x = tidy3d.Boundary.bloch_from_source(
  source=plane_wave,
  domain_size=sim_size[0],
  axis=0,
  medium=medium
)

bloch_y = tidy3d.Boundary.bloch_from_source(
  source=plane_wave,
  domain_size=sim_size[1],
  axis=1,
  medium=medium
)

bspec = tidy3d.BoundarySpec(x=bloch_x, y=bloch_y, z=tidy3d.Boundary.pml())

# Build the simulation.
sim = tidy3d.Simulation(
    center=(0, 0, 0),
    size=sim_size,
    boundary_spec=bspec,
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[unit_cell],
    sources=[plane_wave],
    monitors=[flux_monitor],
    run_time=1e-12,
)

```

Use the convinience method <code>.bloch_from_source()</code> to automatically calculate the Bloch vector based on <code>source</code>, background <code>medium</code>, <code>axis</code>, and <code>domain_size</code> information. The <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> is a generalization of the periodic boundary condition to any incidence angle. However, it is computationally more expensive, so use <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a> boundary to normal incidence. 

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
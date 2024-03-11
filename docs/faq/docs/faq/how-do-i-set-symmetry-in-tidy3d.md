# How do I set symmetry in Tidy3D?

| Date       | Category    |
|------------|-------------|
| 2023-12-15 16:19:59 | Symmetry |


To configure symmetry in your simulation, assign a tuple of integers to the symmetry parameter. This tuple defines the reflection symmetry across planes bisecting the simulation domain normal to the x-, y-, and z-axes. Each element of the tuple can be set to 0 for no symmetry, 1 for even symmetry (equivalent to 'PMC' symmetry), or -1 for odd symmetry (equivalent to 'PEC' symmetry). For example,



```python

# Define the symmetry tuple
symmetry_tuple = (0, 1, -1)

# Build the simulation.
sim = td.Simulation(
    center=(0, 0, 0),
    size=(10, 4, 4),
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=td.PML()),
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[waveguide],
    sources=[mode_source],
    monitors=[mode_monitor],
    run_time=1e-12,
    symmetry=symmetry_tuple,
)

```



It is crucial to consider the vectorial nature of the electromagnetic fields when determining the appropriate symmetry value. For a more extensive discussion on symmetry, please visit the dedicated [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/Symmetry/).
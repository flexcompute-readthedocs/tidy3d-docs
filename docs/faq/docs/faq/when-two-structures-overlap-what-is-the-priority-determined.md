# When two structures overlap, what is the priority determined?

| Date       | Category    |
|------------|-------------|
| 2023-12-06 22:52:18 | Structures |



When two structures overlap, the last ones in the `structures` list will override the permittivities of the previous structures. This [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/OptimizedL3/) illustrates how to use this rule to create a photonic crystal slab. The `holes` geometry with a refractive index of 1 overrides the `slab` permittivities in regions where they overlap, creating the air holes.



```python

# Simulation
sim = td.Simulation(
    size=sim_size,
    grid_spec=grid_spec,
    structures=[slab, holes],
    sources=[source],
    monitors=[time_series_mnt, field_mnt, far_field_mnt],
    run_time=run_time,
    boundary_spec=td.BoundarySpec.all_sides(boundary=td.PML()),
    symmetry=(1, -1, 1),
    shutoff=0,
)

```


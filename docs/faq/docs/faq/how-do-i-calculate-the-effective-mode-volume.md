# How do I calculate the effective mode volume?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 19:27:35 | Resonance Finder |


To calculate the effective mode volume, you should include a [tidy3d.FieldMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldMonitor.html) to record the electromagnetic fields within a box enclosing the cavity resonance. After running the simulation, you can follow this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/CavityFOM/) to obtain the effective mode volume.
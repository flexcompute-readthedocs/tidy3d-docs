# How do I export the final inverse design structure to GDS?

| Date       | Category    |
|------------|-------------|
| 2023-12-21 23:19:25 | Inverse Design |


After performing adjoint inverse designs using the <code>adjoint</code> plugin, you can export the final structure to <code>GDS</code> files using the function <code>.to_gds_file()</code>.

```python
from tidy3d.plugins.adjoint.utils.penalty import RadiusPenalty

# Convert the final adjoint simulation to a regular one.
sim_final = sim_adj.to_simulation()[0]

# Export the final simulation to GDS.
sim_final.to_gds_file(fname="inverse_design.gds", z=0, permittivity_threshold=6, frequency=200e14)

```

 

 

 
# How do I include fabrication constraints in adjoint shape optimization?

| Date       | Category    |
|------------|-------------|
| 2023-12-21 22:49:03 | Inverse Design |


To ensure reliable fabrication of a device, it is crucial to avoid using feature sizes below a certain radius of curvature when performing inverse design. To achieve this, you can use a penalty function that estimates the radius of curvature around each boundary vertex and applies a substantial penalty to the objective function if the value falls below the minimum radius. The code <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin5BoundaryGradients/">example</a> below demonstrates how to use the  <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.adjoint.utils.penalty.RadiusPenalty.html">tidy3d.plugins.adjoint.utils.penalty.RadiusPenalty</a> function.

```python
from tidy3d.plugins.adjoint.utils.penalty import RadiusPenalty

penalty = RadiusPenalty(min_radius=.150, alpha=1.0, kappa=10.0)
vertices0 = jnp.array(make_taper(ys0).vertices)
penalty_value = penalty.evaluate(vertices0)

```

 

 

 
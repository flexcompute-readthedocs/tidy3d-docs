# How do I simulate periodic structures in Tidy3D?

| Date       | Category    |
|------------|-------------|
| 2023-12-15 21:48:06 | Boundary Conditions |


You can use the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a> or <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> conditions to simulate periodic structures. These boundary conditions allow users to obtain the response of large periodic structures by simulating only a unit cell. The <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> allows to simulate systems where light is injected at an angle. However, it is computationally more expensive, so use <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a> boundary to normal incidence. 

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
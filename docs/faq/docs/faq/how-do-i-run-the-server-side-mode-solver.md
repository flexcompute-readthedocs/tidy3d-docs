# How do I run the server-side mode solver?

| Date       | Category    |
|------------|-------------|
| 2023-12-18 17:33:17 | Mode Solver |


The following example shows how to create a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a> object to perform optical mode analysis and obtain information such as mode effective index (real and imaginary parts), group index, effective area, polarization fraction, and field distribution.

 



```python
from tidy3d.plugins.mode import ModeSolver
from tidy3d.plugins.mode.web import run as run_mode_solver

# Build the mode solver.
freq0 = tidy3d.C_0 / 1.55
mode_solver = ModeSolver(
  simulation=sim,
  plane=plane,
  mode_spec=mode_spec,
  freqs=[freq0],
)

# Run the server-side mode solver.
mode_data = run_mode_solver(mode_solver)

```

To build the mode solver you need to create a simulation object and a plane where you want to calculate the modes, as well as specify the mode characteristics and frequencies of interest. The results are returned in a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolverData.html#tidy3d.plugins.mode.ModeSolverData">ModeSolverData</a> object. For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.
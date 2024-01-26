# What are the differences between running the server-side and the local mode solver?

| Date       | Category    |
|------------|-------------|
| 2023-12-18 17:45:50 | Mode Solver |


The server-side <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a> includes  group index calculation and subpixel-smoothing to improve solver accuracy.  For example:

 



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



When using the local version, the solver will run on your own computer and will not require any credits. You can run the local mode solver version using:

```python
from tidy3d.plugins.mode import ModeSolver

# Build the mode solver.
freq0 = tidy3d.C_0 / 1.55
mode_solver = ModeSolver(
  simulation=sim,
  plane=plane,
  mode_spec=mode_spec,
  freqs=[freq0],
)

# Run the local mode solver version.
mode_data = mode_solver.solve()

```

In both cases, the results are returned in a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolverData.html#tidy3d.plugins.mode.ModeSolverData">ModeSolverData</a> object. For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.
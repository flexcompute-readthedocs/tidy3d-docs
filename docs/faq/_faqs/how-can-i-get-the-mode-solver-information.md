---
_schema: default
title: How can I get the mode solver information?
date: 2023-12-18 21:23:43
enabled: true
category: Mode Solver
_inputs:
  title:
    type: text
    label: QUESTION TITLE
  enabled:
    type: switch
    hidden: true
  date:
    type: datetime
    label: DATE
    instance_value: NOW
  category:
    type: select
    options:
      values: data.faq_categories
      value_key: key
      preview:
        text:
          - key: category_name
---
<div>Using the Tidy3D <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a> you can perform optical mode analysis and obtain information such as mode effective index (real and imaginary parts), group index, effective area, polarization fraction, and field distribution. The results are returned within a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolverData.html#tidy3d.plugins.mode.ModeSolverData">ModeSolverData</a> object. In the following example, we illustrate how to obtain the information of the first four waveguide modes. We have considered a 500 x 220 nm silicon-on-insulator (SOI) waveguide operating at 1.55 $\mu$m.</div>

<div> </div>

<div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.mode import ModeSolver
from tidy3d.plugins.mode.web import run as run_mode_solver

# Define the waveguide.
waveguide = tidy3d.Structure(
    geometry=tidy3d.Box(size=(tidy3d.inf, 0.5, 0.22)),
    medium=tidy3d.Medium(permittivity=3.47**2),
)

# Build a simulation object including the waveguide.
sim = tidy3d.Simulation(
    size=(10, 2.5, 1.5),
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[waveguide],
    run_time=1e-12,
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PML()),
)

# Plane where we want to solve the modes.
plane = tidy3d.Box(center=(0, 0, 0), size=(0, 2.5, 1.5))

# Mode specification.
mode_spec = tidy3d.ModeSpec(
  num_modes=4,
  target_neff=3.47,
  group_index_step=True,
)

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

# Print out the results.
mode_data.to_dataframe()

{% endhighlight %}
{% include copy-button.html %}</div>

<div><p>For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.</p></div>
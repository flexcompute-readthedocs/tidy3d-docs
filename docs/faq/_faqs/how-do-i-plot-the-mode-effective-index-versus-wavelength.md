---
_schema: default
title: How do I plot the mode effective index versus wavelength?
date: 2023-12-18 21:43:47
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
<div>To plot the effective index of the optical modes calculated using the Tidy3D <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a>, you can follow the example below. We have considered a 500 x 220 nm silicon-on-insulator (SOI) waveguide operating between 1.5 and 1.6 $\mu$m.</div>

<div> </div>

<div markdown class="code-snippet">{% highlight python %}
import numpy as np
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
wvl = np.linspace(1.5, 1.6, 51)
freqs = tidy3d.C_0 / wvl
mode_solver = ModeSolver(
  simulation=sim,
  plane=plane,
  mode_spec=mode_spec,
  freqs=freqs,
)

# Run the server-side mode solver.
mode_data = run_mode_solver(mode_solver)

# Plot the mode effective index.
n_eff = mode_data.n_eff.values.squeeze()
fig, ax = plt.subplots(1, 1, figsize=(6, 4), tight_layout=True)

for mid in range(mode_spec.num_modes):
    ax.plot(wvl, n_eff[:, mid], label=(f"mode {mid}"))

{% endhighlight %}
{% include copy-button.html %}</div>

<div><p>For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.</p></div>
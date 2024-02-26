---
_schema: default
title: How do I set the mode polarization?
date: 2023-12-18 22:25:04
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
<div>After running the Tidy3D&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a>, the results are returned within a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.mode.ModeSolverData.html#tidy3d.plugins.mode.ModeSolverData">ModeSolverData</a> object. The solver always computes the&nbsp;<code>num_modes</code>&nbsp;modes closest to the given&nbsp;<code>target_neff</code>. If&nbsp;<code>filter_pol==None</code>, they are simply sorted in order of decresing effective index. If a polarization filter is selected, the modes are rearranged such that the first&nbsp;<code>n_pol</code>&nbsp;modes in the list are the ones with the selected polarization fraction larger than or equal to 0.5, while the next&nbsp;<code>num_modes - n_pol</code>&nbsp;modes are the ones where it is smaller than 0.5 (i.e. the opposite polarization fraction is larger than 0.5). The modes are still ordered within each polarization subset by decreasing effective index.</div>

<div> </div>

<div>The example below shows how to set the mode solver to return the TE modes first in the mode list.</div>

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
  filter_pol='te',
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

# Get the mode polarization fraction.
print("TE polarization fraction:")
print(np.asarray(mode_data.pol_fraction['te']).squeeze())

{% endhighlight %}
{% include copy-button.html %}</div>

<div> </div>
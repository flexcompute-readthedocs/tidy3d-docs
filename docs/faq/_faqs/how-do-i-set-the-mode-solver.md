---
_schema: default
title: How do I set the mode solver?
date: 2023-12-18 11:05:43
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
<div>Use the Tidy3D <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a> to perform optical mode analysis and obtain information such as mode effective index (real and imaginary parts), group index, effective area, polarization fraction, and field distribution. To illustrate how to set up a mode solver, let's consider the case of a silicon-on-insulator (SOI) waveguide operating at 1.55 $\mu$m.</div>

<div> </div>

<div markdown class="code-snippet">{% highlight python %}

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

{% endhighlight %}
{% include copy-button.html %}</div>

<div><p>You can use a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Box.html#tidy3d.Box">Box</a> object to define the plane where you want to solve the modes. We use a plane perpendicular to the waveguide propagation axis in this example. Symmetries are applied if they are defined in the simulation and the mode plane center sits on the simulation center. Then, use the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSpec.html#tidy3d.ModeSpec">tidy3d.ModeSpec</a>&nbsp;object to specify the number of modes (<code>num_modes</code>), the initial effective index guess (<code>target_neff</code>), polarization, and other characteristics of the modes you are looking for. Make&nbsp;<code>group_index_step=True</code> to enable mode group index calculation.</p><div markdown class="code-snippet">{% highlight python %}

# Plane we want to solve the modes.
plane = tidy3d.Box(center=(0, 0, 0), size=(0, 2.5, 1.5))

# Mode specification.
mode_spec = tidy3d.ModeSpec(
  num_modes=4,
  target_neff=3.47,
  group_index_step=True,
)

{% endhighlight %}
{% include copy-button.html %}</div><p>Now you can create and execute the mode solver, which returns the results in a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.mode.ModeSolverData.html#tidy3d.plugins.mode.ModeSolverData">ModeSolverData</a> object. For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.</p><div markdown class="code-snippet">{% highlight python %}
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

{% endhighlight %}
{% include copy-button.html %}</div><p>If you prefer, you can run the local version of mode solver through the code <code>mode_data=mode_solver.solve()</code>. This means that the solver will run on your own computer and will not require any credits. However, it's important to note that the local version will not include the group index calculation or subpixel-smoothing, even if these options are specified in the simulation. As a result, the local version's results will not perfectly match the server-side ones.</p></div>
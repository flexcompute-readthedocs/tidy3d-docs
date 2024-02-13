---
_schema: default
title: How do I run the server-side mode solver?
date: 2023-12-18 17:33:17
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
<div>The following example shows how to create a&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a>&nbsp;object to perform optical mode analysis and obtain information such as mode effective index (real and imaginary parts), group index, effective area, polarization fraction, and field distribution.</div>

<div> </div>

<div><div markdown class="code-snippet">{% highlight python %}
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
{% include copy-button.html %}</div><p>To build the mode solver you need to create a simulation object and a plane where you want to calculate the modes, as well as specify the mode characteristics and frequencies of interest. The results are returned in a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.mode.ModeSolverData.html#tidy3d.plugins.mode.ModeSolverData">ModeSolverData</a> object. For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.</p></div>
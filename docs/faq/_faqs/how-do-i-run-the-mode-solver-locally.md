---
_schema: default
title: How do I run the mode solver locally?
date: 2023-12-18 17:27:21
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
<div>You can run the local version of <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.mode.ModeSolver.html#tidy3d.plugins.mode.ModeSolver">mode solver</a> through the&nbsp;<code>.solve()</code>&nbsp;method. For example:</div>

<div> </div>

<div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.mode import ModeSolver

# Build the mode solver.
freq0 = tidy3d.C_0 / 1.55
mode_solver = ModeSolver(
  simulation=sim,
  plane=plane,
  mode_spec=mode_spec,
  freqs=[freq0],
)

# Run the local mode solver.
mode_data = mode_solver.solve()

{% endhighlight %}
{% include copy-button.html %}</div>

<div>This means that the solver will run on your own computer and will not require any credits. However, it's important to note that the local version will not include the group index calculation or subpixel-smoothing, even if these options are specified in the simulation. As a result, the local version's results will not perfectly match the server-side ones.&nbsp;<span>For more details on how to set up, run and visualize the solver results, please refer to this </span><a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a><span>.</span></div>
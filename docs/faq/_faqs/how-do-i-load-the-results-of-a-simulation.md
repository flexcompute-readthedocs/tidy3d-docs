---
title: How do I load the results of a simulation?
date: 2023-12-03 14:29:16
enabled: true
category: "Simulations"
---
After the simulation is complete, you can load the results into a&nbsp;[SimulationData](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData)&nbsp;object by its `task_id` using:

<div markdown class="code-snippet">{% highlight python %}

sim_data = web.load(task_id, path="outt/sim.hdf5", verbose=verbose)

{% endhighlight %}
{% include copy-button.html %}</div>

The [web.load()](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.web.load.html) method is very convenient to load and postprocess results from simulations created using [Tidy3D GUI](https://tidy3d.simulation.cloud/v).

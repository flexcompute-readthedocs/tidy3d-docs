---
title: How do I access the original Simulation object that created the data?
date: 2023-12-03 20:22:51
enabled: true
category: "Simulations"
---
To access the original [Simulation](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Simulation.html){: target="_blank" rel="noopener"} object that created the simulation data you can use&nbsp;

<div markdown class="code-snippet">{% highlight python %}

# Run the simulation.
sim_data = web.run(simulation, task_name='task_name', path='out/sim.hdf5')

# Get a copy of the original simulation object.
sim_copy = sim_data.simulation

{% endhighlight %}
{% include copy-button.html %}</div>

<div><div>to get a copy of the original simulation object.</div></div>

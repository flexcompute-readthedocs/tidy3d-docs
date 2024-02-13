---
title: "How do I loop through\_tidy3d.web.BatchData\_without loading all of the data into memory?"
date: 2023-12-04 20:01:52
enabled: true
category: "Parameter Sweep"
---
<div>After running the simulations, you can get the results from the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.web.BatchData.html#tidy3d.web.BatchData">tidy3d.web.BatchData</a>&nbsp;object directly, using for example &nbsp;<code>sim_data_1 = batch_results["sim_1"]</code>. Or iterating over it in a loop, as below:</div>

<div><div markdown class="code-snippet">{% highlight python %}

sim_data = []
for task_name, sim_data in batch_results.items():
  sim_data.append(sim_data)

{% endhighlight %}
{% include copy-button.html %}</div><p><span>So, you will get access to the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData">tidy3d.SimulationData</a> instances to perform your postprocessing.</span></p></div>

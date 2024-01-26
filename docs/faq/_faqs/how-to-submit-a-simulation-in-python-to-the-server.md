---
title: How to submit a simulation in Python to the server?
date: 2023-12-03 13:12:40
enabled: true
category: "Simulations"
---
<div>Submitting a simulation to our cloud server is very easily done by a simple web API call.</div>

<div><div markdown class="code-snippet">{% highlight python %}

sim_data = tidy3d.web.run(simulation, task_name='my_task', path='out/data.hdf5')

{% endhighlight %}
{% include copy-button.html %}</div></div>

<div>Alternatively, you can first define a job by</div>

<div><div markdown class="code-snippet">{% highlight python %}

job = tidy3d.web.Job(simulation, task_name)

{% endhighlight %}
{% include copy-button.html %}</div></div>

<div>Then submit the job by using the <code>run</code> method as</div>

<div><div markdown class="code-snippet">{% highlight python %}

sim_data = job.run(path)

{% endhighlight %}
{% include copy-button.html %}</div></div>

<div>After the simulation is complete, result data will be automatically returned to&nbsp;<code>sim_data</code>.</div>

<div> </div>

<div>See <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/notebooks/WebAPI.html">this</a> complete example on submitting simulations to the server.</div>

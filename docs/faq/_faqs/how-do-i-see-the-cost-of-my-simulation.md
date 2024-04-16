---
title: How do I see the cost of my simulation?
date: 2023-12-04 20:20:48
enabled: true
category: "Simulations"
---
To obtain the cost of a simulation, you can use the function `tidy3d.web.real_cost(task_id)`. In the example below, a job is created, and its cost is estimated. After running the simulation, the real cost can be obtained. It is important to note that the real cost may not be available immediately after the simulation is finished.

<div markdown class="code-snippet">{% highlight python %}
import time

# initializes job, puts task on server (but doesnt run it)
job = web.Job(simulation=sim, task_name="job", verbose=verbose)

# estimate the maximum cost
estimated_cost = web.estimate_cost(job.task_id)

print(f'The estimated maximum cost is {estimated_cost:.3f} Flex Credits.')

# Runs the simulation.
sim_data = job.run(path="data/sim_data.hdf5")

time.sleep(5)

# Get the billed FlexCredit cost after a simulation run.
cost = web.real_cost(job.task_id)

{% endhighlight %}
{% include copy-button.html %}</div>

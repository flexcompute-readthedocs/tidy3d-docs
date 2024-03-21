---
title: >-
  How do I load the results of a job that has already been finished without
  knowing the task ID?
date: 2023-12-03 20:42:45
enabled: true
category: "Simulations"
---
The `job` container has a convenient method to save and load the results of a job that has already finished without needing to know the&nbsp;`task_id`, as below:

<div markdown class="code-snippet">{% highlight python %}

# Saves the job metadata to a single file.
job.to_file("data/job.json")

# You can exit the session, break here, or continue in new session.

# Load the job metadata from file.
job_loaded = web.Job.from_file("data/job.json")

# Download the data from the server and load it into a SimulationData object.
sim_data = job_loaded.load(path="data/sim.hdf5")

{% endhighlight %}
{% include copy-button.html %}</div>

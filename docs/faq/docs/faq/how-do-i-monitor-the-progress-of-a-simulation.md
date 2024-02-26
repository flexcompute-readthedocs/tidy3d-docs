# How do I monitor the progress of a simulation?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 14:18:19 | Simulations |


The <code>web.run()</code> method shows the simulation progress by default.  When uploading a simulation to the server without running it, you can use the <code>web.monitor(task_id)</code>, <code>job.monitor()</code>, or <code>batch.monitor()</code> methods to display the progress of your simulation(s). You can find detailed information on submitting simulation to the server in <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/notebooks/WebAPI.html">this tutorial</a>.

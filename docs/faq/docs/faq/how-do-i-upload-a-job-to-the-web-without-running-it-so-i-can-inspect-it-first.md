# How do I upload a job to the web without running it so I can inspect it first?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 13:25:27 | Simulations |


Once you've created a <code>job</code> object using <code>tidy3d.web.Job</code>, you can upload it to our servers with <code>web<strong>.</strong>upload<strong>(</strong>simulation<strong>,</strong> task_name<strong>=</strong>"task_name"<strong>,</strong> verbose<strong>=</strong>verbose<strong>)</strong></code> and it will not run until you explicitly tell it to do so with <code>web.start(job.task_id)</code>. To monitor the simulation's progress and wait for its completion, use <code>web<strong>.</strong>monitor(job.task_id<strong>,</strong> verbose<strong>=</strong>verbose)</code>. After running the simulation, you can load the results using <code>sim_data = web<strong>.</strong>load(job.task_id<strong>, </strong>path=​​​​​"out/simulation.hdf5"<strong>,</strong> verbose<strong>=</strong>verbose)</code>. In <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/notebooks/WebAPI.html">this notebook</a>, you will find detailed information on how to run simulations using the web API.

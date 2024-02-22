# How to submit a simulation in Python to the server?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 13:12:40 | Simulations |


Submitting a simulation to our cloud server is very easily done by a simple web API call.



```python

sim_data = tidy3d.web.run(simulation, task_name='my_task', path='out/data.hdf5')

```



Alternatively, you can first define a job by



```python

job = tidy3d.web.Job(simulation, task_name)

```



Then submit the job by using the <code>run</code> method as



```python

sim_data = job.run(path)

```



After the simulation is complete, result data will be automatically returned to <code>sim_data</code>.

 

See <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/notebooks/WebAPI.html">this</a> complete example on submitting simulations to the server.

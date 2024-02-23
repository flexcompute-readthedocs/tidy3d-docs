# How do I estimate how many credits my simulation will take?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 14:38:36 | Simulations |


We can get the cost estimate of running the task before actually running it. This prevents us from accidentally running large jobs that we set up by mistake. The estimated cost is the maximum cost corresponding to running all the time steps. To do so, run  a code like below:



```python

# initializes job, puts task on server (but doesnt run it)
job = web.Job(simulation=sim, task_name="job", verbose=verbose)

# estimate the maximum cost
estimated_cost = web.estimate_cost(job.task_id)

print(f'The estimated maximum cost is {estimated_cost:.3f} Flex Credits.')

```



See [this notebook](https://docs.flexcompute.com/projects/tidy3d/en/latest/notebooks/WebAPI.html) to obtain other details about submitting simulations to the server.

# How do I loop through tidy3d.web.BatchData without loading all of the data into memory?

| Date       | Category    |
|------------|-------------|
| 2023-12-04 20:01:52 | Parameter Sweep |


After running the simulations, you can get the results from the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.web.BatchData.html#tidy3d.web.BatchData">tidy3d.web.BatchData</a> object directly, using for example  <code>sim_data_1 = batch_results["sim_1"]</code>. Or iterating over it in a loop, as below:



```python

sim_data = []
for task_name, sim_data in batch_results.items():
  sim_data.append(sim_data)

```

So, you will get access to the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData">tidy3d.SimulationData</a> instances to perform your postprocessing.

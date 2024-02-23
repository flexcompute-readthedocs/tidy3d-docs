# How do I submit multiple simulations?

| Date       | Category    |
|------------|-------------|
| 2023-12-04 14:46:02 | Parameter Sweep |


To submit multiple simulations and run them concurrently in the server, you can create a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.web.api.container.Batch.html">tidy3d.web.Batch</a> object including all the simulations you want to run. Then, use <code>tidy3d.web.Batch.run()</code> to upload, run, and get the simulations results in a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.web.api.container.BatchData.html">tidy3d.web.BatchData</a> object. For example:

```python

# Create a dictionary including all the simulations.
sims = {"sim_1": sim_1, "sim_2": sim_2, "sim_3": sim_3}

# Build a Batch object.
batch = tidy3d.web.Batch(simulations=sims, verbose=True)

# Run all the simulations and get the results.
batch_results = batch.run(path_dir="data")

```

Alternatively, you can use the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.web.api.asynchronous.run_async.html">tidy3d.web.run_async</a>, which submits and runs multiple simulations using only one command. 

```python

# Create a dictionary including all the simulations.
sims = {"sim_1": sim_1, "sim_2": sim_2, "sim_3": sim_3}

# Run all the simulations and get the results.
batch_results = batch.run_async(sims, path_dir="data")

```

After running the simulations, you can get the results from the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.web.api.container.BatchData.html">tidy3d.web.BatchData</a> object directly, using for example  <code>sim_data_1 = batch_results["sim_1"]</code>. Or iterating over it in a loop, as below:

```python

sim_data = []
for task_name, sim_data in batch_results.items():
  sim_data.append(sim_data)

```

In <a target="_blank" rel="noopener" href="https://www.flexcompute.com/tidy3d/examples/notebooks/ParameterScan/">this notebook</a>, you will find a detailed example of how to run parameter sweeps.
# How do I save or load a tidy3d.web.Batch so I can work with it later?

| Date       | Category    |
|------------|-------------|
| 2023-12-04 20:12:20 | Parameter Sweep |


Like most other Tidy3D objects, <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.web.Batch.html#tidy3d.web.Batch">tidy3d.web.Batch</a> instances have <code>to_file(path)</code> and <code>from_file(path)</code> methods that will export and load their metadata as JSON files.  This is especially useful for loading batches for long analysis after they have run. For example, one can save the batch information to file and load the batch at a later time, if needing to disconnect from the service while the jobs are running.

```python

# Save batch metadata.
batch.to_file("data/batch_data.json")

# Load batch metadata into a new batch.
loaded_batch = web.Batch.from_file("data/batch_data.json")

```

 

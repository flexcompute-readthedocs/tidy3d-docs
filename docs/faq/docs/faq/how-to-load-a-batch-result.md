# How to load a batch result?

| Date       | Category    |
|------------|-------------|
| 2023-12-04 18:41:54 | Parameter Sweep |


When a batch is created, a `batch.hdf5` file will be created automatically. Users can use this file to collect all the simulation results from the batch. First, load the `batch.hdf5` file by



```python

batch = web.Batch.from_file(“folder_name/batch.hdf5”)

```



Then download and load all simulations results into a BatchData object by



```python

batch_results = batch.load(path_dir=“data”)

```



Then you can further extract the result for each simulation from`batch_results`.


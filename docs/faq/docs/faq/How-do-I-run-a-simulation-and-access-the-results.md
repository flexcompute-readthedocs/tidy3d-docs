# How do I run a simulation and access the results?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 13:41:06 | Simulations |


Submitting and monitoring jobs and downloading the results are all done through our [web API](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/index.html#web-api). After a successful run, all data for all monitors can be downloaded in a single `.hdf5` file using `tidy3d.web.load()`, and the raw data can be loaded into a [SimulationData](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData) object.

From the [SimulationData](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData) object, one can grab and plot the data for each monitor with square bracket indexing, inspect the original [Simulation](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Simulation.html#tidy3d.Simulation) object, and view the log from the solver run. For more details, see [this beginer tutorial](/tidy3d/examples/notebooks/VizSimulation/) and [this advanced tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/XarrayTutorial/).

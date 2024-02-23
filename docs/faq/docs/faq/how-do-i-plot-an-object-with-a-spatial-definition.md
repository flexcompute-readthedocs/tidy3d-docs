# How do I plot an object with a spatial definition?

| Date       | Category    |
|------------|-------------|
| 2023-12-18 22:43:01 | Data Visualization and Postprocessing |


If you have an object which includes spatial definition such as <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Simulation.html">tidy3d.Simulation</a> or <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Structure.html">tidy3d.Structure</a>, using <code>obj.plot(x=0)</code> will plot the object on the <code>x=0</code> plane. Note that <code>y</code> and <code>z</code> are alternatively  accepted to specify other planar axes.  Include the <code>ax</code> argument to plot to an existing axis, ie. <code>obj.plot(y=0, ax=ax)</code>.
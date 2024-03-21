# How can I define a nonlinear material?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 20:35:00 | Mediums |


To create nonlinear material, you should specify a [tidy3d.NonlinearSusceptibility](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.NonlinearSusceptibility.html#tidy3d.NonlinearSusceptibility) to the `nonlinear_spec` parameter of any medium. For example:



```python

medium = tidy3d.Medium(permittivity=2, nonlinear_spec=tidy3d.NonlinearSusceptibility(chi3=1, numiters=5))

```



Where <code>chi3</code> is the nonlinear susceptibility, and <code>numiters</code> is the number of iterations for solving nonlinear constitutive relation. Se <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/BistablePCCavity/">this notebook</a> for an example on using material nonlinearity.

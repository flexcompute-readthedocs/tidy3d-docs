# Can I import my own tabulated material data?

| Date       | Category    |
|------------|-------------|
| 2023-12-04 19:01:40 | Mediums |



Yes, users can import their own tabulated material data and fit it using one of Tidy3D's dispersion fitting tools. The [FastDispersionFitter](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.dispersion.FastDispersionFitter.html) tool performs an optimization to find a medium defined as a dispersive PoleResidue model that minimizes the RMS error between the model results and the data. The user can provide data through one of the following methods:

* Numpy arrays directly by specifying `wvl_um`, `n_data`, and optionally `k_data`.
* A data file with the `from_file` utility function. The data file has columns for wavelength ($μm$), the real part of the refractive index ($n$), and the imaginary part of the refractive index ($k$). $k$ data is optional. Note: `from_file` uses `np.loadtxt` under the hood, so additional keyword arguments for parsing the file follow the same format as `np.loadtxt`.
* URL link to a CSV/TXT file that contains wavelength ($μm$), $n$, and optionally $k$ data with the `from_url` utility function. URL can come from [refractiveindex](https://refractiveindex.info/).

This [notebook](https://docs.flexcompute.com/projects/tidy3d/en/stable/notebooks/Fitting.html) provides detailed instructions and examples of using the fitter.

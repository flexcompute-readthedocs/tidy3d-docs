---
title: Can I import my own tabulated material data?
date: 2023-12-04 19:01:40
enabled: true
category: "Mediums"
---

Yes, users can import their own tabulated material data and fit it using one of Tidy3D's dispersion fitting tools. The [FastDispersionFitter](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.dispersion.FastDispersionFitter.html){: rel="nofollow"}&nbsp;tool performs an optimization to find a medium defined as a dispersive PoleResidue model that minimizes the RMS error between the model results and the data. The user can provide data through one of the following methods:

* Numpy arrays directly by specifying&nbsp;`wvl_um`,&nbsp;`n_data`, and optionally&nbsp;`k_data`.
* A data file with the&nbsp;`from_file`&nbsp;utility function. The data file has columns for wavelength ($μm$), the real part of the refractive index ($n$), and the imaginary part of the refractive index ($k$).&nbsp;$k$&nbsp;data is optional. Note:&nbsp;`from_file`&nbsp;uses&nbsp;`np.loadtxt`&nbsp;under the hood, so additional keyword arguments for parsing the file follow the same format as&nbsp;`np.loadtxt`.
* URL link to a CSV/TXT file that contains wavelength ($μm$),&nbsp;$n$, and optionally&nbsp;$k$&nbsp;data with the&nbsp;`from_url`&nbsp;utility function. URL can come from&nbsp;[refractiveindex](https://refractiveindex.info/){: rel="nofollow"}.

This&nbsp;[notebook](https://docs.flexcompute.com/projects/tidy3d/en/stable/notebooks/Fitting.html){: rel="nofollow"}&nbsp;provides detailed instructions and examples of using the fitter.

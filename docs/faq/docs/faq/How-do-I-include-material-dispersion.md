# How do I include material dispersion?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 16:28:59 | Mediums |


Dispersive materials are supported in Tidy3D and we provide an extensive [material library](https://docs.flexcompute.com/projects/tidy3d/en/latest/api.html#material-library) with pre-defined materials. Standard [dispersive material models](https://docs.flexcompute.com/projects/tidy3d/en/latest/api.html#dispersive-mediums) can also be defined. If you need help inputting a custom material, let us know!

It is important to keep in mind that dispersive materials are inevitably slower to simulate than their dispersion-less counterparts, with complexity increasing with the number of poles included in the dispersion model. For simulations with a narrow range of frequencies of interest, it may sometimes be faster to define the material through its real and imaginary refractive index at the center frequency. This can be done by defining directly a value for the real part of the relative permittivity $\mathrm{Re}(\epsilon_r)$ and electric conductivity $\sigma$ of a [Medium](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Medium.html#tidy3d.Medium), or through a real part $n$ and imaginary part $k$. The relationship between the two equivalent models is $\mathrm{Re}(\epsilon_r) = n^2 - k^2$, $\mathrm{Im}(\epsilon_r) = 2nk$, and $\sigma = 2 \pi f \epsilon_0 \mathrm{Im}(\epsilon_r)$.

In the case of (almost) lossless dielectrics, the dispersion could be negligible in a broad frequency window, but generally, it is importat to keep in mind that such a material definition is best suited for single-frequency results.

For lossless, weakly dispersive materials, the best way to incorporate the dispersion without doing complicated fits and without slowing the simulation down significantly is to provide the value of the refractive index dispersion $\mathrm{d}n/\mathrm{d}\lambda$ in [Sellmeier.from\_dispersion()](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Sellmeier.html#tidy3d.Sellmeier.from_dispersion). The value is assumed to be at the central frequency or wavelength (whichever is provided), and a one-pole model for the material is generated. These values are for example readily available from the [refractive index database](https://refractiveindex.info/).

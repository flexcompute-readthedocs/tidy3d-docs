# What are the units used in the simulation?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 14:48:15 | Simulations |


We generally assume the following physical units in component definitions:

> * Length: micron (μm, $10^{-6}$​​​ meters)
> * Time: Second ($s$)
> * Frequency: Hertz ($Hz$)
> * Electric conductivity: Siemens per micron ($S/μm$)

Thus, the user should be careful, for example, to use the speed of light in μm/s when converting between wavelength and frequency. The built-in speed of light [C\_0](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.C_0.html#tidy3d.C_0) has a unit of μm/s.

For example:



```python

wavelength_um = 1.55
freq_Hz = td.C_0 / wavelength_um
wavelength_um = td.C_0 / freq_Hz

```





Currently, only linear evolution is supported, and so the output fields have an arbitrary normalization proportional to the amplitude of the current sources, which is also in arbitrary units. In the API Reference, the units are explicitly stated where applicable.

Output quantities are also returned in physical units, with the same base units as above. For time-domain outputs as well as frequency-domain outputs when the source spectrum is normalized out (default), the following units are used:

> * Electric field: Volt per micron ($V/μm$)
> * Magnetic field: Ampere per micron ($A/μm$)
> * Flux: Watt ($W$)
> * Poynting vector: Watt per micron squared ($W/μm^{2}$​​​​​)
> * Modal amplitude: Square root of watt ($W^{1/2}$​​​​​)

If the source normalization is not applied, the electric field, magnetic field, and modal amplitudes are divided by Hz, while the flux and Poynting vector are divided by $Hz^{2}$.

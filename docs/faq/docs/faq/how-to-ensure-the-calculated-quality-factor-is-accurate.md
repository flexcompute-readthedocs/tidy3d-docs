# How to Ensure the Calculated Quality Factor is Accurate?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 18:51:02 | Resonance Finder |



To calculate low-quality factor resonances using Tidy3D you can build and run a simulation until the electromagnetic fields fully decay to negligible values within the simulation domain. Then, you can obtain the resonance quality factor from the spectral response obtained from frequency-domain monitors. In this case, it is crucial to ensure the fields have fully decayed by the end of the simulation to get an accurate spectral response.

When looking for long-lived resonances, the total time to the fields fully decay within the simulation domain can be extremely long. In this situation, the [tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html) plugin allows one to find resonances and extract information from time domain field monitors without the necessity of waiting for the fields to decay completely. To calculate accurate quality factors using the `ResonanceFinder` you should start the monitors after the source pulse has decayed.

In any case, a grid resolution convergence test is also essential to improve the results.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/ResonanceFinder/) for more details on the `ResonanceFinder` plugin.

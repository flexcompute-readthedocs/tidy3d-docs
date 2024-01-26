# How do I get resonance quality factors?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 18:51:02 | Resonance Finder |


To calculate low-quality factor resonances using Tidy3D you can build and run a simulation until the electromagnetic fields fully decay to negligible values within the simulation domain. Then, you can obtain the resonance quality factor from the spectral response obtained from frequency-domain monitors.

However, when looking for long-lived resonances, the total time to the fields fully decay within the simulation domain can be extremely long. In this situation, the [tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html) plugin allows one to find resonances and extract their information from time domain field monitors without the necessity of waiting for the fields to completely decay. The `ResonanceFinder` plugin needs [tidy3d.FieldTimeMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FieldTimeMonitor.html) to record the field as a function of time.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/ResonanceFinder/) for more details on the `ResonanceFinder` plugin.
# How do I calculate the Purcell factor?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 19:58:28 | Resonance Finder |


You can calculate the Purcell factor from the cavity quality factor and effective mode volume using [tidy3d.FieldMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FieldMonitor.html) and the [tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html) plugin, as detailed in this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/CavityFOM/).

Alternatively, you can calculate the Purcell factor as the ratio between the dipole power emitted in the final device and in the bulk semiconductor using [tidy3d.FluxMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FluxMonitor.html). Refer to this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/BullseyeCavityPSO/) for more details on this later approach.
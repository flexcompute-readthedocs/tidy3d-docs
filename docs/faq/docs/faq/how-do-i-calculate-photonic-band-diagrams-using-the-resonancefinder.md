# How do I calculate photonic band diagrams using the ResonanceFinder?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 19:13:49 | Resonance Finder |


To calculate photonic band diagrams using Tidy3D you can excite the structure with several [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PointDipole.html) sources and measure the response with several [tidy3d.FieldTimeMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldTimeMonitor.html) monitors. You should excite modes with a fixed Bloch wavevector by using [tidy3d.BlochBoundary](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html) boundary conditions. Then, use the [tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html) to find the resonant frequencies. By sweeping the Bloch wavevector, you can obtain the complete band structure of a photonic crystal structure.

This [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/Bandstructure/) shows a complete example of calculating a band diagram of a photonic crystal slab.
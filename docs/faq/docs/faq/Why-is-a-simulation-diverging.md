# Why is a simulation diverging?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 15:55:24 | Simulation Troubleshoot |


Sometimes, a simulation is numerically unstable and can result in
divergence. All known cases where this may happen are related to PML
boundaries and/or dispersive media. Below is a checklist of things to
consider.

-   For dispersive materials with $\epsilon_{\infty} < 1$, decrease the value of the Courant stability factor to below
    $\sqrt{\epsilon_{\infty}}$.
-   Move PML boundaries further away from structure interfaces inside the simulation domain, or from sources that may be injecting evanescent waves, like [PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PointDipole.html#tidy3d.PointDipole), [UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.UniformCurrentSource.html#tidy3d UniformCurrentSource), or [CustomFieldSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomFieldSource.html#tidy3d.CustomFieldSource).
-   Make sure structures are translationally invariant into the PML, or if not possible, use [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber) boundaries.
-   Remove dispersive materials extending into the PML, or if not possible, use [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber) boundaries.
-   If using our fitter to fit your own material data, ensure you are using the `plugins.StableDispersionFitter`.
-   If none of the above work, try using [StablePML](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.StablePML.html#tidy3d.StablePML) or [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber) boundaries anyway (note: these may introduce more reflections than in usual simulations with regular PML).


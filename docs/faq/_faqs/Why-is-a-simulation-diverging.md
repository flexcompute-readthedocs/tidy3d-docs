---
title: Why is a simulation diverging?
date: 2023-10-24 15:55:24
enabled: true
category: "Simulation Troubleshoot"
---
Sometimes, a simulation is numerically unstable and can result in
divergence. All known cases where this may happen are related to PML
boundaries and/or dispersive media. Below is a checklist of things to
consider.

-   For dispersive materials with $\epsilon_{\infty} < 1$, decrease the
    value of the Courant stability factor to below
    $\sqrt{\epsilon_{\infty}}$.
-   Move PML boundaries further away from structure interfaces inside
    the simulation domain, or from sources that may be injecting
    evanescent waves, like [PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PointDipole.html#tidy3d.PointDipole){: .color-primary-hover}, [UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.UniformCurrentSource.html#tidy3d.UniformCurrentSource){: .color-primary-hover}, or [CustomFieldSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomFieldSource.html#tidy3d.CustomFieldSource){: .color-primary-hover}.
-   Make sure structures are translationally invariant into the PML, or
    if not possible, use [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: .color-primary-hover}
    boundaries.
-   Remove dispersive materials extending into the PML, or if not
    possible, use [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: .color-primary-hover}
    boundaries.
-   If using our fitter to fit your own material data, make sure you are
    using the `plugins.StableDispersionFitter`{: .interpreted-text
    role="class"}.
-   If none of the above work, try using [StablePML](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.StablePML.html#tidy3d.StablePML){: .color-primary-hover} or [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: .color-primary-hover}
    boundaries anyway (note: these may introduce more reflections than
    in usual simulations with regular PML).


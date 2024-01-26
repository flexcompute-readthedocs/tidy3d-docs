# How do I calculate the power radiated by a PointDipole source?

| Date       | Category    |
|------------|-------------|
| 2023-12-08 11:40:56 | Sources |


The [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html) source is normalized such that the power injected in a homogeneous material of refractive index $n$ at frequency $\omega = 2\pi f$ is given by

$\frac{\omega^2}{12\pi}\frac{\mu_0 n}{c}$.​​​​​

To calculate the radiated power of a dipole in the presence of dispersive, lossy, or non-homogeneous materials, you can use a [tidy3d.FluxMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FluxMonitor.html) box. Refer to this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BullseyeCavityPSO/) for an example.
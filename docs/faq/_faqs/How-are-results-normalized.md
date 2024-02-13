---
_schema: default
title: How are results normalized?
date: 2023-10-24 15:21:50
enabled: true
category: Sources
_inputs:
  title:
    type: text
    label: QUESTION TITLE
  enabled:
    type: switch
    hidden: true
  date:
    type: datetime
    label: DATE
    instance_value: NOW
  category:
    type: select
    options:
      values: data.faq_categories
      value_key: key
      preview:
        text:
          - key: category_name
---
In many cases, Tidy3D simulations can be run and well-normalized results
can be obtained without normalizing/empty runs. This is because care is
taken internally to normalize the injected power, as well as the output
results, in a meaningful way. To understand this, there are two separate
normalizations that happen, outlined below. Both of those are discussed
with respect to frequency-domain results, as those are the most commonly
used.

## Source spectrum normalization

Every source has a spectrum associated to its particular time dependence
that is imprinted on the fields injected in the simulation. Usually,
this is somewhat arbitrary and it is most convenient for it to be taken
out of the frequency-domain results. By default, after a run, Tidy3D
normalizes all frequency-domain results by the spectrum of the first
source in the list of sources in the simulation. This choice can be
modified using the `Simulation.normalize_index`{: .interpreted-text
role="py:obj"} attribute, or normalization can be turned off by setting
that to `None`. Results can even be renoramlized after the simulation
run using [SimulationData.renormalize()](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData.renormalize){: .color-primary-hover}.
If multiple sources are used, but they all have the same time
dependence, the default normalization is still meaningful. However, if
different sources have a different time dependence, then it may not be
possible to obtain well-normalized results without a normalizing run.

This type of normalization is applied directly to the frequency-domain
results. The custom pulse amplitude and phase defined in
`SourceTime.amplitude`{: .interpreted-text role="py:obj"} and
`SourceTime.phase`{: .interpreted-text role="py:obj"}, respectively, are
**not** normalized out. This gives the user control over a (complex)
prefactor that can be applied to scale any source. Additionally, the
power injected by each type of source may have some special
normalization, as outlined below.

## Source power normalization

Source power normalization is applied depending on the source type. In
the cases where normalization is applied, the actual injected power may
differ slightly from what is described below due to finite grid effects.
The normalization should become exact with sufficiently high resolution.
That said, in most cases the error is negligible even at default
resolution.

The injected power values described below assume that the source
spectrum normalization has also been applied.

-   [PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PointDipole.html#tidy3d.PointDipole){: .color-primary-hover}: Normalization is
    such that the power injected by the source in a homogeneous material
    of refractive index $n$ at frequency $\omega = 2\pi f$ is given by

    $$\frac{\omega^2}{12\pi}\frac{\mu_0 n}{c}.$$

-   [UniformCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.UniformCurrentSource.html#tidy3d.UniformCurrentSource){: .color-primary-hover}: No extra
    normalization applied.

-   [CustomFieldSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.CustomFieldSource.html#tidy3d.CustomFieldSource){: .color-primary-hover}: No extra
    normalization applied.

-   [ModeSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.ModeSource.html#tidy3d.ModeSource){: .color-primary-hover},
    [PlaneWave](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PlaneWave.html#tidy3d.PlaneWave){: .color-primary-hover},
    [GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianBeam.html#tidy3d.GaussianBeam){: .color-primary-hover},
    [AstigmaticGaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.AstigmaticGaussianBeam.html#tidy3d.AstigmaticGaussianBeam){: .color-primary-hover}:
    Normalized to inject 1W power at every frequency. If supplied
    `SourceTime.num_freqs`{: .interpreted-text role="py:obj"} is `1`,
    this normalization is only exact at the central frequency of the
    associated [SourceTime](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.components.source.SourceTime.html#tidy3d.components.source.SourceTime){: .color-primary-hover} pulse, but
    should still be very close to 1W at nearby frequencies too.
    Increasing `num_freqs` can be used to make sure the normalization
    works well for a broadband source. The correct usage for a [PlaneWave](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PlaneWave.html#tidy3d.PlaneWave){: .color-primary-hover}
    source is to span the whole simulation domain for a simulation with
    periodic (or Bloch) boundaries, in which case the normalization of
    this technically infinite source is equivalent to 1W per unit cell.
    For the other sources which have a finite extent, the normalization
    is correct provided that the source profile decays by the boundaries
    of the source plane. Verifying that this is the case is always
    advised, as otherwise results may be spurious beyond just the
    normalization (numerical artifacts will be present at the source
    boundary).

-   `TFSFSource`{: .interpreted-text role="class"}: Normalized to inject
    $1W/μm^{2}$ in the direction of the source injection axis. This is
    convenient for computing scattering and absorption cross sections
    without the need for additional normalization. Note that for angled
    incidence, a factor of $1/\cos(\theta)$ needs to be applied to
    convert to the power carried by the plane wave in the propagation
    direction, which is at an angle $\theta$ with respect to the
    injection axis. Note also that when the source spans the entire
    simulation domain with periodic or Bloch boundaries, the conversion
    between the normalization of a `TFSFSource`{: .interpreted-text
    role="class"} and a [PlaneWave](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PlaneWave.html#tidy3d.PlaneWave){: .color-primary-hover} is
    just the area of the simulation domain in the plane normal to the
    injection axis.

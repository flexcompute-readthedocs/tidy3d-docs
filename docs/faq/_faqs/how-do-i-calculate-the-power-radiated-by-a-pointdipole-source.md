---
_schema: default
title: How do I calculate the power radiated by a PointDipole source?
date: 2023-12-08 11:40:56
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
The&nbsp;[tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PointDipole.html){: target="_blank" rel="noopener"} source is normalized such that the power injected in a homogeneous material of refractive index&nbsp;$n$ at frequency $\omega = 2\pi f$&nbsp;is given by

$\frac{\omega^2}{12\pi}\frac{\mu_0 n}{c}$.​​​​​

To calculate the radiated power of a dipole in the presence of dispersive, lossy, or non-homogeneous materials, you can use a [tidy3d.FluxMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FluxMonitor.html){: target="_blank" rel="noopener"} box. Refer to this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BullseyeCavityPSO/) for an example.
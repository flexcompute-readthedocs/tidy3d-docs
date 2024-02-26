---
_schema: default
title: How do I calculate photonic band diagrams using the ResonanceFinder?
date: 2023-12-20 19:13:49
enabled: true
category: Resonance Finder
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
To calculate photonic band diagrams using Tidy3D you can excite the structure with several [tidy3d.PointDipole](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PointDipole.html){: target="_blank" rel="noopener"} sources, and measure the response with several [tidy3d.FieldTimeMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldTimeMonitor.html){: target="_blank" rel="noopener"} monitors. You should excite modes with a fixed Bloch wavevector by using [tidy3d.BlochBoundary](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html){: target="_blank" rel="noopener"} boundary conditions. Then, use the [tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html){: target="_blank" rel="noopener"} to find the resonant frequencies. By sweeping the Bloch wavevector, you can obtain the full band structure of a photonic crystal structure.

This [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/Bandstructure/) shows a complete example on calculating a band diagram of a photonic crystal slab.
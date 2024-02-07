---
_schema: default
title: How do I calculate the Purcell factor?
date: 2023-12-20 19:58:28
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
You can calculate the Purcell factor from the cavity quality factor and effective mode volume using [tidy3d.FieldMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldMonitor.html){: target="_blank" rel="noopener"}&nbsp;and the&nbsp;[tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html){: target="_blank" rel="noopener"}&nbsp;plugin, as detailed in this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/CavityFOM/).

Alternatively, you can calculate the Purcell factor as the ratio between the dipole power emitted in the final device and in the bulk semiconductor using [tidy3d.FluxMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FluxMonitor.html). Refer to this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/BullseyeCavityPSO/) for more details on this later approach.
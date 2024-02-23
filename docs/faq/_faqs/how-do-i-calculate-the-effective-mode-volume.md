---
_schema: default
title: How do I calculate the effective mode volume?
date: 2023-12-20 19:27:35
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
To calculate the effective mode volume, you should include a [tidy3d.FieldMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldMonitor.html){: target="_blank" rel="noopener"}&nbsp;to record the electromagnetic fields within a box enclosing the cavity resonance. After running the simulation, you can follow this [example](https://www.flexcompute.com/tidy3d/examples/notebooks/CavityFOM/) to obtain the effective mode volume.
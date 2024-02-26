---
_schema: default
title: Why is it preferable to use symmetry whenever possible?
date: 2023-12-15 16:18:40
enabled: true
category: Symmetry
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
In many Tidy3D simulations, the application of field symmetries can markedly decrease computational time and FlexCredit cost, potentially achieving reductions by factors of 1/2, 1/4, or even 1/8. Therefore, we prefer to use symmetry whenever applicable. In addition, symmetry effectively filters out unwanted light polarizations or modes.

However, it is important to set up the symmetry correctly to avoid getting incorrect results. For a more extensive discussion on symmetry, please visit the dedicated [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/Symmetry/).
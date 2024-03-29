---
_schema: default
title: Does Tidy3D support continuous and discrete rotational symmetries?
date: 2023-12-15 16:25:04
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

At the moment, Tidy3D does not support continuous and discrete rotational symmetries. Only mirror symmetries are supported. For more information on using symmetry to significantly reduce simulation time and cost, please refer to the tutorial [Defining and using symmetries](https://www.flexcompute.com/tidy3d/examples/notebooks/Symmetry/) tutorial.

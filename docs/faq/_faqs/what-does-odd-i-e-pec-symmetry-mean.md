---
_schema: default
title: What does “odd, i.e. ‘PEC’ symmetry” mean?
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
PEC symmetry (odd) corresponds to zero tangential electric fields and zero normal magnetic fields at the symmetry plane.

![](./img/pec-1.png){: width="223" height="485"}
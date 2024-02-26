---
_schema: default
title: What does “even, i.e. ‘PMC’ symmetry” mean?
date: 2023-12-15 16:26:26
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
PMC symmetry (even) corresponds to zero tangential electric field and zero normal magnetic field at the symmetry plane.

![](./img/pmc-1.png){: width="229" height="482"}
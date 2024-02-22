---
_schema: default
title: What is the ideal distance between the geometry and absorbing layers?
date: 2023-12-15 21:35:25
enabled: true
category: Boundary Conditions
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
In Tidy3D, a warning will appear if the distance between a structure and the absorbing layers is smaller than half of a wavelength to prevent evanescent fields from leaking into PML. In most cases, the evanescent field will naturally die off within half a wavelength, but in some instances, a larger distance may be required. It is important to keep in mind that PML only absorbs propagating fields. For evanescent fields, PML can act as an amplification medium and cause a simulation to diverge.
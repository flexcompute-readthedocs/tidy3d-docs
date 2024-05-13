---
_schema: default
title: How do I create a dispersive material from model parameters?
date: 2023-12-05 19:26:45
enabled: true
category: Mediums
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
To create a dispersive material from model parameters, you only need to instantiate the medium object and provide its parameters. For example, `debye_medium = td.Debye(eps_inf=2.0, coeffs=[(1,2),(3,4)])`.

<div> </div>

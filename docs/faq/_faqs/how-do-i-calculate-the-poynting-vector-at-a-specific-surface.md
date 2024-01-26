---
_schema: default
title: How do I calculate the Poynting vector at a specific surface?
date: 2023-12-19 17:29:25
enabled: true
category: Monitors
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
The Poynting vector quantifies the directional energy flux of an electromagnetic field, representing the rate of energy transfer per unit area per unit time, and thus characterizing the power flow within the field.

The Poynting vector at a specific plane can be calculated by first placing a FieldMonitor object at that plane to obtain the fields. Then the Poynting vector can be calculated as&nbsp;$\boldsymbol{S} = \boldsymbol{E} \times \boldsymbol{H}$

For example, the z-component of the Poynting vector is calculated from&nbsp;$E_x$,&nbsp;$E_y$,$H_x$, and&nbsp;$H_y$&nbsp;as&nbsp;$S_z = (E_x H_y^* - E_y H_x^*)$. For time-averaged Poynting vector, we need to multiply by a factor of 0.5.
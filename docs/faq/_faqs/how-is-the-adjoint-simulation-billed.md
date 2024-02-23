---
_schema: default
title: How is the adjoint simulation billed?
date: 2023-12-21 21:19:39
enabled: true
category: Inverse Design
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
<div>Both the <code>forward</code> and the <code>adjoint</code> simulations are billed when running inverse design optimizations using the&nbsp;<code>adjoint</code>&nbsp;plugin. That represents a significant reduction in computation cost as the adjoint method allows one to calculate the gradient of an objective function with respect to thousands of design parameters in only two simulations.</div>

<div> </div>

<div>We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method. You can also go through this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin1Intro/">tutorial</a> for an introduction to the basic concepts related to automatic differentiation and adjoint optimization.</div>
---
_schema: default
title: What is adjoint simulation?
date: 2023-12-21 18:38:55
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
<div>The&nbsp;<code>adjoint</code>&nbsp;plugin allows users to take derivatives of arbitrary functions involving Tidy3D simulations through the use of the "adjoint method". The advantage of the adjoint method is that the gradients can be computed using only&nbsp;<strong>two</strong>&nbsp;FDTD simulations, the <code>forward</code> and the <code>adjoint</code> one, independent of the number of parameters. This makes it possible to do gradient-based optimization or sensitivity analysis of devices with enormous numbers of parameters with minimal computational overhead.&nbsp;</div>

<div> </div>

<div>We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method. You can also go through this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin1Intro/">tutorial</a> for an introduction to the basic concepts related to automatic differentiation and adjoint optimization.</div>
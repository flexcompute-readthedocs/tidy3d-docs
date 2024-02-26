---
_schema: default
title: How to install jax?
date: 2023-12-21 21:38:20
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
<div>The&nbsp;<code>adjoint</code>&nbsp;plugin requires the <a target="_blank" rel="noopener" href="https://jax.readthedocs.io/en/latest/index.html">jax</a> module, which is&nbsp;<a href="https://github.com/hips/autograd">Autograd</a>&nbsp;and&nbsp;<a href="https://www.tensorflow.org/xla">XLA</a>, brought together for high-performance numerical computing. We recommend running&nbsp;<code>pip install "tidy3d[jax]"</code>&nbsp;to install <code>jax</code>.</div>
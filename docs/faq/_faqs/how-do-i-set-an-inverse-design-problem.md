---
_schema: default
title: How do I set an adjoint inverse design simulation?
date: 2023-12-21 19:01:14
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
<div><p>To create an adjoint inverse design set up, you need to use a special&nbsp;<code>Simulation</code>&nbsp;subclass called&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxSimulation.html#tidy3d.plugins.adjoint.JaxSimulation">tidy3d.plugins.adjoint.JaxSimulation</a>, which is<span>&nbsp;a&nbsp;</span><code>jax</code><span>-compatible stand in for&nbsp;</span><code>Simulation</code><span>&nbsp;and behaves almost entirely the same, except for a few important differences:</span></p><ol><li>This feature allows for the inclusion of an extra field (<code>.input_structures</code>) consisting of&nbsp;<code>jax</code>-compatible Tidy3D structures. For example, the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxStructure.html#tidy3d.plugins.adjoint.JaxStructure">tidy3d.plugins.adjoint.JaxStructure</a>, which contains a&nbsp;<code>.medium</code>&nbsp;and a&nbsp;<code>.geometry</code>&nbsp;field, both of which may depend on the design parameters. The final gradients of the objective function will be given with respect to the values of the fields mentioned above.</li><li>It accepts the additional field <code>.output_monitors</code>, that defines the set of monitors and corresponding data that the objective function will depend on.</li></ol></div>

<div>Once the adjoint simulation is defined, you must use the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.web.run.html">tidy3d.plugins.adjoint.web.run</a>&nbsp;method to send the simulation set up to our servers. After computing the forward and adjoint simulations, a&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxSimulationData.html#tidy3d.plugins.adjoint.JaxSimulationData">tidy3d.plugins.adjoint.JaxSimulationData</a> is returned, so you can compute the objective function value.&nbsp;</div>

<div> </div>

<div>Lastly, use&nbsp;<code>jax.value_and_grad</code>&nbsp;to both compute the objective function&nbsp;<strong>and</strong>&nbsp;the gradient with respect to the design parameters. The objective function gradients can them feed a gradient-based optimization algorithm to drive the inverse design process.&nbsp;</div>

<div> </div>

<div>We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method. You can also go through this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin1Intro/">tutorial</a> for an introduction to the basic concepts related to automatic differentiation and adjoint optimization.</div>

<div> </div>

<div> </div>
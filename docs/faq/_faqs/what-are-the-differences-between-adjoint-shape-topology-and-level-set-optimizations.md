---
_schema: default
title: >-
  What are the differences between adjoint shape, topology, and level set
  optimizations?
date: 2023-12-21 20:21:23
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
<div>The&nbsp;<code>adjoint</code>&nbsp;plugin allows users to take derivatives of arbitrary functions involving Tidy3D simulations through the use of the "adjoint method". The advantage of the adjoint method is that the gradients can be computed using only two FDTD simulations, the <code>forward</code> and the <code>adjoint</code> one, independent of the number of parameters. This makes it possible to do gradient-based optimization or sensitivity analysis of devices with enormous numbers of parameters with minimal computational overhead.</div>

<div> </div>

<div>Currently, you can drive the structure changes to maximize device response using <strong>shape</strong>, <strong>topology</strong>, and <strong>level set</strong>-based optimizations.</div>

<div> </div>

<div>Shape optimization involves parameterizing specific structures such as boxes, cylinders, or polygons by using design parameters. This means that the device boundaries are determined by the values of the design parameters. While this approach leads to well-defined device boundaries, it is heavily reliant on the initial design geometry. See this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin5BoundaryGradients/">tutorial</a> for more details on shape optimization.</div>

<div> </div>

<div>In topology or density-based optimization methods, the permittivity values of each grid cell in a design area can be controlled by adjusting the design parameters. This means that the permittivity can vary between a minimum and a maximum value, allowing for greater flexibility in the final design. The use of projection filters can help to ensure that the final design is binary and does not contain intermediary permittivity values. This is a powerful approach that is less reliant on the initial geometry and can lead to interesting and unconventional designs. This <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin6GratingCoupler/">tutorial</a> presents a detailed explanation on topology optimization.</div>

<div> </div>

<div>The level set-based optimization method combines the characteristics of both shape and topology optimizations. In this method, the device boundaries are defined by the zero-contour level of a continuous function over the space, which is called the level set function. The topology of the level set surface is controlled by the design parameters, which then moves the device boundaries. This approach results in well-defined device boundaries, similar to the shape optimization approach, but it is less dependent on the initial device structure. See this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin10YBranchLevelSet/">tutorial</a> for more details on level set optimization.</div>

<div> </div>

<div>We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method.</div>
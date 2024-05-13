---
_schema: default
title: How do I create a time-domain field animation?
date: 2023-12-19 15:04:11
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
Animations are often created from FDTD simulations to provide a more intuitive understanding of the physical phenomena being modeled. These animations can visualize the evolution of the field distribution over time, showing wave propagation, interactions, and other dynamic effects that static images cannot adequately depict.&nbsp;

To create a time-domain field animation, we need to capture the frames at different time instances of the simulation. This can be done by using a&nbsp;[FieldTimeMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldTimeMonitor.html). Usually, an FDTD simulation contains a large number of time steps and grid points. Recording the field at every time step and grid point will result in a large dataset. For the purpose of making animations, this is usually unnecessary. In Tidy3D, we provide both spatial and temporal downsampling options to greatly reduce the animation data size.

Please refer to the detailed [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/AnimationTutorial/) on FDTD animation creation.
---
_schema: default
title: How do I simulate periodic structures in Tidy3D?
date: 2023-12-15 21:48:06
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
<div><div>You can use the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a>&nbsp;or <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a>&nbsp;conditions to simulate periodic structures. These boundary conditions allow users to obtain the response of large periodic structures by simulating only a unit cell. The&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> allows to simulate systems where light is injected at an angle. However, it is computationally more expensive, so use <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a>&nbsp;boundary to normal incidence.</div><div> </div></div>

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
---
_schema: default
title: Which types of boundary conditions are available in Tidy3D?
date: 2023-10-24 14:48:15
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
Tidy3D includes the following boundary condition types: [Periodic](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic){: target="_blank" rel="noopener"}, [PECBoundary](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PECBoundary.html#tidy3d.PECBoundary){: target="_blank" rel="noopener"}, [PMCBoundary](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PMCBoundary.html#tidy3d.PMCBoundary){: target="_blank" rel="noopener"}, [BlochBoundary](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary){: target="_blank" rel="noopener"}, [PML](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PML.html#tidy3d.PML){: target="_blank" rel="noopener"}, [StablePML](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.StablePML.html#tidy3d.StablePML){: target="_blank" rel="noopener"}, and [Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: target="_blank" rel="noopener"}.
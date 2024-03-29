---
_schema: default
title: How do I identify the symmetry planes of my simulation?
date: 2023-12-15 16:23:55
enabled: true
category: Symmetry
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
To identify the symmetry planes in your simulation, the first step is to look for reflection symmetries in the geometry as well as the sources of your setup. If your entire simulation setup has reflection symmetry with respect to the x=0 plane, then symmetry can be applied to the x direction. Same for the y and z directions. This only determines if symmetry exists but doesn’t tell us what type (even or odd) of symmetry should be applied.

Once we identify the existence of symmetry in a direction, we need to evaluate the source field. When symmetry exists, certain field components are necessarily zero at the plane of symmetry. PEC symmetry (odd) corresponds to zero normal electric field and zero tangential magnetic field at the symmetry plane. PMC symmetry (even) corresponds to zero tangential electric fields and zero normal magnetic fields at the symmetry plane. Another rule of thumb is to check if the electric field created by the source is perpendicular to the symmetry plane (odd symmetry) or parallel to the symmetry plane (even symmetry).

For example, a plane wave polarized in the y direction propagating in the z direction has symmetry (1, -1, 0) since the electric field is parallel to the x=0 plane and perpendicular to the y=0 plane.

For a more extensive discussion on symmetry, please visit the dedicated [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/Symmetry/).
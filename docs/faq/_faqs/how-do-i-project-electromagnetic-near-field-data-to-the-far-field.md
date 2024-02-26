---
_schema: default
title: How do I project electromagnetic near-field data to the far field?
date: 2023-12-19 16:42:38
enabled: true
category: Data Visualization and Postprocessing
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
In Tidy3D you can use field projections to obtain electromagnetic field data far away from a structure with knowledge of only near-field data. When projecting fields, geometric approximations can be invoked to allow computing fields far away from the structure quickly and with good accuracy, but in Tidy3D we can also turn these approximations off when projecting fields at intermediate distances away, which gives a lot of flexibility. These field projections are particularly useful for eliminating the need to simulate large regions of empty space around a structure.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/FieldProjections/) to details on:

* how to compute projected fields on your local machine after a simulation is run, or on our servers during the simulation run.
* how to extract various quantities related to projected fields such as fields in different coordinate systems, power, and radar cross section.
* how, when far field approximations are used, the fields can dynamically be re-projected to new distances without having to run a new simulation.
* when geometric far field approximations should and should not be invoked, depending on the projection distance and the geometry of the structure.
* how to set up projections for finite-sized objects (e.g., scattering at a sphere) vs. thin but large-area structures (e.g., metasurfaces).
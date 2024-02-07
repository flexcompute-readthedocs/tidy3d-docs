---
_schema: default
title: How do I set a custom current source?
date: 2023-12-11 16:01:43
enabled: true
category: Sources
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
The [tidy3d.CustomCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomCurrentSource.html){: target="_blank" rel="noopener"}&nbsp;source can be used to inject a raw electric and magnetic current distribution within the simulation. Its syntax is very similar to&nbsp;`CustomFieldSource`, except the source accepts a&nbsp;`current_dataset` instead of a&nbsp;`field_dataset`, and it can be volumetric or planar without requiring tangential components. This dataset still contains the `E{x,y,z}` and `H{x,y,z}` field components, which correspond to `J` and `M` components respectively.

See this notebook to an&nbsp;[example](https://www.flexcompute.com/tidy3d/examples/notebooks/CustomFieldSource/)&nbsp;on setting up a [tidy3d.CustomCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomCurrentSource.html){: target="_blank" rel="noopener"}&nbsp;source.
---
_schema: default
title: How do I create a flux box?
date: 2023-12-19 15:28:53
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
A flux box can be defined by creating a FluxMonitor object with a 3D geometry. The total power coming out of the box is returned by integrating the flux over all box surfaces (excpet the ones defined in&nbsp;`exclude_surfaces`).&nbsp;

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FluxMonitor.html).
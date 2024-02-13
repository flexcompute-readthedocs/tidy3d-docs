---
_schema: default
title: How do I plot an object with a spatial definition?
date: 2023-12-18 22:43:01
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
<div><div>If you have an object which includes spatial definition such as <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Simulation.html">tidy3d.Simulation</a> or <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Structure.html">tidy3d.Structure</a>, using <code>obj.plot(x=0)</code> will plot the object on the <code>x=0</code> plane. Note that&nbsp;<code>y</code> and <code>z</code> are alternatively&nbsp; accepted to specify other planar axes.&nbsp; Include the <code>ax</code> argument to plot to an existing axis, ie. <code>obj.plot(y=0, ax=ax)</code>.</div></div>
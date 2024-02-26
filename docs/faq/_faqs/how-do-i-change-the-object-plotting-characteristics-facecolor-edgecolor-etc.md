---
_schema: default
title: >-
  How do I change the object plotting characteristics (facecolor, edgecolor,
  etc)?
date: 2023-12-18 22:53:35
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
<div>Plotting keyword arguments can be supplied to <code>plot()</code>, for example <code>obj.plot(x=0, edgecolor='blue', fill=False)</code>. These keyword arguments correspond to those fed to <a target="_blank" rel="noopener" href="https://tinyurl.com/2nf5c2fk">Matplotlib Patches</a>.</div>
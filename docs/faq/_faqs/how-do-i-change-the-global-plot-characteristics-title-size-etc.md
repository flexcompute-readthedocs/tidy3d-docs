---
_schema: default
title: How do I change the global plot characteristics (title, size, etc)?
date: 2023-12-18 22:57:51
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
<div><div><div>The plotting function return a matplotlib <code>Axes</code>, wihch can be manipulated, for example <code>ax = obj.plot(x=0); &nbsp;ax.set_title('my_title')</code>.</div></div></div>
---
_schema: default
title: How do I specify mappings between scattering matrix elements?
date: 2023-12-20 18:30:12
enabled: true
category: Scattering Matrix
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
You can specify mappings between scattering matrix elements that you want to be equal up to a multiplicative factor. You can define these as&nbsp;`element_mappings`&nbsp;in the&nbsp;[tidy3d.plugins.smatrix.ComponentModeler](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.smatrix.ComponentModeler.html){: target="_blank" rel="noopener"}.

"Indices" are defined as a tuple of&nbsp;`(port_name: str, mode_index: int)`

"Elements" are defined as a tuple of output and input indices, respectively.

The element mappings are therefore defined as a tuple of&nbsp;`(element, element, value)`&nbsp;where the first&nbsp;`element`&nbsp;is set by the value of the 2nd&nbsp;`element`&nbsp;times the supplied&nbsp;`value`.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/SMatrix/) for more details on computing the scattering matrix.
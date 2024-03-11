---
_schema: default
title: How do I calculate mode overlap?
date: 2023-12-19 19:11:53
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
Very often we want to calculate the overlap integral of two modes to compute the coupling efficiency. This can be done conveniently using the outer\_dot method such as&nbsp;

<div markdown class="code-snippet">{% highlight python %}

overlap = waveguide_mode_data_1.outer_dot(waveguide_mode_data_2)

{% endhighlight %}
{% include copy-button.html %}
</div>

where <code markdown class="language-plaintext">waveguide_mode_data_1</code>&nbsp;and&nbsp;<code markdown class="language-plaintext">waveguide_mode_data_2</code>&nbsp;are ModeSolverData objects from performing the mode solving.&nbsp;

For advanced monitor data manipulation such as integration, please refer to the [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/XarrayTutorial/).
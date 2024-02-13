---
_schema: default
title: How do I set a PermittivityMonitor?
date: 2023-12-19 17:11:46
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
records the diagonal components of the complex-valued relative permittivity tensor in the frequency domain. You can define a PermittivityMonitor object by

<div markdown class="code-snippet">{% highlight python %}

monitor = PermittivityMonitor(
    center=(1,2,3),
    size=(2,2,2),
    freqs=[250e12, 300e12],
    name='eps_monitor')

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the[API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.PermittivityMonitor.html).
---
_schema: default
title: How do I set a FieldMonitor?
date: 2023-12-19 15:00:41
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
A FieldMonitor object records electromagnetic fields in the frequency domain. You can define a FieldMonitor object by

<div markdown class="code-snippet">{% highlight python %}

monitor = FieldMonitor(
    center=(1,2,3),
    size=(2,2,2),
    fields=['Hx'],
    freqs=[250e12, 300e12],
    name='steady_state_monitor',
colocate=True)

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldMonitor.html).
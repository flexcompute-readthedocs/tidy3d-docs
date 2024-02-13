---
_schema: default
title: How do I set a FieldTimeMonitor?
date: 2023-12-19 15:11:26
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
A FieldTimeMonitor object records electromagnetic fields in the time domain. You can define a FieldTimeMonitor object by

<div markdown class="code-snippet">{% highlight python %}

monitor = FieldTimeMonitor(
    center=(1,2,3),
    size=(2,2,2),
    fields=['Hx'],
    start=1e-13,
    stop=5e-13,
    interval=2,
    colocate=True,
    name='movie_monitor')

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.FieldTimeMonitor.html).
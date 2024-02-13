---
_schema: default
title: How do I set a DiffractionMonitor?
date: 2023-12-19 17:20:15
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
A DiffractionMonitor object uses a 2D Fourier transform to compute the diffraction amplitudes and efficiency for allowed diffraction orders. You can define a DiffractionMonitor object by

<div markdown class="code-snippet">{% highlight python %}

monitor = DiffractionMonitor(
    center=(1,2,3),
    size=(inf,inf,0),
    freqs=[250e12, 300e12],
    name='diffraction_monitor',
    normal_dir='+',
    )

{% endhighlight %}
{% include copy-button.html %}
</div>

For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.DiffractionMonitor.html).
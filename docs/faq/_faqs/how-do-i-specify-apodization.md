---
_schema: default
title: How do I specify apodization?
date: 2023-12-19 17:25:24
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
Apodization applies a windowing function to the Fourier transform of the time-domain fields into frequency-domain ones. It can be used to truncate the beginning and/or end of the time signal, for example, to eliminate the source pulse when studying the eigenmodes of a system. Note that apodization affects the normalization of the frequency-domain fields.

To apply anodization, we first need to define an `ApodizationSpec` object and then add it to the monitor. For example,

<div markdown class="code-snippet">{% highlight python %}

# Apodization to exclude the source pulse from the frequency-domain monitors
apodization = td.ApodizationSpec(start=t_start, width=2e-13)

# Define a FieldMonitor object and add apodization to it
field_mnt = td.FieldMonitor(
    center=[0, 0, 0],
    size=[4, 2 * np.sqrt(3), 0],
    freqs=[freq0],
    name="field",
    apodization=apodization,
)

{% endhighlight %}
{% include copy-button.html %}
</div>
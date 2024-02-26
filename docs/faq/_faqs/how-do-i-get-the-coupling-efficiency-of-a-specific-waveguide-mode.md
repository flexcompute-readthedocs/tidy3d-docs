---
_schema: default
title: How do I get the coupling efficiency of a specific waveguide mode?
date: 2023-12-19 17:05:41
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
The coupling efficiency of a specific waveguide mode can be calculated from the mode monitor data by first extracting the complex mode amplitude and then taking the square modulus.&nbsp;

<div markdown class="code-snippet">{% highlight python %}

# extract the complex mode amplitude from the mode monitor data
amp = sim_data["mode"].amps.sel(mode_index=0, direction="+")

# compute the coupling efficiency
T = np.abs(amp)**2

{% endhighlight %}
{% include copy-button.html %}
</div>

As an example, you can reference the waveguide Y junction [case study](https://www.flexcompute.com/tidy3d/examples/notebooks/YJunction/).
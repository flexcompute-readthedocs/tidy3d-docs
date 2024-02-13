---
_schema: default
title: How do I set the ResonanceFinder?
date: 2023-12-20 18:38:31
enabled: true
category: Resonance Finder
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
The&nbsp;[tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html){: target="_blank" rel="noopener"}&nbsp;plugin allows one to find resonances and extract their information from time domain field monitors without the necessity of waiting for the fields to completely decay. The&nbsp;`ResonanceFinder`&nbsp;plugin needs&nbsp;[tidy3d.FieldTimeMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FieldTimeMonitor.html){: target="_blank" rel="noopener"}&nbsp;to record the field as a function of time. Importantly, you should start the monitors after the source pulse has decayed.

After setting up and running the simulation you should construct a&nbsp;`ResonanceFinder`&nbsp;object and then call&nbsp;`run()`&nbsp;on the list of&nbsp;`FieldTimeData`&nbsp;objects. This will add up the signals from all field time monitors included in simulation before searching for resonances.

<div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.resonance import ResonanceFinder

resonance_finder = ResonanceFinder(freq_window=(190e14, 210e14))
resonance_data = resonance_finder.run(signals=sim_data.data)
resonance_data.to_dataframe()

{% endhighlight %}
{% include copy-button.html %}</div>



The&nbsp;`run()`&nbsp;method returns an&nbsp;`xr.Dataset`&nbsp;containing the decay rate, Q factor, amplitude, phase, and estimation error for each resonance as a function of frequency.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/ResonanceFinder/){: target="_blank" rel="noopener"} for more details on the `ResonanceFinder`&nbsp;plugin.
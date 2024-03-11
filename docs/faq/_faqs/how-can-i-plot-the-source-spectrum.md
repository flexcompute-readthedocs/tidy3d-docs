---
_schema: default
title: How can I plot the source spectrum?
date: 2023-12-11 18:47:30
enabled: true
category: Sources
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
When you define a source, you need to specify a source time profile, which is typically Gaussian. For example, we can define a plane wave as

<div markdown class="code-snippet">{% highlight python %}

plane_wave = td.PlaneWave(
  source_time=td.GaussianPulse(freq0=freq0, fwidth=0.5 * freqw),
  size=(td.inf, td.inf, 0),
  center=(0, 0, 0.3 * lda0),
  direction="-",
  pol_angle=0,
)

{% endhighlight %}
{% include copy-button.html %}</div>

Here the source time is a Gaussian pulse with central frequency `freq0` and frequency width `0.5 * freqw`. To visualize the spectrum it gives, we can use the `plot_spectrum` method by

<div markdown class="code-snippet">{% highlight python %}

plane_wave.source_time.plot_spectrum(
  times=np.linspace(0, sim.run_time, 2000), val="abs"
)
plt.show()

{% endhighlight %}
{% include copy-button.html %}</div>

Here we need to specify the sampled time instances. To ensure the source spectrum is plotted correctly, we need to ensure the time sampling is sufficiently fine and the end time is sufficiently long compared to the pulse width.
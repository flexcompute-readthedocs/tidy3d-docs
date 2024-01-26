---
_schema: default
title: How can I plot the source spectrum and time-dependence?
date: 2023-12-11 17:33:25
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
The [tidy3d.GaussianPulse](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.GaussianPulse.html){: target="_blank" rel="noopener"}&nbsp;object has the built-in functions `plot_spectrum` and `plot` that allow users to visualize the source spectrum and time-dependence, respectively. For example:

<div markdown class="code-snippet">{% highlight python %}

# Simulation wavelength and bandwidth.
wl = 1.55
bw = 0.1
wl_max = wl + bw / 2
wl_min = wl - bw / 2
freq0 = td.C_0 / wl
fwidth = 0.5 * (td.C_0 / wl_min - td.C_0 / wl_max)
run_time = 1e-12

# Source bandwidth.
pulse = td.GaussianPulse(freq0=freq0, fwidth=fwidth)

# Source definition
pt_dipole = td.PointDipole(
  center=(1,2,3),
  source_time=pulse,
  polarization='Ex',
  interpolate=True,
  name="dipole",
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4), tight_layout=True)

# Plot the source spectrum.
pt_dipole.source_time.plot_spectrum(
    times=np.linspace(0, run_time, 2000), val="abs", ax=ax1,
)

# Plot the source time-dependence.
pt_dipole.source_time.plot(
    times=np.linspace(0, run_time / 3, 2000), val='real', ax=ax2,
)

plt.show()

{% endhighlight %}
{% include copy-button.html %}</div>
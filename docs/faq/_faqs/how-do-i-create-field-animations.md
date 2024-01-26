---
_schema: default
title: How do I create field animations?
date: 2023-12-19 19:35:24
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
<div>Animations are often created from FDTD simulations to provide a more intuitive understanding of the physical phenomena being modeled. These animations can visualize the evolution of the field distribution over time, showing wave propagation, interactions, and other dynamic effects that static images cannot adequately depict.&nbsp;</div>

<div> </div>

<div>To create time-domain animation you can use the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FieldTimeMonitor.html#tidy3d.FieldTimeMonitor">tidy3d.FieldTimeMonitor</a> or the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FluxTimeMonitor.html#tidy3d.FluxTimeMonitor">tidy3d.FluxTimeMonitor</a> to record the time-domain fields along the FDTD time-stepping process. Then, use&nbsp;<code>matplotlib</code>'s&nbsp;<a target="_blank" rel="noopener" href="https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html">FuncAnimation</a>&nbsp;to create the animation.</div>

<div> </div>

<div>Alternatively, you can also create animations from the Fourier-transformed fields calculated using the frequency-domain monitors by changing the <code>phase</code> parameter in the&nbsp;<a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData.plot_field">plot_field()</a> function.</div>

<div> </div>

<div>See this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AnimationTutorial/">tutorial</a> to a complete example on creating field animations.</div>
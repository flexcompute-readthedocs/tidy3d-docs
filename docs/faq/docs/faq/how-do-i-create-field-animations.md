# How do I create field animations?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 19:35:24 | Monitors |


Animations are often created from FDTD simulations to provide a more intuitive understanding of the physical phenomena being modeled. These animations can visualize the evolution of the field distribution over time, showing wave propagation, interactions, and other dynamic effects that static images cannot adequately depict. 

 

To create time-domain animation, you can use the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldTimeMonitor.html#tidy3d.FieldTimeMonitor">tidy3d.FieldTimeMonitor</a> or the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FluxTimeMonitor.html#tidy3d.FluxTimeMonitor">tidy3d.FluxTimeMonitor</a> to record the time-domain fields along the FDTD time-stepping process. Then, use <code>matplotlib</code>'s <a target="_blank" rel="noopener" href="https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html">FuncAnimation</a> to create the animation.

 

Alternatively, you can also create animations from the Fourier-transformed fields calculated using the frequency-domain monitors by changing the <code>phase</code> parameter in the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.SimulationData.html#tidy3d.SimulationData.plot_field">plot_field()</a> function.

 

See this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AnimationTutorial/">tutorial</a> to a complete example on creating field animations.
---
_schema: default
title: How do I set the periodic boundary condition?
date: 2023-12-14 22:07:57
enabled: true
category: Boundary Conditions
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
<div><div>The <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Periodic.html#tidy3d.Periodic">tidy3d.Periodic</a> boundary condition allows users to obtain the response of large periodic structures by simulating only a unit cell. The example below illustrates how to set up boundary conditions in a typical case, where we have a unit cell and need to include periodic boundaries in two directions and PML in the perpendicular direction.</div><div> </div><div markdown class="code-snippet">{% highlight python %}

# Definition of periodic boundary condition in the x and y directions.
# PML in the z-direction.
bspec = tidy3d.BoundarySpec(
    x=tidy3d.Boundary(minus=tidy3d.Periodic(), plus=tidy3d.Periodic()),
    y=tidy3d.Boundary(minus=tidy3d.Periodic(), plus=tidy3d.Periodic()),
    z=tidy3d.Boundary(minus=tidy3d.PML(), plus=tidy3d.PML()),
)

# Build the simulation.
sim = tidy3d.Simulation(
    center=(0, 0, 0),
    size=(2, 2, 10),
    boundary_spec=bspec,
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[unit_cell],
    sources=[plane_wave],
    monitors=[flux_monitor],
    run_time=1e-12,
)

{% endhighlight %}
{% include copy-button.html %}</div><h5>Details about the periodic boundary condition&nbsp;</h5><div>Floquet's (or Bloch's) theorem describes electromagnetic fields interacting with periodic structures. Considering the fields&nbsp;$\vec{E}$&nbsp;and&nbsp;$\vec{H}$&nbsp;propagating in the <code>x</code>-direction along a periodic structure<span>&nbsp;</span> with period&nbsp;$L_x$, they must satisfy:</div><div> </div><div>$\vec{E}(x+L_x, y, z)=\vec{E}(x, y, z)e^{-jk_x L_x}$</div><div> </div><div>and</div><div> </div><div>$\vec{H}(x+L_x, y, z)=\vec{H}(x, y, z)e^{jk_x L_x}$,</div><div> </div><div>where $k_x$&nbsp;is the light wave vector in the <code>x</code>-direction.</div><div> </div><div>Note that when using periodic boundary conditions, both structures and fields must exhibit periodicity. Therefore, it is important to include the sources correctly. If the source is injected at an angle, use <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.BlochBoundary.html#tidy3d.BlochBoundary">tidy3d.BlochBoundary</a> instead.</div><div> </div></div>

See this [notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/) for more details on setting up boundary conditions.
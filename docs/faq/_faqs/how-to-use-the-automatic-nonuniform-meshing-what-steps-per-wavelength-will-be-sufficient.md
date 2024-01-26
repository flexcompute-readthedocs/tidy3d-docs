---
title: >-
  How to use the automatic nonuniform meshing? What steps per wavelength will be
  sufficient?
date: 2023-12-04 18:58:43
enabled: true
category: "Grid Specification"
---
By default, Tidy3D configures the&nbsp;[GridSpec](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.GridSpec.html){: rel="nofollow"}&nbsp;object to having&nbsp;[AutoGrid](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.AutoGrid.html){: rel="nofollow"}, which is an advanced meshing algorithm to automatically define a nonuniform grid, in all the three domain direction. The resolution of this grid is specified using the desired minimum steps per wavelength in each material (`min_steps_per_wvl = 10 by default`). This specification, therefore, requires a target wavelength, which can be either provided directly to&nbsp;`grid_spec`&nbsp;or inferred from any sources present in the simulation. Detailed examples on how to set up&nbsp;[AutoGrid](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.AutoGrid.html){: rel="nofollow"}&nbsp;are present on this&nbsp;[notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/AutoGrid/){: rel="nofollow"}.

As a gold rule of thumb, the default value of 10 grid points per wavelength should be a good starting value for&nbsp;`min_steps_per_wvl`. However, other application-specific features must be considered when defining the appropriate simulation mesh, such as very thin geometries or large electric field gradients, as can usually occur, for example, in the presence of resonances, highly confined fields, or at metal-dielectric interfaces. Additional control over the mesh is obtained by the&nbsp;`dl_min`&nbsp;parameter, which imposes a lower bound of the grid size regardless of the structures present in the simulation, including override structures with&nbsp;`enforced=True`. This is, however, a soft bound, meaning that the actual minimal grid size might be slightly smaller. Finally, the&nbsp;`max_scale`&nbsp;sets the maximum ratio between two consecutive grid steps. Different grid configurations can be chosen for each direction, as illustrated bellow:

<div markdown class="code-snippet">{% highlight python %}

grid_spec = td.GridSpec(
grid_x=td.AutoGrid(min_steps_per_wvl=20,dl_min=0.01),
grid_y=td.AutoGrid(min_steps_per_wvl=15),
grid_z=td.AutoGrid(min_steps_per_wvl=10,max_scale=1.6),
wavelength=1.0,
)

{% endhighlight %}
{% include copy-button.html %}</div>

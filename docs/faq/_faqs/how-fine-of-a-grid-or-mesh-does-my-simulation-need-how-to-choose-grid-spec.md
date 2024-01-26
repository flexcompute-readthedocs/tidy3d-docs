---
title: How fine of a grid or mesh does my simulation need? How to choose grid spec?
date: 2023-12-04 18:56:06
enabled: true
category: "Grid Specification"
---
The FDTD and other similar numerical methods will always give approximate results for a set of finite-difference equations. The accuracy of Maxwell's equations solution for any geometry can be arbitrarily increased by using smaller and smaller values of the space and time increments. This strategy often involves increased simulation time and memory, so it is essential to consider, for your application, what is the desired accuracy in results so that you can run your simulations as quickly as possible. As a gold rule of thumb, ten grid points per wavelength in the highest refractive index medium should be a good starting value for the grid resolution. However, other application specificities must be considered when defining the appropriate simulation mesh, such as very thin geometries or large electric field gradients, as usually occurs, for example, in the presence of resonances, highly confined fields, or at metal-dielectric interfaces.

Tidy3D has many features to give the user a simple and flexible way to build the simulation mesh. The&nbsp;[GridSpec](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.GridSpec.html){: rel="nofollow"}&nbsp;object enables the user to chose between an&nbsp;[AutoGrid](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.AutoGrid.html){: rel="nofollow"}, a&nbsp;[UniformGrid](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.UniformGrid.html){: rel="nofollow"}, or a&nbsp;[CustomGrid](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.CustomGrid.html){: rel="nofollow"}, at each of the simulation x-, y-, z-direction. An example code snippet is shown below:

<div markdown class="code-snippet">{% highlight python %}

uniform = tidy3d.UniformGrid(dl=0.1)

custom = tidy3d.CustomGrid(dl=[0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2])

auto = tidy3d.AutoGrid(min_steps_per_wvl=12)

grid_spec = tidy3d.GridSpec(grid_x=uniform, grid_y=custom, grid_z=auto, wavelength=1.5)

{% endhighlight %}
{% include copy-button.html %}</div>

More examples of setting up the simulation mesh are available on this&nbsp;[notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/AutoGrid/){: rel="nofollow"}.

In general, a good strategy is to start with the default object&nbsp;[AutoGrid](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.AutoGrid.html){: rel="nofollow"}&nbsp;to discretize the whole simulation domain and fine-tune the mesh by increasing the grid resolution at directions or regions containing smallest geometric features or high field gradients or even relaxing the discretization along directions of invariant geometry, e.g., the propagation direction of channel waveguides. The definition of an override structure is an efficient way to improve simulation accuracy while keeping small the run time.

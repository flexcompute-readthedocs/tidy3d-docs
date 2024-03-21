---
_schema: default
title: How can I reduce the simulation cost?
date: 2023-10-24 14:48:15
enabled: true
category: Simulations
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
The cost of a simulation is primarily affected by the number of grid points and time steps. To reduce the simulation cost, you can take specific actions. However, it's essential to gather relevant information about the simulation first to help you in this process.

<div markdown class="code-snippet">{% highlight python %}

# Initializes job, puts task on server (but doesn't run it).
job = tidy3d.web.Job(simulation=sim, task_name="job", verbose=verbose)

# Estimate the maximum cost before running the simulation.
estimated_cost = tidy3d.web.estimate_cost(job.task_id)
print(f'The estimated maximum cost is {estimated_cost:.3f} Flex Credits.')

# Run the simulation.
sim_data = tidy3d.web.run(simulation=sim, task_name="task", path="data/data.hdf5", verbose=True)

# Print simulation information such as grid points and time steps.
print(sim_data.log)

{% endhighlight %}
{% include copy-button.html %}</div>

##### Symmetry

In Tidy3D simulations, field symmetries can significantly reduce computational time and FlexCredit cost, sometimes by factors of 1/2, 1/4, or even 1/8. Therefore, symmetry is preferred whenever applicable. However, it is crucial to set up the symmetry correctly to avoid inaccurate results. For a more detailed explanation of symmetry, please refer to the dedicated [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/Symmetry/).

##### Meshing Strategy

To reduce the number of grid points (and time steps) in a simulation, you can adjust the [GridSpec](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GridSpec.html){: target="_blank" rel="nofollow noopener"} specifications. You have the option to choose between [AutoGrid](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.AutoGrid.html){: rel="nofollow"},&nbsp;[UniformGrid](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.UniformGrid.html){: rel="nofollow"}, or&nbsp;[CustomGrid](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomGrid.html){: rel="nofollow"} for each simulation direction. Starting with the default object [AutoGrid](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.AutoGrid.html){: rel="nofollow"}&nbsp;is generally a good strategy to discretize the entire simulation domain. You can then fine-tune the mesh by increasing grid resolution for directions or regions with smaller geometric features or high field gradients. You can also relax the discretization along directions of invariant geometry, such as the propagation direction of channel waveguides. Another way to enhance simulation accuracy while keeping the grid points small is by defining an override structure.

##### Shutoff

By default, Tidy3D periodically checks the total field intensity left in the simulation and compares that to the maximum total field intensity recorded at previous times. If it is found that the ratio of these two values is smaller than​​​&nbsp;$$10^{-5}$$​​, the simulation is terminated as the fields remaining in the simulation are deemed negligible. The shutoff value can be controlled using the&nbsp;`tidy3d.Simulation.shutoff`&nbsp;parameter, or completely turned off by setting it to zero. In most cases, the default behavior ensures that results are correct while avoiding unnecessarily long run times. The Flex Unit cost of the simulation is also proportionally scaled down when early termination is encountered.

##### Boundary Conditions

When running simulations, it's important to use appropriate boundary conditions to absorb incoming waves and minimize reflection accurately. The [tidy3d.PML](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PML.html#tidy3d.PML){: target="_blank" rel="noopener"} boundary condition is generally the best choice, as it can absorb waves from all angles with minimal reflection. However, in some instances where an angled structure or dispersive materials are present within the PML, you may need to use the [tidy3d.Absorber](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Absorber.html#tidy3d.Absorber){: target="_blank" rel="noopener"} instead. While the absorber performs a similar function to the PML, it has a slightly higher reflection rate and requires more computation, resulting in higher simulation costs.

See this&nbsp;[notebook](https://www.flexcompute.com/tidy3d/examples/notebooks/BoundaryConditions/)&nbsp;for more details on setting up boundary conditions.

<!-- notionvc: 236d2784-3134-4b85-9b57-777825079203 -->

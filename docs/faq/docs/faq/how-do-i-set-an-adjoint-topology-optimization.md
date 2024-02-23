# How do I set an adjoint topology optimization?

| Date       | Category    |
|------------|-------------|
| 2023-12-21 22:12:45 | Inverse Design |


To create an adjoint topology (or density-based) optimization set up, you can control the permittivity values of a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxCustomMedium.html">tidy3d.plugins.adjoint.JaxCustomMedium</a> based on the optimization design parameters. After that, you need to include it in a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxStructure.html">tidy3d.plugins.adjoint.JaxStructure</a>. Be sure of adding the adjoint structures in the <code>.input_structures</code> parameter of the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxSimulation.html#tidy3d.plugins.adjoint.JaxSimulation">tidy3d.plugins.adjoint.JaxSimulation</a> object. In addition, you must specify an adjoint compatible monitor in <code>.output_monitors</code>, that defines the set of monitors and corresponding data that the objective function will depend on.​​​​Once the adjoint simulation is defined, you must use the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.web.run.html">tidy3d.plugins.adjoint.web.run</a> method to send the simulation set up to our servers. After computing the forward and adjoint simulations, a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.adjoint.JaxSimulationData.html#tidy3d.plugins.adjoint.JaxSimulationData">tidy3d.plugins.adjoint.JaxSimulationData</a> is returned, so you can compute the objective function value. 

 

Lastly, use <code>jax.value_and_grad</code> to both compute the objective function and the gradient with respect to the design parameters. The objective function gradients can them feed a gradient-based optimization algorithm to drive the inverse design process. 

 

We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method. You can also go through this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin6GratingCoupler/">tutorial</a> for an example on adjoint topology optimization.

 

 
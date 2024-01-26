# How do I set an adjoint inverse design simulation?

| Date       | Category    |
|------------|-------------|
| 2023-12-21 19:01:14 | Inverse Design |


To create an adjoint inverse design set up, you need to use a special <code>Simulation</code> subclass called <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.adjoint.JaxSimulation.html#tidy3d.plugins.adjoint.JaxSimulation">tidy3d.plugins.adjoint.JaxSimulation</a>, which is a <code>jax</code>-compatible stand in for <code>Simulation</code> and behaves almost entirely the same, except for a few important differences:<ol><li>This feature allows for the inclusion of an extra field (<code>.input_structures</code>) consisting of <code>jax</code>-compatible Tidy3D structures. For example, the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.adjoint.JaxStructure.html#tidy3d.plugins.adjoint.JaxStructure">tidy3d.plugins.adjoint.JaxStructure</a>, which contains a <code>.medium</code> and a <code>.geometry</code> field, both of which may depend on the design parameters. The final gradients of the objective function will be given with respect to the values of the fields mentioned above.</li><li>It accepts the additional field <code>.output_monitors</code>, that defines the set of monitors and corresponding data that the objective function will depend on.</li></ol>

Once the adjoint simulation is defined, you must use the <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.adjoint.web.run.html">tidy3d.plugins.adjoint.web.run</a> method to send the simulation set up to our servers. After computing the forward and adjoint simulations, a <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.adjoint.JaxSimulationData.html#tidy3d.plugins.adjoint.JaxSimulationData">tidy3d.plugins.adjoint.JaxSimulationData</a> is returned, so you can compute the objective function value. 

 

Lastly, use <code>jax.value_and_grad</code> to both compute the objective function <strong>and</strong> the gradient with respect to the design parameters. The objective function gradients can them feed a gradient-based optimization algorithm to drive the inverse design process. 

 

We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method. You can also go through this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin1Intro/">tutorial</a> for an introduction to the basic concepts related to automatic differentiation and adjoint optimization.

 

 
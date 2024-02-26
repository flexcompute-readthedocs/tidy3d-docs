# How is the adjoint simulation billed?

| Date       | Category    |
|------------|-------------|
| 2023-12-21 21:19:39 | Inverse Design |


Both the <code>forward</code> and the <code>adjoint</code> simulations are billed when running inverse design optimizations using the <code>adjoint</code> plugin. That represents a significant reduction in computation cost as the adjoint method allows one to calculate the gradient of an objective function with respect to thousands of design parameters in only two simulations.

 

We highly recommend watching the <a href="https://www.flexcompute.com/tidy3d/learning-center/inverse-design/">Inverse Design</a> lectures if you are new to the adjoint method. You can also go through this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/AdjointPlugin1Intro/">tutorial</a> for an introduction to the basic concepts related to automatic differentiation and adjoint optimization.
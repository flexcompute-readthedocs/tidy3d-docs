---
title: How long should I run the simulation?
date: 2023-12-03 21:05:09
enabled: true
category: "Simulations"
---
The frequency-domain response obtained in the FDTD simulation only accurately represents the continuous-wave response of the system if the fields at the beginning and at the end of the time stepping are (very close to) zero. So, you should run the simulation for a time enough to allow the electromagnetic fields decay to negligible values within the simulation domain.

When dealing with light propagation in a NON-RESONANT device, like a simple optical waveguide, a good initial guess to simulation `run_time` would be the a few times the largest domain dimension ($L$) multiplied by the waveguide mode group index ($n_g$), divided by the speed of light in a vacuum ($c_0$), plus the `source_time`.

<div><div>By default, Tidy3D checks periodically the total field intensity left in the simulation, and compares that to the maximum total field intensity recorded at previous times. If it is found that the ratio of these two values is smaller than $10^{-5}$, the simulation is terminated as the fields remaining in the simulation are deemed negligible. The shutoff value can be controlled using the <code>tidy3d.Simulation.shutoff</code> parameter, or completely turned off by setting it to zero. In most cases, the default behavior ensures that results are correct, while avoiding unnecessarily long run times. The Flex Unit cost of the simulation is also proportionally scaled down when early termination is encountered.</div></div>

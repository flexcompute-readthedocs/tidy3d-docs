---
title: Why did my simulation finish early?
date: 2023-10-24 17:02:34
enabled: true
category: "Simulation Troubleshoot"
---
By default, Tidy3D periodically checks the total field intensity left in the simulation, and compares that to the maximum total field intensity recorded at previous times. If it is found that the ratio of these two values is smaller than $$10^{-5}$$, the simulation is terminated as the fields remaining in the simulation are deemed negligible. The shutoff value can be controlled using the `Simulation.shutoff`{: .interpreted-text role="py:obj"} parameter or completely turned off by setting it to zero. In most cases, the default behavior ensures that results are correct while avoiding unnecessarily long run times. The Flex Unit cost of the simulation is also proportionally scaled down when early termination is encountered.


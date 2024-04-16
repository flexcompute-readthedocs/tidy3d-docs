---
title: What is The Difference Between Periodic and Bloch Boundaries?
date: 2023-12-06 21:43:10
enabled: true
category: "Boundary Conditions"
---

`Periodic` and `Bloch` boundary conditions are very useful for simulating periodic structures. When using `Periodic` boundary conditions, the fields are registered on one edge of the simulation domain and re-injected at the opposite edge. `Bloch` boundary conditions are similar, but they also apply a phase correction term to the fields. In other words, `Periodic` boundary conditions can be considered a special case of `Bloch` boundaries. When a normal incident plane wave is considered, there will not be any difference between them. However, if we consider a plane wave propagating at an angle, the fields from one period to the next will not be exactly periodic and will be out of phase by some amount. The `Bloch` boundary condition corrects this factor. Therefore, when injecting plane waves at an angle, `Bloch` boundaries should be used.
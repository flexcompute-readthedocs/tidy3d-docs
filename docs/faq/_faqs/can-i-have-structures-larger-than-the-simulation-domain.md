---
title: Can I have structures larger than the simulation domain?
date: 2023-12-04 19:00:07
enabled: true
category: "Simulation Troubleshoot"
---
Structures can indeed be larger than the simulation domain in Tidy3D. In such cases, Tidy3D will automatically truncate the geometry that goes beyond the domain boundaries. For best results, structures that intersect with absorbing boundaries or simulation edges should extend all the way through. In many such cases, an "infinite" size td.inf can be used to define the size along that dimension.

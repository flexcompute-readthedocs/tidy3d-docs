---
title: Why can I not change Tidy3D instances after they are created?
date: 2023-10-24 18:09:43
enabled: true
category: 'Simulation Troubleshoot'
---
You may notice in Tidy3D versions 1.5 and above that it is no longer
possible to modify instances of Tidy3D components after they are
created. Making Tidy3D components immutable like this was an intentional
design decision intended to make Tidy3D safer and more performant.

For example, Tidy3D contains several \"validators\" on input data. If
models are mutated, we can\'t always guarantee that the resulting
instance will still satisfy our validations and the simulation may be
invalid.

Furthermore, making the objects immutable allows us to cache the results
of many expensive operations. For example, we can now compute and store
the simulation grid once, without needing to worry about the value
becoming stale at a later time, which significantly speeds up plotting
and other operations.

If you have a Tidy3D component that you want to recreate with a new set
of parameters, instead of `obj.param1 = param1_new`, you can call
`obj_new = obj.copy(update=dict(param1=param1_new))`. Note that you may
also pass more key value pairs to the dictionary in `update`. Also, note
you can use a convenience method
`obj_new = obj.updated_copy(param1=param1_new)`, which is just a
shortcut to the `obj.copy()` call above.


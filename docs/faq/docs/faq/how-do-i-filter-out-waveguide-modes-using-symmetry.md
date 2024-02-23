# How do I filter out waveguide modes using symmetry?

| Date       | Category    |
|------------|-------------|
| 2023-12-15 16:27:04 | Symmetry |


Different waveguide modes process different symmetries. When we define the symmetry for the simulation, only the waveguide modes with the same symmetry can be found at the mode sources and mode monitors.

For example, for a rectangular strip waveguide buried in oxide with a mode source propagating in the y direction as shown below, we can identify two symmetry planes at x=0 and z=0. All TE modes with electric field predominantly in the x direction has symmetry (0,0,1), while all TM modes has symmetry (0,0,-1). Furthermore, even TE modes (TE0, TE2, TE4, …) have symmetry (-1,0,1) while odd TE modes (TE1, TE3, TE5, …) have symmetry (1,0,1). Even TM modes (TM0, TM2, TM4, ..) have symmetry (1,0,-1) while odd TM modes (TM1, TM3, TM5, ..) have symmetry (-1,0,-1). Therefore, by using certain symmetry, we can selectively filter out waveguide modes. Note that when the cladding and substrate materials are different or the waveguide has a nonzero sidewall angle, certain symmetry will be broken.

![](/uploads/waveguide-1.png)

For a more extensive discussion on waveguide mode filtering using symmetry, please visit the dedicated [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/Symmetry/).
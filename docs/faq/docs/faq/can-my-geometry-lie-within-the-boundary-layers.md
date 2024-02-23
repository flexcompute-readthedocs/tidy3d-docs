# Can my geometry lie within the boundary layers?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 14:48:15 | Boundary Conditions |


Structures can indeed be larger than the simulation domain in Tidy3D. In such cases, Tidy3D will automatically truncate the geometry that goes beyond the domain boundaries. For best results, structures that intersect with absorbing boundaries or simulation edges should extend all the way through. In many such cases, an "infinite" size tidy3d.inf can be used to define the size along that dimension.

It is important to keep in mind that PML only absorbs propagating fields. For evanescent fields, PML can act as an amplification medium and cause a simulation to diverge. In Tidy3D, a warning will appear if the distance between a structure is smaller than half of a wavelength to prevent evanescent fields from leaking into PML. In most cases, the evanescent field will naturally die off within half a wavelength, but in some instances, a larger distance may be required.
# What is the ideal distance between the geometry and absorbing layers?

| Date       | Category    |
|------------|-------------|
| 2023-12-15 21:35:25 | Boundary Conditions |


In Tidy3D, a warning will appear if the distance between a structure and the absorbing layers is smaller than half of a wavelength to prevent evanescent fields from leaking into PML. In most cases, the evanescent field will naturally die off within half a wavelength, but in some instances, a larger distance may be required. It is important to keep in mind that PML only absorbs propagating fields. PML can act as an amplification medium for evanescent fields and cause a simulation to diverge.
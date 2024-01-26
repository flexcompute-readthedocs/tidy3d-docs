# How do I create an anisotropic material?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 19:12:04 | Mediums |


To create fully anisotropic mediums including all 9 components of the permittivity and conductivity tensors, you can use the [tidy3d.FullyAnisotropicMedium](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.FullyAnisotropicMedium.html) object. The provided permittivity tensor and the symmetric part of the conductivity tensor must have coinciding main directions. However, a non-symmetric conductivity tensor can be used to model magneto-optic effects. Note that dispersive properties and subpixel averaging are currently not supported for fully anisotropic materials.



```python

perm = [[2, 0, 0], [0, 1, 0], [0, 0, 3]]
cond = [[0.1, 0, 0], [0, 0, 0], [0, 0, 0]]
anisotropic_dielectric = FullyAnisotropicMedium(permittivity=perm, conductivity=cond)

```



Alternatively, you can create a diagonaly anisotropic material, using the [tidy3d.AnisotropicMedium(xx=medium\_xx, yy=medium\_yy, zz=medium\_zz)](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.AnisotropicMedium.html#tidy3d.AnisotropicMedium) object, and then include three medium objects defining the diagonal elements of the permittivity tensor. In this case, the medium objects can be of type [Medium](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Medium.html#tidy3d.Medium), [PoleResidue](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.PoleResidue.html#tidy3d.PoleResidue), [Sellmeier](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Sellmeier.html#tidy3d.Sellmeier), [Lorentz](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Lorentz.html#tidy3d.Lorentz), [Debye](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Debye.html#tidy3d.Debye), or [Drude](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Drude.html#tidy3d.Drude). For example:



```python

medium_xx = Medium(permittivity=4.0)
medium_yy = Medium(permittivity=4.1)
medium_zz = Medium(permittivity=3.9)
anisotropic_dielectric = AnisotropicMedium(xx=medium_xx, yy=medium_yy, zz=medium_zz)

```



 

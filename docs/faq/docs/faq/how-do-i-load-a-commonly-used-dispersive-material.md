# How do I load a commonly used dispersive material?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 19:44:23 | Mediums |


Tidy3D has an extensive <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api.html#material-library">material library</a> containing various dispersive models from real world materials. You can import one of several material models using only a single line of code, as below: 



```python

from tidy3d import material_library

silver = material_library['Ag']['Rakic1998BB']

```



The key of the dictionary is the abbreviated material name. Some materials have multiple variant models, in which case the second key is the “variant” name.

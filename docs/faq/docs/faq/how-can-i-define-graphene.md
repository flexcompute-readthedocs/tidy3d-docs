# How can I define graphene?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 20:22:01 | Mediums |


You can create a graphene medium using [tidy3d.Graphene](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.Graphene.html#tidy3d.Graphene), which defines a parametric surface conductivity model for graphene. For example:



```python

gamma = 0.0033  # Scattering rate (eV).
mu_c = 0.5  # Graphene chemical potential (eV).
temp = 300  # Temperature (K).
scaling = 2  # Number of graphene layers.

graphene = td.material_library["graphene"](
    gamma=gamma, mu_c=mu_c, temp=temp, scaling=scaling
).medium

# or
# graphene = tidy3d.Graphene(
#    gamma=gamma, mu_c=mu_c, temp=temp, scaling=scaling
# ).medium

```



See <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/GrapheneMetamaterial/">this example</a> for details on creating and using a Graphene medium.

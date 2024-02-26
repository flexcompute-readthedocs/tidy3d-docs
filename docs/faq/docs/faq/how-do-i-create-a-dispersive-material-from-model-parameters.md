# How do I create a dispersive material from model parameters?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 19:26:45 | Mediums |


To create a dispersive material from model parameters, you only need to instantiate the medium object and provide their parameters. For example `debye_medium = td.Debye(eps_inf=2.0, coeffs=[(1,2),(3,4)])`.

 

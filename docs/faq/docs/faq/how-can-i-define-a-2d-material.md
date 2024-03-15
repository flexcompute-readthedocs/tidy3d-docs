# How can I define a 2D material?

| Date       | Category    |
|------------|-------------|
| 2023-12-05 20:06:53 | Mediums |


You can create a 2D material using the [tidy3d.Medium2D](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Medium2D.html) object. This is especially helpful for building very thin materials, like metal layers.



```python

t_copper = 0.0001  # Thickness of the copper layer.
sigma_copper = 50  # Copper conductivity in S/um.

# Define copper as a Medium2D.
copper = td.Medium2D.from_medium(
    td.Medium(conductivity=sigma_copper), thickness=t_copper
)

```



Since the copper layer is very thin, we have modeled it as a <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Medium2D.html?__hstc=197414576.85a08fc595b47d0b94ebfa20ba44cd6d.1696006513341.1701804845497.1701806942901.23&amp;__hssc=197414576.4.1701806942901&amp;__hsfp=3209960735">Medium2D</a> in this example instead of a regular <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Medium.html?__hstc=197414576.85a08fc595b47d0b94ebfa20ba44cd6d.1696006513341.1701804845497.1701806942901.23&amp;__hssc=197414576.4.1701806942901&amp;__hsfp=3209960735">Medium</a>. This way, we do not need to use a very fine grid to resolve the actual thickness of the copper layer. The <code>from_medium</code> method is a convenient way to construct a <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Medium2D.html?__hstc=197414576.85a08fc595b47d0b94ebfa20ba44cd6d.1696006513341.1701804845497.1701806942901.23&amp;__hssc=197414576.4.1701806942901&amp;__hsfp=3209960735">Medium2D</a>. Alternatively, you can specify the <code>ss</code> and <code>tt</code> parameters directly, e.g <code>medium_2d=tidy3d.Medium2D(ss=medium_a, tt=medium_b)</code>, where <code>medium_a</code> and <code>medium_b</code> are of type <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Medium.html#tidy3d.Medium">Medium</a>, <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.PoleResidue.html#tidy3d.PoleResidue">PoleResidue</a>, <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Sellmeier.html#tidy3d.Sellmeier">Sellmeier</a>, <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Lorentz.html#tidy3d.Lorentz">Lorentz</a>, <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Debye.html#tidy3d.Debye">Debye</a>, or <a href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Drude.html#tidy3d.Drude">Drude</a>.

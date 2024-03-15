# How do I set a custom current source?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 16:01:43 | Sources |


The [tidy3d.CustomCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomCurrentSource.html) source can be used to inject a raw electric and magnetic current distribution within the simulation. Its syntax is very similar to that of `CustomFieldSource`, except the source accepts a `current_dataset` instead of a `field_dataset`, and it can be volumetric or planar without requiring tangential components. This dataset still contains the `E{x,y,z}` and `H{x,y,z}` field components, which correspond to `J` and `M` components, respectively.

See this notebook to an [example](https://www.flexcompute.com/tidy3d/examples/notebooks/CustomFieldSource/) on setting up a [tidy3d.CustomCurrentSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomCurrentSource.html) source.
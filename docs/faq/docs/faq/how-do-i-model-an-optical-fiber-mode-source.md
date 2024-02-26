# How do I model an optical fiber mode source?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 14:41:31 | Sources |


To simulate an optical fiber mode source, you can use the [tidy3d.ModeSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.ModeSource.html). This object allows you to solve for the optical modes of a fiber cross-section. You can then include this in your simulation by following the steps outlined in the [example](https://www.flexcompute.com/tidy3d/examples/notebooks/BilayerSiNEdgeCoupler/).

If you prefer, you can also use the [tidy3d.GaussianBeam](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.GaussianBeam.html) source instead to approximate the optical mode of the fiber with a Gaussian distribution, as explained in more detail in another [example](https://www.flexcompute.com/tidy3d/examples/notebooks/EdgeCoupler/).
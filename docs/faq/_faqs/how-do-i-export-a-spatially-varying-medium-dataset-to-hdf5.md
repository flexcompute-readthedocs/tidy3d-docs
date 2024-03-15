---
title: How do I export a spatially varying medium dataset to HDF5?
date: 2024-01-17 15:53:00
enabled: true
category: "Mediums"
---
To export a spatially varying medium dataset to a HDF5 file you should use the `to_hdf5(filename)` method. In the example below, we illustrate how to do that after creating a [tidy3d.CustomMedium](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomMedium.html#tidy3d.CustomMedium){: target="_blank" rel="noopener"}.

<div markdown class="code-snippet">{% highlight python %}

# The coordinate for the refractive index data that includes x, y, z, and frequency
X = np.linspace(-20, 20, 100)  # x grid
Y = np.linspace(-20, 20, 100)  # y grid
Z = [0]  # z grid

# Create a permittivity dataset and a custom medium.
n_data = np.ones((100, 100, 1, 1)) * 12
n_dataset = tidy3d.SpatialDataArray(n_data, coords=dict(x=X, y=Y, z=Z, f=[freq0]))
data = tidy3d.PermittivityDataset(eps_xx=n_dataset, eps_yy=n_dataset, eps_zz=n_dataset)
mat_custom = tidy3d.CustomMedium(eps_dataset=data, interp_method="nearest")

# Export the custom medium dataset to HDF5.
mat_custom.to_hdf5(fname="CustomMedium.hdf5")

{% endhighlight %}
{% include copy-button.html %}</div>
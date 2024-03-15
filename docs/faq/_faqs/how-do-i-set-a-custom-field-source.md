---
_schema: default
title: How do I set a custom field source?
date: 2023-12-11 15:31:59
enabled: true
category: Sources
_inputs:
  title:
    type: text
    label: QUESTION TITLE
  enabled:
    type: switch
    hidden: true
  date:
    type: datetime
    label: DATE
    instance_value: NOW
  category:
    type: select
    options:
      values: data.faq_categories
      value_key: key
      preview:
        text:
          - key: category_name
---
The [tidy3d.CustomFieldSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomFieldSource.html){: target="_blank" rel="noopener"}&nbsp;source can be used to inject a specific (`E`, `H`) field distribution on a plane, e.g. coming from another simulation. Internally, we use the equivalence principle to compute the actual source currents (all sources in FDTD have to be converted to current sources). Because of this, the custom field source will only produce reliable results if the provided fields decay by the edges of the source plane, or if they extend through the simulation boundaries and are well-matched to those boundaries.

The example below illustrates how to define the&nbsp;[tidy3d.CustomFieldSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomFieldSource.html){: target="_blank" rel="noopener"}&nbsp;using a dataset containing the `E` and `H` fields to describe a Gaussian field profile.

<div markdown class="code-snippet">{% highlight python %}

# Source bandwidth.
pulse = tidy3d.GaussianPulse(freq0=200e12, fwidth=20e12)

# Scalar gaussian field.
waist_radius = 2
ys, zs = np.linspace(-4, 4, 101), np.linspace(-4, 4, 101)
y_grid, z_grid = np.meshgrid(ys, zs)
scalar_gaussian = np.exp(-(y_grid**2 + z_grid**2) / waist_radius**2)

# Field dataset defining both E and H
dataset_EH = tidy3d.FieldDataset(
    Ey=tidy3d.ScalarFieldDataArray(
        scalar_gaussian[None, ..., None],
        coords={
            "x": [0],
            "y": ys,
            "z": zs,
            "f": [200e12],
        },
    ),
    Hz=tidy3d.ScalarFieldDataArray(
        scalar_gaussian[None, ..., None] / td.ETA_0,
        coords={
            "x": [0],
            "y": ys,
            "z": zs,
            "f": [200e12],
        },
    ),
)

# Source definition
custom_field_src = tidy3d.CustomFieldSource(
    source_time=pulse,
    center=(-1, 1, 0),
    size=(0, 8, 8),
    field_dataset=dataset_EH,
)

{% endhighlight %}
{% include copy-button.html %}</div>

See this notebook to an&nbsp;[example](https://www.flexcompute.com/tidy3d/examples/notebooks/CustomFieldSource/)&nbsp;on setting up a [tidy3d.CustomFieldSource](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.CustomFieldSource.html){: target="_blank" rel="noopener"}&nbsp;source.
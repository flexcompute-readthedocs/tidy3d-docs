# How do I set a DiffractionMonitor?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 17:20:15 | Monitors |


A DiffractionMonitor object uses a 2D Fourier transform to compute the diffraction amplitudes and efficiency for allowed diffraction orders. You can define a DiffractionMonitor object by



```python

monitor = DiffractionMonitor(
    center=(1,2,3),
    size=(inf,inf,0),
    freqs=[250e12, 300e12],
    name='diffraction_monitor',
    normal_dir='+',
    )

```



For details, please refer to the [API reference](https://docs.flexcompute.com/projects/tidy3d/en/stable/_autosummary/tidy3d.DiffractionMonitor.html).
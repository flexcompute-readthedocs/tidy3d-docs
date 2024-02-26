# How do I set the ResonanceFinder?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 18:38:31 | Resonance Finder |


The [tidy3d.plugins.resonance.ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder.html) plugin allows one to find resonances and extract their information from time domain field monitors without the necessity of waiting for the fields to completely decay. The `ResonanceFinder` plugin needs [tidy3d.FieldTimeMonitor](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.FieldTimeMonitor.html) to record the field as a function of time. Importantly, you should start the monitors after the source pulse has decayed.

After setting up and running the simulation you should construct a `ResonanceFinder` object and then call `run()` on the list of `FieldTimeData` objects. This will add up the signals from all field time monitors included in simulation before searching for resonances.



```python
from tidy3d.plugins.resonance import ResonanceFinder

resonance_finder = ResonanceFinder(freq_window=(190e14, 210e14))
resonance_data = resonance_finder.run(signals=sim_data.data)
resonance_data.to_dataframe()

```





The `run()` method returns an `xr.Dataset` containing the decay rate, Q factor, amplitude, phase, and estimation error for each resonance as a function of frequency.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/ResonanceFinder/) for more details on the `ResonanceFinder` plugin.
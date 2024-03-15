# How can I plot the source spectrum?

| Date       | Category    |
|------------|-------------|
| 2023-12-11 18:47:30 | Sources |


When defining a source, you must specify a source time profile, typically Gaussian. For example, we can define a plane wave as



```python

plane_wave = td.PlaneWave(
  source_time=td.GaussianPulse(freq0=freq0, fwidth=0.5 * freqw),
  size=(td.inf, td.inf, 0),
  center=(0, 0, 0.3 * lda0),
  direction="-",
  pol_angle=0,
)

```



Here, the source time is a Gaussian pulse with central frequency `freq0` and frequency width `0.5 * freqw`. To visualize the spectrum it gives, we can use the `plot_spectrum` method by



```python

plane_wave.source_time.plot_spectrum(
  times=np.linspace(0, sim.run_time, 2000), val="abs"
)
plt.show()

```



Here, we need to specify the sampled time instances. To ensure the source spectrum is plotted correctly, we need to ensure the time sampling is sufficiently fine and the end time is sufficiently long compared to the pulse width.
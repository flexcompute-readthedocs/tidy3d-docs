# How do I get the coupling efficiency of a specific waveguide mode?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 17:05:41 | Monitors |


The coupling efficiency of a specific waveguide mode can be calculated from the mode monitor data by first extracting the complex mode amplitude and then taking the square modulus. 



```python

# extract the complex mode amplitude from the mode monitor data
amp = sim_data["mode"].amps.sel(mode_index=0, direction="+")

# compute the coupling efficiency
T = np.abs(amp)**2

```



As an example, you can reference the waveguide Y junction [case study](https://www.flexcompute.com/tidy3d/examples/notebooks/YJunction/).
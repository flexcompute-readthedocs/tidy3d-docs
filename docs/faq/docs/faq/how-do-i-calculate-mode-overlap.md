# How do I calculate mode overlap?

| Date       | Category    |
|------------|-------------|
| 2023-12-19 19:11:53 | Monitors |


Very often we want to calculate the overlap integral of two modes to compute the coupling efficiency. This can be done conveniently using the outer\_dot method such as 



```python

overlap = waveguide_mode_data_1.outer_dot(waveguide_mode_data_2)

```



where <code markdown class="language-plaintext">waveguide_mode_data_1</code> and <code markdown class="language-plaintext">waveguide_mode_data_2</code> are ModeSolverData objects from performing the mode solving. 

For advanced monitor data manipulation such as integration, please refer to the [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/XarrayTutorial/).
# What source bandwidth should I use for my simulation?

| Date       | Category    |
|------------|-------------|
| 2023-12-04 18:52:21 | Sources |


Tidy3D's broadband source feature is designed to produce the most accurate results in the frequency range of `(freq0 - 1.5 * fwidth, freq0 + 1.5 * fwidth)`. Therefore, it is necessary to define the source center frequency `freq0` and bandwidth `fwidth` to properly cover the desired application frequency range. For example, if the user wants to adjust the source bandwidth to cover a wavelength range between `wl_min` and `wl_max`, the source bandwidth can be defined as: `fwidth = alpha * (C_0/wl_max - C_0/wl_min)`, where `alpha` is a constant typically chosen between 1/3 and 1/2 to ensure accurate results.

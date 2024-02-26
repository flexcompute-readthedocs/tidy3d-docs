---
title: What source bandwidth should I use for my simulation?
date: 2023-12-04 18:52:21
enabled: true
category: "Sources"
---
Tidy3D's broadband source feature is designed to produce the most accurate results in the frequency range of&nbsp;`(freq0 - 1.5 * fwidth, freq0 + 1.5 * fwidth)`. Therefore, it is necessary to define the source center frequency&nbsp;`freq0`&nbsp;and bandwidth&nbsp;`fwidth`&nbsp;to properly cover the desired application frequency range. For example, if the user wants to adjust the source bandwidth to cover a wavelength range between&nbsp;`wl_min`&nbsp;and&nbsp;`wl_max`, the source bandwidth can be defined as:&nbsp;`fwidth = alpha * (C_0/wl_max - C_0/wl_min)`, where&nbsp;`alpha`&nbsp;is a constant typically chosen between 1/3 and 1/2 to ensure accurate results.

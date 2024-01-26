# How do I specify mappings between scattering matrix elements?

| Date       | Category    |
|------------|-------------|
| 2023-12-20 18:30:12 | Scattering Matrix |


You can specify mappings between scattering matrix elements that you want to be equal up to a multiplicative factor. You can define these as `element_mappings` in the [tidy3d.plugins.smatrix.ComponentModeler](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.smatrix.ComponentModeler.html).

"Indices" are defined as a tuple of `(port_name: str, mode_index: int)`

"Elements" are defined as a tuple of output and input indices, respectively.

The element mappings are therefore defined as a tuple of `(element, element, value)` where the first `element` is set by the value of the 2nd `element` times the supplied `value`.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/SMatrix/) for more details on computing the scattering matrix.
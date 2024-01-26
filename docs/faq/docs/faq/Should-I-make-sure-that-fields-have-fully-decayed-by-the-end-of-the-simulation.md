# Should I make sure that fields have fully decayed by the end of the simulation?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 17:36:08 | Simulation Troubleshoot |


Conversely to early termination, you may sometimes get a warning that
the fields remaining in the simulation at the end of the run have not
decayed down to the pre-defined shutoff value. This should **usually**
be avoided (that is to say, `Simulation.run_time`{: .interpreted-text
role="py:obj"} should be increased), but there are some cases in which
it may be inevitable. The important thing to understand is that in such
simulations, frequency-domain results cannot always be trusted. The
frequency-domain response obtained in the FDTD simulation only
accurately represents the continuous-wave response of the system if the
fields at the beginning and at the end of the time stepping are (very
close to) zero. That said, there could be non-negligible fields in the
simulation yet the data recorded in a given monitor can still be
accurate, if the leftover fields will no longer be passing through the
monitor volume. From the point of view of that monitor, fields have
already fully decayed. However, there is no way to automatically check
this. The accuracy of frequency-domain monitors when fields have not
fully decayed is also discussed in one of our [FDTD 101
videos](/fdtd101/Lecture-3-Applying-FDTD-to-Photonic-Crystal-Slab-Simulation/).

The main use case in which you may want to ignore this warning is when
you have high-Q modes in your simulation that would require an extremely
long run time to decay. In that case, you can use the the
[ResonanceFinder](https://docs.flexcompute.com/projects/tidy3d/en/latest/_autosummary/tidy3d.plugins.resonance.ResonanceFinder.html#tidy3d.plugins.resonance.ResonanceFinder) plugin to analyze the
modes, as well as field monitors with apodization to capture the modal
profiles. The only thing to note is that the normalization of these
modal profiles would be arbitrary, and would depend on the exact run
time and apodization definition. An example of such a use case is
presented in our high-Q photonic crystal cavity [case
study](/tidy3d/examples/notebooks/OptimizedL3/).

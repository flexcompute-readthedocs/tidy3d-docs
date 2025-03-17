.. currentmodule:: tidy3d

Sources
=======
In order to inject electromagnetic fields into the simulation domain, we need to specify a source. 
Thus, Tidy3D provides a variety of sources, including point dipoles, plane waves, Gaussian beams, and many more.

Types of Sources
----------------

Point Dipole
""""""""""""
A point dipole is a localized (zero size) electromagnetic source that radiates fields symmetrically around a small oscillating charge separation.
The source corresponds to an infinitesimal antenna with a fixed current density,
and is slightly different from a related definition that is used in some contexts, namely an oscillating electric or magnetic dipole.
The two are related through a factor of omega ** 2 in the power normalization, where omega is the angular frequency of the oscillation.

You can define a dipole using the ``PointDipole`` and ``GaussianPulse`` classes:

.. code-block:: python

   from tidy3d import GaussianPulse
   pulse = GaussianPulse(freq0=200e12, fwidth=20e12)
   pt_dipole = PointDipole(center=(1,2,3), source_time=pulse, polarization='Ex')


Uniform Current Source
""""""""""""""""""""""
Source in a rectangular volume with uniform time dependence.

Inputting the parameter ``size=(0,0,0)`` defines the equivalent of a point source:

.. code-block:: python

   from tidy3d import GaussianPulse
   pulse = GaussianPulse(freq0=200e12, fwidth=20e12)
   pt_source = UniformCurrentSource(size=(0,0,0), source_time=pulse, polarization='Ex')


Plane Wave
""""""""""
A plane wave is an electromagnetic wave with uniform amplitude and phase across any plane perpendicular to its direction of propagation.
It is an idealized wave often used in simulations to approximate free-space propagation and analyze how waves interact with materials.

Mode Source
"""""""""""
A mode source excites specific electromagnetic modes in waveguides or resonant structures.
It is highly useful in photonics and microwave engineering to study guided wave propagation,
ensuring that only a particular mode is launched into a device which avoids radiating EM waves into the surroundings.

Gaussian Beam
"""""""""""""
A Gaussian beam is a focused beam of electromagnetic radiation with an intensity profile that follows a Gaussian function.
It has very well-defined propagation characteristics, including a minimum beam waist and predictable divergence.

Astigmatic Gaussian Beam
""""""""""""""""""""""""
On the other hand, an astigmatic Gaussian beam has different focal points along two orthogonal axes, leading to an elliptical beam shape.
This occurs due to asymmetric optical elements or cylindrical focusing, making it important in laser systems where precise beam shaping is required.

Custom Field Source
"""""""""""""""""""
A custom field source allows for the direct specification of arbitrary electric or magnetic field distributions.
This is useful in simulations where the predefined sources above are insufficient.

Custom Current Source
"""""""""""""""""""""
Analogous to the custom field source, a custom current source allows for the direct specification of arbitrary current distributions.
It is particularly useful for simulating antennas, current-driven devices, or any scenario where precise control over source currents is necessary.

TFSF (Total-Field / Scattered-Field)
""""""""""""""""""""""""""""""""""""
The TFSF method separates the total field region, where an incident wave is defined,
from the scattered field region, where only the scattered components exist.
This technique is widely used in computational electromagnetics to analyze scattering problems while avoiding interference from the incident wave.


For more information, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.PointDipole
   tidy3d.UniformCurrentSource
   tidy3d.PlaneWave
   tidy3d.ModeSource
   tidy3d.GaussianBeam
   tidy3d.AstigmaticGaussianBeam
   tidy3d.CustomFieldSource
   tidy3d.CustomCurrentSource
   tidy3d.TFSF


Source Time Dependence
----------------------

Gaussian Pulse
""""""""""""""

Continuous Wave
"""""""""""""""

Custom Source Time
""""""""""""""""""




For more information on the time dependence of sources, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.GaussianPulse
   tidy3d.ContinuousWave
   tidy3d.CustomSourceTime


Angled Plane Wave Specifications
--------------------------------

Fixed In Plane Wavevector
""""""""""""""""""""""""

Fixed Angle Wave
""""""""""""""""


For more information on angled plane waves, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.FixedInPlaneK
   tidy3d.FixedAngle

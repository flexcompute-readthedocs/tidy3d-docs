.. currentmodule:: tidy3d

EM Mediums
==========
Structures within the simulation are made of mediums through which electromagnetic (EM) fields propagate,
and different materials exhibit unique properties such as the relative permittivity (:math:`\epsilon`), permeability (:math:`\mu`), and conductivity (:math:`\sigma`)
that influence this process. Here, the relative permittivity (:math:`\epsilon`) measures a material's ability to polarize in response to an electric field,
essentially dictating how much electric energy the material can store. The permeability (:math:`\mu`) quantifies the material's support for magnetic field formation
and thus affects how magnetic flux is established within it. And the conductivity (:math:`\sigma`) indicates how easily electrical charges move through the material,
leading to energy losses via heating. Collectively, these parameters determine how EM waves slow down, are reflected, absorbed, and *distorted* as they travel through different mediums.

Tidy3D classifies mediums into the following categories:

+ :ref:`Non-dispersive mediums <non-dispersive-medium>`, where :math:`\epsilon`, :math:`\mu` are constant with frequency.
+ :ref:`Dispersive mediums <dispersive-medium>`, where :math:`\epsilon`, :math:`\mu` are functions of frequency.
+ :ref:`Medium perturbations <medium-perturbations>`, where :math:`\epsilon`, :math:`\mu` are functions of position.
+ :ref:`General mediums <general-medium>`, which can be both dispersive and non-dispersive.

You can further modify mediums by specifying various nonlinear (:class:`NonlinearSpec`) and 
time-modulation effects (:class:`ModulationSpec`), both spatially uniform and spatially varying.
It is also possible to fit the parameters of dispersive models to experimental data using :class:`SurfaceImpedanceFitterParam`.

Lastly, we provide a :class:`tidy3d.components.material.multi_physics.MultiPhysicsMedium` class, which allows for the combinination of different fields (electric, magnetic, thermal, etc.) in a single simulation.

To get started with predefined materials, see our `Material Collection <material_library.html>`_ and `RF Material Library <rf_material_library.html>`_.


.. image:: /_static/img/mediums_overview.png
   :align: center
   :width: 100%
   :class: mt-3


.. _non-dispersive-medium:

Non-Dispersive Medium
---------------------
In a non-dispersive medium, the electric permittivity (:math:`\epsilon`) and magnetic permeability (:math:`\mu`) are constant with respect to frequency,
meaning that wave speed remains uniform. In other words, regardless of the signal's frequency, the material responds in the same way.
That is because these are non-conductive materials where free charge movement is negligible. 
In FDTD, this simplifies the update equations because you don't need to account for history or "memory effects" (i.e., convolution with a response function).
Still, this is a good starting point for most simulations as it still allows to accurately predict phenomena like refraction and reflection at boundaries.

Spatially Uniform
^^^^^^^^^^^^^^^^^
In the spatially uniform case, the material properties (:math:`\epsilon`, :math:`\mu`) are the same everywhere.
This represents a homogeneous medium where every cell in your simulation grid has identical electromagnetic properties.

Medium
""""""
A basic class for a dispersion-less medium where the displacement field :math:`\mathbf{D}(t)`
reacts instantaneously to the applied electric field :math:`\mathbf{E}(t)`

.. math::

   \mathbf{D}(t) = \epsilon \mathbf{E}(t)

is the :class:`tidy3d.components.medium.Medium` class.

For example, this is how you would define a dielectric medium:

.. code-block:: python

   dielectric = Medium(permittivity=4.0, name='my_medium')
   eps = dielectric.eps_model(200e12)

Here we define a dielectric medium with a relative permittivity of 4.0 and name it ``my_medium`` in the first line
and then evaluate the complex-valued permittivity at 200 THz in the second line. Below is a complete example of a simulation
with a dielectric cube at the center of the simulation domain.

.. code-block:: python

   # imports
   import numpy as np
   import matplotlib.pylab as plt
   import tidy3d as td
   import tidy3d.web as web

   # set up parameters of simulation (length scales are micrometers)
   freq0 = td.C_0 / 0.75

   # create a dielectric medium
   dielectric = td.Medium(permittivity=2.0)

   # create a square structure using the dielectric medium
   square = td.Structure(
      geometry=td.Box(center=(0, 0, 0), size=(1.5, 1.5, 1.5)), 
      medium=dielectric
   )

   # create source
   source = td.PointDipole(
      center=(-1.5, 0, 0),
      source_time=td.GaussianPulse(freq0=freq0, fwidth=freq0 / 10.0),
      polarization="Ey",
   )

   # create monitor
   monitor = td.FieldMonitor(
      size=(td.inf, td.inf, 0),
      freqs=[freq0],
      name="fields",
      colocate=True,
   )

   # define the complete simulation
   sim = td.Simulation(
      size=(4, 3, 3),
      grid_spec=td.GridSpec.auto(min_steps_per_wvl=25),
      structures=[square],
      sources=[source],
      monitors=[monitor],
      run_time=120/freq0,
   )

   # run simulation
   data = td.web.run(sim, task_name="medium_demo", path="data/data.hdf5", verbose=True)

   # plot the field data stored in the monitor
   ax = data.plot_field("fields", "Ey", z=0)

This will return the image of the electric field :math:`E_y` in the :math:`x,z`-plane,
with the dielectric medium at the center of the simulation and the source left to it.

.. image:: /_static/img/mediums_1.png
   :align: right
   :width: 50%
   :class: mt-3

Note how the medium can be defined as a parameter to the :class:`tidy3d.Structure` class.
This allows us to reuse the same dielectric medium for multiple structures and helps both with creating more complex structures as well as more complex mediums.

.. note::

   To better understand the :class:`tidy3d.Medium` class and mediums in general, it is useful to know that this class inherits
   from the :class:`tidy3d.AbstractMedium` class (see :ref:`AbstractMedium <abstract-medium>`) which includes
   several common attributes in mediums. Below is some information on these core properties as well as the arguments for modifications.


Lossy Metal Medium
""""""""""""""""""
Metals are electrically conductive, leading to energy loss through ohmic heating.
The non-zero conductivity (:math:`\sigma`) causes attenuation of the propagating wave, and the phase can be shifted.
FDTD simulations must account for these losses to predict how much signal is damped over distance.


Surface Impedance Boundary Condition (SIBC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SIBC is used to model the interaction of electromagnetic waves with surfaces, typically thin, 
conductive, or lossy materials, without having to discretely model the material's interior.
Instead of meshing through the entire depth of a material (which could require extremely fine resolution due to the skin effect),
SIBC applies an effective boundary condition at the surface. This condition links the tangential components of the electric field (:math:`\mathbf{E}_t`)
and the magnetic field (:math:`\mathbf{H}`) through the surface impedance (:math:`Z_s`), commonly expressed as:

.. math::
   
   \mathbf{E}_t = Z_s (\mathbf{n} \times \mathbf{H})

Here, :math:`\mathbf{n}` is the unit normal vector at the surface. The impedance :math:`Z_s` encapsulates the material's response,
accounting for losses and the skin effect, and it may be complex and frequency-dependent.
This approach greatly reduces computational cost while still capturing the essential physics of how the material interacts with incident EM fields.

.. note::

   The SIBC is most accurate when the skin depth is much smaller than the structure feature size.
   If this condition is not met, use a regular medium instead,
   or set ``simulation.subpixel.lossy_metal`` to ``td.VolumetricAveraging()`` or ``td.Staircasing()``.

This class inherits from :class:`tidy3d.Medium`.
You can define a lossy metal medium with a conductivity of 10 S/m and a frequency range of 9-10 GHz as such:

.. code-block:: python

   lossy_metal = LossyMetalMedium(conductivity=10, frequency_range=(9e9, 10e9))


Perfect Electric Conductor (PEC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A PEC is an idealized material with infinite conductivity, i.e. it offers no resistance to electric current.
In such a conductor, electromagnetic fields cannot penetrate, and the tangential component of the electric field
at the conductor's surface must be zero.

Although real metals at optical frequencies are not perfect conductors, PECs are still widely used in FDTD simulations for a few key reasons:

+ **Boundary Conditions:** In FDTD, a PEC boundary condition enforces zero tangential electric field on the boundary, 
  causing perfect reflection of incident waves. This simplifies simulations by eliminating the need to model
  the fields inside highly conductive regions.  
+ **Reflectors/Waveguides:** PEC boundaries are used to approximate perfect mirrors or to represent the walls of waveguides and cavities, 
  where negligible penetration of the field is a good approximation.
+ **Computational Efficiency:** By treating a surface as a PEC,
  one avoids the fine spatial discretization required to resolve skin depths in real metals, especially at high frequencies, 
  thereby reducing computational cost.


The :class:`tidy3d.PECMedium` class inherits from :class:`tidy3d.AbstractMedium` class.

.. note::

   To avoid confusion from duplicate PECs, one must import the :class:`tidy3d.PEC` instance directly.


Fully Anisotropic Medium
""""""""""""""""""""""""
For many practical applications, parameters like the permittivity and conductivity are assumed to be isotropic,
meaning they have the same value in all directions.
In more complex scenarios however, materials can be anisotropic, with their electromagnetic response varying with direction. 
The :class:`tidy3d.FullyAnisotropicMedium` class allows for the specification of a fully anisotropic medium,
including all 9 components of the permittivity and conductivity tensors. 
Note that the provided permittivity tensor and the symmetric part of the conductivity tensor must have coinciding main directions.
A non-symmetric conductivity tensor can be used to model magneto-optic effects.

You can define a fully anisotropic medium with a permittivity tensor and a conductivity tensor as follows:

.. code-block:: python

   perm = [[2, 0, 0], [0, 1, 0], [0, 0, 3]] # permittivity tensor
   cond = [[0.1, 0, 0], [0, 0, 0], [0, 0, 0]] # conductivity tensor
   anisotropic_dielectric = FullyAnisotropicMedium(permittivity=perm, conductivity=cond)

Easy! In practice, implementing fully anisotropic materials is more involved though. Please refer to the example notebooks below:

.. seealso::

   :doc:`/_docs/notebooks/FullyAnisotropic`,
   :doc:`/_docs/notebooks/AdiabaticCouplerLN`,
   :doc:`/_docs/notebooks/SWGBroadbandPolarizer`,
   :doc:`/_docs/notebooks/AnisotropicMetamaterialBroadbandPBS`,

.. note::

   Dispersive properties and subpixel averaging are currently not supported for fully anisotropic materials.

.. note::

   Simulations involving fully anisotropic materials are computationally more intensive, thus, 
   they take longer time to complete. This increase strongly depends on the filling fraction of the simulation
   domain by fully anisotropic materials, varying approximately in the range from 1.5 to 5.
   The cost of running a simulation is adjusted correspondingly.

And for further information on non-dispersive mediums in general, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.Medium
   tidy3d.LossyMetalMedium
   tidy3d.PECMedium
   tidy3d.FullyAnisotropicMedium

Spatially Varying
^^^^^^^^^^^^^^^^^
Here, although :math:`\epsilon` and :math:`\mu` are constant in frequency, their values can change from one location to another.
This is used to model inhomogeneous materials where different regions have different constants, 

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.CustomMedium

Fitting Parameters
^^^^^^^^^^^^^^^^^^
In some cases, even for non-dispersive models, one might adjust :math:`\epsilon` and :math:`\mu` (or related parameters) to better fit experimental data.
These "fitting parameters" are tuned to match the actual behavior of the material under study.

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.SurfaceImpedanceFitterParam


.. _dispersive-medium:

Dispersive Mediums
------------------
In contrast to non-dispersive materials, a dispersive medium has permittivity and permeability that depend on the frequency.
This frequency dependence means that different spectral components of a pulse will travel differently, often leading to pulse broadening or distortion.

Dispersive materials have properties (particularly permittivity) that vary with frequency.
This frequency dependence means that different spectral components of a pulse travel at different speeds, causing dispersion.
In practical terms, this leads to pulse broadening and scattering—effects that are critical in high-speed communications and optical applications.
FDTD implementations often use models like the Drude, Lorentz, or Debye formulations to capture this behavior accurately.

Material dispersion occurs because the material's polarization does not react instantaneously to an applied electric field :math:`\mathbf{E}`.
This delayed response is incorporated into FDTD simulations by modifying the constitutive relation :math:`\mathbf{D} = \varepsilon \mathbf{E}`. Specifically, it is rewritten as:

.. math::

   \mathbf{D} = \varepsilon_{\infty} \mathbf{E} + \mathbf{P}

Here, :math:`\varepsilon_{\infty}` represents the instantaneous dielectric response (the high-frequency limit of the permittivity) and must be positive.
The remaining term, :math:`\mathbf{P}`, accounts for the frequency-dependent polarization within the material.
The behavior of :math:`\mathbf{P}` over time is governed by its own evolution equation, which ultimately defines how the permittivity :math:`\varepsilon(\omega)` varies with frequency.

Spatially Uniform
^^^^^^^^^^^^^^^^^
Here, the dispersion characteristics (i.e., the frequency dependence of :math:`\epsilon` and :math:`\mu`) are the same throughout the simulation space.
Still, there are many different models for the frequency dependence of :math:`\epsilon` and :math:`\mu`!

Pole Residue
""""""""""""
In many dispersion models, the frequency-dependent response is represented by poles in the complex frequency plane. 
Each pole corresponds to a natural resonance of the system, and the residue associated with each pole indicates the strength or weight of that resonance.
When you write a dispersion relation as a sum of contributions from several poles, you get an expression like:

.. math::

   \epsilon(\omega) = \epsilon_\infty - \sum_i \left[\frac{c_i}{j \omega + a_i} + \frac{c_i^*}{j \omega + a_i^*}\right]

Here, :math:`a_i` are the pole frequencies, :math:`c_i` are the residues, and :math:`a_i^*` are the complex conjugates of the pole frequencies.
This form is useful for breaking down complex material responses into simpler, resonant components.

Example:

.. code-block:: python

   pole_res = PoleResidue(eps_inf=2.0, poles=[((-1+2j), (3+4j)), ((-5+6j), (7+8j))])
   eps = pole_res.eps_model(200e12)


Lorentz
"""""""
The Lorentz model describes how bound electrons in a material respond to an oscillating electric field.
It treats electrons like harmonic oscillators that are displaced by the field. The model gives the permittivity as:

.. math::

   \epsilon(f) = \epsilon_\infty + \sum_i \frac{\Delta\epsilon_i f_i^2}{f_i^2 - 2jf\delta_i - f^2}

where :math:`\epsilon_\infty` is the permittivity at high frequencies,
:math:`\Delta\epsilon_i` is the difference in permittivity at the plasma frequency,
:math:`f_i` is the plasma frequency, and
:math:`\delta_i` is the damping rate.

For example:

.. code-block:: python

   lorentz_medium = Lorentz(eps_inf=2.0, coeffs=[(1,2,3), (4,5,6)])
   eps = lorentz_medium.eps_model(200e12)


Sellmeier
"""""""""
The Sellmeier equation is an empirical formula used to describe the wavelength dependence of the refractive index 
:math:`n` of a material. It typically takes the form:

.. math::

   n(\lambda)^2 = 1 + \sum_i \frac{B_i \lambda^2}{\lambda^2 - C_i}

where :math:`B_i` and :math:`C_i` are coefficients determined by experiments.

For lossless, weakly dispersive materials, the best way to incorporate the dispersion without doing complicated fits
and without slowing the simulation down significantly is to provide the value of the refractive index dispersion 
in :func:`tidy3d.Sellmeier.from_dispersion()`.
The value is assumed to be at the central frequency or wavelength (whichever is provided),
and a one-pole model for the material is generated.

For example:

.. code-block:: python

   sellmeier_medium = Sellmeier(coeffs=[(1,2), (3,4)])
   eps = sellmeier_medium.eps_model(200e12)


Drude
"""""
The Drude model describes the electrical response of free electrons in a conductor (or plasma).
It assumes that these electrons move freely and occasionally collide with fixed ions.
The permittivity in the Drude model is given by:

.. math::

   \epsilon(f) = \epsilon_\infty - \sum_i \frac{ f_i^2}{f^2 + jf\delta_i}

For example:

.. code-block:: python

   drude_medium = Drude(eps_inf=2.0, coeffs=[(1,2), (3,4)])
   eps = drude_medium.eps_model(200e12)


Debye
"""""
The Debye model describes the dielectric relaxation of polar molecules in a medium.
It explains how the polarization of a material responds to a changing electric field,
especially in the context of slow, relaxational processes. We define it as:

.. math::

   \epsilon(f) = \epsilon_\infty + \sum_i \frac{\Delta\epsilon_i}{1 - jf\tau_i}

where :math:`\epsilon_\infty` is the high-frequency permittivity (as frequency approaches infinity),
:math:`\Delta\epsilon_i` is the difference between static and high-frequency permittivity for each relaxation process,
and :math:`\tau_i` is the relaxation time for each process, indicating how fast the material's polarization can respond.
This model is particularly useful for understanding the behavior of liquids and polymers.

Example:

.. code-block:: python
   
   debye_medium = Debye(eps_inf=2.0, coeffs=[(1,2),(3,4)])
   eps = debye_medium.eps_model(200e12)

In this example, `eps_inf=2.0` sets the high-frequency permittivity to 2.0, and `coeffs=[(1,2),(3,4)]` specifies two Debye relaxation processes:
the first with :math:`\Delta\epsilon_1 = 1` and :math:`\tau_1 = 2`, and the second with :math:`\Delta\epsilon_2 = 3` and :math:`\tau_2 = 4`.

For more information on spatially uniform dispersive models, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.PoleResidue
   tidy3d.Lorentz
   tidy3d.Sellmeier
   tidy3d.Drude
   tidy3d.Debye


Spatially Varying
^^^^^^^^^^^^^^^^^
Of course, the dispersion properties can vary from region to region as well.
Thus Tidy3D extends the spatially uniform dispersive models above to spatially varying ones.

For more information on spatially varying dispersive models, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.CustomPoleResidue
   tidy3d.CustomLorentz
   tidy3d.CustomSellmeier
   tidy3d.CustomDrude
   tidy3d.CustomDebye


.. _medium-perturbations:


Medium Perturbations
--------------------
Similarly, there can be minor perturbations of the medium where the base material properties are modified by small spatial variations.
In other words, :math:`\epsilon` and :math:`\mu` are functions of position,
representing slight deviations or "perturbations" from an otherwise uniform medium.
This is particularly useful for studying defects, interfaces, or localized changes within a material.

For more information on medium perturbations, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.PerturbationMedium
   tidy3d.PerturbationPoleResidue


.. _general-medium:


General Mediums
---------------
Where previously we have seen spatially uniform and spatially varying dispersive and non-dispersive mediums,
a general medium can include both dispersive and non-dispersive components.
This flexibility allows you to model materials that have a baseline response (non-dispersive) along with additional frequency-dependent behavior (dispersive).
As with the other cases, these properties can be spatially uniform or spatially varying.

Spatially Uniform
^^^^^^^^^^^^^^^^^

Anisotropic Medium
""""""""""""""""""
In three dimensions, the permittivity and permeability tensors are 3x3 matrices.
We can use the :class:`tidy3d.AnisotropicMedium` class to specify different permittivities along different directions.

Example:

.. code-block:: python

   medium_xx = Medium(permittivity=4.0)
   medium_yy = Medium(permittivity=4.1)
   medium_zz = Medium(permittivity=3.9)
   anisotropic_dielectric = AnisotropicMedium(xx=medium_xx, yy=medium_yy, zz=medium_zz)

Medium2D
""""""""
This is a 2D diagonally anisotropic medium. For example, for in-plane propagation, this means the refractive index varies along the 
:math:`x` and :math:`y` directions, affecting light propagation differently in each direction.
This anisotropy can be used to control birefringence, waveguiding, or polarization-dependent effects.

Example using the Drude model:

.. code-block:: python

   drude_medium = Drude(eps_inf=2.0, coeffs=[(1,2), (3,4)])
   medium2d = Medium2D(ss=drude_medium, tt=drude_medium)


For more information on spatially uniform general mediums, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.AnisotropicMedium
   tidy3d.Medium2D


Spatially Varying
^^^^^^^^^^^^^^^^^
Once again, when the properties change with position, Tidy3D provides the :class:`tidy3d.CustomAnisotropicMedium` class.

For more information on spatially varying general mediums, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.CustomAnisotropicMedium


Medium Specifications
---------------------
The medium specificatins allow you to add properties to an existing medium, notably nonlinearities and time-modulations.

Nonlinear
^^^^^^^^^
Nonlinear effects in optics and photonics arise when a material's response to an electromagnetic field
depends on the field's intensity rather than simply being proportional to it.
This leads to phenomena such as frequency mixing, harmonic generation, self-focusing,
and optical switching—capabilities that are not possible in strictly linear media.

.. image:: /_static/img/SHG_BBO.png
   :align: right
   :width: 40%
   :class: mt-3

For example, the image on the right shows second harmonic generation (SHG) in a Beta Barium Borate (BBO) crystal, 
a commonly used nonlinear optical material. The red waves represent the fundamental light at frequency :math:`\omega` entering (and partially exiting) the crystal,
and the blue wave denotes the second harmonic light at frequency :math:`2\omega` that is generated inside the crystal.
BBO is favored for SHG because it has a relatively large second-order nonlinear susceptibility (:math:`\chi^{(2)}`) and a wide transparency range,
allowing efficient frequency conversion from the fundamental to the second harmonic.


In nonlinear FDTD simulations, the dielectric permittivity can itself be modified by the electric field. 
In general, the change in permittivity can be expressed as a power series in the electric field components:

.. math::

   \Delta\epsilon_{ij} = \sum_k \chi^{(2)}_{ijk} E_k + \sum_{k,\ell} \chi^{(3)}_{ijk\ell} E_k E_\ell + \cdots


Here, :math:`\Delta\epsilon_{ij}` represents the change in the tensor element at position :math:`i,j`,
while the :math:`\chi` terms are the nonlinear susceptibilities.
The first-order nonlinear term (with :math:`\chi^{(2)}`) corresponds to the Pockels effect,
which describes a linear response of the material polarization to the electric field,
whereas the second term (with :math:`\chi^{(3)}`) represents the Kerr effect, describing a quadratic (hence nonlinear) response.

Nonlinear Specifications
""""""""""""""""""""""""
The :class:`tidy3d.NonlinearSpec` class is an abstract specification for adding nonlinearities to a medium.

.. note::

   The nonlinear constitutive relation is solved iteratively; it may not converge for strong nonlinearities. Increasing num_iters can help with convergence.

Example:

.. code-block:: python

   nonlinear_susceptibility = NonlinearSusceptibility(chi3=1)
   nonlinear_spec = NonlinearSpec(models=[nonlinear_susceptibility])
   medium = Medium(permittivity=2, nonlinear_spec=nonlinear_spec)


NonlinearSusceptibility
"""""""""""""""""""""""
The :class:`tidy3d.NonlinearSusceptibility` class is a specification for a nonlinear susceptibility with the nonlinear polarization given by:

.. math::

   P_{NL} = \varepsilon_0 \chi_3 |E|^2 E

For complex fields (e.g. when using Bloch boundary conditions), the nonlinearity is applied separately to the real and imaginary parts, 
so that the above equation holds when both :math:`E` and :math:`P_{NL}` are replaced by their real or imaginary parts. 
The nonlinearity is only applied to the real-valued fields since they are the physical fields.

Different field components do not interact nonlinearly. For example, when calculating :math:`P_{NL}`, we approximate :math:`|E|^2 \approx |E_x|^2`.
This approximation is valid when the field is predominantly polarized along one of the x, y, or z axes.

We can define a nonlinear susceptibility by specifying :math:`\chi_3`:

.. code-block:: python

   nonlinear_susceptibility = NonlinearSusceptibility(chi3=1)


.. note::

   The nonlinear constitutive relation is solved iteratively; it may not converge for strong nonlinearities.
   Increasing :func:`tidy3d.NonlinearSpec.num_iters` can help with convergence.

Kerr Nonlinearity
"""""""""""""""""
As mentioned above, Kerr nonlinearity is a phenomenon where the refractive index :math:`n` of a material changes
with the intensity of light passing through it. 

For an isotropic and instantaneous medium, the dominant nonlinear effect is captured by the third-order term.
Because the electric field's intensity :math:`I` is proportional to :math:`|\mathbf{E}|^2`, the refractive index :math:`n` can be written as:

.. math::

   n = n_0 + n_2 I,

where :math:`n_0` is the linear refractive index, :math:`n_2` is the Kerr coefficient, representing how strongly the refractive index changes with intensity,
and :math:`I \propto |\mathbf{E}|^2` is the light intensity.

In Tidy3D, the :class:`tidy3d.KerrNonlinearity` model is equivalent to a :class:`tidy3d.NonlinearSusceptibility`.
The relation between the parameters is given below.

.. math::

   P_{NL} = \varepsilon_0 \chi_3 |E|^2 E \\
   n_2 = \frac{3}{4 n_0^2 \varepsilon_0 c_0} \chi_3
 
 
In these equations, :math:`n_0` means the real part of the linear refractive index of the medium.
This expression shows that as the intensity increases, the refractive index changes accordingly.

The Kerr nonlinearity can simply be specified by the Kerr coefficient :math:`n_2`:

.. code-block:: python

   kerr_model = KerrNonlinearity(n2=1)


To simulate nonlinear loss, consider instead using a :class:`tidy3d.TwoPhotonAbsorption` model,
which implements a more physical dispersive loss of the form :math:`\chi_{TPA} = i \frac{c_0 n_0 \beta}{\omega} I`.


Two-Photon Absorption
"""""""""""""""""""""
Two-photon absorption (TPA) is a process where two photons, each with roughly half the energy required for an electronic transition, 
are absorbed simultaneously to excite a material. This process is nonlinear, its probability increases with the square of the light intensity,
and is crucial in advanced optical applications like high-resolution microscopy and the study of nonlinear optical phenomena.

Tidy3D provides the :class:`tidy3d.TwoPhotonAbsorption` class to model the two-photon absorption nonlinearity.
This class defines an intensity-dependent absorption given by

.. math::

   \alpha(\mathbf{E}) = \alpha + \beta |\mathbf{E}|^2.

This model also incorporates free-carrier absorption (FCA) and free-carrier plasma dispersion (FCPD) effects

.. math::

   P_{NL} = P_{TPA} + P_{FCA} + P_{FCPD}

with the nonlinear polarization terms for TPA and FCA:

.. math::

   P_{TPA} = -\frac{4}{3}\frac{c_0^2 \varepsilon_0^2 n_0^2 \beta}{2 i \omega} |E|^2 E \\
   P_{FCA} = -\frac{c_0 \varepsilon_0 n_0 \sigma N_f}{i \omega} E.


For the free-carrier plasma dispersion (FCPD) term, the free-carrier density :math:`N_f`
given the electron and hole concentrations :math:`N_e` and :math:`N_h` evolves according to:

.. math::

   \frac{dN_f}{dt} = \frac{8}{3}\frac{c_0^2 \varepsilon_0^2 n_0^2 \beta}{8 q_e \hbar \omega} |E|^4 - \frac{N_f}{\tau} \\
   N_e = N_h = N_f \\
   P_{FCPD} = \varepsilon_0 2 n_0 \Delta n (N_f) E \\
   \Delta n (N_f) = (c_e N_e^{e_e} + c_h N_h^{e_h})

We can define a two-photon absorption model by specifying :math:`\beta`:

.. code:: python

   tpa_model = TwoPhotonAbsorption(beta=1)


For complex fields (for example, when using Bloch boundary conditions),
the nonlinearity is applied separately to the real and imaginary parts.
In this case, the above equation holds when both :math:`E` and :math:`P_{NL}` are replaced by their real or imaginary components.
Note that the nonlinearity is applied only to the physical, real-valued fields.

Note again, as above, different field components do not interact nonlinearly.
For example, when calculating :math:`P_{NL}`, the approximation :math:`|E|^2 \approx |E_x|^2` is used.
This approximation is valid when the field is predominantly polarized along one of the x, y, or z axes.

For more information on medium specifications, see:

.. autosummary::
   :toctree: _autosummary/
   :template: module.rst

   tidy3d.NonlinearSpec
   tidy3d.NonlinearSusceptibility
   tidy3d.KerrNonlinearity
   tidy3d.TwoPhotonAbsorption


Time Modulation
^^^^^^^^^^^^^^^
We can not just vary the parameters of a medium spatially but also in time!
Tidy3D allows for this by adding a :class:`tidy3d.ModulationSpec` to the medium.

Time Modulation Specifications
""""""""""""""""""""""""""""""
You can use the :class:`tidy3d.ContinuousWaveTimeModulation` class to specify a continuous / harmonic wave time modulation.

Example:

.. code-block:: python

   cw = ContinuousWaveTimeModulation(freq0=200e12, amplitude=1, phase=0)

.. note::

   The space-time modulation must be separable in space and time. e.g. when applied to permittivity,
   :math:`\delta \epsilon(r, t) = \Re[amp\_time(t) \cdot amp\_space(r)]`.


Space Modulation
""""""""""""""""
Further, one may define the modulation profile with a user-supplied spatial distribution
of amplitude and phase as well.

For example:

.. code-block:: python

   Nx, Ny, Nz = 10, 9, 8
   X = np.linspace(-1, 1, Nx)
   Y = np.linspace(-1, 1, Ny)
   Z = np.linspace(-1, 1, Nz)
   coords = dict(x=X, y=Y, z=Z)
   amp = SpatialDataArray(np.random.random((Nx, Ny, Nz)), coords=coords)
   phase = SpatialDataArray(np.random.random((Nx, Ny, Nz)), coords=coords)
   space = SpaceModulation(amplitude=amp, phase=phase)

Here, we have defined a random amplitude and phase profile for the space modulation.
(The :class:`tidy3d.SpatialDataArray` class is a helper class to create a data array with the correct coordinates.)
The :class:`tidy3d.SpaceModulation` class can then be used to specify the space modulation.

For more information on time modulation, see:

.. autosummary::
   :toctree: _autosummary/

   tidy3d.ModulationSpec
   tidy3d.SpaceTimeModulation
   tidy3d.ContinuousWaveTimeModulation
   tidy3d.SpaceModulation

.. _abstract-medium:


Abstract Classes
================
Many of the mediums inherit from the abstract classes below. Hence, it is worth understanding their core properties.

Abstract Medium
---------------

Core Properties
^^^^^^^^^^^^^^^
``permittivity (Union[ConstrainedFloatValue, Box] = 1.0)``: This relative value (unitless) represents the material's ability
to polarize in response to an electric field, essentially determining how much electric energy the material can store.
The default value of 1.0 represents vacuum.

``conductivity (Union[float, Box] = 0.0)``: Measured in S/μm (Siemens per micrometer),
this parameter indicates how easily electrical charges move through the material, leading to energy losses via heating.
It affects the imaginary part of the complex permittivity at a given frequency.

``allow_gain (bool = False)``: This boolean parameter enables active mediums. 
When set to True, the medium can amplify electromagnetic waves rather than merely transmitting or absorbing them.
However, this comes with a caution: simulations with gain mediums are inherently unstable and likely to diverge.
Despite this risk, Tidy3D will still process and charge for such simulations, returning monitor data up to the point of divergence.

Medium Modifications
^^^^^^^^^^^^^^^^^^^^
Beyond these fundamental properties, you can enhance your medium with advanced characteristics:

``nonlinear_spec (Union[NonlinearSpec, NonlinearSusceptibility] = None)``: This optional parameter allows you to incorporate nonlinear effects
where the material's response depends on the field intensity. You can apply models like Kerr nonlinearity
or two-photon absorption to capture phenomena such as self-focusing or intensity-dependent absorption.

``modulation_spec (Optional[ModulationSpec] = None)``: This parameter enables you to introduce time-varying material properties,
allowing for effects like frequency conversion or parametric amplification through controlled modulation of the medium.

``viz_spec (Optional[VisualizationSpec] = None)``: This parameter provides customization options for how the medium appears in visualizations,
helping you to distinguish between different materials in complex geometries.


For more information on the abstract classes, see:

.. autosummary::
   :toctree: _autosummary/

   tidy3d.components.medium.AbstractMedium
   tidy3d.components.medium.AbstractPerturbationMedium
   tidy3d.components.medium.NonlinearModel


Multi-Physics Medium
====================
Finally, Tidy3D is currently in the process of adding more physical interactions to the FDTD simulations,
including heat transfer and charge-carrier transport!

You can use the :class:`tidy3d.MultiPhysicsMedium` class to specify the many multi-physical properties as defined for each solver medium.

For example:

.. code-block:: python

   import tidy3d as td
   SiO2 = td.MultiPhysicsMedium(
      optical=td.Medium(permittivity=3.9),
      charge=td.ChargeInsulatorMedium(permittivity=3.9), # redefining permittivity
      name="SiO2")

This imports the SiO2 medium with the optical properties of a dielectric, and the charge properties of a charge insulator.

A more indepth discussion can be found in the :ref:`charge-transfer-docs` and :ref:`heat-transfer-docs` documentation.

For more information on :class:`tidy3d.MultiPhysicsMedium` class, see:

.. autosummary::
   :toctree: _autosummary/

   tidy3d.components.material.multi_physics.MultiPhysicsMedium





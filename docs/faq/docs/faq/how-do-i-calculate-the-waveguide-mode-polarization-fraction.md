# How do I calculate the waveguide mode polarization fraction?

| Date       | Category    |
|------------|-------------|
| 2023-12-18 22:09:16 | Mode Solver |


You can follow the example below to obtain the waveguide mode polarization fraction of the optical modes calculated using the Tidy3D mode solver. We have considered a 500 x 220 nm silicon-on-insulator (SOI) waveguide operating at 1.55 $\mu$m.

 



```python
import numpy as np
from tidy3d.plugins.mode import ModeSolver
from tidy3d.plugins.mode.web import run as run_mode_solver

# Define the waveguide.
waveguide = tidy3d.Structure(
    geometry=tidy3d.Box(size=(tidy3d.inf, 0.5, 0.22)),
    medium=tidy3d.Medium(permittivity=3.47**2),
)

# Build a simulation object including the waveguide.
sim = tidy3d.Simulation(
    size=(10, 2.5, 1.5),
    grid_spec=tidy3d.GridSpec.auto(min_steps_per_wvl=20, wavelength=1.55),
    structures=[waveguide],
    run_time=1e-12,
    boundary_spec=tidy3d.BoundarySpec.all_sides(boundary=tidy3d.PML()),
)

# Plane where we want to solve the modes.
plane = tidy3d.Box(center=(0, 0, 0), size=(0, 2.5, 1.5))

# Mode specification.
mode_spec = tidy3d.ModeSpec(
  num_modes=4,
  target_neff=3.47,
  group_index_step=True,
)

# Build the mode solver.
freq0 = tidy3d.C_0 / 1.55
mode_solver = ModeSolver(
  simulation=sim,
  plane=plane,
  mode_spec=mode_spec,
  freqs=[freq0],
)

# Run the server-side mode solver.
mode_data = run_mode_solver(mode_solver)

# Get the mode waveguide polarization fraction.
print("TE waveguide polarization fraction:")
print(np.asarray(mode_data.pol_fraction_waveguide['te']).squeeze())

print("TM waveguide polarization fraction:")
print(np.asarray(mode_data.pol_fraction_waveguide['tm']).squeeze())

```



<blockquote>The TE and TM polarization fraction using the waveguide definition. If <code>E1</code> and <code>E2</code> are the electric field components along the two tangential axes and <code>En</code> is the component along the propagation direction, the TE fraction is defined as <code>1 - integrate(En.abs**2) / integrate(E1.abs**2 + E2.abs**2 + En.abs**2)</code>, and the <code>TM</code> fraction is defined as <code>1 - integrate(Hn.abs**2) / integrate(H1.abs**2 + H2.abs**2 + Hn.abs**2)</code>, with <code>H</code> denoting the magnetic field components.</blockquote>For more details on how to set up, run and visualize the solver results, please refer to this <a href="https://www.flexcompute.com/tidy3d/examples/notebooks/ModeSolver/">notebook</a>.
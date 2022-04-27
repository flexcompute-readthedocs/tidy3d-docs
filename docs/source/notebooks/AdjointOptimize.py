import numpy as np
import matplotlib.pylab as plt

import tidy3d as td
from tidy3d import web

# config
plot_structure = True
initial_solves = False

# wavelength and frequency
wavelength = 1.0
freq0 = td.C_0 / wavelength

# resolution control
dl = 0.02

# space between boxes and PML
buffer = 1.5 * wavelength

# initial size of boxes and waveguide
Lx, Ly = 5 * 9 / 7, 5
nx, ny = 9, 7

lx0, ly0, lz0 = Lx/nx, Ly/ny, 10 * dl
wg_width = .7

# simulation parameters
subpixel = False
pml_layers = (td.PML(),) * 3
shutoff = 1e-8
courant = 0.9

wg_eps = 2.75
deps = 0.3

# permittivity at each quadrant of box
quadrants = [f'x_{xi}_y_{yi}' for xi in range(nx) for yi in range(ny)]
permittivities = [wg_eps + deps * (np.random.random()-0.5) for xi in range(nx) for yi in range(ny)]

eps_boxes = {quad: eps for (quad, eps) in zip(quadrants, permittivities)}

# total size
Lx = nx * lx0 + 2 * buffer
Ly = ny * ly0 + 2 * buffer
Lz = lz0 + 2 * buffer

# position of source and monitor (constant for all)
source_x = -lx0*nx/2 - 1
meas_x = lx0*nx/2 + 1

# frequency width and run time
freqw = freq0 / 10
run_time = 10 / freqw

# polarization of initial source
pol = "Ey"

# monitor for plotting
monitor_field = td.FieldMonitor(
    center=[0, 0, 0],
    size=[td.inf, td.inf, 0],
    freqs=[freq0],
    name="field_pattern",
)

# default box center and sizes
center = np.array([0,0,0])#-1e-5, -1e-5, -1e-5])
center = np.array([-1e-5, -1e-5, -1e-5])

size = np.array([lx0, ly0, lz0])
ds = -0.0

num_modes = 4
mode_index = 2

measurement_monitor_name = 'measurement'

waveguide = td.Structure(
    geometry=td.Box(size=(td.inf, wg_width, lz0)),
    medium=td.Medium(permittivity=wg_eps)
)

def make_boxes(permittivities):
    boxes_quad = []
    quad_index = 0
    for xi in range(nx):
        for yi in range(ny):

            center_quad = center.tolist()
            center_quad[0] += lx0 / 2 - lx0 * nx / 2.0
            center_quad[1] += ly0 / 2 - ly0 * ny / 2.0
            size_quad = size.tolist()
            center_quad[0] += xi * lx0
            center_quad[1] += yi * ly0

            permittivity = permittivities[quad_index]
            name = quadrants[quad_index]

            box_quad = td.Structure(
                geometry=td.Box(center=center_quad, size=size_quad),
                medium=td.Medium(permittivity=permittivity),
                name=name,
            )
            boxes_quad.append(box_quad)

            quad_index += 1

    return boxes_quad


def make_sim_base(permittivities, include_field_mon=False):

    boxes_quad = make_boxes(permittivities)
    grad_monitors = []
    for structure in boxes_quad:
        grad_monitors.append(
            td.FieldMonitor(
                center=structure.geometry.center,
                size=structure.geometry.size,
                freqs=[freq0],
                name=structure.name,
            )
        )

    if include_field_mon:
        monitors = [monitor_field] + grad_monitors
    else:
        monitors = grad_monitors

    boxes_quad = make_boxes(permittivities)
    
    sim_base = td.Simulation(
        size=[Lx, Ly, Lz],
        grid_spec=td.GridSpec.uniform(dl=dl),
        # grid_spec=td.GridSpec.auto(wavelength=wavelength),
        structures=[waveguide] + boxes_quad,
        sources=[],
        monitors=monitors,
        run_time=run_time,
        subpixel=subpixel,
        pml_layers=pml_layers,
        shutoff=shutoff,
        courant=courant,
    )
    
    return sim_base

if plot_structure:
    sim_base = make_sim_base(permittivities)
    f, axes = plt.subplots(1, 3, tight_layout=True, figsize=(10, 5))
    for dim, ax in zip('xyz', axes):
        sim_base.plot(**{dim:0.0}, ax=ax)
    plt.show()


def make_sim_forward(permittivities, include_field_mon=False):
    
    sim_base = make_sim_base(permittivities, include_field_mon=include_field_mon)

    sim_forward = sim_base.copy(deep=True)

    mode_size = (0,4,3)

    # source seeding the simulation
    sim_forward.sources.append(
        td.ModeSource(
            source_time=td.GaussianPulse(freq0=freq0, fwidth=freqw),
            center=[source_x, 0, 0],
            size=mode_size,
            mode_index=0,
            direction="+"
        )
    )

    # monitor where we compute the objective function from
    measurement_monitor = td.ModeMonitor(
        center=[meas_x, 0, 0],
        size=mode_size,
        freqs=[freq0],
        mode_spec=td.ModeSpec(num_modes=num_modes),
        name=measurement_monitor_name,
    )

    sim_forward.monitors += [measurement_monitor]
    
    return sim_forward

if plot_structure:
    sim_forward = make_sim_forward(permittivities, include_field_mon=True)
    f, axes = plt.subplots(1, 3, tight_layout=True, figsize=(10, 5))
    for dim, ax in zip('xyz', axes):
        sim_forward.plot(**{dim:0}, ax=ax)
    plt.show()


def compute_objective(sim_data):
    """ Computes both the (complex-valued) electric fields at the measure point and the intensity (the objective function)."""

    # get the measurement monitor fields and positions
    measure_monitor = sim_data.simulation.get_monitor_by_name(measurement_monitor_name)
    measure_amp = sim_data[measurement_monitor_name].amps.sel(direction='+', mode_index=mode_index)
    
    # sum their absolute values squared to give intensity
    power = float(np.sum(np.abs(measure_amp)**2))

    # return both the complex-valued raw fields and the intensity
    return complex(measure_amp), power


def run_forward(permittivities, include_field_mon=False):
    sim_forward = make_sim_forward(permittivities, include_field_mon=include_field_mon)
    sim_data_forward = web.run(sim_forward, task_name='forward', path='data/forward.hdf5')
    return sim_data_forward


if initial_solves:
    sim_data_forward = run_forward(permittivities, include_field_mon=True)
    fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(8, 6))
    ax = sim_data_forward.plot_field('field_pattern', 'Ey', val='real', freq=freq0, ax=ax)


def make_sim_adjoint(permittivities, include_field_mon=False):
    
    sim_base = make_sim_base(permittivities, include_field_mon=include_field_mon)

    sim_forward = make_sim_forward(permittivities, include_field_mon=False)
    measurement_monitor = sim_forward.get_monitor_by_name(measurement_monitor_name)
    
    # measured_amp_forward, _ = compute_objective(sim_data_forward)

    adjoint_source = td.ModeSource(
        source_time=td.GaussianPulse(
            freq0=freq0,
            fwidth=freqw,
            # phase=float(+ np.pi / 2 - np.angle(measured_amp_forward)),
            # amplitude=np.abs(measured_amp_forward),
        ),
        center=measurement_monitor.center,
        size=measurement_monitor.size,
        direction="-",
        mode_index=mode_index,
    )
        
    sim_adjoint = sim_base.copy(deep=True)
    sim_adjoint.sources += [adjoint_source]
    return sim_adjoint

if plot_structure:
    sim_adjoint = make_sim_adjoint(permittivities, include_field_mon=True)
    f, axes = plt.subplots(1, 3, tight_layout=True, figsize=(10, 5))
    for dim, ax in zip('xyz', axes):
        sim_adjoint.plot(**{dim:0}, ax=ax)
    plt.show()


def run_adjoint(permittivities, include_field_mon=False):
    sim_adjoint = make_sim_adjoint(permittivities, include_field_mon=include_field_mon)
    sim_data_adjoint = web.run(sim_adjoint, task_name='adjoint', path='data/adjoint.hdf5')
    return sim_data_adjoint

def run_both(permittivities, include_field_mon=False):
    sim_adjoint = make_sim_adjoint(permittivities, include_field_mon=include_field_mon)
    sim_forward = make_sim_forward(permittivities, include_field_mon=include_field_mon)
    simulations = {'forward': sim_forward, 'adjoint': sim_adjoint}
    batch = web.Batch(simulations=simulations)
    batch_data = batch.run(path_dir='data')
    sim_data_forward = batch_data['forward']
    sim_data_adjoint = batch_data['adjoint']
    return sim_data_forward, sim_data_adjoint

if initial_solves:
    sim_data_adjoint = run_adjoint(permittivities, include_field_mon=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True, figsize=(14, 5))

    ax1 = sim_data_forward.plot_field('field_pattern', 'Ey', val='real', freq=freq0, ax=ax1)
    ax2 = sim_data_adjoint.plot_field('field_pattern', 'Ey', val='real', freq=freq0, ax=ax2)

    ax1.set_title('forward')
    ax2.set_title('adjoint')
    plt.show()


def unpack_grad_monitors(sim_data):
    """Grab the electric field within each of the structures' volumes and package as a dictionary."""
    
    def select_volume_data(scalar_field_data, box):
        """select the fields within the volume of a box, excluding boundaries."""
        scalar_field_f0 = scalar_field_data.isel(f=0)

        # grab the coordinates of the data
        xs = scalar_field_f0.coords['x']
        ys = scalar_field_f0.coords['y']
        zs = scalar_field_f0.coords['z']
        
        # get the bounds of the box
        (xmin, ymin, zmin), (xmax, ymax, zmax) = box.bounds

        # compute the indices where the coordinates are inside the box
        in_x = np.where(np.logical_and(xs >= xmin, xs <= xmax))
        in_y = np.where(np.logical_and(ys >= ymin, ys <= ymax))
        in_z = np.where(np.logical_and(zs >= zmin, zs <= zmax))
        
        # select the coordinates at these indices
        x_sel = xs[in_x]
        y_sel = ys[in_y]
        z_sel = zs[in_z]
    
        # select the scalar field data only at the points inside the box
        return scalar_field_f0.sel(x=x_sel, y=y_sel, z=z_sel)

    
    def unpack_box(field_data, box):
        """Unpack an individual FieldData for a given box."""
    
        # get the electric field components
        Ex = field_data.Ex
        Ey = field_data.Ey
        Ez = field_data.Ez

        # select their volume data and stack together along first axis
        fields_in_volume = [select_volume_data(field, box) for field in (Ex, Ey, Ez)]
        return fields_in_volume
        
    boxes_quad = make_boxes(permittivities)

    # unpack field data in each box
    return {box.name: unpack_box(sim_data[box.name], box.geometry) for box in boxes_quad}


def calc_gradient_adjoint_yee(sim_data_forward, sim_data_adjoint, **kwargs):
    """Compute the gradient from both the forward SimulationData and the adjoint SimulationData."""

    # grab the electric fields from forward and adjoint at each of the box locations
    E_dict_forward = unpack_grad_monitors(sim_data_forward)
    E_dict_adjoint = unpack_grad_monitors(sim_data_adjoint)

    measured_amp, _ = compute_objective(sim_data_forward)

    def compute_derivate(E_forward, E_adjoint):
        """Compute adjoint derivative given the forward and adjoint fields within a box."""
        dV = dl ** 3

        const = dV * 1j * np.conj(measured_amp)

        field_sums = [const * np.sum(Efor * Eadj) for Efor, Eadj in zip(E_forward, E_adjoint)]
        return sum(field_sums)

    # compute gradient for each box
    return {quad: compute_derivate(E_dict_forward[quad], E_dict_adjoint[quad]) for quad in quadrants}


def make_array(grad_dict):
    """Normalize the gradient dictionary and return a normalized array."""

    # convert to array
    grad_arr = np.array(list(grad_dict.values()))
    
    # take real part, if not already real
    grad_arr = np.real(grad_arr)

    # normalize
    return grad_arr #/ np.linalg.norm(grad_arr)


td.set_logging_level('error')

def solve(permittivities):
    
    sim_data_forward, sim_data_adjoint = run_both(permittivities)
    _, objective_fn = compute_objective(sim_data_forward)
    grad_adj_dict = calc_gradient_adjoint_yee(sim_data_forward, sim_data_adjoint)
    gradient = make_array(grad_adj_dict)
    return objective_fn, gradient


Js = []
perms = [permittivities]
def optimize(permittivities, step_size=1e-2, num_steps=30, eps_max=5):
    for i in range(num_steps):
        print(f'step = {i+1}')
        J, gradient = solve(permittivities)
        Js.append(J)
        print(f'\tJ = {J:.2e}')
        print(f'\tgrad_norm = {np.linalg.norm(gradient):.2e}')
        permittivities = [eps + step_size * grad for eps, grad in zip(permittivities, gradient)]
        permittivities = [eps if eps <= eps_max else eps_max for eps in permittivities]
        permittivities = [eps if eps >= 1.0 else 1.0 for eps in permittivities]
        perms.append(permittivities)
    return permittivities

perms_after = optimize(permittivities)

J, _ = solve(perms_after)
Js.append(J)

plt.plot(Js)
plt.xlabel('iterations')
plt.ylabel('objective function')
plt.yscale('log')
plt.show()



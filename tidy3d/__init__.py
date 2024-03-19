""" Tidy3d package imports"""

# grid
from .components.grid.grid import Grid, Coords
from .components.grid.grid_spec import GridSpec, UniformGrid, CustomGrid, AutoGrid
from .components.grid.grid_spec import BenklerConformalMeshSpec, StaircasingConformalMeshSpec
from .components.grid.grid_spec import HeuristicConformalMeshSpec

# geometry
from .components.geometry.base import Box, Transformed, ClipOperation, GeometryGroup
from .components.geometry.primitives import Sphere, Cylinder
from .components.geometry.mesh import TriangleMesh
from .components.geometry.polyslab import PolySlab

# medium
from .components.medium import Medium, PoleResidue, AnisotropicMedium, PEC, PECMedium
from .components.medium import Medium2D, PEC2D, medium_from_nk
from .components.medium import Sellmeier, Debye, Drude, Lorentz
from .components.medium import CustomMedium, CustomPoleResidue
from .components.medium import CustomSellmeier, FullyAnisotropicMedium
from .components.medium import CustomLorentz, CustomDrude, CustomDebye, CustomAnisotropicMedium
from .components.medium import NonlinearSusceptibility, TwoPhotonAbsorption, KerrNonlinearity
from .components.transformation import RotationAroundAxis
from .components.medium import PerturbationMedium, PerturbationPoleResidue
from .components.parameter_perturbation import ParameterPerturbation
from .components.parameter_perturbation import LinearHeatPerturbation, CustomHeatPerturbation
from .components.parameter_perturbation import LinearChargePerturbation, CustomChargePerturbation

# time modulation
from .components.time_modulation import SpaceTimeModulation, SpaceModulation
from .components.time_modulation import ContinuousWaveTimeModulation, ModulationSpec

# structures
from .components.structure import Structure, MeshOverrideStructure

# modes
from .components.mode import ModeSpec

# apodization
from .components.apodization import ApodizationSpec

# sources
from .components.source import GaussianPulse, ContinuousWave, CustomSourceTime
from .components.source import UniformCurrentSource, PlaneWave, ModeSource, PointDipole
from .components.source import GaussianBeam, AstigmaticGaussianBeam
from .components.source import CustomFieldSource, TFSF, CustomCurrentSource

# monitors
from .components.monitor import FieldMonitor, FieldTimeMonitor, FluxMonitor, FluxTimeMonitor
from .components.monitor import ModeMonitor, ModeSolverMonitor, PermittivityMonitor
from .components.monitor import FieldProjectionAngleMonitor, FieldProjectionCartesianMonitor
from .components.monitor import FieldProjectionKSpaceMonitor, FieldProjectionSurface
from .components.monitor import DiffractionMonitor

# lumped elements
from .components.lumped_element import LumpedResistor

# simulation
from .components.simulation import Simulation

# field projection

from .components.field_projection import FieldProjector

# data
from .components.data.data_array import ScalarFieldDataArray, ScalarModeFieldDataArray
from .components.data.data_array import ScalarFieldTimeDataArray, SpatialDataArray
from .components.data.data_array import ModeAmpsDataArray, ModeIndexDataArray
from .components.data.data_array import FluxDataArray, FluxTimeDataArray
from .components.data.data_array import FieldProjectionAngleDataArray
from .components.data.data_array import FieldProjectionCartesianDataArray
from .components.data.data_array import FieldProjectionKSpaceDataArray
from .components.data.data_array import DiffractionDataArray
from .components.data.data_array import HeatDataArray, ChargeDataArray
from .components.data.dataset import FieldDataset, FieldTimeDataset
from .components.data.dataset import PermittivityDataset, ModeSolverDataset
from .components.data.monitor_data import FieldData, FieldTimeData, PermittivityData
from .components.data.monitor_data import FluxData, FluxTimeData
from .components.data.monitor_data import ModeData, ModeSolverData
from .components.data.monitor_data import AbstractFieldProjectionData
from .components.data.monitor_data import FieldProjectionAngleData, FieldProjectionCartesianData
from .components.data.monitor_data import FieldProjectionKSpaceData
from .components.data.monitor_data import DiffractionData
from .components.data.sim_data import SimulationData
from .components.data.sim_data import DATA_TYPE_MAP
from .components.data.data_array import PointDataArray, CellDataArray, IndexedDataArray
from .components.data.dataset import (
    TriangularGridDataset,
    TetrahedralGridDataset,
)

# boundary
from .components.boundary import BoundarySpec, Boundary, BoundaryEdge, BoundaryEdgeType
from .components.boundary import BlochBoundary, Periodic, PECBoundary, PMCBoundary
from .components.boundary import PML, StablePML, Absorber, PMLParams, AbsorberParams, PMLTypes
from .components.boundary import DefaultPMLParameters, DefaultStablePMLParameters
from .components.boundary import DefaultAbsorberParameters

# constants imported as `C_0 = td.C_0` or `td.constants.C_0`
from .constants import C_0, ETA_0, HBAR, EPSILON_0, MU_0, Q_e, K_B, inf

# material library dict imported as `from tidy3d import material_library`
# get material `mat` and variant `var` as `material_library[mat][var]`
from .material_library.material_library import material_library
from .material_library.parametric_materials import Graphene

# for docs
from .components.medium import AbstractMedium, NonlinearSpec, NonlinearModel
from .components.geometry.base import Geometry
from .components.source import Source, SourceTime
from .components.monitor import Monitor
from .components.grid.grid import YeeGrid, FieldGrid, Coords1D

from .log import log, set_logging_file, set_logging_console

# config
from .config import config

# version
from .version import __version__

# updater
from .updater import Updater

# scene
from .components.scene import Scene

# boundary placement for other solvers
from .components.bc_placement import StructureStructureInterface, StructureBoundary
from .components.bc_placement import MediumMediumInterface
from .components.bc_placement import StructureSimulationBoundary
from .components.bc_placement import SimulationBoundary

# device and heat
from .components.device_spec import FluidSpec, SolidSpec, ConductorSpec, InsulatorSpec
from .components.device.heat.simulation import HeatSimulation
from .components.device.simulation import DeviceSimulation
from .components.device.sim_data import HeatSimulationData, DeviceSimulationData
from .components.device.monitor_data import TemperatureData, VoltageData
from .components.device.boundary import (
    TemperatureBC,
    ConvectionBC,
    HeatFluxBC,
    HeatBoundarySpec,
    DeviceBoundarySpec,
    VoltageBC,
    CurrentBC,
    InsulatingBC,
)
from .components.device.source import UniformHeatSource, HeatSource, HeatFromElectricSource
from .components.device.monitor import TemperatureMonitor, VoltageMonitor
from .components.device.grid import UniformUnstructuredGrid, DistanceUnstructuredGrid

# EME
from .components.eme.simulation import EMESimulation
from .components.eme.data.sim_data import EMESimulationData
from .components.eme.monitor import EMECoefficientMonitor, EMEModeSolverMonitor, EMEFieldMonitor
from .components.eme.monitor import EMEMonitor
from .components.data.data_array import EMESMatrixDataArray, EMEScalarFieldDataArray
from .components.data.data_array import EMECoefficientDataArray
from .components.data.data_array import EMEScalarModeFieldDataArray, EMEModeIndexDataArray
from .components.eme.data.dataset import EMEFieldDataset, EMECoefficientDataset, EMESMatrixDataset
from .components.eme.data.dataset import EMEModeSolverDataset
from .components.eme.data.monitor_data import EMEModeSolverData, EMEFieldData, EMECoefficientData
from .components.eme.grid import EMEUniformGrid, EMECompositeGrid, EMEExplicitGrid
from .components.eme.grid import EMEGrid, EMEModeSpec
from .components.eme.sweep import EMELengthSweep, EMEModeSweep


def set_logging_level(level: str) -> None:
    """Raise a warning here instead of setting the logging level."""
    raise DeprecationWarning(
        "``set_logging_level`` no longer supported. "
        f"To set the logging level, call ``tidy3d.config.logging_level = {level}``."
    )


log.info(f"Using client version: {__version__}")

Transformed.update_forward_refs()
ClipOperation.update_forward_refs()
GeometryGroup.update_forward_refs()

__all__ = [
    "Grid",
    "Coords",
    "GridSpec",
    "UniformGrid",
    "CustomGrid",
    "AutoGrid",
    "Box",
    "Sphere",
    "Cylinder",
    "PolySlab",
    "GeometryGroup",
    "ClipOperation",
    "Transformed",
    "TriangleMesh",
    "Medium",
    "PoleResidue",
    "AnisotropicMedium",
    "PEC",
    "PECMedium",
    "Medium2D",
    "PEC2D",
    "Sellmeier",
    "Debye",
    "Drude",
    "Lorentz",
    "CustomMedium",
    "CustomPoleResidue",
    "CustomSellmeier",
    "FullyAnisotropicMedium",
    "CustomLorentz",
    "CustomDrude",
    "CustomDebye",
    "CustomAnisotropicMedium",
    "RotationAroundAxis",
    "PerturbationMedium",
    "PerturbationPoleResidue",
    "ParameterPerturbation",
    "LinearHeatPerturbation",
    "CustomHeatPerturbation",
    "LinearChargePerturbation",
    "CustomChargePerturbation",
    "NonlinearSpec",
    "NonlinearModel",
    "NonlinearSusceptibility",
    "TwoPhotonAbsorption",
    "KerrNonlinearity",
    "Structure",
    "MeshOverrideStructure",
    "ModeSpec",
    "ApodizationSpec",
    "GaussianPulse",
    "ContinuousWave",
    "CustomSourceTime",
    "UniformCurrentSource",
    "PlaneWave",
    "ModeSource",
    "PointDipole",
    "GaussianBeam",
    "AstigmaticGaussianBeam",
    "CustomFieldSource",
    "TFSF",
    "CustomCurrentSource",
    "FieldMonitor",
    "FieldTimeMonitor",
    "FluxMonitor",
    "FluxTimeMonitor",
    "ModeMonitor",
    "ModeSolverMonitor",
    "PermittivityMonitor",
    "FieldProjectionAngleMonitor",
    "FieldProjectionCartesianMonitor",
    "FieldProjectionKSpaceMonitor",
    "FieldProjectionSurface",
    "DiffractionMonitor",
    "Simulation",
    "FieldProjector",
    "ScalarFieldDataArray",
    "ScalarModeFieldDataArray",
    "ScalarFieldTimeDataArray",
    "SpatialDataArray",
    "ModeAmpsDataArray",
    "ModeIndexDataArray",
    "FluxDataArray",
    "FluxTimeDataArray",
    "FieldProjectionAngleDataArray",
    "FieldProjectionCartesianDataArray",
    "FieldProjectionKSpaceDataArray",
    "DiffractionDataArray",
    "HeatDataArray",
    "ChargeDataArray",
    "FieldDataset",
    "FieldTimeDataset",
    "PermittivityDataset",
    "ModeSolverDataset",
    "FieldData",
    "FieldTimeData",
    "PermittivityData",
    "FluxData",
    "FluxTimeData",
    "ModeData",
    "ModeSolverData",
    "AbstractFieldProjectionData",
    "FieldProjectionAngleData",
    "FieldProjectionCartesianData",
    "FieldProjectionKSpaceData",
    "DiffractionData",
    "SimulationData",
    "DATA_TYPE_MAP",
    "BoundarySpec",
    "Boundary",
    "BoundaryEdge",
    "BoundaryEdgeType",
    "BlochBoundary",
    "Periodic",
    "PECBoundary",
    "PMCBoundary",
    "PML",
    "StablePML",
    "Absorber",
    "PMLParams",
    "AbsorberParams",
    "PMLTypes",
    "DefaultPMLParameters",
    "DefaultStablePMLParameters",
    "DefaultAbsorberParameters",
    "C_0",
    "ETA_0",
    "HBAR",
    "EPSILON_0",
    "MU_0",
    "Q_e",
    "K_B",
    "inf",
    "material_library",
    "Graphene",
    "AbstractMedium",
    "Geometry",
    "Source",
    "SourceTime",
    "Monitor",
    "YeeGrid",
    "FieldGrid",
    "Coords1D",
    "log",
    "set_logging_file",
    "set_logging_console",
    "config",
    "__version__",
    "Updater",
    "LumpedResistor",
    "Scene",
    "StructureStructureInterface",
    "StructureBoundary",
    "MediumMediumInterface",
    "StructureSimulationBoundary",
    "SimulationBoundary",
    "FluidSpec",
    "SolidSpec",
    "ConductorSpec",
    "InsulatorSpec",
    "HeatSimulation",
    "HeatSimulationData",
    "TemperatureBC",
    "ConvectionBC",
    "HeatFluxBC",
    "HeatBoundarySpec",
    "VoltageBC",
    "CurrentBC",
    "InsulatingBC",
    "UniformHeatSource",
    "HeatSource",
    "HeatFromElectricSource",
    "UniformUnstructuredGrid",
    "DistanceUnstructuredGrid",
    "TemperatureData",
    "TemperatureMonitor",
    "DeviceSimulation",
    "DeviceSimulationData",
    "VoltageData",
    "DeviceBoundarySpec",
    "VoltageMonitor",
    "SpaceTimeModulation",
    "SpaceModulation",
    "ContinuousWaveTimeModulation",
    "ModulationSpec",
    "PointDataArray",
    "CellDataArray",
    "IndexedDataArray",
    "TriangularGridDataset",
    "TetrahedralGridDataset",
    "medium_from_nk",
    "BenklerConformalMeshSpec",
    "StaircasingConformalMeshSpec",
    "HeuristicConformalMeshSpec",
    "EMESimulation",
    "EMESimulationData",
    "EMEMonitor",
    "EMEModeSolverMonitor",
    "EMEFieldMonitor",
    "EMESMatrixDataArray",
    "EMEFieldDataset",
    "EMECoefficientDataset",
    "EMESMatrixDataset",
    "EMEModeSolverData",
    "EMEFieldData",
    "EMECoefficientData",
    "EMECoefficientMonitor",
    "EMEModeSpec",
    "EMEGrid",
    "EMEUniformGrid",
    "EMECompositeGrid",
    "EMEExplicitGrid",
    "EMEScalarFieldDataArray",
    "EMEScalarModeFieldDataArray",
    "EMEModeIndexDataArray",
    "EMECoefficientDataArray",
    "EMEModeSolverDataset",
    "EMESweepSpec",
    "EMELengthSweep",
    "EMEModeSweep",
]

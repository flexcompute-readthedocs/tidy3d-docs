"""Monitor level data, store the DataArrays associated with a single device monitor."""
from __future__ import annotations
from typing import Union, Tuple, Optional

from abc import ABC

import pydantic.v1 as pd

from .monitor import TemperatureMonitor, VoltageMonitor, DeviceMonitorType
from ..base import skip_if_fields_missing
from ..base_sim.data.monitor_data import AbstractMonitorData
from ..data.data_array import SpatialDataArray
from ..data.dataset import TriangularGridDataset, TetrahedralGridDataset
from ..types import ScalarSymmetry, Coordinate, annotate_type
from ...constants import KELVIN, VOLT

from ...log import log


class DeviceMonitorData(AbstractMonitorData, ABC):
    """Abstract base class of objects that store data pertaining to a single :class:`DeviceMonitor`."""

    monitor: DeviceMonitorType = pd.Field(
        ...,
        title="Monitor",
        description="Monitor associated with the data.",
    )

    symmetry: Tuple[ScalarSymmetry, ScalarSymmetry, ScalarSymmetry] = pd.Field(
        (0, 0, 0),
        title="Symmetry",
        description="Symmetry of the original simulation in x, y, and z.",
    )

    symmetry_center: Coordinate = pd.Field(
        (0, 0, 0),
        title="Symmetry Center",
        description="Symmetry center of the original simulation in x, y, and z.",
    )

    @property
    def symmetry_expanded_copy(self) -> DeviceMonitorData:
        """Return copy of self with symmetry applied."""
        return self.copy()

    def _symmetry_expanded_copy(self, property):
        """Return the property with symmetry applied."""

        if all(sym == 0 for sym in self.symmetry):
            return property

        new_property = property

        for dim in range(3):
            # do not expand monitor with zero size along symmetry direction
            # this is done because 2d unstructured data does not support this
            if self.symmetry[dim] == 1 and self.monitor.size[dim] != 0:
                new_property = new_property.reflect(axis=dim, center=self.symmetry_center[dim])

        return new_property


class TemperatureData(DeviceMonitorData):
    """Data associated with a :class:`TemperatureMonitor`: spatial temperature field.

    Example
    -------
    >>> from tidy3d import TemperatureMonitor, SpatialDataArray
    >>> import numpy as np
    >>> temp_data = SpatialDataArray(
    ...     np.ones((2, 3, 4)), coords={"x": [0, 1], "y": [0, 1, 2], "z": [0, 1, 2, 3]}
    ... )
    >>> temp_mnt = TemperatureMonitor(size=(1, 2, 3), name="temperature")
    >>> temp_mnt_data = TemperatureData(
    ...     monitor=temp_mnt, temperature=temp_data, symmetry=(0, 1, 0), symmetry_center=(0, 0, 0)
    ... )
    >>> temp_mnt_data_expanded = temp_mnt_data.symmetry_expanded_copy
    """

    monitor: TemperatureMonitor = pd.Field(
        ..., title="Monitor", description="Temperature monitor associated with the data."
    )

    temperature: Optional[
        Union[SpatialDataArray, annotate_type(Union[TriangularGridDataset, TetrahedralGridDataset])]
    ] = pd.Field(
        ...,
        title="Temperature",
        description="Spatial temperature field.",
        units=KELVIN,
    )

    @pd.validator("temperature", always=True)
    @skip_if_fields_missing(["monitor"])
    def warn_no_data(cls, val, values):
        """Warn if no data provided."""

        mnt = values.get("monitor")

        if val is None:
            log.warning(
                f"No data is available for monitor '{mnt.name}'. This is typically caused by "
                "monitor not intersecting any solid medium."
            )

        return val

    @property
    def symmetry_expanded_copy(self) -> TemperatureData:
        """Return copy of self with symmetry applied."""

        new_temp = self._symmetry_expanded_copy(property=self.temperature)
        return self.updated_copy(temperature=new_temp, symmetry=(0, 0, 0))


class VoltageData(DeviceMonitorData):
    """Data associated with a :class:`VoltageMonitor`: spatial electric potential field.

    Example
    -------
    >>> from tidy3d import VoltageMonitor, SpatialDataArray
    >>> import numpy as np
    >>> voltage_data = SpatialDataArray(
    ...     np.ones((2, 3, 4)), coords={"x": [0, 1], "y": [0, 1, 2], "z": [0, 1, 2, 3]}
    ... )
    >>> voltage_mnt = VoltageMonitor(size=(1, 2, 3), name="voltage")
    >>> voltage_mnt_data = VoltageData(
    ...     monitor=voltage_mnt, voltage=voltage_data, symmetry=(0, 1, 0), symmetry_center=(0, 0, 0)
    ... )
    >>> voltage_mnt_data_expanded = voltage_mnt_data.symmetry_expanded_copy
    """

    monitor: VoltageMonitor = pd.Field(
        ..., title="Monitor", description="Electric potential monitor associated with the data."
    )

    voltage: Optional[
        Union[SpatialDataArray, annotate_type(Union[TriangularGridDataset, TetrahedralGridDataset])]
    ] = pd.Field(
        ...,
        title="Voltage (electric potential)",
        description="Spatial electric potential field.",
        units=VOLT,
    )

    @pd.validator("voltage", always=True)
    @skip_if_fields_missing(["monitor"])
    def warn_no_data(cls, val, values):
        """Warn if no data provided."""

        mnt = values.get("monitor")

        if val is None:
            log.warning(
                f"No data is available for monitor '{mnt.name}'. This is typically caused by "
                "monitor not intersecting any solid medium."
            )

        return val

    @property
    def symmetry_expanded_copy(self) -> VoltageData:
        """Return copy of self with symmetry applied."""

        new_phi = self._symmetry_expanded_copy(property=self.voltage)
        return self.updated_copy(voltage=new_phi, symmetry=(0, 0, 0))


DeviceMonitorDataType = Union[TemperatureData, VoltageData]

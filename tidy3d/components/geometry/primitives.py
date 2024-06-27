"""Concrete primitive geometrical objects."""

from __future__ import annotations

from math import isclose
from typing import List

import numpy as np
import pydantic.v1 as pydantic
import shapely

from ...constants import LARGE_NUMBER, MICROMETER
from ...exceptions import SetupError, ValidationError
from ...log import log
from ...packaging import verify_packages_import
from ..autograd import AutogradFieldMap
from ..autograd.derivative_utils import DerivativeInfo
from ..autograd.types import TracedNonNegativeFloat
from ..base import cached_property, skip_if_fields_missing
from ..types import Axis, Bound, Coordinate, MatrixReal4x4, Shapely, Tuple
from . import base

# for sampling conical frustum in visualization
_N_SAMPLE_CURVE_SHAPELY = 40

# for shapely circular shapes discretization in visualization
_N_SHAPELY_QUAD_SEGS = 200

# number of points to discretize cylinder edge for adjoint integral
NUM_PTS_ADJOINT_CYLINDER = 30


class Sphere(base.Centered, base.Circular):
    """Spherical geometry.

    Example
    -------
    >>> b = Sphere(center=(1,2,3), radius=2)
    """

    def inside(
        self, x: np.ndarray[float], y: np.ndarray[float], z: np.ndarray[float]
    ) -> np.ndarray[bool]:
        """For input arrays ``x``, ``y``, ``z`` of arbitrary but identical shape, return an array
        with the same shape which is ``True`` for every point in zip(x, y, z) that is inside the
        volume of the :class:`Geometry`, and ``False`` otherwise.

        Parameters
        ----------
        x : np.ndarray[float]
            Array of point positions in x direction.
        y : np.ndarray[float]
            Array of point positions in y direction.
        z : np.ndarray[float]
            Array of point positions in z direction.

        Returns
        -------
        np.ndarray[bool]
            ``True`` for every point that is inside the geometry.
        """
        self._ensure_equal_shape(x, y, z)
        x0, y0, z0 = self.center
        dist_x = np.abs(x - x0)
        dist_y = np.abs(y - y0)
        dist_z = np.abs(z - z0)
        return (dist_x**2 + dist_y**2 + dist_z**2) <= (self.radius**2)

    def intersections_tilted_plane(
        self, normal: Coordinate, origin: Coordinate, to_2D: MatrixReal4x4
    ) -> List[Shapely]:
        """Return a list of shapely geometries at the plane specified by normal and origin.

        Parameters
        ----------
        normal : Coordinate
            Vector defining the normal direction to the plane.
        origin : Coordinate
            Vector defining the plane origin.
        to_2D : MatrixReal4x4
            Transformation matrix to apply to resulting shapes.

        Returns
        -------
        List[shapely.geometry.base.BaseGeometry]
            List of 2D shapes that intersect plane.
            For more details refer to
            `Shapely's Documentation <https://shapely.readthedocs.io/en/stable/project.html>`_.
        """
        normal = np.array(normal)
        unit_normal = normal / (np.sum(normal**2) ** 0.5)
        projection = np.dot(np.array(origin) - np.array(self.center), unit_normal)
        if abs(projection) >= self.radius:
            return []

        radius = (self.radius**2 - projection**2) ** 0.5
        center = np.array(self.center) + projection * unit_normal

        v = np.zeros(3)
        v[np.argmin(np.abs(unit_normal))] = 1
        u = np.cross(unit_normal, v)
        u /= np.sum(u**2) ** 0.5
        v = np.cross(unit_normal, u)

        angles = np.linspace(0, 2 * np.pi, _N_SHAPELY_QUAD_SEGS * 4 + 1)[:-1]
        circ = center + np.outer(np.cos(angles), radius * u) + np.outer(np.sin(angles), radius * v)
        vertices = np.dot(np.hstack((circ, np.ones((angles.size, 1)))), to_2D.T)
        return [shapely.Polygon(vertices[:, :2])]

    def intersections_plane(self, x: float = None, y: float = None, z: float = None):
        """Returns shapely geometry at plane specified by one non None value of x,y,z.

        Parameters
        ----------
        x : float = None
            Position of plane in x direction, only one of x,y,z can be specified to define plane.
        y : float = None
            Position of plane in x direction, only one of x,y,z can be specified to define plane.
        z : float = None
            Position of plane in x direction, only one of x,y,z can be specified to define plane.

        Returns
        -------
        List[shapely.geometry.base.BaseGeometry]
            List of 2D shapes that intersect plane.
            For more details refer to
            `Shapely's Documentation <https://shapely.readthedocs.io/en/stable/project.html>`_.
        """
        axis, position = self.parse_xyz_kwargs(x=x, y=y, z=z)
        if not self.intersects_axis_position(axis, position):
            return []
        z0, (x0, y0) = self.pop_axis(self.center, axis=axis)
        intersect_dist = self._intersect_dist(position, z0)
        if not intersect_dist:
            return []
        return [shapely.Point(x0, y0).buffer(0.5 * intersect_dist, quad_segs=_N_SHAPELY_QUAD_SEGS)]

    @cached_property
    def bounds(self) -> Bound:
        """Returns bounding box min and max coordinates.

        Returns
        -------
        Tuple[float, float, float], Tuple[float, float, float]
            Min and max bounds packaged as ``(minx, miny, minz), (maxx, maxy, maxz)``.
        """
        coord_min = tuple(c - self.radius for c in self.center)
        coord_max = tuple(c + self.radius for c in self.center)
        return (coord_min, coord_max)

    def _volume(self, bounds: Bound) -> float:
        """Returns object's volume within given bounds."""

        volume = 4.0 / 3.0 * np.pi * self.radius**3

        # a very loose upper bound on how much of sphere is in bounds
        for axis in range(3):
            if self.center[axis] <= bounds[0][axis] or self.center[axis] >= bounds[1][axis]:
                volume *= 0.5

        return volume

    def _surface_area(self, bounds: Bound) -> float:
        """Returns object's surface area within given bounds."""

        area = 4.0 * np.pi * self.radius**2

        # a very loose upper bound on how much of sphere is in bounds
        for axis in range(3):
            if self.center[axis] <= bounds[0][axis] or self.center[axis] >= bounds[1][axis]:
                area *= 0.5

        return area


class Cylinder(base.Centered, base.Circular, base.Planar):
    """Cylindrical geometry with optional sidewall angle along axis
    direction. When ``sidewall_angle`` is nonzero, the shape is a
    conical frustum or a cone.

    Example
    -------
    >>> c = Cylinder(center=(1,2,3), radius=2, length=5, axis=2)

    See Also
    --------

    **Notebooks**

    * `THz integrated demultiplexer/filter based on a ring resonator <../../../notebooks/THzDemultiplexerFilter.html>`_
    * `Photonic crystal waveguide polarization filter <../../../notebooks/PhotonicCrystalWaveguidePolarizationFilter.html>`_
    """

    # Provide more explanations on where radius is defined
    radius: TracedNonNegativeFloat = pydantic.Field(
        ...,
        title="Radius",
        description="Radius of geometry at the ``reference_plane``.",
        units=MICROMETER,
    )

    length: pydantic.NonNegativeFloat = pydantic.Field(
        ...,
        title="Length",
        description="Defines thickness of cylinder along axis dimension.",
        units=MICROMETER,
    )

    @pydantic.validator("length", always=True)
    @skip_if_fields_missing(["sidewall_angle", "reference_plane"])
    def _only_middle_for_infinite_length_slanted_cylinder(cls, val, values):
        """For a slanted cylinder of infinite length, ``reference_plane`` can only
        be ``middle``; otherwise, the radius at ``center`` is either td.inf or 0.
        """
        if isclose(values["sidewall_angle"], 0) or not np.isinf(val):
            return val
        if values["reference_plane"] != "middle":
            raise SetupError(
                "For a slanted cylinder here is of infinite length, "
                "defining the reference_plane other than 'middle' "
                "leads to undefined cylinder behaviors near 'center'."
            )
        return val

    @property
    def center_axis(self):
        """Gets the position of the center of the geometry in the out of plane dimension."""
        z0, _ = self.pop_axis(self.center, axis=self.axis)
        return z0

    @property
    def length_axis(self) -> float:
        """Gets the length of the geometry along the out of plane dimension."""
        return self.length

    @cached_property
    def _normal_2dmaterial(self) -> Axis:
        """Get the normal to the given geometry, checking that it is a 2D geometry."""
        if self.length != 0:
            raise ValidationError("'Medium2D' requires the 'Cylinder' length to be zero.")
        return self.axis

    def _update_from_bounds(self, bounds: Tuple[float, float], axis: Axis) -> Cylinder:
        """Returns an updated geometry which has been transformed to fit within ``bounds``
        along the ``axis`` direction."""
        if axis != self.axis:
            raise ValueError(
                f"'_update_from_bounds' may only be applied along axis '{self.axis}', "
                f"but was given axis '{axis}'."
            )
        new_center = list(self.center)
        new_center[axis] = (bounds[0] + bounds[1]) / 2
        new_length = bounds[1] - bounds[0]
        return self.updated_copy(center=new_center, length=new_length)

    @verify_packages_import(["trimesh"])
    def _do_intersections_tilted_plane(
        self, normal: Coordinate, origin: Coordinate, to_2D: MatrixReal4x4
    ) -> List[Shapely]:
        """Return a list of shapely geometries at the plane specified by normal and origin.

        Parameters
        ----------
        normal : Coordinate
            Vector defining the normal direction to the plane.
        origin : Coordinate
            Vector defining the plane origin.
        to_2D : MatrixReal4x4
            Transformation matrix to apply to resulting shapes.

        Returns
        -------
        List[shapely.geometry.base.BaseGeometry]
            List of 2D shapes that intersect plane.
            For more details refer to
            `Shapely's Documentation <https://shapely.readthedocs.io/en/stable/project.html>`_.
        """
        import trimesh

        z0, (x0, y0) = self.pop_axis(self.center, self.axis)
        half_length = self.finite_length_axis / 2

        z_top = z0 + half_length
        z_bot = z0 - half_length

        if np.isclose(self.sidewall_angle, 0):
            r_top = self.radius
            r_bot = self.radius
        else:
            r_top = self.radius_top
            r_bot = self.radius_bottom
            if r_top < 0 or np.isclose(r_top, 0):
                r_top = 0
                z_top = z0 + self._radius_z(z0) / self._tanq
            elif r_bot < 0 or np.isclose(r_bot, 0):
                r_bot = 0
                z_bot = z0 + self._radius_z(z0) / self._tanq

        angles = np.linspace(0, 2 * np.pi, _N_SHAPELY_QUAD_SEGS * 4 + 1)

        if r_bot > 0:
            x_bot = x0 + r_bot * np.cos(angles)
            y_bot = y0 + r_bot * np.sin(angles)
            x_bot[-1] = x0
            y_bot[-1] = y0
        else:
            x_bot = np.array([x0])
            y_bot = np.array([y0])

        if r_top > 0:
            x_top = x0 + r_top * np.cos(angles)
            y_top = y0 + r_top * np.sin(angles)
            x_top[-1] = x0
            y_top[-1] = y0
        else:
            x_top = np.array([x0])
            y_top = np.array([y0])

        x = np.hstack((x_bot, x_top))
        y = np.hstack((y_bot, y_top))
        z = np.hstack((np.full_like(x_bot, z_bot), np.full_like(x_top, z_top)))
        vertices = np.vstack(self.unpop_axis(z, (x, y), self.axis)).T

        if x_bot.shape[0] == 1:
            m = 1
            n = x_top.shape[0] - 1
            faces_top = [(m + n, m + i, m + (i + 1) % n) for i in range(n)]
            faces_side = [(m + (i + 1) % n, m + i, 0) for i in range(n)]
            faces = faces_top + faces_side
        elif x_top.shape[0] == 1:
            m = x_bot.shape[0]
            n = m - 1
            faces_bot = [(n, (i + 1) % n, i) for i in range(n)]
            faces_side = [(i, (i + 1) % n, m) for i in range(n)]
            faces = faces_bot + faces_side
        else:
            m = x_bot.shape[0]
            n = m - 1
            faces_bot = [(n, (i + 1) % n, i) for i in range(n)]
            faces_top = [(m + n, m + i, m + (i + 1) % n) for i in range(n)]
            faces_side_bot = [(i, (i + 1) % n, m + (i + 1) % n) for i in range(n)]
            faces_side_top = [(m + (i + 1) % n, m + i, i) for i in range(n)]
            faces = faces_bot + faces_top + faces_side_bot + faces_side_top

        mesh = trimesh.Trimesh(vertices, faces)

        section = mesh.section(plane_origin=origin, plane_normal=normal)
        if section is None:
            return []
        path, _ = section.to_planar(to_2D=to_2D)
        return path.polygons_full

    def _intersections_normal(self, z: float):
        """Find shapely geometries intersecting cylindrical geometry with axis normal to slab.

        Parameters
        ----------
        z : float
            Position along the axis normal to slab

        Returns
        -------
        List[shapely.geometry.base.BaseGeometry]
            List of 2D shapes that intersect plane.
            For more details refer to
            `Shapely's Documentation <https://shapely.readthedocs.io/en/stable/project.html>`_.
        """

        # radius at z
        radius_offset = self._radius_z(z)

        if radius_offset <= 0:
            return []

        _, (x0, y0) = self.pop_axis(self.center, axis=self.axis)
        return [shapely.Point(x0, y0).buffer(radius_offset, quad_segs=_N_SHAPELY_QUAD_SEGS)]

    def _intersections_side(self, position, axis):
        """Find shapely geometries intersecting cylindrical geometry with axis orthogonal to length.
        When ``sidewall_angle`` is nonzero, so that it's in fact a conical frustum or cone, the
        cross section can contain hyperbolic curves. This is currently approximated by a polygon
        of many vertices.

        Parameters
        ----------
        position : float
            Position along axis direction.
        axis : int
            Integer index into 'xyz' (0, 1, 2).

        Returns
        -------
        List[shapely.geometry.base.BaseGeometry]
            List of 2D shapes that intersect plane.
            For more details refer to
            `Shapely's Documentation <https://shapely.readthedocs.io/en/stable/project.html>`_.
        """
        # position in the local coordinate of the cylinder
        position_local = position - self.center[axis]

        # no intersection
        if abs(position_local) >= self.radius_max:
            return []

        # half of intersection length at the top and bottom
        intersect_half_length_max = np.sqrt(self.radius_max**2 - position_local**2)
        intersect_half_length_min = -LARGE_NUMBER
        if abs(position_local) < self.radius_min:
            intersect_half_length_min = np.sqrt(self.radius_min**2 - position_local**2)

        # the vertices on the max side of top/bottom
        # The two vertices are present in all scenarios.
        vertices_max = [
            self._local_to_global_side_cross_section([-intersect_half_length_max, 0], axis),
            self._local_to_global_side_cross_section([intersect_half_length_max, 0], axis),
        ]

        # Extending to a cone, the maximal height of the cone
        h_cone = (
            LARGE_NUMBER if isclose(self.sidewall_angle, 0) else self.radius_max / abs(self._tanq)
        )
        # The maximal height of the cross section
        height_max = min(
            (1 - abs(position_local) / self.radius_max) * h_cone, self.finite_length_axis
        )

        # more vertices to add for conical frustum shape
        vertices_frustum_right = []
        vertices_frustum_left = []
        if not (isclose(position, self.center[axis]) or isclose(self.sidewall_angle, 0)):
            # The y-coordinate for the additional vertices
            y_list = height_max * np.linspace(0, 1, _N_SAMPLE_CURVE_SHAPELY)
            # `abs()` to make sure np.sqrt(0-fp_eps) goes through
            x_list = np.sqrt(
                np.abs(self.radius_max**2 * (1 - y_list / h_cone) ** 2 - position_local**2)
            )
            for i in range(_N_SAMPLE_CURVE_SHAPELY):
                vertices_frustum_right.append(
                    self._local_to_global_side_cross_section([x_list[i], y_list[i]], axis)
                )
                vertices_frustum_left.append(
                    self._local_to_global_side_cross_section(
                        [
                            -x_list[_N_SAMPLE_CURVE_SHAPELY - i - 1],
                            y_list[_N_SAMPLE_CURVE_SHAPELY - i - 1],
                        ],
                        axis,
                    )
                )

        # the vertices on the min side of top/bottom
        vertices_min = []

        ## termination at the top/bottom
        if intersect_half_length_min > 0:
            vertices_min.append(
                self._local_to_global_side_cross_section(
                    [intersect_half_length_min, self.finite_length_axis], axis
                )
            )
            vertices_min.append(
                self._local_to_global_side_cross_section(
                    [-intersect_half_length_min, self.finite_length_axis], axis
                )
            )
        ## early termination
        else:
            vertices_min.append(self._local_to_global_side_cross_section([0, height_max], axis))

        return [
            shapely.Polygon(
                vertices_max + vertices_frustum_right + vertices_min + vertices_frustum_left
            )
        ]

    def inside(
        self, x: np.ndarray[float], y: np.ndarray[float], z: np.ndarray[float]
    ) -> np.ndarray[bool]:
        """For input arrays ``x``, ``y``, ``z`` of arbitrary but identical shape, return an array
        with the same shape which is ``True`` for every point in zip(x, y, z) that is inside the
        volume of the :class:`Geometry`, and ``False`` otherwise.

        Parameters
        ----------
        x : np.ndarray[float]
            Array of point positions in x direction.
        y : np.ndarray[float]
            Array of point positions in y direction.
        z : np.ndarray[float]
            Array of point positions in z direction.

        Returns
        -------
        np.ndarray[bool]
            ``True`` for every point that is inside the geometry.
        """
        # radius at z
        self._ensure_equal_shape(x, y, z)
        z0, (x0, y0) = self.pop_axis(self.center, axis=self.axis)
        z, (x, y) = self.pop_axis((x, y, z), axis=self.axis)
        radius_offset = self._radius_z(z)
        positive_radius = radius_offset > 0

        dist_x = np.abs(x - x0)
        dist_y = np.abs(y - y0)
        dist_z = np.abs(z - z0)
        inside_radius = (dist_x**2 + dist_y**2) <= (radius_offset**2)
        inside_height = dist_z <= (self.finite_length_axis / 2)
        return positive_radius * inside_radius * inside_height

    @cached_property
    def bounds(self) -> Bound:
        """Returns bounding box min and max coordinates.

        Returns
        -------
        Tuple[float, float, float], Tuple[float, float, float]
            Min and max bounds packaged as ``(minx, miny, minz), (maxx, maxy, maxz)``.
        """
        coord_min = [c - self.radius_max for c in self.center]
        coord_max = [c + self.radius_max for c in self.center]
        coord_min[self.axis] = self.center[self.axis] - self.length_axis / 2.0
        coord_max[self.axis] = self.center[self.axis] + self.length_axis / 2.0
        return (tuple(coord_min), tuple(coord_max))

    def _volume(self, bounds: Bound) -> float:
        """Returns object's volume within given bounds."""

        coord_min = max(self.bounds[0][self.axis], bounds[0][self.axis])
        coord_max = min(self.bounds[1][self.axis], bounds[1][self.axis])

        length = coord_max - coord_min

        volume = np.pi * self.radius_max**2 * length

        # a very loose upper bound on how much of the cylinder is in bounds
        for axis in range(3):
            if axis != self.axis:
                if self.center[axis] <= bounds[0][axis] or self.center[axis] >= bounds[1][axis]:
                    volume *= 0.5

        return volume

    def _surface_area(self, bounds: Bound) -> float:
        """Returns object's surface area within given bounds."""

        area = 0

        coord_min = self.bounds[0][self.axis]
        coord_max = self.bounds[1][self.axis]

        if coord_min < bounds[0][self.axis]:
            coord_min = bounds[0][self.axis]
        else:
            area += np.pi * self.radius_max**2

        if coord_max > bounds[1][self.axis]:
            coord_max = bounds[1][self.axis]
        else:
            area += np.pi * self.radius_max**2

        length = coord_max - coord_min

        area += 2.0 * np.pi * self.radius_max * length

        # a very loose upper bound on how much of the cylinder is in bounds
        for axis in range(3):
            if axis != self.axis:
                if self.center[axis] <= bounds[0][axis] or self.center[axis] >= bounds[1][axis]:
                    area *= 0.5

        return area

    @cached_property
    def radius_bottom(self) -> float:
        """radius of bottom"""
        return self._radius_z(self.center_axis - self.finite_length_axis / 2)

    @cached_property
    def radius_top(self) -> float:
        """radius of bottom"""
        return self._radius_z(self.center_axis + self.finite_length_axis / 2)

    @cached_property
    def radius_max(self) -> float:
        """max(radius of top, radius of bottom)"""
        return max(self.radius_bottom, self.radius_top)

    @cached_property
    def radius_min(self) -> float:
        """min(radius of top, radius of bottom). It can be negative for a large
        sidewall angle.
        """
        return min(self.radius_bottom, self.radius_top)

    def _radius_z(self, z: float):
        """Compute the radius of the cross section at the position z.

        Parameters
        ----------
        z : float
            Position along the axis normal to slab
        """
        if isclose(self.sidewall_angle, 0):
            return self.radius

        radius_middle = self.radius
        if self.reference_plane == "top":
            radius_middle += self.finite_length_axis / 2 * self._tanq
        elif self.reference_plane == "bottom":
            radius_middle -= self.finite_length_axis / 2 * self._tanq

        return radius_middle - (z - self.center_axis) * self._tanq

    def _local_to_global_side_cross_section(self, coords: List[float], axis: int) -> List[float]:
        """Map a point (x,y) from local to global coordinate system in the
        side cross section.

        The definition of the local: y=0 lies at the base if ``sidewall_angle>=0``,
        and at the top if ``sidewall_angle<0``; x=0 aligns with the corresponding
        ``self.center``. In both cases, y-axis is pointing towards the narrowing
        direction of cylinder.

        Parameters
        ----------
        axis : int
            Integer index into 'xyz' (0, 1, 2).
        coords : List[float, float]
            The value in the planar coordinate.

        Returns
        -------
        Tuple[float, float]
            The point in the global coordinate for plotting `_intersection_side`.

        """

        # For negative sidewall angle, quantities along axis direction usually needs a flipped sign
        axis_sign = 1
        if self.sidewall_angle < 0:
            axis_sign = -1

        lx_offset, ly_offset = self._order_by_axis(
            plane_val=coords[0],
            axis_val=axis_sign * (-self.finite_length_axis / 2 + coords[1]),
            axis=axis,
        )
        _, (x_center, y_center) = self.pop_axis(self.center, axis=axis)
        return [x_center + lx_offset, y_center + ly_offset]

    def compute_derivatives(self, derivative_info: DerivativeInfo) -> AutogradFieldMap:
        """Compute the adjoint derivatives for this object."""

        field_paths = derivative_info.paths

        grad_vjps = {}

        for path in field_paths:
            field_name, *rest = path

            if field_name == "radius":
                grad_val = self.compute_derivative_radius(derivative_info=derivative_info)

            elif field_name == "center":
                (index,) = rest
                grad_val = self.compute_derivative_center(
                    derivative_info=derivative_info, axis=index
                )
            else:
                raise NotImplementedError(
                    f"No derivative defined for field 'Cylinder.{field_name}'"
                )

            grad_vjps[path] = grad_val

        return grad_vjps

    @property
    def adjoint_integral_angles(self) -> np.ndarray:
        """angles used for integration in autograd derivatives."""
        return 2 * np.pi * np.linspace(0, 1, NUM_PTS_ADJOINT_CYLINDER + 1)[:-1]

    def compute_derivative_center(self, derivative_info: DerivativeInfo, axis: int) -> Coordinate:
        """Compute the adjoint derivatives for this object."""

        if axis == self.axis:
            log.warning(
                "Derivative with respect to 'Cylinder.center' along 'Cylinder.axis' "
                "is not yet supported. Ignoring gradient."
            )
            return 0.0

        # compute weighted sum depending on axis
        grad_edge = self.compute_derivative_edge_normals(derivative_info=derivative_info)

        angles = self.adjoint_integral_angles
        weights_t1 = np.cos(angles)
        weights_t2 = np.sin(angles)

        weights = self.unpop_axis(0.0, (weights_t1, weights_t2), axis=self.axis)
        return np.sum(weights[axis] * grad_edge)

    def compute_derivative_radius(self, derivative_info: DerivativeInfo) -> float:
        """Compute the adjoint derivatives for this object."""
        grad_edge = self.compute_derivative_edge_normals(derivative_info=derivative_info)
        return np.sum(grad_edge)

    def compute_derivative_edge_normals(
        self,
        derivative_info: DerivativeInfo,
    ) -> float:
        """Compute the adjoint derivatives for this object."""

        angles = self.adjoint_integral_angles

        center_axis, (center_t1, center_t2) = self.pop_axis(self.center, axis=self.axis)

        # evaluation points (NUM_PTS_ADJOINT_CYLINDER, 3)
        pts_t1 = center_t1 + self.radius * np.cos(angles)
        pts_t2 = center_t2 + self.radius * np.sin(angles)
        pts_tangential = np.stack((pts_t1, pts_t2), axis=-1)
        pts_axis = center_axis * np.ones_like(angles)
        pts = self.unpop_axis_vect(ax_coords=pts_axis, plane_coords=pts_tangential)

        # normal vector (NUM_PTS_ADJOINT_CYLINDER, 3)
        normals_t1 = np.cos(angles)
        normals_t2 = np.sin(angles)
        normals_tangential = np.stack((normals_t1, normals_t2), axis=-1)
        normals_axis = np.zeros_like(angles)
        normals = self.unpop_axis_vect(ax_coords=normals_axis, plane_coords=normals_tangential)
        unit_vector_axis = np.zeros(3)
        unit_vector_axis[self.axis] = 1
        tangentials = np.cross(normals, unit_vector_axis)

        # differentials (float)
        d_length = 1.0 if np.isinf(self.length) else self.length
        d_edge = 2 * np.pi * self.radius / NUM_PTS_ADJOINT_CYLINDER
        d_area = d_length * d_edge

        # evaluate E and D maps at the cylinder radius
        pts_interp = dict(zip("xyz", pts.T))
        keys = [f"E{dim}" for dim in "xyz"]
        D_der = {k: derivative_info.D_der_map[k].interp(**pts_interp).sum("f") for k in keys}
        E_der = {k: derivative_info.E_der_map[k].interp(**pts_interp).sum("f") for k in keys}

        # sort into normal and tangential components
        D_normal = self.project_in_basis(der_dataset=D_der, basis_vector=normals)
        E_tangential = self.project_in_basis(der_dataset=E_der, basis_vector=tangentials)

        # permittivity changes inside and outside
        eps_in = derivative_info.eps_in
        eps_out = derivative_info.eps_out
        delta_eps_perps = eps_in - eps_out
        delta_eps_inv_normal = 1.0 / eps_in - 1.0 / eps_out

        grad_unnormalized = -delta_eps_inv_normal * D_normal + delta_eps_perps * E_tangential
        return np.real(grad_unnormalized.values * d_area)

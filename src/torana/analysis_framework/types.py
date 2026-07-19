"""
Analysis Framework type definitions.

This module defines reusable enumerations and immutable value objects
shared across the Analysis Framework.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any


# ============================================================================
# Enumerations
# ============================================================================


class AnalysisCategory(StrEnum):
    """Categories of spatial analyses."""

    HYDROLOGY = auto()
    CLIMATE = auto()
    ENVIRONMENT = auto()
    TERRAIN = auto()
    TRANSPORT = auto()
    URBAN = auto()
    ENERGY = auto()
    ECOLOGY = auto()
    HAZARD = auto()
    CUSTOM = auto()


class OutputType(StrEnum):
    """Logical output types produced by an analysis."""

    RASTER = auto()
    VECTOR = auto()
    TABLE = auto()
    REPORT = auto()
    METADATA = auto()
    STATISTICS = auto()


class OutputFormat(StrEnum):
    """Supported export formats."""

    GEOTIFF = auto()
    GEOPACKAGE = auto()
    GEOJSON = auto()
    SHAPEFILE = auto()
    CSV = auto()
    JSON = auto()
    PDF = auto()
    PNG = auto()
    HTML = auto()


class ParameterType(StrEnum):
    """Supported analysis parameter types."""

    STRING = auto()
    INTEGER = auto()
    FLOAT = auto()
    BOOLEAN = auto()
    PATH = auto()
    ENUM = auto()


# ============================================================================
# Value Objects
# ============================================================================


@dataclass(frozen=True, slots=True)
class AnalysisOutput:
    """
    Describes an output produced by an analysis.
    """

    name: str
    output_type: OutputType
    formats: tuple[OutputFormat, ...]
    optional: bool = False


@dataclass(frozen=True, slots=True)
class ParameterConstraints:
    """
    Validation constraints for a parameter.
    """

    minimum: Any | None = None
    maximum: Any | None = None
    choices: tuple[Any, ...] = ()


@dataclass(frozen=True, slots=True)
class ParameterGroup:
    """
    Groups related analysis parameters.

    Examples
    --------
    General
    DEM
    Hydrology
    Rainfall
    Outputs
    """

    name: str
    description: str | None = None
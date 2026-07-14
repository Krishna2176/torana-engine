"""
Common types used throughout the Dataset Framework.
"""

from __future__ import annotations

from enum import StrEnum


class DatasetCategory(StrEnum):
    ELEVATION = "elevation"
    IMAGERY = "imagery"
    TRANSPORTATION = "transportation"
    HYDROLOGY = "hydrology"
    LANDCOVER = "landcover"
    CLIMATE = "climate"
    BUILDINGS = "buildings"
    BOUNDARIES = "boundaries"


class DatasetType(StrEnum):
    RASTER = "raster"
    VECTOR = "vector"
    TABLE = "table"
    POINT_CLOUD = "point_cloud"


class DatasetDomain(StrEnum):
    TERRAIN = "terrain"
    URBAN = "urban"
    ENVIRONMENTAL = "environmental"
    TRANSPORTATION = "transportation"
    HYDROLOGY = "hydrology"
    CLIMATE = "climate"


class UpdateFrequency(StrEnum):
    STATIC = "static"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
"""
Dataset characteristics.
"""

from __future__ import annotations

from dataclasses import dataclass

from .types import (
    DatasetCategory,
    DatasetDomain,
    DatasetType,
)


@dataclass(frozen=True, slots=True)
class DatasetCharacteristics:
    """
    Intrinsic characteristics of a dataset.
    """

    category: DatasetCategory

    dataset_type: DatasetType

    domain: DatasetDomain

    crs: str | None = None

    resolution: float | None = None

    extent: str | None = None

    tags: tuple[str, ...] = ()
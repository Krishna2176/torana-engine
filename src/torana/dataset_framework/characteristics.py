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
    
    
# ------------------------------------------------------------------
# Compatibility
# ------------------------------------------------------------------

    def is_compatible_with(
        self,
        other: "DatasetCharacteristics",
    ) -> bool:
        """
        Return True if these characteristics satisfy the supplied
        characteristics.

        Compatibility is determined by comparing intrinsic dataset
        properties.
        """

        if self.category != other.category:
            return False

        if self.dataset_type != other.dataset_type:
            return False

        if self.domain != other.domain:
            return False

        if (
            other.crs is not None
            and self.crs != other.crs
        ):
            return False

        if (
            other.resolution is not None
            and self.resolution != other.resolution
        ):
            return False

        if (
            other.extent is not None
            and self.extent != other.extent
        ):
            return False

        if other.tags:

            if not set(other.tags).issubset(
                self.tags,
            ):
                return False

        return True
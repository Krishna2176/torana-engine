"""
Dataset Requirement.
"""

from __future__ import annotations

from dataclasses import dataclass

from .characteristics import DatasetCharacteristics


@dataclass(frozen=True, slots=True)
class DatasetRequirement:
    """
    Declares the characteristics required by an Analysis Plugin.
    """

    characteristics: DatasetCharacteristics
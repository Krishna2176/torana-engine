"""
Dataset Manifest.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from .characteristics import DatasetCharacteristics
from .types import UpdateFrequency


@dataclass(frozen=True, slots=True)
class DatasetManifest:
    """
    Immutable description of a dataset.
    """

    # Identity

    id: str
    name: str
    version: str
    description: str

    # Characteristics

    characteristics: DatasetCharacteristics

    # Temporal

    acquisition_date: str
    update_frequency: UpdateFrequency

    # Provider

    provider: str
    provider_version: str

    # License

    license: str
    attribution: str

    @property
    def identifier(self) -> Final[str]:
        return self.id
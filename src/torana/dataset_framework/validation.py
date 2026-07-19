"""
Dataset Validation.
"""

from __future__ import annotations

from .manifest import DatasetManifest
from .requirement import DatasetRequirement


class DatasetValidation:
    """
    Validates whether a Dataset Manifest satisfies a
    Dataset Requirement.
    """

    def validate(
        self,
        requirement: DatasetRequirement,
        manifest: DatasetManifest,
    ) -> bool:

        return manifest.characteristics.is_compatible_with(
            requirement.characteristics,
        )
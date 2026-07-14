"""
Shared fixtures for Dataset Framework tests.
"""

from __future__ import annotations

import pytest

from torana.dataset_framework import (
    BaseProvider,
    DatasetCategory,
    DatasetCharacteristics,
    DatasetDomain,
    DatasetManifest,
    DatasetRequirement,
    DatasetType,
    UpdateFrequency,
)


# ---------------------------------------------------------------------
# Characteristics
# ---------------------------------------------------------------------


@pytest.fixture
def characteristics() -> DatasetCharacteristics:
    return DatasetCharacteristics(
        category=DatasetCategory.ELEVATION,
        dataset_type=DatasetType.RASTER,
        domain=DatasetDomain.TERRAIN,
        crs="EPSG:4326",
        resolution=30.0,
        extent="India",
        tags=("dem",),
    )


# ---------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------


@pytest.fixture
def manifest(
    characteristics: DatasetCharacteristics,
) -> DatasetManifest:

    return DatasetManifest(
        id="dem_30m",
        name="30m Digital Elevation Model",
        version="1.0.0",
        description="Reference DEM dataset.",

        characteristics=characteristics,

        acquisition_date="2025-01-01",
        update_frequency=UpdateFrequency.STATIC,

        provider="Local Provider",
        provider_version="1.0.0",

        license="CC BY 4.0",
        attribution="TORANA",
    )


# ---------------------------------------------------------------------
# Requirement
# ---------------------------------------------------------------------


@pytest.fixture
def requirement(
    characteristics: DatasetCharacteristics,
) -> DatasetRequirement:

    return DatasetRequirement(
        characteristics=characteristics,
    )


# ---------------------------------------------------------------------
# Dummy Provider
# ---------------------------------------------------------------------


class DummyProvider(BaseProvider):

    def __init__(
        self,
        manifest: DatasetManifest,
    ) -> None:

        super().__init__(
            id="local",
            name="Local Provider",
            version="1.0.0",
            description="Reference Dataset Provider.",
        )

        self._manifest = manifest

    @property
    def manifests(self):

        return (self._manifest,)

    def discover(
        self,
        requirement: DatasetRequirement,
    ):

        return self.manifests

    def is_available(
        self,
        dataset_id: str,
    ) -> bool:

        return dataset_id == self._manifest.id

    def acquire(
        self,
        dataset_id: str,
    ):

        return {
            "dataset_id": dataset_id,
        }


@pytest.fixture
def provider(
    manifest: DatasetManifest,
):

    return DummyProvider(manifest)
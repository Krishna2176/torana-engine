"""
TORANA Engine

Dummy Plugin

Reusable Plugin implementation for unit tests.
"""

from __future__ import annotations

from typing import Any

from torana.core.plugin import Plugin
from torana.core.workflow import Workflow


class DummyPlugin(Plugin):
    """
    Simple Plugin implementation used by the
    TORANA test suite.
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    @property
    def id(self) -> str:
        return "uhi"

    @property
    def name(self) -> str:
        return "Urban Heat Island"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def description(self) -> str:
        return "Dummy Urban Heat Island plugin."

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    @property
    def metadata(self) -> dict[str, Any]:
        return {
            "author": "TORANA",
            "category": "Testing"
        }

    # -------------------------------------------------
    # Configuration
    # -------------------------------------------------

    @property
    def configuration_schema(self) -> dict[str, Any]:
        return {}

    # -------------------------------------------------
    # Dataset Requirements
    # -------------------------------------------------

    @property
    def required_datasets(self) -> list[str]:
        return []

    @property
    def optional_datasets(self) -> list[str]:
        return []

    # -------------------------------------------------
    # Workflow
    # -------------------------------------------------

    @property
    def workflow(self) -> Workflow:
        return Workflow()

    # -------------------------------------------------
    # Outputs
    # -------------------------------------------------

    @property
    def outputs(self) -> list[str]:
        return []

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    def validate(self) -> bool:
        return True
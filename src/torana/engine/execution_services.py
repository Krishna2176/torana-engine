"""
TORANA Engine

Execution Services
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ExecutionServices:
    """
    References to Engine services.

    These are injected by the Engine.
    """

    logger: object | None = None

    cache: object | None = None

    dataset_manager: object | None = None

    exporter: object | None = None
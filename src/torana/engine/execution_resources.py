"""
TORANA Engine

Execution Resources
"""

from __future__ import annotations

from dataclasses import dataclass, field

from torana.common.types import OutputCollection


@dataclass(slots=True)
class ExecutionResources:
    """
    Runtime resources created during execution.
    """

    datasets: dict[str, object] = field(default_factory=dict)

    temporary_files: dict[str, str] = field(default_factory=dict)

    shared_objects: dict[str, object] = field(default_factory=dict)

    outputs: OutputCollection = field(default_factory=dict)
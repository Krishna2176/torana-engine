"""
TORANA Engine

Job Specification
"""

from __future__ import annotations

from dataclasses import dataclass

from torana.common.types import Configuration


@dataclass(frozen=True, slots=True)
class JobSpecification:
    """
    Immutable description of a Job.
    """

    plugin_id: str

    configuration: Configuration
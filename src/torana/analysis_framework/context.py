"""
Analysis execution context.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from torana.engine.execution_context import ExecutionContext


@dataclass(frozen=True, slots=True)
class AnalysisExecutionContext:
    """
    Runtime information available during analysis planning.

    Notes
    -----
    Dataset values are temporarily typed as ``Any`` until the
    Dataset runtime model is introduced.
    """

    execution_context: ExecutionContext

    datasets: Mapping[str, Any]
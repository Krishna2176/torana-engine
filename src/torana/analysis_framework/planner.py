"""
Analysis planning contracts.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from torana.analysis_framework.base_analysis import BaseAnalysis
from torana.analysis_framework.context import AnalysisExecutionContext
from torana.core.workflow import Workflow


class AnalysisPlanner(ABC):
    """
    Converts an Analysis into an executable Workflow.
    """

    @abstractmethod
    def plan(
        self,
        analysis: BaseAnalysis,
        context: AnalysisExecutionContext,
    ) -> Workflow:
        """
        Produce an executable workflow.
        """
        raise NotImplementedError
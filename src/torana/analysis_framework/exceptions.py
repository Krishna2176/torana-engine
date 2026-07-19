"""
Analysis Framework exceptions.
"""


class AnalysisFrameworkError(Exception):
    """Base exception for the Analysis Framework."""


class AnalysisConfigurationError(AnalysisFrameworkError):
    """Raised when analysis configuration is invalid."""


class AnalysisExecutionError(AnalysisFrameworkError):
    """Raised when an analysis cannot be executed."""


class WorkflowBuildError(AnalysisFrameworkError):
    """Raised when workflow generation fails."""
"""
Analysis Framework configuration models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Iterator, Mapping

from torana.analysis_framework.types import (
    ParameterConstraints,
    ParameterGroup,
    ParameterType,
)


# ============================================================================
# Parameter Definitions
# ============================================================================


@dataclass(frozen=True, slots=True)
class AnalysisParameter:
    """
    Defines a configurable analysis parameter.

    This model describes the parameter schema,
    not the runtime value.
    """

    name: str
    description: str
    parameter_type: ParameterType
    group: ParameterGroup

    required: bool = True
    default: Any | None = None
    unit: str | None = None

    constraints: ParameterConstraints = field(
        default_factory=ParameterConstraints
    )


# ============================================================================
# Parameter Schema
# ============================================================================


@dataclass(frozen=True, slots=True)
class AnalysisParameterSchema:
    """
    Immutable collection describing every parameter supported by an analysis.
    """

    parameters: tuple[AnalysisParameter, ...] = ()

    _lookup: Mapping[str, AnalysisParameter] = field(
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "_lookup",
            MappingProxyType(
                {
                    parameter.name: parameter
                    for parameter in self.parameters
                }
            ),
        )

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def get(
        self,
        name: str,
    ) -> AnalysisParameter:
        """
        Return a parameter by name.

        Raises
        ------
        KeyError
            If the parameter does not exist.
        """
        return self._lookup[name]

    # ------------------------------------------------------------------
    # Collection Protocol
    # ------------------------------------------------------------------

    def __getitem__(
        self,
        name: str,
    ) -> AnalysisParameter:
        return self._lookup[name]

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return name in self._lookup

    def __iter__(
        self,
    ) -> Iterator[AnalysisParameter]:
        return iter(self.parameters)

    def __len__(
        self,
    ) -> int:
        return len(self.parameters)

    # ------------------------------------------------------------------
    # Convenience API
    # ------------------------------------------------------------------

    def contains(
        self,
        name: str,
    ) -> bool:
        """
        Return True if the parameter exists.
        """
        return name in self

    # ------------------------------------------------------------------
    # Derived Collections
    # ------------------------------------------------------------------

    @property
    def required_parameters(
        self,
    ) -> tuple[AnalysisParameter, ...]:
        """
        Return all required parameters.
        """
        return tuple(
            parameter
            for parameter in self.parameters
            if parameter.required
        )

    @property
    def optional_parameters(
        self,
    ) -> tuple[AnalysisParameter, ...]:
        """
        Return all optional parameters.
        """
        return tuple(
            parameter
            for parameter in self.parameters
            if not parameter.required
        )

    @property
    def groups(
        self,
    ) -> tuple[ParameterGroup, ...]:
        """
        Return all unique parameter groups.
        """
        unique: dict[str, ParameterGroup] = {}

        for parameter in self.parameters:
            unique.setdefault(
                parameter.group.name,
                parameter.group,
            )

        return tuple(unique.values())


# ============================================================================
# Runtime Configuration
# ============================================================================


@dataclass(frozen=True, slots=True)
class AnalysisConfiguration:
    """
    Immutable runtime configuration supplied to an analysis.
    """

    values: Mapping[str, Any] = field(
        default_factory=dict,
    )

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "values",
            MappingProxyType(dict(self.values)),
        )

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def get(
        self,
        name: str,
        default: Any = None,
    ) -> Any:
        """
        Return a configuration value.
        """
        return self.values.get(
            name,
            default,
        )

    # ------------------------------------------------------------------
    # Mapping Protocol
    # ------------------------------------------------------------------

    def __getitem__(
        self,
        name: str,
    ) -> Any:
        return self.values[name]

    def __contains__(
        self,
        name: object,
    ) -> bool:
        return name in self.values

    def __iter__(
        self,
    ) -> Iterator[str]:
        return iter(self.values)

    def __len__(
        self,
    ) -> int:
        return len(self.values)

    # ------------------------------------------------------------------
    # Convenience API
    # ------------------------------------------------------------------

    def contains(
        self,
        name: str,
    ) -> bool:
        """
        Return True if a configuration value exists.
        """
        return name in self
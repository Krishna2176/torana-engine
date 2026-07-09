# Engineering Decisions

This document records the major engineering and architectural decisions that guide the development of TORANA Engine.

Detailed rationale and discussion for significant architectural decisions are documented separately in the Architecture Decision Records (ADRs).

This document should be updated whenever a long-term engineering decision is made.

---

# System Architecture

- TORANA Engine follows a modular architecture.
- Engine Core remains independent of all domain-specific analysis.
- The Plugin Framework is the extensibility layer of the Engine.
- Analysis is independent from visualization.
- Execution is workflow-driven.
- Every domain-specific capability should be implemented as a Plugin without modifying the Engine Core.
- Composition is preferred over inheritance.
- Dependency Injection is preferred over global state.

---

# Engine Core

- Engine acts as a thin orchestrator.
- Engine validates Plugins but never executes analysis directly.
- ExecutionManager owns the execution lifecycle.
- Scheduler determines executable Tasks.
- Scheduler remains stateless.
- TaskExecutor executes individual Tasks.
- Workflow owns task dependency graphs.
- Runtime state is isolated from configuration.
- Engine Core v1.0 is frozen.
- Future capabilities should be implemented through extension frameworks rather than expanding the Engine Core.
- Changes to Engine Core are limited to:
  - Bug fixes
  - Documentation improvements
  - Additional tests
  - Non-breaking refactoring

---

# Plugin Framework

- Plugin Framework defines plugin contracts, lifecycle, metadata, validation, and discovery.
- Analysis Plugins define domain knowledge.
- Plugins construct Workflows; they do not execute analyses.
- Plugins communicate with the Engine only through defined contracts.
- Plugins are independently versioned.
- Flood Risk is the reference implementation for all Analysis Plugins.

Future plugin categories will include:

- Dataset Provider Plugins
- Visualization Plugins
- Report Plugins
- Export Plugins

---

# Development Process

- Architecture before implementation.
- Documentation before coding.
- Test Design before implementation.
- Small iterative milestones.
- Refactor continuously.
- Documentation must remain synchronized with implementation.
- Every milestone follows the TORANA Definition of Done.

---

# Repository

- Private repository.
- Proprietary source code.
- All Rights Reserved.
- The repository documentation is the authoritative source of project state.
- Architectural decisions should be documented before implementation begins.

---

# Documentation

- Every subsystem maintains its own architecture documentation.
- Architecture documents describe system design.
- Specifications describe implementation contracts.
- ADRs record architectural reasoning.
- Project documentation records engineering progress and project state.

---

# Future Direction

TORANA Engine is being developed as a long-term geospatial computation framework.

Future architectural work will expand the platform through reusable frameworks rather than increasing the complexity of the Engine Core.
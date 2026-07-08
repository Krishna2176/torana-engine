# TORANA Engine Architecture

**Version:** 0.1  
**Status:** Active  
**Last Updated:** July 2026

---

# Vision

TORANA (Terrain-Oriented Research, Analysis & Network Automation) is a modular geospatial computation framework designed to automate spatial analysis, simulation, visualization, and reporting.

The long-term goal of TORANA is to allow a user to describe **what** they want to analyse rather than **how** to perform the analysis.

Instead of manually downloading datasets, writing GIS scripts, processing rasters, exporting maps, and creating reports, the Engine orchestrates the entire workflow through reusable plugins and standardized execution pipelines.

---

# Purpose

TORANA separates responsibilities into independent components.

This separation allows each subsystem to evolve without affecting the others.

The architecture is built around the following principles:

- Modular
- Extensible
- Plugin-driven
- Testable
- Maintainable
- Independent of any specific GIS software

---

# Core Principles

## 1. Analysis is independent of visualization

Spatial analysis produces results.

Visualization consumes results.

Neither component depends on the implementation of the other.

---

## 2. Plugins define analysis

The Engine never contains analysis logic.

Instead, analyses are implemented as Plugins.

Examples include:

- Urban Heat Island
- Flood Risk
- Walkability
- Solar Potential
- Accessibility
- Land Suitability

---

## 3. Engine orchestrates execution

The Engine coordinates execution.

It does not implement GIS algorithms.

Its responsibilities include:

- Loading plugins
- Creating jobs
- Managing workflows
- Scheduling tasks
- Reporting execution status

---

## 4. Workflows define execution order

A Workflow is a Directed Acyclic Graph (DAG) describing task dependencies.

The Engine executes the Workflow.

The Workflow itself never executes tasks.

---

## 5. Tasks are independent

A Task represents one unit of work.

Tasks contain state and metadata only.

Dependency management belongs to the Workflow.

Execution belongs to the Engine.

---

# System Architecture

```text
                 User
                   │
                   ▼
            Analysis Request
                   │
                   ▼
               Engine
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 Plugin Registry         Job Manager
        │                     │
        ▼                     ▼
     Plugins            Workflow (DAG)
                               │
                               ▼
                             Tasks
                               │
                               ▼
                      Analysis Services
                               │
                               ▼
                         Generated Outputs
```

---

# Project Structure

```text
torana-engine/

├── src/
│   └── torana/
│       ├── core/
│       ├── engine/
│       ├── plugins/
│       ├── services/
│       ├── analysis/
│       ├── datasets/
│       ├── visualization/
│       └── utils/
│
├── docs/
├── tests/
├── data/
├── outputs/
├── configs/
└── scripts/
```

---

# Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Engine | Orchestrates execution |
| Plugin | Defines an analysis |
| Registry | Stores available plugins |
| Workflow | Defines task dependencies |
| Task | Represents one executable unit of work |
| Services | Shared infrastructure (logging, caching, exporting, scheduling) |

---

# Execution Pipeline

A typical execution follows these stages:

1. User submits an analysis request.
2. Engine selects the requested Plugin.
3. Plugin defines the required Workflow.
4. Workflow identifies executable Tasks.
5. Engine schedules Tasks.
6. Analysis Services perform computations.
7. Outputs are generated.
8. Visualization consumes the outputs.

---

# Development Principles

TORANA follows several engineering principles.

- Architecture before implementation.
- One feature at a time.
- Every feature has tests.
- Documentation evolves with implementation.
- Components have a single responsibility.
- Public APIs should remain stable.
- Design for extensibility rather than quick solutions.

---

# Current Implementation Status

| Component | Status |
|-----------|--------|
| Plugin | ✅ Implemented |
| Registry | ✅ Implemented |
| Task | ✅ Implemented |
| Workflow | ✅ Implemented |
| Job | 🚧 Planned |
| Engine | 🚧 Planned |
| Scheduler | 🚧 Planned |
| Executor | 🚧 Planned |
| Dataset Manager | 🚧 Planned |

---

# Future Roadmap

The next major milestones are:

1. Job
2. Engine
3. Scheduler
4. Task Executor
5. Dataset Manager
6. Plugin Loader
7. Built-in Analysis Plugins
8. Visualization Pipeline
9. Reporting System

---

# Notes

This document describes the high-level architecture of TORANA.

Detailed behavior of individual components is documented separately:

- `concepts.md`
- `engine.md`
- `plugin.md`
- `workflow.md`
- `task_system.md`
- `plugin_spec.md`
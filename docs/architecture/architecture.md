# TORANA Engine Architecture

**Milestone:** Engine Core v1.0

**Status:** Stable

**Last Updated:** July 2026

---

# Vision

TORANA Engine is a modular geospatial computation framework designed to automate spatial analysis through reusable plugins.

The framework separates domain models, execution orchestration, infrastructure services, visualization, and plugin implementations into independent modules.

Every analysis supported by TORANA should be implementable as a Plugin without requiring modifications to the Engine.

---

# Design Goals

The architecture is designed around five goals.

- Modular
- Extensible
- Testable
- Deterministic
- Scalable

The Engine should coordinate execution while remaining completely independent of GIS algorithms.

---

# Architectural Principles

TORANA follows several architectural principles.

## Single Responsibility

Every component has one responsibility.

Examples

- Engine coordinates execution.
- Scheduler determines executable Tasks.
- TaskExecutor executes Tasks.
- Workflow owns dependency graphs.

---

## Composition over Inheritance

Complex behavior is created by composing smaller components.

The Engine composes:

- PluginRegistry
- ExecutionManager

The ExecutionManager composes:

- Scheduler
- TaskExecutor

---

## Plugin Architecture

Spatial analysis is implemented through Plugins.

The Engine itself never performs GIS analysis.

This allows new analyses to be added without changing the Engine.

---

## Runtime Isolation

Execution state is separated from configuration.

A Job describes what should be executed.

An ExecutionContext describes how that Job is currently executing.

---

## Dependency Injection

Core components receive their collaborators through constructors.

Examples include:

- Engine → ExecutionManager
- ExecutionManager → Scheduler
- ExecutionManager → TaskExecutor

This improves testing and future extensibility.

---

# High-Level Architecture

```text
                           User
                             │
                             ▼
                            Job
                             │
                             ▼
                          Engine
                             │
                             ▼
                    ExecutionManager
                  ┌──────────┴──────────┐
                  ▼                     ▼
             Scheduler           TaskExecutor
                  │                     │
                  └──────────┬──────────┘
                             ▼
                         Workflow
                             │
                             ▼
                           Tasks
```

---

# Architectural Layers

TORANA is divided into distinct architectural layers.

---

## Domain Layer

Defines the core business models.

Components

- Plugin
- Job
- Workflow
- Task

These classes describe analysis without executing it.

---

## Runtime Layer

Represents execution state.

Components

- ExecutionContext
- ExecutionState
- ExecutionResources
- ExecutionServices

These objects exist only while a Job executes.

---

## Orchestration Layer

Coordinates execution.

Components

- Engine
- ExecutionManager
- Scheduler
- TaskExecutor
- PluginRegistry

This layer never performs GIS analysis.

---

## Infrastructure Layer

Provides reusable services.

Examples

- Dataset Manager
- Configuration
- Cache
- Exporter
- Logger

---

## Plugin Layer

Contains user-developed analyses.

Examples

- Urban Heat Island
- Walkability
- Flood Risk
- Solar Potential
- Noise Mapping

Each Plugin defines:

- configuration
- datasets
- workflow
- outputs

---

# Execution Flow

```text
User

↓

Create Job

↓

Engine.submit()

↓

Validate Plugin

↓

Create ExecutionContext

↓

ExecutionManager

↓

Scheduler

↓

TaskExecutor

↓

Workflow

↓

Tasks

↓

Results
```

---

# Responsibilities

## Engine

Responsible for:

- Job validation
- Plugin validation
- ExecutionContext creation
- Delegating execution

Not responsible for:

- Scheduling
- Task execution
- GIS analysis

---

## ExecutionManager

Responsible for:

- Execution lifecycle
- Coordinating Scheduler
- Coordinating TaskExecutor

---

## Scheduler

Responsible for:

- Discovering executable Tasks
- Determining execution frontier

---

## TaskExecutor

Responsible for:

- Executing one Task
- Managing Task lifecycle

---

## Workflow

Responsible for:

- Dependency graph
- Graph queries
- Task relationships

---

## Plugin

Responsible for:

- Declaring analysis
- Declaring workflow
- Declaring datasets
- Providing analysis implementation

---

# Current Engine Pipeline

```text
                Engine

                   │

                   ▼

         ExecutionManager

          │             │

          ▼             ▼

    Scheduler     TaskExecutor

          │             │

          └──────┬──────┘

                 ▼

             Workflow

                 │

                 ▼

               Tasks
```

---

# Future Architecture

The following components are planned.

Execution

- Retry Policy
- Parallel Execution
- Distributed Execution

Services

- Dataset Manager
- Resource Manager
- Plugin Loader

Plugins

- Urban Heat Island
- Walkability
- Flood Risk
- Shadow Analysis
- Solar Potential
- Noise Mapping

Visualization

- Three.js
- Blender
- Reports
- Interactive Maps

---

# Engine Core Status

## Implemented

### Core Models

- Plugin
- Task
- Workflow
- Job

### Runtime

- ExecutionContext
- ExecutionState
- ExecutionResources
- ExecutionServices

### Execution

- Engine
- PluginRegistry
- Scheduler
- ExecutionManager
- TaskExecutor

### Testing

- Comprehensive unit tests
- Shared testing fixtures
- Dependency injection

### Documentation

- Architecture
- Engine
- Workflow
- Scheduler
- Execution pipeline

---

## Next Milestone

Plugin Framework v1.0

This milestone introduces:

- Plugin discovery
- Plugin execution
- Urban Heat Island Plugin
- Configuration validation
- Dataset requirements

---

# Summary

The Engine Core establishes the execution framework of TORANA.

From this point onward, future development focuses on implementing reusable Plugins rather than expanding the Engine itself.

The Engine is intended to remain small, stable, and independent of domain-specific GIS algorithms.
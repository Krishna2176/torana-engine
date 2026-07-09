# TORANA Engine Architecture

**Version:** 0.2

**Status:** Active

**Last Updated:** July 2026

---

# Vision

TORANA Engine is a modular geospatial computation framework designed to automate spatial analysis through reusable analysis plugins.

The framework separates domain models, runtime execution, orchestration, infrastructure services, and visualization into independent modules.

The primary objective is to provide a scalable architecture capable of supporting GIS workflows, remote sensing analyses, urban simulations, and future distributed execution.

---

# High-Level Architecture

```
                    User
                     │
                     ▼
                    Job
                     │
                     ▼
                  Engine
                     │
                     ▼
            Execution Context
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 ExecutionState ExecutionResources ExecutionServices
                     │
                     ▼
                 Workflow
                     │
                     ▼
                    Tasks
```

---

# Layers

TORANA is organized into five architectural layers.

## Domain Layer

Defines the business objects.

Includes:

- Plugin
- Task
- Workflow
- Job

These classes describe *what* the Engine executes.

---

## Runtime Layer

Represents execution state.

Includes:

- ExecutionContext
- ExecutionState
- ExecutionResources
- ExecutionServices

These classes exist only while a Job is executing.

---

## Orchestration Layer

Coordinates execution.

Includes:

- Engine
- PluginRegistry

Future additions:

- Scheduler
- TaskExecutor

---

## Infrastructure Layer

Provides shared services.

Examples:

- Dataset Manager
- Logger
- Cache
- Exporter
- Configuration

---

## Extension Layer

Contains user-developed Plugins.

Every analysis is implemented as a Plugin rather than inside the Engine.

---

# Core Principles

- Composition over inheritance
- Separation of responsibilities
- Plugin-based architecture
- Workflow-driven execution
- Immutable specifications
- Runtime isolation
- Service injection

---

# Execution Flow

```
User
    │
    ▼
Create Job
    │
    ▼
Engine.submit()
    │
    ▼
Validate Plugin
    │
    ▼
Create ExecutionContext
    │
    ▼
Workflow Execution
    │
    ▼
Results
```

---

# Current Status

## Implemented

- Plugin
- Plugin Registry
- Task
- Workflow
- Job
- Execution Context
- Engine

## Planned

- Scheduler
- Task Executor
- Dataset Manager
- Plugin Loader
- Service Injection
- Distributed Execution

---

# Notes

TORANA intentionally separates execution orchestration from analysis implementation.

The Engine coordinates execution but never performs GIS analysis itself.
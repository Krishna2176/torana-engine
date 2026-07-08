# Task Model

**Version:** 0.1  
**Status:** Active  
**Last Updated:** July 2026

---

# Vision

Tasks are the smallest executable units within TORANA.

Every analysis is ultimately decomposed into independent Tasks that the Engine can schedule, monitor, and execute.

Tasks intentionally contain only execution state and metadata.

They do not perform execution themselves.

---

# Purpose

A Task represents one atomic unit of work within a Workflow.

Examples include:

- Download a dataset
- Clip a raster
- Compute NDVI
- Generate contours
- Calculate slope
- Export a GeoPackage

Tasks are reusable building blocks that can be combined into many different Workflows.

---

# Responsibilities

A Task is responsible for:

- Providing a unique identity
- Holding execution status
- Storing metadata
- Representing a unit of work

A Task is **not** responsible for:

- Scheduling
- Execution
- Dependency management
- Job management
- Dataset management

---

# Design Principles

## Independent

Tasks are independent objects.

They have no knowledge of other Tasks.

---

## Stateless Execution

A Task stores execution state only.

Execution logic belongs elsewhere.

---

## Reusable

The same Task definition may be used by multiple Workflows.

---

# Data Model

Every Task contains:

- id
- name
- description
- status
- metadata

The exact implementation may evolve, but these concepts remain stable.

---

# Task Lifecycle

Tasks progress through the following lifecycle.

```text
CREATED
    │
    ▼
READY
    │
    ▼
RUNNING
    │
    ▼
COMPLETED
```

Possible alternative states include:

```text
RUNNING
    │
    ├──► FAILED
    │
    └──► CANCELLED
```

The Engine is responsible for changing Task states.

---

# Relationships

```text
Workflow
      │
      ▼
    Task
      │
      ▼
 Services
```

A Workflow organizes Tasks.

The Engine executes them.

Services provide the required infrastructure.

---

# Task Metadata

Metadata provides additional information about a Task.

Examples include:

- processing hints
- execution priority (future)
- estimated runtime (future)
- logging information

Metadata should never contain execution logic.

---

# Execution

Tasks are executed by the Engine through future execution components such as:

- Scheduler
- Task Executor

The Task itself never performs execution.

---

# Future Extensions

Future versions may introduce:

- progress reporting
- retry policies
- execution priorities
- resource requirements
- cancellation tokens
- distributed execution metadata

These additions should extend the Task model without changing its fundamental responsibility.

---

# Notes

Tasks represent work.

Workflows organize work.

The Engine executes work.

Keeping these responsibilities separate allows TORANA to remain modular, testable, and extensible.
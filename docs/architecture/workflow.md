# Workflow Architecture

**Version:** 0.1  
**Status:** Active  
**Last Updated:** July 2026

---

# Vision

A Workflow defines **how an analysis is organized**, not **how it is executed**.

It represents the execution structure of an analysis by organizing independent Tasks into a Directed Acyclic Graph (DAG).

The Workflow enables the Engine to determine execution order without embedding scheduling logic inside Tasks or Plugins.

---

# Purpose

A Workflow connects individual Tasks into a complete analysis pipeline.

Its primary responsibilities are to:

- Organize Tasks
- Define dependencies
- Validate execution order
- Identify Tasks that are ready for execution

The Workflow itself never performs execution.

---

# Responsibilities

A Workflow is responsible for:

- Managing Tasks
- Managing dependency relationships
- Maintaining a valid execution graph
- Identifying executable Tasks
- Providing execution structure to the Engine

A Workflow is **not** responsible for:

- Executing Tasks
- Scheduling Tasks
- Managing Jobs
- Running GIS algorithms
- Producing Outputs

---

# Design Principles

## Directed Acyclic Graph (DAG)

TORANA represents every Workflow as a Directed Acyclic Graph.

This ensures:

- deterministic execution
- dependency tracking
- parallel execution (future)
- cycle prevention

---

## Separation of Responsibilities

Tasks represent work.

The Workflow represents relationships between Tasks.

The Engine performs execution.

---

## Declarative Structure

A Workflow describes execution.

It does not perform execution.

This allows the Engine to apply different scheduling strategies without changing the Workflow itself.

---

# Workflow Structure

Conceptually a Workflow consists of:

- Tasks
- Dependency Graph
- Validation Rules

Example:

```text
Download DEM
       │
       ▼
Clip DEM
   ┌───┴────┐
   ▼        ▼
Slope    Aspect
   └───┬────┘
       ▼
 Export Results
```

Each node is a Task.

Each edge represents a dependency.

---

# Dependency Management

Dependencies belong to the Workflow.

Tasks remain completely independent.

This allows:

- Task reuse
- Flexible scheduling
- Easer testing
- Cleaner architecture

---

# Ready Tasks

One of the Workflow's primary responsibilities is determining which Tasks are ready for execution.

A Task is considered ready when all of its dependencies have completed successfully.

The Engine uses this information to decide what to execute next.

---

# Validation

A Workflow should ensure:

- Every Task has a unique identifier.
- All dependencies reference valid Tasks.
- No cyclic dependencies exist.
- The execution graph is complete.

Validation occurs before execution begins.

---

# Relationships

```text
Plugin
    │
    ▼
Workflow
    │
    ▼
Tasks
    │
    ▼
Engine
```

The Plugin defines the Workflow.

The Workflow defines the execution structure.

The Engine executes the Workflow.

---

# Future Extensions

Future versions of TORANA may extend the Workflow with:

- Conditional branches
- Parallel execution
- Retry paths
- Resource constraints
- Distributed execution
- Dynamic task generation

These capabilities should extend the Workflow without changing its core responsibility.

---

# Notes

The Workflow is the execution blueprint of an analysis.

It provides structure, not execution.

By separating execution order from execution logic, TORANA remains modular, extensible, and capable of supporting increasingly complex geospatial analyses.
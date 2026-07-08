# TORANA Documentation

Welcome to the official documentation for **TORANA Engine**.

This documentation describes the architecture, specifications, and development practices used throughout the project.

The documentation is organized by purpose rather than by implementation.

---

# Documentation Structure

```text
docs/

├── architecture/
├── specifications/
├── adr/
├── diagrams/
├── tutorials/
├── guides/
└── api/
```

---

# Where to Start

If you are new to TORANA, read the documentation in the following order:

1. `architecture/architecture.md`
2. `architecture/concepts.md`
3. `architecture/engine.md`
4. `architecture/plugin.md`
5. `architecture/task_system.md`
6. `architecture/workflow.md`

This sequence introduces the architecture from the highest level down to individual components.

---

# Documentation Categories

## Architecture

Describes the design and philosophy of TORANA.

Files include:

- architecture.md
- concepts.md
- engine.md
- plugin.md
- workflow.md
- task_system.md

These documents answer:

> Why does this component exist?

---

## Specifications

Defines implementation contracts.

Current specifications include:

- plugin_spec.md
- config_spec.md
- dataset_spec.md
- api_spec.md

These documents answer:

> What must an implementation provide?

---

## Architecture Decision Records (ADR)

ADRs record important engineering decisions.

Examples include:

- Source layout
- Plugin architecture
- Workflow design
- Registry design

These documents answer:

> Why was this design chosen?

---

## Diagrams

Visual representations of the architecture.

Examples:

- System Architecture
- Workflow DAG
- Execution Pipeline
- Job Lifecycle

---

## Guides

Practical documentation for contributors.

Examples:

- Project setup
- Coding standards
- Development workflow

---

## Tutorials

Step-by-step learning material.

Examples:

- Creating a Plugin
- Running the Engine
- Developing a Workflow

---

## API

Reference documentation for public interfaces.

This section will expand as the Engine matures.

---

# Documentation Philosophy

TORANA separates documentation into four distinct layers.

## Architecture

Explains the system design.

Focus:

- responsibilities
- relationships
- design principles

---

## Specifications

Defines implementation contracts.

Focus:

- required interfaces
- public APIs
- implementation rules

---

## ADRs

Explain architectural decisions.

Focus:

- context
- alternatives
- consequences

---

## Tutorials & Guides

Teach users and contributors how to work with the framework.

---

# Development Workflow

Every feature follows the same lifecycle.

```text
Design
    ↓
Implement
    ↓
Test
    ↓
Update Documentation
    ↓
Commit
    ↓
Push
```

Documentation should always reflect the current implementation.

---

# Current Status

Current implementation includes:

- Plugin architecture
- Plugin Registry
- Task model
- Workflow (DAG)

The following components are planned:

- Job
- Engine
- Scheduler
- Task Executor
- Dataset Manager
- Plugin Loader

---

# Contributing

When contributing to TORANA:

- Keep documentation synchronized with code.
- Follow the documented architecture.
- Write tests for new functionality.
- Preserve public APIs whenever possible.
- Prefer modular and extensible designs.

---

# Notes

The documentation is intended to evolve alongside the Engine.

Architecture documents describe *why* the system is designed as it is.

Specification documents describe *how* components must behave.

Together they form the engineering reference for TORANA.
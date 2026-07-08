# TORANA Engine

**Version:** 0.1  
**Status:** Active  
**Last Updated:** July 2026

---

# Vision

The Engine is the orchestration layer of TORANA.

Its responsibility is to coordinate analysis workflows while remaining independent of analysis algorithms, datasets, and visualization.

The Engine is designed to answer one question:

> **How should this analysis be executed?**

It never answers:

> **How is this analysis performed?**

That responsibility belongs to Plugins.

---

# Purpose

The Engine coordinates the complete lifecycle of a Job.

It acts as the central controller that connects:

- Plugins
- Jobs
- Workflows
- Tasks
- Services
- Outputs

The Engine itself performs no GIS analysis.

---

# Responsibilities

The Engine is responsible for:

- Receiving analysis requests
- Creating Jobs
- Loading Plugins
- Validating configuration
- Building execution Workflows
- Scheduling Tasks
- Monitoring execution
- Managing execution state
- Producing Outputs

The Engine never implements analysis algorithms.

---

# Core Principles

## Orchestration over Implementation

The Engine coordinates execution.

Plugins perform analysis.

---

## Stateless Execution

Each Job is executed independently.

The Engine should avoid storing analysis-specific state between Jobs.

---

## Plugin Driven

Every analysis is defined through a Plugin.

The Engine only understands the Plugin contract.

It never depends on specific analyses such as:

- Urban Heat Island
- Flood Risk
- Walkability
- Solar Analysis

---

## Workflow Driven

The Engine executes Workflows.

Execution order is determined entirely by the Workflow.

The Engine never hardcodes execution sequences.

---

# Engine Lifecycle

The Engine progresses through several states during its lifetime.

```text
STOPPED
    │
    ▼
INITIALIZING
    │
    ▼
READY
    │
    ▼
RUNNING
    │
    ▼
SHUTDOWN
```

---

# Job Lifecycle

Every analysis request creates a new Job.

```text
User Request
      │
      ▼
Create Job
      │
      ▼
Load Plugin
      │
      ▼
Create Workflow
      │
      ▼
Execute Tasks
      │
      ▼
Generate Outputs
      │
      ▼
Complete Job
```

---

# Execution Pipeline

A typical execution follows these stages.

1. User requests an analysis.
2. Engine creates a Job.
3. Registry provides the requested Plugin.
4. Plugin defines the Workflow.
5. Workflow identifies executable Tasks.
6. Engine schedules Tasks.
7. Services perform computation.
8. Outputs are generated.
9. Job is completed.

---

# Interaction with Other Components

## Plugin

Defines the analysis.

---

## Registry

Provides Plugin discovery.

---

## Workflow

Defines execution order.

---

## Task

Represents executable work.

---

## Services

Provide reusable infrastructure such as:

- Logging
- Configuration
- Scheduling
- Dataset Management
- Exporting

---

# Public Interface

The Engine will eventually expose operations similar to:

- Create Job
- Submit Job
- Execute Job
- Monitor Job
- Cancel Job
- Retrieve Outputs

These represent conceptual operations rather than implementation details.

---

# Future Extensions

The Engine architecture is designed to support future capabilities including:

- Parallel execution
- Distributed execution
- Cloud execution
- Progress reporting
- Job persistence
- Automatic retries
- Plugin discovery
- Remote execution

---

# Design Principles

The Engine follows these principles.

- Single Responsibility
- Dependency Inversion
- Plugin Architecture
- Loose Coupling
- Testability
- Extensibility

---

# Notes

The Engine is the coordinator of TORANA.

It owns execution but never analysis.

Analysis belongs to Plugins.

Execution order belongs to Workflows.

Infrastructure belongs to Services.
# Execution Manager

**Component:** ExecutionManager

**Milestone:** Engine Core v1.0

**Status:** Stable

---

# Purpose

The ExecutionManager owns the execution lifecycle of a Job.

It coordinates execution by delegating responsibilities to specialized components while remaining independent of GIS analysis.

The ExecutionManager never performs spatial analysis itself.

Instead, it orchestrates execution through:

- Scheduler
- TaskExecutor

---

# Responsibilities

The ExecutionManager is responsible for:

- Managing the execution lifecycle
- Coordinating Scheduler
- Coordinating TaskExecutor
- Managing execution flow

The ExecutionManager is **not** responsible for:

- Plugin discovery
- GIS analysis
- Dataset acquisition
- Visualization

---

# Position in the Architecture

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

The ExecutionManager is the central coordinator of runtime execution.

---

# Execution Lifecycle

Current execution follows these stages.

```text
ExecutionContext

↓

Scheduler

↓

Ready Tasks

↓

TaskExecutor

↓

Task Status Updated

↓

Repeat Until Complete
```

Execution finishes when no executable Tasks remain.

---

# Execution Algorithm

The current implementation follows the algorithm below.

```text
Receive ExecutionContext

↓

Retrieve Workflow

↓

While Workflow has pending Tasks

↓

Ask Scheduler for ready Tasks

↓

Execute every ready Task

↓

Repeat
```

The Scheduler determines **what** can execute.

The TaskExecutor determines **how** a Task executes.

---

# Collaboration

## Scheduler

The Scheduler identifies every executable Task.

It does not modify the Workflow.

It does not execute Tasks.

---

## TaskExecutor

The TaskExecutor executes one Task at a time.

It manages Task lifecycle transitions.

Example:

```text
CREATED

↓

RUNNING

↓

COMPLETED
```

Future versions may also support:

```text
RUNNING

↓

FAILED

↓

RETRY
```

---

## Workflow

The Workflow owns:

- dependency graph
- ready Task discovery
- completed Task queries
- pending Task queries

The ExecutionManager never manipulates graph structures directly.

---

# Dependency Injection

Current constructor:

```python
ExecutionManager(
    scheduler,
    task_executor,
)
```

Both collaborators are injected to improve:

- testing
- extensibility
- future customization

---

# Design Principles

## Delegation

ExecutionManager coordinates.

It never performs specialized work itself.

---

## Separation of Concerns

Scheduling belongs to Scheduler.

Execution belongs to TaskExecutor.

Graph management belongs to Workflow.

---

## Stateless Components

ExecutionManager owns no Workflow data.

Execution state remains inside the ExecutionContext and Task objects.

---

## Extensible

Future execution strategies can be introduced without changing the Engine.

Examples:

- Parallel execution
- Distributed execution
- Retry policies
- Resource-aware scheduling

---

# Current Pipeline

Current implementation executes the following pipeline.

```text
Engine

↓

ExecutionManager

↓

Scheduler

↓

Ready Tasks

↓

TaskExecutor

↓

Completed Tasks

↓

Workflow Updated

↓

Scheduler

↓

...
```

The loop continues until no executable Tasks remain.

---

# Future Pipeline

The execution pipeline will gradually expand.

```text
Engine

↓

ExecutionManager

↓

Retry Policy

↓

Scheduler

↓

Priority Queue

↓

TaskExecutor

↓

Plugin Execution

↓

Resource Manager

↓

Execution Metrics

↓

Results
```

Every new capability will be introduced as a dedicated component rather than expanding the responsibilities of the ExecutionManager.

---

# Current Implementation

Implemented

- Execution lifecycle coordination
- Scheduler integration
- TaskExecutor integration
- Dependency injection

---

# Planned Enhancements

ExecutionManager will eventually support:

Execution

- Retry policies
- Task cancellation
- Pause / Resume
- Execution monitoring

Performance

- Parallel execution
- Multi-threaded execution
- Distributed execution

Observability

- Progress reporting
- Logging
- Metrics
- Event system

---

# Summary

The ExecutionManager is the orchestration layer of TORANA.

It coordinates execution without performing analysis.

By delegating scheduling and task execution to dedicated components, the ExecutionManager remains small, maintainable, and extensible while providing a stable foundation for future execution capabilities.
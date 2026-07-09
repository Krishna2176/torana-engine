# Scheduler

**Component:** Scheduler

**Milestone:** Engine Core v1.0

**Status:** Stable

---

# Purpose

The Scheduler determines which Tasks are ready for execution.

It never executes Tasks.

It never modifies the Workflow.

It never changes Task state.

The Scheduler is a pure decision component.

---

# Responsibilities

The Scheduler is responsible for:

- Querying the Workflow
- Determining executable Tasks
- Reporting pending execution

The Scheduler is NOT responsible for:

- Running Tasks
- Updating Task status
- Managing execution state
- Performing analysis

---

# Position in the Architecture

```text
        ExecutionManager
               │
               ▼
          Scheduler
               │
               ▼
           Workflow
               │
               ▼
             Tasks
```

The Scheduler delegates dependency evaluation to the Workflow.

---

# Public API

```python
class Scheduler:

    def get_ready_tasks(
        workflow: Workflow,
    ) -> list[Task]

    def has_pending_tasks(
        workflow: Workflow,
    ) -> bool
```

The Scheduler contains no mutable state.

---

# Scheduling Philosophy

TORANA schedules execution frontiers rather than individual Tasks.

Instead of asking:

```text
What is the next Task?
```

the Scheduler answers:

```text
Which Tasks can execute now?
```

Example:

```text
        A
      /   \
     B     C
      \   /
        D
```

Execution order:

```text
Ready

[A]
```

↓

```text
A completed

Ready

[B, C]
```

↓

```text
B completed
C completed

Ready

[D]
```

The Scheduler always returns every executable Task.

---

# Design Principles

## Stateless

Stores no execution state.

---

## Pure

Never modifies Tasks.

Never modifies Workflow.

---

## Deterministic

Same Workflow state always produces the same result.

---

## Scalable

Supports future:

- Parallel execution
- Distributed execution
- Remote workers

without changing its API.

---

# Collaboration

The Scheduler collaborates with:

- Workflow
- ExecutionManager

It never communicates directly with Plugins.

---

# Current Implementation

Implemented

- Ready Task discovery
- Pending Task detection

---

# Planned Enhancements

Future Scheduler features:

- Priority scheduling
- Resource-aware scheduling
- Conditional execution
- Retry-aware scheduling

---

# Summary

The Scheduler determines executable Tasks while remaining completely independent of execution.
# Execution Context

**Component:** ExecutionContext

**Milestone:** Engine Core v1.0

**Status:** Stable

---

# Purpose

The ExecutionContext represents the runtime environment of a Job.

Every executing Job owns exactly one ExecutionContext.

---

# Responsibilities

Stores:

- Job
- ExecutionState
- ExecutionResources
- ExecutionServices

The ExecutionContext contains runtime information only.

---

# Composition

```text
ExecutionContext

├── Job
├── ExecutionState
├── ExecutionResources
└── ExecutionServices
```

---

# Runtime Components

## Job

The Job being executed.

---

## ExecutionState

Tracks runtime progress.

Examples:

- Current Task
- Completed Tasks
- Progress

---

## ExecutionResources

Stores runtime resources.

Examples:

- Temporary datasets
- Shared objects
- Intermediate outputs

---

## ExecutionServices

Provides shared infrastructure.

Examples:

- Logger
- Cache
- Dataset Manager
- Exporter

---

# Lifecycle

```text
Engine

↓

ExecutionContext created

↓

ExecutionManager

↓

Scheduler

↓

TaskExecutor

↓

Completed
```

The ExecutionContext exists only during execution.

---

# Design Principles

## Runtime Isolation

Execution state never modifies JobSpecification.

---

## Composition

Runtime behavior is divided into focused components.

---

## Dependency Injection

Services are injected rather than globally accessed.

---

## Extensible

New runtime services can be added without changing Engine.

---

# Current Implementation

Implemented

- Runtime container
- Execution resources
- Execution services
- Execution state

---

# Planned Enhancements

Future additions:

- Metrics
- Cancellation tokens
- Progress events
- Shared runtime cache

---

# Summary

ExecutionContext is the runtime container that allows the Engine and ExecutionManager to coordinate execution without storing runtime state inside the Engine itself.
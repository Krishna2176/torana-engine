# Execution Context

**Version:** 0.2

---

# Purpose

The Execution Context represents the runtime environment of a Job.

Every Job receives exactly one Execution Context.

---

# Responsibilities

Execution Context stores:

- Runtime state
- Runtime resources
- Shared service references

It does not execute Tasks.

---

# Composition

```
ExecutionContext

├── Job
├── ExecutionState
├── ExecutionResources
└── ExecutionServices
```

---

# ExecutionState

Tracks execution progress.

Examples:

- Current Task
- Completed Tasks
- Failed Tasks
- Progress

---

# ExecutionResources

Stores runtime data.

Examples:

- Datasets
- Temporary files
- Shared objects
- Outputs

---

# ExecutionServices

Contains injected services.

Examples:

- Logger
- Cache
- Dataset Manager
- Exporter

---

# Lifecycle

```
Created

↓

Initialized

↓

Used by Engine

↓

Destroyed
```

---

# Design Principles

- Runtime only
- One context per Job
- Independent of Plugins
- Service injection

---

# Current Status

Implemented.

Future versions will expand the Context with Scheduler state and runtime metadata.
# Execution Context

**Version:** 0.1  
**Status:** Active  
**Last Updated:** July 2026

---

# Vision

The Execution Context represents the runtime environment of a Job.

It provides the Engine with a single object containing all runtime state, resources, and service references required during execution.

The Execution Context exists only while a Job is executing.

---

# Purpose

The Execution Context separates runtime concerns from the Job definition.

A Job represents **what** should be executed.

The Execution Context represents **how** that execution is managed.

---

# Responsibilities

The Execution Context is responsible for:

- Providing runtime state
- Providing runtime resources
- Providing shared service references
- Acting as the communication layer between Engine, Scheduler and Tasks

It is not responsible for:

- Executing Tasks
- Scheduling Workflows
- Performing GIS analysis
- Producing visualizations

---

# Architecture

```
                ExecutionContext
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
ExecutionState   ExecutionResources   ExecutionServices
```

---

# Execution State

Tracks the current execution.

Examples include:

- Current Task
- Completed Tasks
- Failed Tasks
- Progress

---

# Execution Resources

Stores temporary runtime resources.

Examples include:

- Downloaded datasets
- Temporary files
- Shared objects
- Intermediate outputs

---

# Execution Services

Provides references to shared infrastructure.

Examples include:

- Logger
- Cache
- Dataset Manager
- Exporter

The Execution Context does not own these services.

It only stores references supplied by the Engine.

---

# Lifecycle

```
Create
    │
    ▼
Initialize
    │
    ▼
Execution
    │
    ▼
Cleanup
    │
    ▼
Destroy
```

---

# Design Principles

- Composition over inheritance
- Separation of responsibilities
- Runtime only
- Engine managed
- Independent of specific service implementations

---

# Notes

A new Execution Context is created for every Job.

Once the Job completes, the Execution Context may be destroyed or archived depending on the execution strategy.
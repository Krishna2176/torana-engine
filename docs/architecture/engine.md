# Engine

**Version:** 0.2

---

# Purpose

The Engine is the central coordinator of TORANA.

It does not perform analysis.

Instead, it validates Jobs, prepares runtime execution, and delegates work to specialized components.

---

# Responsibilities

The Engine is responsible for:

- Receiving Jobs
- Validating Plugins
- Creating Execution Contexts
- Coordinating execution

The Engine is NOT responsible for:

- GIS analysis
- Dataset processing
- Scheduling Tasks
- Executing Tasks

---

# Architecture

```
Job
 │
 ▼
Engine
 │
 ├── Plugin Registry
 ├── Execution Context
 └── Scheduler (future)
```

---

# Current Execution

Current implementation performs:

1. Validate Plugin
2. Create Execution Context
3. Mark Job READY

Future versions will continue by invoking the Scheduler.

---

# Design Principles

- Thin orchestration layer
- No GIS logic
- No Plugin knowledge
- Runtime coordination only

---

# Current Status

Implemented:

- Job validation
- Plugin lookup
- ExecutionContext creation

Planned:

- Scheduler
- Task Executor
- Runtime monitoring
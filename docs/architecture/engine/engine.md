# Engine

**Component:** Engine

**Milestone:** Engine Core v1.0

**Status:** Stable

---

# Purpose

The Engine is the public entry point of TORANA.

Its responsibility is to receive Jobs, validate them, prepare the execution environment, and delegate execution to the Execution Manager.

The Engine intentionally contains very little business logic.

---

# Responsibilities

The Engine is responsible for:

- Receiving Jobs
- Validating Plugins
- Creating ExecutionContext objects
- Preparing Job runtime state
- Delegating execution

The Engine does **not**:

- Execute Tasks
- Schedule Tasks
- Perform GIS analysis
- Manage datasets
- Execute Plugins directly

---

# Position in the Architecture

```text
               User
                 │
                 ▼
                Job
                 │
                 ▼
              Engine
                 │
                 ▼
        ExecutionManager
```

The Engine sits at the boundary between the public API and the execution pipeline.

---

# Execution Flow

Current execution follows these steps.

```text
Job

↓

Engine.submit()

↓

Validate Plugin

↓

Create ExecutionContext

↓

ExecutionManager.execute()

↓

Return ExecutionContext
```

---

# Engine Lifecycle

## 1. Receive Job

The Engine accepts a fully constructed Job.

The Job contains:

- JobSpecification
- JobRuntime
- JobResults

---

## 2. Validate Plugin

The Engine checks whether the requested Plugin exists in the Plugin Registry.

If the Plugin cannot be found, execution stops immediately.

---

## 3. Prepare Runtime

The Engine initializes runtime execution.

Current implementation:

- JobStatus becomes READY
- ExecutionContext is created

Future versions may also initialize:

- Resources
- Temporary storage
- Logging
- Metrics

---

## 4. Delegate Execution

Execution is delegated entirely to the ExecutionManager.

The Engine does not control execution loops.

---

# Collaboration

The Engine collaborates with the following components.

## PluginRegistry

Provides Plugin lookup.

The Engine validates that the requested Plugin exists before execution.

---

## ExecutionContext

Represents runtime execution.

Created by the Engine.

Passed to the ExecutionManager.

---

## ExecutionManager

Owns the execution lifecycle.

The Engine delegates execution immediately after creating the ExecutionContext.

---

# Dependency Injection

The Engine receives its collaborators through its constructor.

Current dependencies:

```python
Engine(
    registry,
    execution_manager,
)
```

This allows alternative implementations during testing.

---

# Design Principles

The Engine follows several design principles.

## Thin Orchestrator

The Engine coordinates.

It does not perform work.

---

## Stateless

The Engine stores no Job-specific execution state.

Every Job receives its own ExecutionContext.

---

## Plugin Agnostic

The Engine never knows how Plugins perform analysis.

It only validates their existence.

---

## Delegation

Execution responsibility belongs to the ExecutionManager.

---

# Current Implementation

Implemented:

- Plugin validation
- Job validation
- ExecutionContext creation
- Delegation to ExecutionManager

---

# Planned Enhancements

Future Engine improvements include:

- Job queue support
- Cancellation
- Progress reporting
- Event notifications
- Batch execution

These features should remain orchestration responsibilities and should not introduce GIS-specific logic.

---

# Summary

The Engine is intentionally small.

Its role is to validate, prepare, and delegate.

All execution behavior is implemented by downstream components, allowing the Engine to remain stable even as the execution pipeline evolves.
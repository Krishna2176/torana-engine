# ADR-004 — Plugin Lifecycle

**Status:** Accepted

**Date:** July 2026

**Milestone:** Plugin Framework v1.0

---

# Context

Plugins participate in two distinct activities within the Plugin Framework.

First, Plugins must be discovered, registered, and validated before they become available to the Engine.

Second, a validated Plugin participates in analysis by constructing a Workflow that is executed by the Engine Core.

Treating these activities as a single lifecycle would mix Plugin management with runtime execution, increasing coupling between the Plugin Framework and the Engine Core.

TORANA requires a clear separation between Plugin management and Plugin execution.

---

# Decision

TORANA separates the Plugin Lifecycle into two independent architectural lifecycles.

## Plugin Registration Lifecycle

Responsible for making Plugins available to the Engine.

```text
Discover

↓

Register

↓

Validate

↓

Ready
```

This lifecycle is managed entirely by the Plugin Registry.

---

## Plugin Execution Lifecycle

Responsible for contributing analytical behaviour during Job execution.

```text
Receive Request

↓

Validate Configuration

↓

Declare Dataset Requirements

↓

Construct Workflow

↓

Return Workflow

↓

Execution Complete
```

The Plugin Framework completes its responsibilities once the Workflow has been constructed.

Execution of the Workflow is delegated entirely to the Engine Core.

---

# Rationale

Separating registration from execution provides several architectural benefits.

- Clear separation of responsibilities.
- Independent Plugin management.
- Stable Engine Core.
- Simplified testing.
- Cleaner execution pipeline.
- Future support for dynamic Plugin loading.

The Plugin Registry manages Plugin availability.

The Engine Core manages runtime execution.

---

# Alternatives Considered

## Single Plugin Lifecycle

Registration and execution are treated as one continuous process.

Advantages

- Simpler conceptual model.
- Fewer lifecycle definitions.

Disadvantages

- Blurred architectural responsibilities.
- Tight coupling between registration and execution.
- Difficult future extension.

---

## Separate Registration and Execution Lifecycles (Accepted)

Plugin management and Plugin execution are treated as independent architectural concerns.

Advantages

- Clear subsystem boundaries.
- Improved maintainability.
- Easier testing.
- Greater architectural flexibility.
- Better support for future Plugin Framework capabilities.

Trade-offs

- Two lifecycle models must be documented.
- Slightly more complex architecture.

---

# Consequences

Positive

- Plugin Registry owns Plugin availability.
- Engine Core owns execution.
- Plugin Framework remains independent of runtime.
- Lifecycle responsibilities become easier to understand.
- Future Plugin categories follow the same lifecycle model.

Negative

- Developers must understand two related lifecycles.
- Documentation is slightly more extensive.

These trade-offs are acceptable because they preserve a clean separation between management and execution.

---

# Related Documents

- plugin_lifecycle.md
- plugin_registry.md
- plugin_architecture.md
- plugin_contract.md

---

# Notes

The Plugin Lifecycle describes how Plugins participate in the Plugin Framework.

It does not describe Job execution or Workflow execution.

Execution remains the responsibility of the Engine Core after the Plugin has constructed and returned a Workflow.
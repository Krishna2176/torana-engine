# Plugin Lifecycle

**Component:** Plugin Framework

**Document:** Plugin Lifecycle

**Milestone:** Plugin Framework v1.0

**Status:** In Progress

---

# Purpose

The Plugin Lifecycle defines how Plugins participate in the TORANA Engine from discovery through workflow construction.

The lifecycle distinguishes between the lifecycle of a Plugin itself and the execution lifecycle of the Workflows it constructs.

This separation preserves the architectural boundary between the Plugin Framework and the Engine Core.

---

# Lifecycle Overview

The Plugin Framework defines two complementary lifecycles:

1. Plugin Registration Lifecycle
2. Plugin Execution Lifecycle

The Plugin Registration Lifecycle manages Plugin availability.

The Plugin Execution Lifecycle describes how a Plugin participates in creating executable Workflows.

Execution itself remains the responsibility of the Engine Core.

---

# Plugin Registration Lifecycle

Plugins progress through the following registration states.

```text
Discovered

↓

Registered

↓

Validated

↓

Ready
```

A Plugin reaches the **Ready** state after successful validation and becomes available for execution requests.

---

# Plugin Execution Lifecycle

For each submitted Job, the Plugin participates in the following sequence.

```text
Receive Request

↓

Read Configuration

↓

Validate Input

↓

Declare Dataset Requirements

↓

Construct Workflow

↓

Return Workflow

↓

Engine Core Execution
```

The Plugin completes its responsibilities after returning the Workflow.

The Engine Core assumes responsibility for execution.

---

# Plugin States

Plugins may exist in one of the following states.

## Discovered

The Plugin has been located by the Plugin Registry.

---

## Registered

The Plugin has been registered within the Engine.

---

## Validated

The Plugin satisfies the Plugin Contract and compatibility requirements.

---

## Ready

The Plugin is available to construct Workflows.

---

## Unavailable

The Plugin cannot participate in execution due to validation or compatibility failures.

---

# Lifecycle Responsibilities

## Plugin Framework

Responsible for:

- Plugin discovery
- Registration
- Validation
- Workflow construction

---

## Engine Core

Responsible for:

- Workflow execution
- Runtime management
- Task scheduling
- Task execution
- Result collection

---

# State Transitions

```text
Discovered
      │
      ▼
Registered
      │
      ▼
Validated
      │
      ▼
Ready
      │
      ▼
Construct Workflow
      │
      ▼
Engine Core
```

If validation fails:

```text
Discovered

↓

Registered

↓

Unavailable
```

---

# Architectural Principles

The Plugin Lifecycle follows several principles.

## Separation of Responsibilities

Plugins construct Workflows.

The Engine executes Workflows.

---

## Deterministic Behaviour

Plugins should construct equivalent Workflows for equivalent inputs.

---

## Loose Coupling

Plugins interact with the Engine only through the Plugin Contract.

---

## Independent Lifecycle

Plugin registration is independent of Workflow execution.

---

# Future Evolution

Future Plugin Framework versions may introduce:

- Dynamic Plugin loading
- Plugin unloading
- Hot reloading
- Plugin dependencies
- Remote Plugin repositories

These capabilities should preserve the lifecycle defined in this document.

---

# Summary

The Plugin Lifecycle defines how Plugins become available to the Engine and how they participate in preparing execution.

Plugins remain responsible for describing analysis through Workflows, while the Engine Core remains responsible for executing those Workflows.
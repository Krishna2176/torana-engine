# Plugin Contract

**Component:** Plugin Framework

**Document:** Plugin Contract

**Milestone:** Plugin Framework v1.0

**Status:** In Progress

---

# Purpose

The Plugin Contract defines the architectural requirements that every Plugin must satisfy in order to integrate with the TORANA Engine.

Rather than prescribing implementation details, the contract defines the capabilities that every Plugin must expose to the Engine Core.

The contract ensures that all Plugins behave consistently while remaining independent of any specific analytical domain.

---

# Contract Overview

Every Plugin participates in the Engine through three architectural contracts.

```text
                    Plugin Contract
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Identity Contract   Execution Contract   Output Contract
```

Together these contracts define:

- who the Plugin is,
- how it participates in execution,
- what outputs it produces.

---

# Identity Contract

The Identity Contract uniquely identifies a Plugin.

Every Plugin defines:

- Name
- Version
- Description
- Category
- Tags
- Author
- License
- Engine Compatibility

The Identity Contract contains metadata only.

It never contains execution logic.

---

# Execution Contract

The Execution Contract defines how a Plugin participates in the Engine execution pipeline.

Every Plugin defines:

## Configuration Schema

Describes the configuration accepted by the Plugin.

---

## Input Validation

Validates user input before execution begins.

---

## Dataset Requirements

Declares the datasets required to perform the analysis.

The Plugin declares requirements rather than loading datasets directly.

---

## Workflow Builder

Constructs a Workflow describing the analysis.

The Workflow is executed by the Engine Core.

The Plugin never executes the Workflow itself.

---

# Output Contract

The Output Contract defines the artifacts produced by a Plugin.

Typical outputs include:

- Raster layers
- Vector layers
- Statistics
- Reports
- Metadata

The Plugin specifies outputs but does not determine storage or visualization.

---

# Plugin Responsibilities

Every Plugin is responsible for:

- Providing metadata
- Defining configuration
- Validating inputs
- Declaring dataset requirements
- Constructing Workflows
- Defining outputs

Plugins are **not** responsible for:

- Executing Workflows
- Scheduling Tasks
- Managing runtime state
- Performing visualization
- Managing storage
- Coordinating execution

---

# Engine Responsibilities

The Engine Core is responsible for:

- Discovering Plugins
- Validating compatibility
- Executing Workflows
- Managing runtime state
- Scheduling Tasks
- Collecting execution results

The Engine never performs domain-specific analysis.

---

# Deterministic Behaviour

Plugins should produce deterministic results.

Given:

- identical inputs,
- identical configuration,
- identical datasets,

the Plugin should construct an equivalent Workflow and produce equivalent outputs.

Plugins should not depend on:

- hidden global state,
- previous executions,
- random behaviour,
- external mutable state unless explicitly declared.

This principle improves reproducibility, testing, and scientific validation.

---

# Contract Stability

The Plugin Contract defines the stable interface between Plugins and the Engine Core.

Future Plugin Framework versions may extend the contract but should maintain backward compatibility whenever possible.

Changes that break the Plugin Contract require a new Plugin Framework version.

---

# Summary

The Plugin Contract establishes a consistent architectural interface for every Plugin in TORANA Engine.

By separating identity, execution, and output responsibilities, the contract allows new capabilities to be introduced without modifying the Engine Core while maintaining a stable, extensible architecture.
# Plugin Development Guide

**Component:** Plugin Framework

**Document:** Plugin Development Guide

**Milestone:** Plugin Framework v1.0

**Status:** In Progress

---

# Purpose

This guide defines the recommended process for developing Plugins for the TORANA Engine.

It translates the architectural principles established by the Plugin Framework into practical development guidelines.

Every Plugin should follow the same structure, responsibilities, and development workflow to ensure consistency, maintainability, and interoperability across the TORANA ecosystem.

---

# Development Philosophy

Plugins extend the capabilities of the TORANA Engine without modifying the Engine Core.

A Plugin contributes domain knowledge by describing an analysis.

The Engine Core remains responsible for execution.

Plugins should be:

- Modular
- Deterministic
- Testable
- Reusable
- Independent
- Well documented

---

# Plugin Anatomy

Every Plugin consists of several logical components.

```text
Plugin

├── Plugin Manifest
├── Configuration
├── Input Validation
├── Dataset Requirements
├── Workflow Builder
├── Tasks
├── Output Specification
├── Tests
└── Documentation
```

Each component has a single responsibility.

---

# Plugin Development Workflow

Plugins should be developed using the following workflow.

```text
Analysis Idea

↓

Plugin Manifest

↓

Configuration

↓

Validation

↓

Dataset Requirements

↓

Workflow Builder

↓

Output Specification

↓

Tasks

↓

Tests

↓

Documentation
```

Following this sequence ensures that architecture and design are established before implementation.

---

# Recommended Directory Structure

The following structure is recommended for all Plugins.

```text
plugins/

    flood_risk/

        __init__.py

        manifest.py

        config.py

        validator.py

        workflow.py

        tasks/

        outputs/

        tests/

        README.md
```

Individual Plugins may introduce additional modules when justified, but the overall structure should remain consistent.

---

# Building a Plugin

Every Plugin should provide the following components.

## Plugin Manifest

Describes the Plugin.

Includes:

- Identity
- Classification
- Compatibility
- Capabilities
- Administration

---

## Configuration

Defines the runtime configuration accepted by the Plugin.

Configuration should remain independent of implementation.

---

## Validation

Validates configuration and user input before execution.

Validation should fail early whenever possible.

---

## Dataset Requirements

Declare the datasets required to perform the analysis.

Plugins should never locate or download datasets directly.

Dataset acquisition belongs to the Dataset Framework.

---

## Workflow Builder

Constructs a Workflow representing the analysis.

The Plugin never executes the Workflow.

Execution remains the responsibility of the Engine Core.

---

## Tasks

Tasks implement the individual computational steps required by the analysis.

Each Task should perform one well-defined operation.

---

## Output Specification

Defines the artifacts produced by the Plugin.

Examples include:

- Raster layers
- Vector layers
- Statistics
- Reports
- Metadata

Plugins specify outputs but do not determine storage or visualization.

---

# Development Principles

Plugins should follow these principles.

## Single Responsibility

Each Plugin should implement one analytical capability.

---

## Deterministic Behaviour

Given the same:

- Inputs
- Configuration
- Datasets

a Plugin should construct an equivalent Workflow and produce equivalent outputs.

---

## Engine Independence

Plugins should never control execution.

The Engine Core owns orchestration.

---

## Dataset Independence

Plugins declare dataset requirements.

Dataset management belongs to the Dataset Framework.

---

## Workflow Driven

Plugins construct Workflows.

They never execute Tasks directly.

---

## Documentation First

Every Plugin should include:

- README
- Tests
- Documentation

Documentation should evolve alongside implementation.

---

# Best Practices

Recommended practices include:

- Keep Plugins focused on a single analytical domain.
- Prefer composition over inheritance.
- Reuse shared algorithms from the Analysis Framework.
- Keep Tasks small and independent.
- Validate inputs before constructing Workflows.
- Declare all external requirements through the Plugin Manifest.
- Maintain clear separation between analysis and visualization.

---

# Common Mistakes

Avoid the following.

## Performing Execution

Plugins should never execute Tasks or Workflows.

Execution belongs to the Engine Core.

---

## Managing Datasets

Plugins should not download, discover, or manage datasets.

Only declare dataset requirements.

---

## Managing Runtime State

Plugins should not manipulate ExecutionContext or runtime state.

---

## Producing Visualizations

Visualization belongs to the Visualization Framework.

Plugins define outputs but do not render them.

---

## Combining Multiple Analyses

A Plugin should remain focused on a single analytical capability.

Large analyses should be composed from reusable Tasks rather than unrelated functionality.

---

# Reference Plugin

The Flood Risk Plugin serves as the reference implementation for all Analysis Plugins.

Future Plugins should follow the same architecture, structure, and development practices established by the reference implementation.

---

# Plugin Development Checklist

Before considering a Plugin complete, verify that the following have been completed.

```text
□ Plugin Manifest completed

□ Category defined

□ Domain defined

□ Configuration documented

□ Validation implemented

□ Dataset Requirements declared

□ Workflow Builder implemented

□ Tasks implemented

□ Output Specification completed

□ Tests written

□ Documentation completed
```

---

# Summary

A well-designed Plugin extends the TORANA Engine by describing an analysis rather than performing execution.

The Engine Core remains responsible for orchestration, while the Plugin contributes domain knowledge through its Plugin Manifest, configuration, validation, workflow construction, and output specification.

Following the standards defined in this guide ensures that every Plugin remains modular, maintainable, and fully compatible with the TORANA Plugin Framework.
# Plugin Architecture

**Version:** 0.1  
**Status:** Active  
**Last Updated:** July 2026

---

# Vision

Plugins are the extension mechanism of TORANA.

Every analysis supported by the Engine is implemented as a Plugin.

This architecture allows the Engine to remain independent of domain-specific geospatial algorithms while enabling new analyses to be added without modifying the Engine itself.

---

# Purpose

A Plugin defines **what** an analysis is.

It describes:

- required datasets
- configuration schema
- workflow
- outputs
- metadata

A Plugin does **not** define **how** execution is managed.

Execution is the responsibility of the Engine.

---

# Responsibilities

A Plugin is responsible for:

- Describing an analysis
- Declaring required datasets
- Providing configuration requirements
- Defining the analysis workflow
- Declaring expected outputs
- Validating its own configuration

A Plugin is **not** responsible for:

- Scheduling execution
- Managing Jobs
- Executing Tasks
- Producing visualizations
- Managing datasets

---

# Plugin Lifecycle

Every Plugin follows the same lifecycle.

```text
Register
    │
    ▼
Discover
    │
    ▼
Validate
    │
    ▼
Create Workflow
    │
    ▼
Execute (Engine)
    │
    ▼
Generate Outputs
```

The Engine controls the lifecycle.

---

# Plugin Architecture

```text
               Plugin
                  │
     ┌────────────┼────────────┐
     │            │            │
 Metadata   Configuration   Workflow
     │            │            │
     └────────────┼────────────┘
                  │
             Expected Outputs
```

The Plugin acts as a declaration of an analysis rather than an execution engine.

---

# Plugin Discovery

Plugins are discovered through the Plugin Registry.

The Engine never references specific plugins directly.

Instead, it requests plugins from the Registry using their unique identifiers.

---

# Plugin Registration

Plugins must be registered before they can be executed.

The Registry is responsible for:

- registering plugins
- preventing duplicate registrations
- discovering plugins
- providing plugin lookup

---

# Plugin Validation

Before execution begins, every Plugin validates:

- configuration
- required parameters
- dataset requirements

Validation occurs before a Job enters execution.

---

# Plugin Metadata

Every Plugin exposes descriptive metadata.

Typical metadata includes:

- identifier
- name
- version
- description
- author (future)
- license (future)

Metadata enables discovery and documentation without executing the Plugin.

---

# Relationships

```text
Engine
    │
    ▼
Registry
    │
    ▼
Plugin
    │
    ▼
Workflow
    │
    ▼
Tasks
```

---

# Design Principles

Plugins follow several architectural principles.

- Single Responsibility
- Open for extension
- Closed for modification
- Independent of execution
- Independent of visualization
- Declarative rather than procedural

---

# Future Extensions

The Plugin architecture is designed to support future capabilities such as:

- Automatic discovery
- Plugin packages
- Version compatibility
- Dependency resolution
- Marketplace distribution
- Third-party plugins

---

# Notes

Plugins define analyses.

The Engine executes analyses.

The Registry discovers analyses.

Together, these three components form the extension architecture of TORANA.
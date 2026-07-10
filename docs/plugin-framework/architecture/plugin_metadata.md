# Plugin Metadata

**Component:** Plugin Framework

**Document:** Plugin Metadata

**Milestone:** Plugin Framework v1.0

**Status:** In Progress

---

# Purpose

The Plugin Metadata defines the information required to describe, classify, validate, and manage Plugins within the TORANA Engine.

Collectively, the Plugin Metadata forms the **Plugin Manifest**, which provides a complete, machine-readable description of a Plugin.

The Plugin Manifest enables the Engine Core, Plugin Registry, command-line tools, graphical interfaces, documentation generators, and future plugin repositories to interact with Plugins without requiring plugin-specific logic.

---

# Metadata Overview

Every Plugin provides a Plugin Manifest composed of five metadata groups.

```text
                     Plugin Manifest
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
     Identity        Classification     Compatibility
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
          Capability          Administration
```

Each group has a distinct responsibility.

---

# Identity Metadata

Identity Metadata uniquely identifies a Plugin.

Every Plugin defines:

- Name
- Version
- Description

Identity Metadata answers:

> Who are you?

Identity Metadata never changes during execution.

---

# Classification Metadata

Classification Metadata describes the type of Plugin.

Every Plugin defines:

- Category
- Domain
- Tags

Category identifies the architectural role of the Plugin.

Examples:

- Analysis
- Dataset Provider
- Visualization
- Report
- Export

Domain identifies the problem domain addressed by the Plugin.

Examples:

- Hydrology
- Transportation
- Urban Climate
- Environmental Analysis
- Remote Sensing

Tags provide additional searchable keywords.

Classification Metadata answers:

> What kind of Plugin are you?

---

# Compatibility Metadata

Compatibility Metadata describes where a Plugin can execute.

Every Plugin defines:

- Minimum Engine Version
- Plugin Framework Version
- Dependencies

Optional metadata may include:

- Maximum Engine Version
- Python Version

Compatibility Metadata answers:

> Can you run?

---

# Capability Metadata

Capability Metadata describes the analytical capabilities provided by the Plugin.

Every Plugin defines:

- Capabilities
- Dataset Requirements
- Supported Output Types

Capabilities describe what analyses the Plugin performs.

Examples:

Flood Risk Plugin

- Flood Depth
- Flood Velocity
- Flood Hazard
- Building Exposure

Walkability Plugin

- Accessibility
- Connectivity
- Service Area Analysis

Capability Metadata answers:

> What can you do?

Capability Metadata does not describe runtime configuration.

---

# Administrative Metadata

Administrative Metadata identifies ownership and maintenance information.

Typical fields include:

- Author
- Maintainer
- License
- Repository
- Documentation

Administrative Metadata answers:

> Who maintains you?

---

# Metadata Principles

The Plugin Manifest follows several architectural principles.

## Machine Readable

Metadata should be structured so that it can be consumed by software without manual interpretation.

---

## Declarative

Metadata describes a Plugin.

It never performs work.

---

## Immutable

Metadata remains constant throughout Plugin execution.

Runtime configuration belongs to the execution request rather than the Plugin Manifest.

---

## Framework Independent

Metadata describes architectural concepts rather than implementation details.

The Plugin Manifest should remain valid regardless of programming language or execution environment.

---

# Metadata Responsibilities

The Plugin Manifest supports multiple components of the TORANA ecosystem.

Examples include:

- Plugin Registry
- Engine Core
- Command Line Interface
- Desktop Application
- Documentation Generator
- Future Plugin Marketplace

Each component should obtain Plugin information exclusively through the Plugin Manifest.

---

# Current Scope

Plugin Framework v1.0 requires every Plugin to provide, at minimum:

- Name
- Version
- Category
- Domain
- Minimum Engine Version

Additional metadata is strongly encouraged to improve discoverability and interoperability.

---

# Future Evolution

Future versions of the Plugin Manifest may introduce support for:

- Plugin Dependencies
- Capability Discovery
- Plugin Marketplace Metadata
- Digital Signatures
- Plugin Certification
- Security Metadata

These additions should extend the existing metadata groups while preserving backward compatibility.

---

# Summary

The Plugin Metadata defines a structured, machine-readable description of every Plugin in TORANA Engine.

Together, the metadata groups form the Plugin Manifest, providing a consistent and extensible foundation for Plugin discovery, validation, classification, and ecosystem integration while remaining independent of implementation details.
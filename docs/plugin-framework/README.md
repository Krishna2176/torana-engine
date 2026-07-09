# Plugin Framework

## Overview

The Plugin Framework is the extensibility layer of the TORANA Engine. It provides the architecture, contracts, lifecycle, and development standards required to build analysis plugins that integrate seamlessly with the Engine Core.

Rather than embedding analysis logic directly into the Engine, TORANA delegates domain-specific functionality to plugins. This design allows new analytical capabilities to be added without modifying the Engine itself.

The Plugin Framework defines **how plugins are built**, while individual Analysis Plugins define **what analyses are performed**.

---

# Relationship with Engine Core

The TORANA Engine is composed of two primary architectural layers:

* **Engine Core** — Responsible for orchestration, workflow execution, scheduling, runtime management, logging, and system coordination.
* **Plugin Framework** — Responsible for defining the contracts, lifecycle, discovery mechanism, and standards that all plugins must follow.

Analysis logic is intentionally excluded from the Engine Core.

Each analysis, such as Flood Risk, Walkability, Urban Heat Island, Solar Potential, Noise Analysis, or Shadow Analysis, is implemented as an independent Analysis Plugin.

---

# Core Principle

> Analysis Plugins define **what** should be analyzed.
> The Engine Core defines **how** that analysis is executed.

This separation ensures that the Engine remains independent of any specific analytical domain while allowing plugins to evolve independently.

---

# Plugin Categories

Version 1.0 introduces the concept of **Analysis Plugins**.

Examples include:

* Flood Risk
* Walkability
* Urban Heat Island (UHI)
* Solar Potential
* Noise Analysis
* Shadow Analysis

The architecture is intentionally designed so additional plugin categories can be introduced in future releases, such as:

* Dataset Provider Plugins
* Visualization Plugins
* Report Generator Plugins
* Export Plugins

---

# Plugin Framework Goals

The Plugin Framework is designed around the following goals:

* Extensibility
* Modularity
* Consistency
* Isolation
* Discoverability
* Independent Versioning
* Testability
* Long-term Maintainability

---

# Documentation Structure

| Document                          | Purpose                                                         |
| --------------------------------- | --------------------------------------------------------------- |
| `plugin_architecture.md`          | Overall architecture and design principles                      |
| `plugin_contract.md`              | Required plugin interface and responsibilities                  |
| `plugin_lifecycle.md`             | Plugin execution lifecycle                                      |
| `plugin_metadata.md`              | Metadata model and compatibility rules                          |
| `plugin_registry.md`              | Plugin discovery and registration architecture                  |
| `plugin_development_guide.md`     | Guide for developing new plugins                                |
| `adr/ADR-001-plugin-framework.md` | Architectural decision record for adopting the Plugin Framework |

---
## Documentation

The Plugin Framework documentation is organized into the following documents:

* [Plugin Architecture](plugin_architecture.md) — High-level architecture, design principles, and system overview.
* [Plugin Contract](plugin_contract.md) — Defines the contract every Analysis Plugin must implement.
* [Plugin Lifecycle](plugin_lifecycle.md) — Describes how plugins interact with the Engine Core during execution.
* [Plugin Metadata](plugin_metadata.md) — Specifies the metadata model and compatibility requirements.
* [Plugin Registry](plugin_registry.md) — Explains plugin discovery, registration, and lookup.
* [Plugin Development Guide](plugin_development_guide.md) — Standards and best practices for developing Analysis Plugins.
* [ADR-001 – Plugin Framework](adr/ADR-001-plugin-framework.md) — Records the architectural decision to adopt the Plugin Framework.


# Scope of Version 1.0

Plugin Framework v1.0 establishes:

* A standard plugin architecture
* A common plugin contract
* Plugin metadata definitions
* Plugin discovery through the Plugin Registry
* A standardized execution lifecycle
* A reference implementation using the Flood Risk Analysis Plugin

Future versions will extend the framework with additional plugin types, automated plugin discovery, dataset providers, visualization providers, and plugin dependency management while maintaining compatibility with the core architecture.

---

# Design Philosophy

The Plugin Framework follows the same engineering principles as the Engine Core:

* Design before implementation.
* Define stable contracts before writing code.
* Keep components loosely coupled.
* Prefer composition over tight integration.
* Maintain clear separation of responsibilities.
* Ensure every plugin is independently testable and versioned.

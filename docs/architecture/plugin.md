# TORANA Engine - Plugin Specification

## Overview

Plugins are the analytical building blocks of the TORANA Engine.

Each plugin represents a single geospatial analysis that can be executed by the Engine.

Plugins do not control execution. Instead, they describe an analysis through metadata, configuration, dataset requirements, workflow definitions, and references to reusable processing components.

The Engine interprets the plugin specification and executes the analysis accordingly.

---

# Purpose

The purpose of a plugin is to describe:

* What analysis should be performed.
* What datasets are required.
* Which parameters are configurable.
* Which workflow should be executed.
* Which processing components should be used.
* Which outputs should be generated.

A plugin should never be responsible for scheduling, logging, caching, or execution management.

Those responsibilities belong exclusively to the Engine.

---

# Design Principles

Plugins should be:

* Self-contained
* Declarative
* Reusable
* Versioned
* Extensible
* Independent of the Engine implementation

Every plugin should follow the same structure regardless of the analysis it performs.

---

# Plugin Structure

A plugin consists of the following sections:

```text
Plugin

├── Metadata
├── Capabilities
├── Configuration Schema
├── Dataset Requirements
├── Validation Rules
├── Workflow Definition
├── Processing Components
├── Output Definitions
├── Visualization Definitions
├── Export Definitions
└── Documentation
```

---

# Metadata

Metadata identifies the plugin.

Typical metadata includes:

* Plugin ID
* Plugin Name
* Version
* Description
* Author
* License
* Tags
* Category

Example

```yaml
id: uhi

name: Urban Heat Island

version: 1.0.0

category: Climate

description: Calculates Urban Heat Island intensity using satellite imagery.
```

---

# Plugin Capabilities

Capabilities describe what the plugin can perform.

Capabilities are used for:

* Plugin discovery
* Searching
* Filtering
* Future workflow composition
* Compatibility checks

Example

```yaml
capabilities:

- raster_analysis

- remote_sensing

- thermal_analysis

- climate
```

Another plugin may expose:

```yaml
capabilities:

- network_analysis

- accessibility

- graph_analysis
```

Capabilities describe functionality rather than implementation.

---

# Configuration Schema

Each plugin defines its configurable parameters.

Examples include:

* Spatial resolution
* Time period
* Cloud cover threshold
* Buffer distance
* Classification method
* Output resolution

The configuration schema specifies:

* Parameter name
* Data type
* Default value
* Allowed values
* Validation rules
* Description

Example

```yaml
resolution:
    type: integer
    default: 10

year:
    type: integer
    default: 2024

cloud_cover:
    type: integer
    default: 20
```

---

# Dataset Requirements

Plugins explicitly declare every dataset required for execution.

Datasets are classified as:

## Required

Execution cannot continue without these datasets.

Examples:

* Study boundary
* Sentinel imagery
* DEM

## Optional

Execution can continue without these datasets.

Examples:

* Weather observations
* Population
* Land use

The Engine is responsible for acquiring datasets.

Plugins only declare requirements.

---

# Validation Rules

Plugins define validation rules before execution begins.

Examples include:

* Study area exists
* Dataset available
* Date range supported
* Cloud cover acceptable
* Resolution supported

Validation failures should generate meaningful error messages.

---

# Workflow Definition

The plugin defines an analysis workflow.

A workflow consists of ordered Tasks connected through dependencies.

Example

```text
Acquire Sentinel Imagery

↓

Cloud Mask

↓

Calculate NDVI

↓

Calculate LST

↓

Normalize

↓

Generate Heat Map

↓

Export
```

The workflow defines **what** must happen.

The Engine determines **how** the workflow is executed.

---

# Processing Components

Plugins reference reusable processing components rather than implementing every algorithm directly.

Examples include:

* Raster Clip
* Raster Reprojection
* NDVI Calculator
* LST Calculator
* Zonal Statistics
* Raster Classification
* Vector Buffer
* Spatial Join

Multiple plugins may reuse the same processing component.

This minimizes code duplication and encourages consistency across analyses.

---

# Task Definitions

Each workflow consists of Tasks.

Every Task should define:

* Task ID
* Description
* Inputs
* Outputs
* Dependencies
* Processing component
* Expected result

Tasks remain independent whenever possible.

---

# Output Definitions

Plugins declare the outputs they generate.

Outputs may include:

* Raster layers
* Vector layers
* Tables
* Statistics
* Reports
* Images
* Interactive maps

The Engine collects all outputs once execution is complete.

---

# Visualization Definitions

Plugins may recommend default visualization settings.

Examples include:

* Colour ramp
* Classification method
* Legend
* Labels
* Opacity
* Default map extent

Visualization recommendations improve consistency while remaining optional.

---

# Export Definitions

Plugins declare supported export formats.

Examples include:

* GeoTIFF
* GeoJSON
* Shapefile
* CSV
* PNG
* PDF
* HTML

The Export Manager generates the requested deliverables.

---

# Documentation

Every plugin should include documentation describing:

* Purpose
* Scientific methodology
* Input requirements
* Configuration parameters
* Generated outputs
* References
* Limitations

Documentation should allow users to understand and reproduce the analysis.

---

# Plugin Lifecycle

Every plugin follows the same lifecycle.

```text
Registered

↓

Discovered

↓

Loaded

↓

Validated

↓

Configured

↓

Workflow Generated

↓

Executed

↓

Completed
```

The Engine manages the lifecycle.

Plugins remain passive throughout execution.

---

# Plugin Responsibilities

Plugins are responsible for:

* Declaring metadata
* Defining configuration
* Declaring datasets
* Defining validation rules
* Defining workflows
* Referencing processing components
* Declaring outputs
* Recommending visualization
* Defining export formats

---

# Plugin Non-Responsibilities

Plugins must never:

* Execute themselves
* Schedule Tasks
* Manage Jobs
* Download datasets
* Handle caching
* Write logs
* Manage retries
* Control execution order

These responsibilities belong to the Engine.

---

# Relationship with Other Concepts

```text
Engine
    │
    ├── Loads Plugin
    │
    ├── Creates Job
    │
    └── Executes Workflow
                    │
                    ▼
                Plugin
                    │
                    ├── Metadata
                    ├── Configuration
                    ├── Dataset Requirements
                    ├── Validation Rules
                    ├── Workflow
                    ├── Processing Components
                    ├── Outputs
                    ├── Visualization
                    └── Export Definitions
```

---

# Future Extensibility

The plugin system is designed to support future capabilities including:

* Plugin versioning
* Plugin dependencies
* Community-developed plugins
* Plugin marketplace
* Composite workflows
* Cloud-based execution
* AI-assisted workflow generation

These capabilities should be achievable without modifying the Engine architecture.

---

# Summary

A TORANA plugin is a declarative specification describing a geospatial analysis.

It defines what is required, how the analysis is structured, which reusable processing components are needed, and which outputs should be produced.

The Engine remains responsible for execution, while plugins remain responsible for analytical knowledge.

This separation allows TORANA to support a growing ecosystem of reusable, maintainable, and extensible geospatial analyses without increasing the complexity of the Engine.

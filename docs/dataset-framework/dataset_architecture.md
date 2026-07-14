# Dataset Framework Architecture

**Component:** Dataset Framework

**Milestone:** Dataset Framework v1.0

**Status:** In Progress

---

# Purpose

The Dataset Framework is the data acquisition and management layer of TORANA Engine.

Its responsibility is to standardize how datasets are described, discovered, validated, acquired, and made available to Analysis Plugins.

Rather than allowing Plugins to directly locate or download datasets, TORANA delegates these responsibilities to the Dataset Framework.

This architecture ensures that data management remains independent from analytical implementation.

---

# Responsibilities

The Dataset Framework is responsible for:

- Defining the Dataset Manifest
- Standardizing Dataset metadata
- Providing Dataset discovery
- Managing Dataset registration
- Validating Dataset compatibility
- Providing Dataset Providers
- Supporting Dataset acquisition
- Managing Dataset availability

The Dataset Framework does **not**:

- Execute analyses
- Execute Workflows
- Manage Jobs
- Produce visualizations
- Implement GIS algorithms

These responsibilities belong to other TORANA frameworks.

---

# Position in the TORANA Architecture

```text
                    TORANA Engine
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
   Plugin Framework                 Dataset Framework
        │                                   │
        ▼                                   ▼
 Analysis Plugins                  Dataset Providers
        │                                   │
        └─────────────────┬─────────────────┘
                          ▼
                    Execution Pipeline
```

The Plugin Framework defines analytical capabilities.

The Dataset Framework supplies the data required to execute those capabilities.

---

# Framework Components

Dataset Framework v1.0 consists of the following architectural components.

## Dataset Manifest

Describes every dataset using standardized metadata.

---

## Dataset Provider

Defines how datasets are discovered and acquired.

---

## Dataset Registry

Provides dataset registration and lookup.

---

## Dataset Discovery

Finds datasets that satisfy Plugin requirements.

---

## Dataset Validation

Ensures datasets are compatible before execution.

---

## Reference Provider

A simple provider implementation used to validate the framework.

---

# Dataset Lifecycle

Datasets participate in the execution pipeline through the following lifecycle.

```text
Register

↓

Discover

↓

Validate

↓

Acquire

↓

Provide

↓

Plugin Execution
```

Plugins request datasets.

The Dataset Framework resolves those requests.

---

# Collaboration

The Dataset Framework collaborates with several TORANA components.

## Plugin Framework

Plugins declare required datasets.

---

## Engine Core

The Engine coordinates execution.

---

## Execution Manager

Executes Workflows after required datasets become available.

---

## Analysis Plugins

Consume validated datasets.

---

# Architectural Principles

The Dataset Framework follows several architectural principles.

## Data Independence

Datasets remain independent of analytical implementations.

---

## Standardized Metadata

Every dataset is described using a consistent manifest.

---

## Provider-Based Acquisition

Datasets are obtained through Dataset Providers.

---

## Separation of Responsibilities

Plugins request datasets.

Dataset Providers acquire datasets.

The Engine coordinates execution.

---

## Extensibility

Support for new data sources should be added by implementing new Dataset Providers rather than modifying the Engine.

---

# Current Scope

Dataset Framework v1.0 introduces support for:

- Dataset Manifest
- Dataset Registry
- Dataset Provider
- Dataset Discovery
- Dataset Validation
- Reference Dataset Provider

---

# Future Evolution

Future versions of the Dataset Framework may support:

- Cloud data providers
- Google Earth Engine providers
- PostGIS providers
- STAC Catalog providers
- Local cache providers
- Remote API providers
- Versioned datasets

The framework is intentionally designed to support these extensions without requiring changes to the Engine Core.

---

# Summary

The Dataset Framework establishes the architectural foundation for data management within TORANA.

It standardizes how datasets are described, discovered, validated, and acquired while preserving the independence of the Engine Core and Plugin Framework.

Future functionality should extend the framework through Dataset Providers rather than by modifying existing Engine components.
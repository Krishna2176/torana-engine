# TORANA Engine - Core Concepts

## Overview

This document defines the core concepts used throughout the TORANA Engine.

These concepts establish a common vocabulary for the architecture, implementation, documentation, and future development of the platform.

Every subsystem within TORANA should use these definitions consistently.

---

# Design Philosophy

TORANA is built around a small number of well-defined concepts.

Each concept has a single responsibility and interacts with other concepts through clearly defined relationships.

By separating responsibilities, the system remains modular, maintainable, and extensible.

---

# Concept Hierarchy

```text
Engine
│
├── Job
│   │
│   ├── Workflow
│   │   │
│   │   ├── Task
│   │   │   │
│   │   │   └── Operation
│   │   │
│   │   └── Task
│   │
│   ├── Outputs
│   ├── Logs
│   └── Metadata
│
├── Plugin Registry
├── Dataset Manager
├── Cache Service
├── Logging Service
└── Configuration Service
```

---

# Engine

## Definition

The Engine is the long-lived execution coordinator of TORANA.

It provides the infrastructure required to execute geospatial analyses but contains no analysis-specific knowledge.

The Engine remains active throughout the application's lifetime.

---

## Purpose

Coordinate execution.

Manage shared services.

Create Jobs.

Load Plugins.

Provide execution infrastructure.

---

## Responsibilities

* Create Jobs
* Load Plugins
* Manage execution services
* Coordinate workflows
* Schedule execution
* Manage configuration
* Provide logging infrastructure
* Provide caching infrastructure

---

## Does Not Own

* Analysis algorithms
* Spatial computations
* Domain knowledge
* Plugin implementations

---

## Lifetime

Application lifetime.

---

# Job

## Definition

A Job represents one execution of the TORANA Engine.

Every time a user starts an analysis, a new Job is created.

The Job owns all execution-specific state.

---

## Purpose

Represent a complete analysis execution.

---

## Responsibilities

* Store execution state
* Store workflow instance
* Track task progress
* Store outputs
* Store logs
* Store execution metadata
* Track execution status

---

## Owns

* Workflow
* Task states
* Outputs
* Metadata
* Execution logs
* Temporary execution state

---

## Created By

Engine

---

## Lifetime

From analysis start until completion or archival.

---

# Plugin

## Definition

A Plugin implements one domain-specific geospatial analysis.

Each plugin defines the knowledge required to perform a specific analysis.

Examples include:

* Urban Heat Island
* Flood Risk
* Walkability
* Solar Potential
* Noise Analysis
* Urban Morphology

---

## Purpose

Describe how a specific analysis should be performed.

---

## Responsibilities

* Declare required datasets
* Define parameters
* Define workflow
* Implement algorithms
* Define outputs
* Define visualization requirements

---

## Does Not Own

* Execution
* Scheduling
* Logging
* Caching

These responsibilities belong to the Engine.

---

## Loaded By

Plugin Manager

---

# Workflow

## Definition

A Workflow is an executable plan generated from a Plugin.

It describes the sequence of Tasks required to complete an analysis.

---

## Purpose

Organize execution into a structured process.

---

## Responsibilities

* Define execution order
* Define dependencies
* Organize Tasks
* Describe expected outputs

---

## Owns

* Tasks
* Dependency graph

---

## Created By

Plugin

---

# Task

## Definition

A Task is the smallest meaningful unit of work executed by the Engine.

Tasks should perform one clearly defined responsibility.

---

## Examples

* Download Sentinel imagery
* Download OpenStreetMap data
* Clip raster
* Cloud masking
* Calculate NDVI
* Calculate LST
* Generate heat map
* Export GeoTIFF

---

## Responsibilities

* Perform one operation
* Produce outputs
* Report progress
* Record execution status

---

## Owns

* Inputs
* Outputs
* Dependencies
* Status
* Execution metadata

---

## Executed By

Engine Scheduler

---

# Operation

## Definition

An Operation is the lowest-level computational action performed within a Task.

Operations are individual function calls or algorithmic steps.

Examples include:

* Read raster
* Reproject layer
* Compute statistics
* Apply raster calculator
* Write GeoTIFF

Multiple Operations may exist within a single Task.

---

## Purpose

Perform atomic computational work.

---

# Dataset

## Definition

A Dataset is any external or generated spatial resource used during analysis.

Datasets may be downloaded, generated, cached, or exported.

---

## Examples

* Satellite imagery
* Building footprints
* Road networks
* Digital Elevation Models
* Weather observations
* Census data
* Land use layers

---

## Dataset Types

* Raster
* Vector
* Point Cloud
* Tabular
* Time Series

---

## Managed By

Dataset Manager

---

# Configuration

## Definition

Configuration defines how a Job should execute.

Configuration contains user-selected parameters and execution settings.

---

## Examples

* Study area
* Analysis type
* Spatial resolution
* Time period
* Dataset source
* Output format

---

## Purpose

Separate execution behavior from source code.

---

## Managed By

Configuration Manager

---

# Execution Service

## Definition

Execution Services are long-lived infrastructure components provided by the Engine.

They support Jobs but do not belong to any specific Job.

---

## Examples

* Plugin Manager
* Dataset Manager
* Scheduler
* Cache Manager
* Logging Service
* Configuration Manager
* Export Manager

---

## Purpose

Provide reusable infrastructure.

---

# Output

## Definition

An Output is any result generated by a completed Job.

Outputs may be intermediate or final.

---

## Examples

* GeoTIFF
* GeoJSON
* CSV
* PNG
* Interactive Map
* PDF Report
* Statistical Summary

---

## Generated By

Plugins

---

## Managed By

Export Manager

---

# Metadata

## Definition

Metadata describes a Job without containing its analytical results.

Metadata enables reproducibility, auditing, and traceability.

---

## Examples

* Job ID
* Plugin Version
* Execution Time
* Creation Date
* User Configuration
* Dataset Versions
* Software Version
* Execution Duration

---

# Execution State

Execution State represents the current progress of a Job or Task.

Typical Job states include:

* Created
* Validating
* Preparing
* Running
* Paused
* Completed
* Failed
* Cancelled

Task states follow a similar lifecycle but are managed independently.

---

# Relationships

```text
Engine
    │
    ├── Creates ───────────────► Job
    │                               │
    │                               ├── Uses ─────────────► Plugin
    │                               │
    │                               ├── Owns ─────────────► Workflow
    │                               │                           │
    │                               │                           ├── Owns ─────► Tasks
    │                               │                           │                   │
    │                               │                           │                   └── Executes Operations
    │                               │
    │                               ├── Uses ─────────────► Configuration
    │                               │
    │                               ├── Produces ─────────► Outputs
    │                               │
    │                               └── Records ──────────► Metadata
    │
    └── Provides Execution Services
```

---

# Ownership Model

Ownership within TORANA follows a strict hierarchy.

* The Engine owns shared infrastructure.
* Jobs own execution state.
* Workflows own Tasks.
* Tasks execute Operations.
* Plugins define analytical knowledge.
* Services provide reusable capabilities.

This ownership model minimizes coupling and keeps responsibilities clearly separated.

---

# Summary

TORANA is built around a small set of fundamental concepts:

* **Engine** orchestrates execution.
* **Job** represents a single analysis execution.
* **Plugin** provides domain-specific knowledge.
* **Workflow** defines the execution plan.
* **Task** performs meaningful units of work.
* **Operation** performs atomic computations.
* **Dataset** provides spatial information.
* **Configuration** controls execution behavior.
* **Execution Services** provide shared infrastructure.
* **Outputs** store analysis results.
* **Metadata** records execution information.

These concepts form the conceptual foundation of the TORANA Engine and should remain stable as the platform evolves.

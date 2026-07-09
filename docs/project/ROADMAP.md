# TORANA Engine Roadmap

The roadmap defines the long-term evolution of TORANA Engine.

Development progresses through stable architectural milestones. Each milestone introduces a reusable framework that becomes a permanent part of the Engine.

Every milestone follows the TORANA Development Workflow:

Architecture → Documentation → Test Design → Implementation → Refactoring → Documentation Synchronization → Validation → Version Control → Project Update

---

# ❄️ Phase 1 — Engine Core v1.0

**Status**

Completed

**Objective**

Build the execution foundation of TORANA Engine.

**Scope**

### Core Domain

- Plugin
- Task
- Workflow
- Job

### Runtime

- ExecutionContext
- ExecutionResources
- ExecutionServices
- ExecutionState

### Execution

- Engine
- Scheduler
- TaskExecutor
- ExecutionManager
- PluginRegistry

### Engineering

- Testing Infrastructure
- Architecture Documentation
- Specifications

---

# 🟡 Phase 2 — Plugin Framework v1.0

**Status**

In Progress

**Objective**

Create the extensibility framework that allows new capabilities to be added without modifying the Engine Core.

**Scope**

### Framework

- Plugin Architecture
- Plugin Contract
- Plugin Lifecycle
- Plugin Metadata
- Plugin Registry
- Plugin SDK

### Engineering

- Plugin Test Infrastructure
- Plugin Documentation
- ADR-001

### Reference Implementation

- Flood Risk Analysis Plugin

---

# ⚪ Phase 3 — Dataset Framework v1.0

**Status**

Planned

**Objective**

Provide a unified framework for dataset acquisition, validation, storage, and access.

**Scope**

### Dataset Management

- Dataset Manager
- Dataset Registry
- Dataset Metadata
- Dataset Validation

### Dataset Providers

- Local Datasets
- Remote Datasets
- Google Earth Engine
- Future Cloud Providers

---

# ⚪ Phase 4 — Analysis Framework v1.0

**Status**

Planned

**Objective**

Provide reusable computational algorithms shared across Analysis Plugins.

**Scope**

### Spatial Analysis

- Raster Processing
- Vector Processing
- Terrain Analysis
- Hydrology
- Network Analysis

### Shared Libraries

- GIS Utilities
- Computational Algorithms

---

# ⚪ Phase 5 — Visualization Framework v1.0

**Status**

Planned

**Objective**

Provide reusable visualization capabilities independent of analysis logic.

**Scope**

### Visualization

- Interactive Maps
- Three.js
- Blender
- Dashboards

### Outputs

- Reports
- Export Pipelines
- Visual Assets

---

# ⚪ Phase 6 — Desktop Framework v1.0

**Status**

Planned

**Objective**

Develop the desktop application for managing TORANA projects and executing analyses.

**Scope**

- Project Management
- Plugin Management
- Dataset Management
- Analysis Execution
- Visualization Interface

---

# ⚪ Phase 7 — Cloud Framework v1.0

**Status**

Planned

**Objective**

Enable distributed execution and cloud-native deployment of TORANA Engine.

**Scope**

### Execution

- Remote Execution
- Distributed Processing
- Job Queue

### Services

- REST API
- Authentication
- Cloud Storage
- Monitoring

---

# 🚀 TORANA Engine v1.0

**Status**

Future

**Objective**

Deliver the first stable production release of TORANA Engine.

This release will integrate all major frameworks into a unified geospatial computation platform capable of automated spatial analysis, visualization, and reporting.

---

# Long-Term Vision

TORANA Engine is being developed as a modular geospatial computation platform.

Rather than continually expanding the Engine Core, future capabilities will be introduced through reusable frameworks and plugins that build upon the stable execution architecture established in Engine Core v1.0.
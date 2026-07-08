# TORANA Engine Architecture

## Vision

TORANA Engine is a modular geospatial computation framework that automatically acquires spatial data, executes configurable geospatial analyses, and generates professional visualizations and exports for urban planning, architecture, environmental studies, and spatial research.

The engine is designed around **analysis-first execution**, where the selected analysis determines the required datasets, processing steps, and outputs.

---

# Core Philosophy

## Analysis is the source of truth.

Visualization is only a representation of analysis results.

```text
Data
    ↓
Processing
    ↓
Analysis
    ↓
Results
    ↓
Visualization
```

Analysis should never depend on visualization.

Visualization should never modify analysis results.

---

# Design Principles

* Analysis-first architecture.
* Everything is modular.
* Every module has a single responsibility.
* Workflows orchestrate analyses without implementing them.
* Datasets are reusable across analyses.
* Analysis results are immutable once produced.
* Visualization is completely independent from analysis.
* Modules communicate only through well-defined interfaces.
* New analyses should be added without modifying the Core Engine.

---

# High-Level Architecture

```text
                User
                  │
                  ▼
             Project
                  │
                  ▼
            Core Engine
                  │
                  ▼
        Workflow Planner
                  │
                  ▼
      Dependency Resolver
                  │
                  ▼
            Data Engine
                  │
                  ▼
        Processing Engine
                  │
                  ▼
         Analysis Engine
                  │
                  ▼
        Result Repository
                  │
                  ▼
     Visualization Engine
                  │
                  ▼
          Export Engine
```

---

# Core Components

## 1. Project

Represents a user's workspace.

Stores:

* Place
* Configuration
* Selected analyses
* Output preferences
* Metadata

A project defines **what** should be produced, not **how**.

---

## 2. Core Engine

The orchestrator of the entire system.

Responsibilities:

* Manage execution
* Coordinate modules
* Handle errors
* Logging
* Plugin discovery
* Task scheduling
* Progress tracking

The Core Engine never performs analysis itself.

---

## 3. Workflow Planner

Converts a user's request into an executable workflow.

Example:

```
User selects

Urban Heat Island
```

Workflow Planner creates:

```
Acquire imagery

↓

Clip boundary

↓

Calculate LST

↓

Generate UHI

↓

Visualize

↓

Export
```

A workflow defines execution order but contains no analytical logic.

---

## 4. Dependency Resolver

Determines everything required before execution.

Dependencies may include:

### Required datasets

* DEM
* Buildings
* Roads
* Population
* Satellite imagery
* Rainfall

### Required analyses

For example:

```
Heat Vulnerability

requires

• Urban Heat Island
• Population Density
• Tree Canopy
```

The resolver builds an execution graph automatically.

---

## 5. Data Engine

Responsible for acquiring and managing datasets.

Responsibilities:

* Download datasets
* Connect to external providers
* Cache datasets
* Validate datasets
* Store metadata
* Manage versions

Examples:

* OpenStreetMap
* Google Earth Engine
* Government portals
* Raster datasets
* Vector datasets

No processing or analysis occurs here.

---

## 6. Processing Engine

Transforms raw datasets into analysis-ready inputs.

Examples:

* Reprojection
* Clipping
* Topology fixing
* Raster alignment
* Cleaning geometries
* Resampling
* Vectorization
* Rasterization

Output:

Standardized datasets ready for analysis.

---

## 7. Analysis Engine

Executes geospatial algorithms.

Examples:

* Urban Heat Island
* Flood Analysis
* Walkability
* Solar Potential
* Visibility
* Accessibility
* Noise Mapping
* Density Analysis
* Morphology Analysis

Each analysis is independent.

Each analysis defines:

* Required datasets
* Optional datasets
* Required analyses
* Processing requirements
* Outputs

---

## 8. Result Repository

Stores analysis outputs.

Results become the authoritative source for downstream modules.

Examples:

* Raster outputs
* Vector layers
* Statistical summaries
* Network graphs
* Derived indicators

Visualization and export consume results from this repository.

---

## 9. Visualization Engine

Transforms analysis results into visual representations.

Examples:

* Maps
* Interactive web maps
* 3D scenes
* Dashboards
* Charts
* Animations

Visualization never modifies analytical results.

---

## 10. Export Engine

Produces deliverables.

Examples:

* GeoTIFF
* GeoPackage
* GeoJSON
* Shapefile
* PNG
* PDF
* HTML
* GLB
* CSV

---

# System Layers

## Layer 1 — Data

Acquire spatial datasets.

Examples:

* DEM
* Roads
* Buildings
* Satellite imagery
* Population
* Rainfall
* Land Cover

---

## Layer 2 — Processing

Prepare datasets for analysis.

Examples:

* Reprojection
* Clipping
* Cleaning
* Raster processing
* CRS conversion

---

## Layer 3 — Analysis

Generate knowledge from processed data.

Examples:

* Flood
* UHI
* Solar
* Accessibility
* Walkability
* Visibility
* Noise

---

## Layer 4 — Results

Store standardized outputs from analyses.

These outputs become the single source of truth for visualization and export.

---

## Layer 5 — Visualization

Communicate analytical findings through maps, 3D scenes, dashboards, and graphics.

---

## Layer 6 — Export

Generate final deliverables.

---

# Analysis-First Execution Model

Execution begins by selecting one or more analyses.

Example:

```
Project

↓

Urban Heat Island

↓

Dependency Resolver

↓

Required Datasets

↓

Acquire Data

↓

Process Data

↓

Run Analysis

↓

Store Results

↓

Visualize

↓

Export
```

Only datasets required for the selected analyses are acquired.

---

# Dependency Model

Each analysis declares its dependencies.

Example:

```
Analysis:
Urban Heat Island

Required Datasets
- Thermal Imagery
- Boundary

Optional Datasets
- Buildings
- Population

Outputs
- Land Surface Temperature
- UHI Classes
```

Example:

```
Analysis:
Flood Analysis

Required Datasets
- DEM
- Rivers
- Rainfall
- Land Cover

Outputs
- Flow Direction
- Flow Accumulation
- Flood Risk
```

This enables automatic workflow generation and simplifies the addition of new analyses.

---

# Extensibility

New analyses should be added as independent modules.

Each module should declare:

* Name
* Description
* Required datasets
* Optional datasets
* Required analyses
* Outputs
* Parameters

The Core Engine discovers and integrates these modules without modification.

---

# Long-Term Vision

TORANA Engine should evolve into a geospatial computation platform where a user can express a high-level objective such as:

> "Generate an Urban Heat Island assessment for Nashik and produce an interactive web map, PDF report, and GeoPackage."

The engine should automatically:

1. Determine required analyses.
2. Resolve dependencies.
3. Acquire required datasets.
4. Process datasets.
5. Execute analyses.
6. Store results.
7. Generate visualizations.
8. Export professional deliverables.

The primary goal is to make new capabilities extensible through modular analyses and workflows while keeping the Core Engine stable and maintainable.

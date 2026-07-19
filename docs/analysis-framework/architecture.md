# Analysis Framework Architecture

```
          Plugin
             │
             ▼
     Base Analysis
             │
             ▼
   Analysis Planner
             │
             ▼
        Workflow
             │
             ▼
          Engine
```

## Responsibilities

### Base Analysis

Describes an analysis.

### Planner

Converts an analysis into a workflow.

### Engine

Executes the workflow.

The planner never executes tasks.

The engine never understands analysis-specific logic.
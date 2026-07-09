# Changelog

All significant architectural milestones are documented here.

---

# Engine Core v1.0

## Added

### Core Models

- Plugin
- Task
- Workflow
- Job

### Runtime

- ExecutionContext
- ExecutionState
- ExecutionResources
- ExecutionServices

### Execution

- Engine
- PluginRegistry
- Scheduler
- ExecutionManager
- TaskExecutor

### Architecture

- Dependency Injection
- Workflow DAG
- Stateless Scheduler
- Engine Composition

### Testing

- Comprehensive pytest suite
- Shared fixtures
- Dependency injection testing

### Documentation

- Architecture documentation
- ADRs
- Specifications

# Engine Core v1.0

**Status:** Frozen

## Completed

### Engine Core

- Engine
- ExecutionManager
- Scheduler
- TaskExecutor
- Runtime
- Workflow
- Job
- Plugin Registry

### Documentation

- Engine Architecture
- Specifications
- Project Documentation
- Engineering Workflow
- Versioning Strategy

### Testing

- Unit Test Infrastructure
- Shared Fixtures

## Notes

Engine Core v1.0 is considered stable.

Future development will extend the Engine through the Plugin Framework rather than expanding the Engine Core.

Only bug fixes, documentation improvements, tests, and non-breaking refactoring are permitted.
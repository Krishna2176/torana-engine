# TORANA Project Documentation

This directory contains the project governance documentation for **TORANA Engine**.

Unlike the architecture documentation, which describes how the software is designed, this directory describes how the project is planned, managed, and developed throughout its lifecycle.

These documents provide the single source of truth for project status, milestones, development workflow, engineering decisions, and release planning.

---

# Purpose

The Project Documentation exists to:

- Track the current state of the project.
- Define the development workflow.
- Record major engineering decisions.
- Organize milestones and roadmap.
- Maintain project governance.
- Reduce dependency on conversation history by making the repository the authoritative source of project state.

All future development should begin by reviewing this directory.

---

# Documentation Structure

## PROJECT_STATUS.md

Provides a snapshot of the current state of the project.

Use this document to quickly understand:

- Current milestone
- Current workflow stage
- Completed milestones
- Active work
- Repository health

---

## CURRENT_PHASE.md

Describes the milestone currently under development.

Includes:

- Current objective
- Current deliverable
- Immediate tasks
- Blockers
- Next milestone review

---

## ROADMAP.md

Defines the long-term development roadmap for TORANA Engine.

---

## MILESTONES.md

Describes each major engineering milestone.

Each milestone includes:

- Objective
- Deliverables
- Status

---

## DECISIONS.md

Records important engineering and architectural decisions.

Detailed reasoning is documented separately in the Architecture Decision Records (ADRs).

---

## DEFINITION_OF_DONE.md

Defines the minimum quality standard required before any feature, subsystem, or milestone is considered complete.

---

## VERSIONING.md

Defines the internal milestone versioning strategy and public release versions.

---

## RELEASE_PROCESS.md

Defines the standard release procedure followed before completing every milestone.

---

# Recommended Reading Order

Before beginning a development session, review the documents in the following order:

1. PROJECT_STATUS.md
2. CURRENT_PHASE.md
3. DECISIONS.md
4. ROADMAP.md
5. MILESTONES.md
6. DEFINITION_OF_DONE.md

This provides sufficient context to continue development without relying on previous conversations.

---

# Relationship to Architecture Documentation

| Architecture Documentation | Project Documentation |
|----------------------------|-----------------------|
| Defines how the system is designed | Defines how the project is managed |
| Software architecture | Project governance |
| Technical specifications | Development workflow |
| Component responsibilities | Milestones and progress |
| Architecture Decision Records | Project status and planning |

---

# Guiding Principle

The repository documentation is the authoritative source of truth for TORANA Engine.

Architectural decisions, project status, development workflow, and milestone progress should always be documented before implementation continues.
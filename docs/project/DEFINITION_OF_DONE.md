# Definition of Done

A milestone, subsystem, or feature is considered complete only when every item in this checklist has been completed.

This document defines the minimum engineering standard for all development within TORANA Engine.

---

# 1. Architecture

The component has been architecturally designed.

Completed items include:

- Responsibilities defined
- Interfaces identified
- Interactions documented
- Architecture reviewed

---

# 2. Documentation

Architecture and supporting documentation have been written.

This may include:

- Architecture documents
- Specifications
- Guides
- ADRs

---

# 3. Test Design

Tests have been designed before implementation.

This includes:

- Unit test cases
- Expected behavior
- Failure scenarios
- Edge cases

---

# 4. Implementation

The feature has been implemented according to the approved architecture and specifications.

---

# 5. Refactoring

Implementation has been reviewed and improved.

Goals include:

- Improved readability
- Reduced duplication
- Better maintainability
- Consistency with project architecture

---

# 6. Documentation Synchronization

Documentation has been updated to match the implementation.

Update documentation where required, including:

- Architecture
- Specifications
- Guides
- CHANGELOG

---

# 7. Validation

The implementation has been validated.

Minimum requirement:

```bash
python -m pytest
```

Future validation may also include:

- Type checking
- Linting
- Performance benchmarks

---

# 8. Version Control

Commit the completed work.

Typical workflow:

```bash
git add .

git commit -m "Meaningful commit message"

git push
```

Tag milestone releases when appropriate.

---

# 9. Project Documentation Update

Update project management documentation if required.

Review and update:

- PROJECT_STATUS.md
- CURRENT_PHASE.md
- CHANGELOG.md
- MILESTONES.md

---

# Completion Criteria

A feature, subsystem, or milestone is **not considered complete** until every step in this document has been successfully completed.

This Definition of Done applies to all future development within TORANA Engine.
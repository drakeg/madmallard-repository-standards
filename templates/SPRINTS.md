# Product vision and sprint plan

**Vision:** Deliver the smallest reliable, free-to-adopt standards toolkit that lets developers and agents improve many independent repositories without misrepresenting project state or erasing local requirements.

Sprints are planned sequentially; dates and scope are adjusted when contributors' capacity is known. Each sprint records goals, deliverables, acceptance and outcome.

## Sprint 0 — Foundation (initial implementation)

**Goal:** Create the public template repository and demonstrate safe, verified, idempotent automation.

- [x] Public repository and template setting
- [x] README / AGENTS / CONTRIBUTING / SPRINTS / BACKLOG / RELEASES / SECURITY / adoption docs
- [x] Conservative Python badge generator and standards auditor with repeatable CLI
- [x] Automated unit tests and GitHub Actions read-only validation
- [ ] PR review and initial merge (pending maintainer review)

**Acceptance:** Two consecutive badge updates produce no second diff; invalid badge markers fail safely; validation workflow passes; application README text is retained.

## Sprint 1 — Broader detection and validation

**Goal:** Increase detection accuracy with fixture-backed language/framework/database detection, structured reporting, improved version verification, and a schema for policy exceptions.

**Acceptance:** More representative fixture tests with zero fabricated status/version/license claims; check mode identifies drift without editing.

## Sprint 2 — Safe multi-repo adoption

**Goal:** Offer opt-in PR automation with repository allowlists, isolated temp clones, branch collision handling, GitHub API rate-limit handling, and least-privilege token documentation.

**Acceptance:** End-to-end sandbox test proves no unapproved pushes and only reviewable PRs.

## Sprint 3 — Central reusable workflows and release tooling

**Goal:** Add version-pinned reusable workflow examples, safe caller configuration, SemVer validation and changelog automation.

**Acceptance:** Caller samples pass GitHub validation and permissions tests; no automatic release without verified criteria.

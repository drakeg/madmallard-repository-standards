# Contributing

All constructive contributions, including AI-authored PRs, are welcome. Open an issue explaining the change, intended benefit, risk, and acceptance criteria. Maintainers triage it into the current sprint or prioritized backlog; urgent break/fix may bypass sprint scheduling but still needs documentation.

## Workflow

1. Fork or branch from the current default branch.
2. Use small scoped commits, preferably Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`, or `feat!:` for breaking changes.
3. Add or update unit tests and documentation for behavior changes.
4. Run `python3 -m unittest discover -s tests -v`, `python3 scripts/audit.py --check` and `python3 scripts/badges.py --mode check`.
5. Open a PR describing the linked issue, sprint, impact, test evidence, migration needs, rollback, and security considerations.
6. Require a human review and passing CI before merge; resolve comments, keep changes traceable, and use squash merges where appropriate.

## Definition of Ready

An issue has an owner or clear acceptance process, business/user rationale, boundaries, dependencies, acceptance criteria, and an estimated scope small enough for a sprint.

## Definition of Done

Acceptance criteria met; tests and security checks pass; docs/templates updated; badge claims verified; code reviewed; no leaked secrets; release impact recorded; relevant sprint/backlog issue closed or updated.

Accessibility: documentation should use informative headings, descriptive links, legible text, keyboard-accessible examples, and no color-only status communication.

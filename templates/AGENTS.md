# Agent operating instructions

Scope: this repository and voluntary adopters only. Preserve application architecture, credentials, deployment constraints, product-specific instructions, and any stricter security or quality rules. Project-level requirements take precedence where appropriate; escalate material conflicts for review.

1. Read README, SPRINTS, BACKLOG, CONTRIBUTING, RELEASES, SECURITY and existing workflow definitions before editing.
2. Associate ordinary changes with a planned sprint issue or prioritized backlog item. Break/fix changes may be expedited, then documented.
3. Use feature branches and pull requests; document changes, tests, risk and rollback. Never silently merge or deploy to another project.
4. Keep the standard README badges directly beneath the first project H1. Inspect configuration, lockfiles, workflows, releases, licenses and infrastructure **before claiming** a technology or status.
5. Use official dynamic GitHub Actions badges, Shields.io dynamic release/license/issues/PR badges. Never hardcode passing results or invent licenses or supported versions.
6. Run `python3 scripts/badges.py --mode dry-run` then `--mode write`, review the diff and run `--mode check`. Do not duplicate markers or replace application-specific sections.
7. Update standards and badges in the same feature PR when supported technologies/workflows change. Include regression tests for generator behavior.
8. Request minimal `contents: read` permissions for validation. Write automations require explicit opting in and narrow `contents: write` / `pull-requests: write` permissions.
9. Never expose secrets in command output, logs or PR comments. Run local tests and report failures accurately.
10. Keep changelog/release documentation aligned with SemVer; no release without user-visible change and validated tag.

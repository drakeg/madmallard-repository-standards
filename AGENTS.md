# Agent operating instructions

Scope: this repository and voluntary adopters only. Preserve application architecture, credentials, deployment constraints, product-specific instructions, and any stricter security or quality rules. Project-level requirements take precedence where appropriate; escalate material conflicts for review.

1. Read README, SPRINTS, BACKLOG, CONTRIBUTING, RELEASES, SECURITY and existing workflow definitions before editing.
2. Associate ordinary changes with a planned sprint issue or prioritized backlog item. Break/fix changes may be expedited, then documented.
3. Use feature branches and pull requests; document changes, tests, risk and rollback. Formal review approval is optional by default; owners may merge directly when GitHub permits it. Never silently merge or deploy to another project.
4. Keep the standard README badges directly beneath the first project H1. Inspect configuration, lockfiles, workflows, releases, licenses and infrastructure **before claiming** a technology or status.
5. Use official dynamic GitHub Actions badges, Shields.io dynamic release/license/issues/PR badges. Never hardcode passing results or invent licenses or supported versions.
6. Run `python3 scripts/badges.py --mode dry-run` then `--mode write`, review the diff and run `--mode check`. Do not duplicate markers or replace application-specific sections.
7. Update standards and badges in the same feature PR when supported technologies/workflows change. Include regression tests for generator behavior.
8. Request minimal `contents: read` permissions for validation. Write automations require explicit opting in and narrow `contents: write` / `pull-requests: write` permissions.
9. Never expose secrets in command output, logs or PR comments. Run local tests and report failures accurately.
10. Keep changelog/release documentation aligned with SemVer; no release without user-visible change and validated tag.

## Development continuity and commercialization

**Commercialization is an ultimate goal, never a development gate.** The owner explicitly permits build-first, exploratory, personal-use, community, open-source, and "if you build it, they will come" development. Do not require customer interviews, outreach, pricing evidence, revenue, product-market fit, or sales validation before continuing approved implementation.

- Follow **Build → Deploy → Test → Fix → Redeploy → Continue** when a deployment/test environment is available. Do not claim unrun tests or deployments.
- Read the current Sprint and prioritized backlog; implement the next ready task, satisfy acceptance criteria, test, fix defects, update docs, and proceed to the next ready Sprint or backlog item **within the current authorized execution session**. A completed PR, Sprint, milestone, or release is not a stopping condition.
- Treat customer discovery, pricing, sales, and outreach as **parallel, optional workstreams**, not prerequisites. Record opportunities honestly; never fabricate demand, customers, feedback, or revenue.
- If external outreach or another action needs permission, pause **only that action** and continue unrelated authorized work. If a task is blocked, select another ready task rather than declaring the whole project blocked.
- Make ordinary technical decisions autonomously; ask only for consequential authorization, genuinely missing essential information, or unavoidable dependencies. Maintain CI, security and existing branch protections; formal GitHub PR review approval remains optional by default.
- Development runs during authorized sessions only. Do not promise unattended/background work or imply activity continues after the session ends.

## First-deployment account setup

Every application with authentication must provide a documented, usable first-run administrator setup workflow. On a fresh installation, guide the operator to create their own initial administrator account before normal login. Require a trusted installation context or one-time bootstrap authorization; never expose unrestricted administrator registration on a public endpoint. Use database-backed authentication and framework password hashing and validation. Close bootstrap registration atomically after successful setup, including concurrent requests; never promote subsequent registrants automatically. Preserve existing accounts and data on upgrades and restarts. Do not ship default credentials or log passwords. Document administrator recovery and test fresh installation, successful setup, repeat/concurrent attempts, existing installations, and normal login. Include these acceptance criteria in the MVP deployment checklist.

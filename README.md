# Mad Mallard Repository Standards

<!-- madmallard-badges:start -->
[![standards](https://github.com/drakeg/madmallard-repository-standards/actions/workflows/standards.yml/badge.svg)](https://github.com/drakeg/madmallard-repository-standards/actions/workflows/standards.yml) [![License](https://img.shields.io/github/license/drakeg/madmallard-repository-standards)](https://github.com/drakeg/madmallard-repository-standards/blob/HEAD/LICENSE) [![Issues](https://img.shields.io/github/issues/drakeg/madmallard-repository-standards)](https://github.com/drakeg/madmallard-repository-standards/issues) [![Pull requests](https://img.shields.io/github/issues-pr/drakeg/madmallard-repository-standards)](https://github.com/drakeg/madmallard-repository-standards/pulls)
<!-- madmallard-badges:end -->

Shared, open-source engineering standards and portable automation for Mad Mallard projects. This repository is a **template** and a source of reusable tooling; adopting its conventions never means replacing an application's code or documentation.

## Capabilities

- Generate verified, dynamic README badges for detected local technologies and configured GitHub Actions.
- Audit one or multiple local repositories for missing standard documents.
- Run safely in **dry-run** mode by default; updates are opt-in and repeatable.
- Follow sprint planning, code review, security, contribution and semantic release guidance.

## Quick start

Requires Python 3.9+ and Git; GitHub CLI is optional for checking existing published releases.

```bash
python3 scripts/badges.py --repo /path/to/project --mode dry-run
python3 scripts/badges.py --repo /path/to/project --mode write
python3 scripts/badges.py --repo /path/to/project --mode check
python3 scripts/audit.py --repo /path/to/project
python3 -m unittest discover -s tests -v
```

For multiple projects, repeat `--repo`. No changes are made in dry-run or check mode. A write changes only the README between bounded badge markers, or inserts a new block after its first H1. Back up changes and review the diff before committing. The generator never copies whole application README files from this template.

## Badge policy

Technology badges require evidence from files such as manifests, Dockerfiles, Compose files, Terraform, or verified dependency declarations. Version claims are intentionally omitted until independently verifiable. GitHub Actions badges link to real workflow filenames and reflect GitHub's live status. License badges require an existing license file; release badges require a published release verified with `gh release view`. Issue and PR badges are live GitHub statistics. Detection is conservative rather than exhaustive: missing badges are preferable to false claims.

Project-specific badge edits can be reapplied with `scripts/badges.py --mode write`; do not manually duplicate the bounded block. Existing README content is retained. See [templates](templates/), [contributing](CONTRIBUTING.md), [agent guidance](AGENTS.md), and [adoption instructions](ADOPTION.md).

## GitHub template and adoption

Choose **Use this template** on GitHub to start a new repository containing the standards skeleton. For existing apps, copy only the relevant files and scripts, customize the documentation, and open a reviewable PR. See [ADOPTION.md](ADOPTION.md) for detailed commands. No automation here automatically pushes to external repositories.

## Development and governance

Current delivery scope is tracked in [SPRINTS.md](SPRINTS.md) and [BACKLOG.md](BACKLOG.md). [RELEASES.md](RELEASES.md) defines release triggers and semantic versioning; [SECURITY.md](SECURITY.md) explains responsible disclosure. Contributions use reviewable PRs and passing required checks; formal GitHub Review approval is optional unless a repository explicitly requires it. Reuse is encouraged under the repository's [MIT License](LICENSE).

## First-deployment account setup

Every application with authentication must provide a documented, usable first-run administrator setup workflow. On a fresh installation, guide the operator to create their own initial administrator account before normal login. Require a trusted installation context or one-time bootstrap authorization; never expose unrestricted administrator registration on a public endpoint. Use database-backed authentication and framework password hashing and validation. Close bootstrap registration atomically after successful setup, including concurrent requests; never promote subsequent registrants automatically. Preserve existing accounts and data on upgrades and restarts. Do not ship default credentials or log passwords. Document administrator recovery and test fresh installation, successful setup, repeat/concurrent attempts, existing installations, and normal login. Include these acceptance criteria in the MVP deployment checklist.

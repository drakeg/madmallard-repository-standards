# Adopting standards in an existing repository

## New project

Open the [template repository](https://github.com/drakeg/madmallard-repository-standards), choose **Use this template**, choose a public or private target as appropriate, and customize README, AGENTS, roadmap, product-specific backlog and dependencies. A template produces an independent repository, not an ongoing synchronization link.

## Existing project

Do not template over an existing project. In a feature branch, copy only selected files from `templates/`, adapting them to existing requirements. Preserve original README, workflows, application source, license and release approach. Inspect any existing AGENTS.md first and merge guidance rather than overwrite it.

Fetch a tagged version of this toolkit or use a checked-out local copy:

```bash
python3 /path/to/standards/scripts/audit.py --repo /path/to/application
python3 /path/to/standards/scripts/badges.py --repo /path/to/application --mode dry-run
python3 /path/to/standards/scripts/badges.py --repo /path/to/application --mode write
git -C /path/to/application diff -- README.md
```

Open a PR, let the existing CI run, and request review. Repeat each command with multiple `--repo` arguments for multiple local checkouts. For a batch of repositories, prepare **separate PRs**; the tool intentionally does not push, merge, or grant itself cross-repository permissions.

## Central validation

Sprint 0 validation runs in this template repository with read-only access. Centralized reusable workflows for adopters are planned for Sprint 3; GitHub supports `workflow_call` workflows, but consuming repositories must opt in with a pinned revision and minimally scoped token permissions. Do not point consuming repositories at mutable `main` for security-sensitive reusable automation.

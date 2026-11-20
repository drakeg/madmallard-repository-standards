# Releases and versioning

Use Semantic Versioning: MAJOR for incompatible interfaces or adoption behavior; MINOR for backward-compatible new features and detectors; PATCH for backward-compatible fixes and documentation corrections where a release is justified.

Initial stable `v1.0.0` requires maintainer acceptance of the CLI contract, validated CI, and documented adoption behavior. Prior to stability use `v0.x.y` if releases are needed. No release is created simply because a PR merged; publish when a meaningful, tested change is ready for consumers.

**Release checklist:** reviewed changes, green required tests, no exposed secrets, verified README badges, updated roadmap/backlog, release notes with migration/compatibility guidance, and signed-off version/tag selection. Publish a GitHub release tied to the version tag. Reverts and security fixes may justify an expedited PATCH. Breaking behavior must state migration steps and target the next MAJOR version.

Prefer Conventional Commits to clarify changes, but manually verify impact before choosing a release version; no workflow assumes commit prefixes are sufficient evidence of compatibility.

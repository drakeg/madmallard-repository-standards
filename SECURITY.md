# Security policy

Please **do not** submit credentials, sensitive data, or working exploits in public issues. Privately contact the repository owner through GitHub's private vulnerability reporting facility if enabled; otherwise contact the maintainer privately through a mutually agreed channel before sharing details.

Automation defaults to read-only operations. Do not add broad personal access tokens to workflows. Fork PRs should run with read-only permissions, avoid untrusted script execution with write credentials, and never receive production secrets. Review dependency and action changes before upgrading. Report impact, affected versions and safe reproduction steps privately.

Supported versions: until a first stable release is published, work is supported on the current default branch only; after release, maintainers will state supported release lines here.

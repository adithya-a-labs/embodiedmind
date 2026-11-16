# Explain the VS Code Sync destination

- Objective — Explain why VS Code displays origin/master instead of the published experiment branch.
- Result — The local embodiedmind-experiment branch at 42f5dde4 tracks origin/master by prior request. VS Code Sync uses the upstream. The local remote-tracking comparison shows one outgoing commit relative to origin/embodiedmind-experiment.
- Verification — Checked Git status, upstream, rev-list counts, commit subject, and official VS Code documentation. Added this local record. No refs or settings changed.

# Enable private viewer access from a phone

Retrospective record. Reconstructed from this chat, Git history, and cited evidence. Related follow-up turns are grouped by task.

## Changes

Added an exact HTTPS origin option in the viewer CLI and server, with tests and README instructions. Created a private port-8765 tunnel and restarted the WSL viewer. Committed and pushed as `995fbb2`.

## Rationale

Kept the viewer on loopback and forwarded only the viewer port. Restricted accepted Sandbox origins to preserve local and authenticated tunnel use.

## Verification and evidence

67 tests passed. A configured origin returned 200 and an unrelated origin returned 403 in the local harness. The user confirmed phone access.

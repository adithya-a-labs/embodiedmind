# Expose all project games and memory agents in the dashboard

## Objective

Check Replay, Live Monitor, and Sandbox for coverage of every EmbodiedMind game and B0–B10. Close discovery gaps in the private tunnel-backed dashboard.

## Changes and decisions

- `src/embodiedmind/viewer/data.py` adds optional per-run game and variant coverage from completed jobs. The Live Monitor poll keeps its lightweight catalog.
- `src/embodiedmind/viewer/server.py` serves the agent registry and enables coverage for replay-catalog requests.
- `src/embodiedmind/viewer/static/index.html`, `viewer.css`, and `viewer.js` add global game and agent filters, retain archived scenario/seed constraints, prefer the chosen filter agent on the left, and display an individual replay when a seed has only one agent. Sandbox selectors use the server registry. The filters retain the three existing controls B0G, B3G and B9N.
- `tests/test_viewer.py` verifies that incomplete manifest jobs do not advertise replay coverage.
- Restarted the viewer on port 8765 with its existing private tunnel origin. No external records changed. No experiments or inference calls ran during this dashboard change.
- This record and the six code/test changes are in the working tree on `embodiedmind-experiment`, based on `72c28725`. The prior retrospective record was already untracked.

## Verification and limits

- Inventoried 2,263 completed entries across 30 manifests. All 12 project environments and all primary variants have recordings. B4 and B5 have no saved runs on GoToObj or GoToObjMaze. Sandbox presents these four combinations without inventing replay evidence. Existing Live Monitor uses snapshots from monitored runs.
- The full pytest suite passed with 101 tests. `git diff --check` and `node --check src/embodiedmind/viewer/static/viewer.js` passed.
- A Playwright test initially read the selectors before the catalog had loaded. Waiting for the first reconstructed board fixed the test. Verified the default DoorKey replay, B10 versus B9 on MultiRoom, missing Maze/B5 replay, the 390 px layout, Live Monitor controls and all Sandbox options.
- Port 8765 responded after restart with 12 games, all primary variants and 30 archives using the configured tunnel host header. The external tunnel responded to an unauthenticated GET with a redirect and to HEAD with 401. An authenticated phone session was unavailable for verification.

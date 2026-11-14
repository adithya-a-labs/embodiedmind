# Start the large all-game memory comparison

- Objective — Compare B6, B7, B8, B9 and B9N across all currently supported stock and custom games.
- Configuration — On embodiedmind-experiment, d6eea75 adds configs/memory-large-stock-dev.yaml (550 jobs) and configs/memory-large-shift-dev.yaml (150 jobs). Matched fresh seeds 4001–4010, ten per variant and condition, retain 48 actions/calls, 768 memory bytes and single-worker inference. GoToShift keeps the original no-change, dropout and relocation definitions and two scripted opening turns.
- Launch — Started WSL user service embodiedmind-memory-large-20261114-173852. It runs the stock archive followed serially by the shift archive, each with --monitor, dedicated stdout/stderr and the runner’s evidence packaging. Paths outputs/memory-large-stock-20261114-173852 and outputs/memory-large-shift-20261114-173852.
- Rationale — Chose ten fresh development seeds per condition to expand coverage while keeping existing benchmark rosters intact. Kept stock and custom configurations separate so stock episodes do not receive GoToShift interventions.
- Verification — Compared the roster with the factory allowlist, intervention definitions and variant registry. Verified an active WSL service and a live board snapshot via the tunnel-facing API. Added the launch checklist to the Notion roadmap. This record is a working-tree addition. Final coverage, checksums and evidence commit are pending at this checkpoint.

## Completion

- Both stages exited 0. Verified 550 stock and 150 GoToShift episodes with every required pair intact, no errors or exclusions, 700 readable GIFs, and 32,325 SHA-256 entries. The stock log recorded a mission-generation rejection that was recovered within the environment reset. The model digest and task settings came from the runner manifest.
- Added report/all-game-comparison.md in the stock archive. It contains a complete success matrix, mean actions, mean tokens, outcomes and per-variant intervention exposure. All 100 dropout and relocation events applied. Committed both archives together as 2e308ae and updated the Notion checklist and results.
- Findings — B7 led DoorKey 10/10, B9 solved all ten seeds in both Memory games, Key Corridor and Put Next, and B8 led Dynamic Obstacles 7/10. MultiRoom and Blocked Unlock Pickup had 100 budget timeouts combined. Results measure configured policies on fresh development seeds at 48 steps. No push.

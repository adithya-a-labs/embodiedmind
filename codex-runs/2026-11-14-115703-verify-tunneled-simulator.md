# Verify the tunneled simulator

- Objective — Confirm the simulator meant by the user is the existing private Dev Tunnel viewer and verify that its upstream app serves the memory upgrades.
- Branch — embodiedmind-experiment at 6feb9db, tracking origin/master. The checkout was clean before writing this record.
- Verification — Checked the running process arguments and used curl against port 8765 with the configured tunnel Host. The JavaScript lists B5, B6, and B7, and the run catalog lists the revised DoorKey development archive.
- Changes — This Git-eligible record is the only addition. No source, tunnel, or external records changed. No experiment was run. This checked the tunnel-facing local service. An authenticated off-device request was not tested.

# Explain the six relocation memory variants

- Objective — Explain the implementation differences between B0–B5 and how to read the relocation comparison.
- Evidence — Inspected the agent registry, reactive and text memory, structured memory, Hybrid, GroundedMemory, BeliefLedger and grounding mode flags. B4 and B5 share a memory backend. B5 adds map-guided decisions to the shared guarded controller.
- Branch — embodiedmind-experiment, experiment evidence 6f56667. This note is a working-tree addition. No source, run archive or external record changed.
- Verification — Source reads and ripgrep confirmed storage, retrieval, revision and controller distinctions. A PowerShell path glob and initial brace syntax failed, so explicit paths and directory searches were used. No experiment rerun.

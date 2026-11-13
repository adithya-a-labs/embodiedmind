# Failures

- Gate 0: Offline dependency resolution lacked cached registry metadata. Online resolution completed and a fresh locked setup passed.
- First B0 GoToObj smoke: reached the 24-call cap without satisfying the mission. This is a valid smoke trajectory and a task failure. Kept the raw trace and replay.
- Two-slot Ollama calibration: lower observed throughput and 3 of 12 different raw responses compared with serial. Retained measurement logs and stopped the temporary server. Use one slot for all scored variants.
- Dynamic development attempt `dynamic-dev/e00-s00000-relocation-B1-r0`: evaluator outputs could contain NumPy integer coordinates, which blocked JSON serialization. Preserved the old attempt and normalized coordinate types in `a0311bf`. Validated the fix with a regression test and initiated a fresh matched development roster.
- Initial dynamic development design attempted relocation at step five. All six assignments stayed in the original world because the endpoints were still visible, so the held-out design now uses two shared scripted left turns and an earlier fixed trigger. The first two dynamic designs remain in the run archive.

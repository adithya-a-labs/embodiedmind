# Decisions

- Use one `uv` project with Python 3.12.16. Preserve system Python and existing environment packages.
- Reserve seeds 0–19 for development, 1000–1029 for static held-out evaluation and 2000–2029 for custom dynamic evaluation. Use seed 42 for the standalone interface smoke fixture.
- Keep one local Ollama inference slot for the scored study because the isolated two-slot development measurement decreased throughput and changed some outputs.
- Use the same route hint for all baselines. It uses only the current visible view and leaves the action choice to the frozen model. Compare the specified memory configurations under this shared controller.
- Keep all assigned dynamic episodes in the main comparison, including missed interventions. Report exposure separately.
- Use immutable attempt directories. Compare matching environment, seed, mission, intervention and replicate. Record preserved attempts and exact source/config hashes in the manifest.

# Decisions

- Use one `uv` project with Python 3.12.16. Preserve system Python and existing environment packages.
- Reserve seeds 0–19 for development and 1000–1029 for static held-out evaluation. Use seed 42 for a standalone interface smoke test. Register dynamic seeds independently before scoring.
- Freeze the common runtime and methodological settings after development and before held-out jobs. Keep evaluator-only data and renders outside policy inputs.
- Use immutable attempt directories. Each comparison pairs by environment, seed, mission, intervention and replicate.

# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes development. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 32 of 32 cells were attempted, 32 validated, 0 excluded and 32 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| development | MiniGrid-MemoryS13-v0 | none | B0 | 4 | 4 | 4 | 0.500 | 10.000 | 3951.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | B1 | 4 | 4 | 4 | 0.500 | 29.750 | 19311.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | B2 | 4 | 4 | 4 | 0.250 | 28.500 | 18913.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | B3 | 4 | 4 | 4 | 0.250 | 19.750 | 13198.250 | — |
| development | MiniGrid-MemoryS13-v0 | none | B4 | 4 | 4 | 4 | 0.500 | 10.000 | 4089.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | B5 | 4 | 4 | 4 | 0.000 | 48.000 | 22320.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | B6 | 4 | 4 | 4 | 0.000 | 48.000 | 22320.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | B7 | 4 | 4 | 4 | 0.000 | 48.000 | 22320.500 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| development | MiniGrid-MemoryS13-v0 | none | success | B5 − B4 | 4 | -0.500 | — |
| development | MiniGrid-MemoryS13-v0 | none | blocked_actions | B5 − B4 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | verification_requests | B5 − B4 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | success | B6 − B5 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | blocked_actions | B6 − B5 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | verification_requests | B6 − B5 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | success | B7 − B5 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | blocked_actions | B7 − B5 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | verification_requests | B7 − B5 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | success | B6 − B7 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | blocked_actions | B6 − B7 | 4 | 0.000 | — |
| development | MiniGrid-MemoryS13-v0 | none | verification_requests | B6 − B7 | 4 | 0.000 | — |

Differences use only identical environment, intervention, mission, seed and replicate. Replicate differences are averaged within seed before estimating intervals with a deterministic 4,000-draw seed bootstrap. Intervals are shown for at least five matched seeds. Valid task failures are included. Missing measurements stay missing. The main dynamic comparisons retain episodes under their assigned condition. Exposure counts show how often the intervention was recorded as applied.

## Interpretation and limits

- Treat development evidence as feasibility and diagnostics. The two held-out benchmark rosters must both be supplied for full experiment interpretation.
- Estimates apply to the frozen local model, configured action/prompt budgets and abstract 2D worlds. The study concerns planning in simulation.
- A small paired sample and sparse contradiction events can yield imprecise estimates. The stale-action measure requires an explicit evidence ID and misses uncited intent. Unsupported references are missing, invalid or unprovided IDs, a narrower observation than all model hallucinations.
- B3 adds belief revision, aging warnings and working memory to structured memory. The contrast with B2 evaluates that bundle. The B1 result applies to the specified bounded factual history.
- A hidden relocation can be missed when either cell is visible or a policy changes the world before the trigger. Assigned-arm results include these no-ops. Equal measured rates with rare cited contradictions give limited evidence about revision.
- Traces record prompt usage, which can vary by memory treatment under a shared ceiling. Shorter paths and higher success may compete with greater inference cost.
- The observation encoder and model use symbolic features. Navigation depends on the shared controller and odometry inferred from permitted action feedback. Identical-looking objects can be misidentified.

## Failure evidence

- development · MiniGrid-MemoryS13-v0 · none · B0 seed 14 · terminated_failure (11 steps). Trace at `episodes/e00-s00014-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s00014-none-B0-r0/finish.png), [000000.png](../episodes/e00-s00014-none-B0-r0/frames/000000.png), [000001.png](../episodes/e00-s00014-none-B0-r0/frames/000001.png), [000002.png](../episodes/e00-s00014-none-B0-r0/frames/000002.png), [000003.png](../episodes/e00-s00014-none-B0-r0/frames/000003.png), [000004.png](../episodes/e00-s00014-none-B0-r0/frames/000004.png), [000005.png](../episodes/e00-s00014-none-B0-r0/frames/000005.png), [000006.png](../episodes/e00-s00014-none-B0-r0/frames/000006.png), [000007.png](../episodes/e00-s00014-none-B0-r0/frames/000007.png), [000008.png](../episodes/e00-s00014-none-B0-r0/frames/000008.png), [000009.png](../episodes/e00-s00014-none-B0-r0/frames/000009.png), [000010.png](../episodes/e00-s00014-none-B0-r0/frames/000010.png), [000011.png](../episodes/e00-s00014-none-B0-r0/frames/000011.png), [start.png](../episodes/e00-s00014-none-B0-r0/start.png), [replay.gif](../episodes/e00-s00014-none-B0-r0/replay.gif)

## Outcome distribution

- development · MiniGrid-MemoryS13-v0 · none — budget_timeout: 16, success: 8, terminated_failure: 8

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `memory-hallway-all-48-20261114-123128`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/memory-hallway-all-48-20261114-123128/manifest.json`. Source `c6b32ee59a31c80954fd1ce6c41232625748b60c`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-hallway-all-48-20261114-123128" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-hallway-all-48-20261114-123128/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

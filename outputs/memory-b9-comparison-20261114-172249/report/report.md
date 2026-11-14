# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes development. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 45 of 45 cells were attempted, 45 validated, 0 excluded and 45 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| development | BabyAI-KeyCorridorS3R3-v0 | none | B8 | 5 | 5 | 5 | 0.000 | 48.000 | 21768.600 | — |
| development | BabyAI-KeyCorridorS3R3-v0 | none | B9 | 5 | 5 | 5 | 1.000 | 31.200 | 14670.400 | — |
| development | BabyAI-KeyCorridorS3R3-v0 | none | B9N | 5 | 5 | 5 | 0.000 | 48.000 | 21595.200 | — |
| development | BabyAI-PutNextS5N2-v0 | none | B8 | 5 | 5 | 5 | 0.000 | 48.000 | 22803.000 | — |
| development | BabyAI-PutNextS5N2-v0 | none | B9 | 5 | 5 | 5 | 1.000 | 11.200 | 5391.600 | — |
| development | BabyAI-PutNextS5N2-v0 | none | B9N | 5 | 5 | 5 | 0.000 | 48.000 | 22678.800 | — |
| development | MiniGrid-MemoryS17Random-v0 | none | B8 | 5 | 5 | 5 | 1.000 | 16.200 | 8134.200 | — |
| development | MiniGrid-MemoryS17Random-v0 | none | B9 | 5 | 5 | 5 | 1.000 | 13.000 | 6561.000 | — |
| development | MiniGrid-MemoryS17Random-v0 | none | B9N | 5 | 5 | 5 | 0.600 | 30.400 | 15168.400 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| development | BabyAI-KeyCorridorS3R3-v0 | none | success | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | blocked_actions | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | verification_requests | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | success | B9 − B9N | 5 | 1.000 | [1.000, 1.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | blocked_actions | B9 − B9N | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | verification_requests | B9 − B9N | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | success | B9 − B8 | 5 | 1.000 | [1.000, 1.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | blocked_actions | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-KeyCorridorS3R3-v0 | none | verification_requests | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | success | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | blocked_actions | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | verification_requests | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | success | B9 − B9N | 5 | 1.000 | [1.000, 1.000] |
| development | BabyAI-PutNextS5N2-v0 | none | blocked_actions | B9 − B9N | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | verification_requests | B9 − B9N | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | success | B9 − B8 | 5 | 1.000 | [1.000, 1.000] |
| development | BabyAI-PutNextS5N2-v0 | none | blocked_actions | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | BabyAI-PutNextS5N2-v0 | none | verification_requests | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | success | B9N − B8 | 5 | -0.400 | [-0.800, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | blocked_actions | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | verification_requests | B9N − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | success | B9 − B9N | 5 | 0.400 | [0.000, 0.800] |
| development | MiniGrid-MemoryS17Random-v0 | none | blocked_actions | B9 − B9N | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | verification_requests | B9 − B9N | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | success | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | blocked_actions | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-MemoryS17Random-v0 | none | verification_requests | B9 − B8 | 5 | 0.000 | [0.000, 0.000] |

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

- development · BabyAI-KeyCorridorS3R3-v0 · none · B8 seed 3001 · budget_timeout (48 steps). Trace at `episodes/e00-s03001-none-B8-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s03001-none-B8-r0/finish.png), [000000.png](../episodes/e00-s03001-none-B8-r0/frames/000000.png), [000001.png](../episodes/e00-s03001-none-B8-r0/frames/000001.png), [000002.png](../episodes/e00-s03001-none-B8-r0/frames/000002.png), [000003.png](../episodes/e00-s03001-none-B8-r0/frames/000003.png), [000004.png](../episodes/e00-s03001-none-B8-r0/frames/000004.png), [000005.png](../episodes/e00-s03001-none-B8-r0/frames/000005.png), [000006.png](../episodes/e00-s03001-none-B8-r0/frames/000006.png), [000007.png](../episodes/e00-s03001-none-B8-r0/frames/000007.png), [000008.png](../episodes/e00-s03001-none-B8-r0/frames/000008.png), [000009.png](../episodes/e00-s03001-none-B8-r0/frames/000009.png), [000010.png](../episodes/e00-s03001-none-B8-r0/frames/000010.png), [000011.png](../episodes/e00-s03001-none-B8-r0/frames/000011.png), [000012.png](../episodes/e00-s03001-none-B8-r0/frames/000012.png), [000013.png](../episodes/e00-s03001-none-B8-r0/frames/000013.png), [000014.png](../episodes/e00-s03001-none-B8-r0/frames/000014.png), [000015.png](../episodes/e00-s03001-none-B8-r0/frames/000015.png), [000016.png](../episodes/e00-s03001-none-B8-r0/frames/000016.png), [000017.png](../episodes/e00-s03001-none-B8-r0/frames/000017.png), [000018.png](../episodes/e00-s03001-none-B8-r0/frames/000018.png), [000019.png](../episodes/e00-s03001-none-B8-r0/frames/000019.png), [000020.png](../episodes/e00-s03001-none-B8-r0/frames/000020.png), [000021.png](../episodes/e00-s03001-none-B8-r0/frames/000021.png), [000022.png](../episodes/e00-s03001-none-B8-r0/frames/000022.png), [000023.png](../episodes/e00-s03001-none-B8-r0/frames/000023.png), [000024.png](../episodes/e00-s03001-none-B8-r0/frames/000024.png), [000025.png](../episodes/e00-s03001-none-B8-r0/frames/000025.png), [000026.png](../episodes/e00-s03001-none-B8-r0/frames/000026.png), [000027.png](../episodes/e00-s03001-none-B8-r0/frames/000027.png), [000028.png](../episodes/e00-s03001-none-B8-r0/frames/000028.png), [000029.png](../episodes/e00-s03001-none-B8-r0/frames/000029.png), [000030.png](../episodes/e00-s03001-none-B8-r0/frames/000030.png), [000031.png](../episodes/e00-s03001-none-B8-r0/frames/000031.png), [000032.png](../episodes/e00-s03001-none-B8-r0/frames/000032.png), [000033.png](../episodes/e00-s03001-none-B8-r0/frames/000033.png), [000034.png](../episodes/e00-s03001-none-B8-r0/frames/000034.png), [000035.png](../episodes/e00-s03001-none-B8-r0/frames/000035.png), [000036.png](../episodes/e00-s03001-none-B8-r0/frames/000036.png), [000037.png](../episodes/e00-s03001-none-B8-r0/frames/000037.png), [000038.png](../episodes/e00-s03001-none-B8-r0/frames/000038.png), [000039.png](../episodes/e00-s03001-none-B8-r0/frames/000039.png), [000040.png](../episodes/e00-s03001-none-B8-r0/frames/000040.png), [000041.png](../episodes/e00-s03001-none-B8-r0/frames/000041.png), [000042.png](../episodes/e00-s03001-none-B8-r0/frames/000042.png), [000043.png](../episodes/e00-s03001-none-B8-r0/frames/000043.png), [000044.png](../episodes/e00-s03001-none-B8-r0/frames/000044.png), [000045.png](../episodes/e00-s03001-none-B8-r0/frames/000045.png), [000046.png](../episodes/e00-s03001-none-B8-r0/frames/000046.png), [000047.png](../episodes/e00-s03001-none-B8-r0/frames/000047.png), [000048.png](../episodes/e00-s03001-none-B8-r0/frames/000048.png), [start.png](../episodes/e00-s03001-none-B8-r0/start.png), [replay.gif](../episodes/e00-s03001-none-B8-r0/replay.gif)
- development · BabyAI-PutNextS5N2-v0 · none · B8 seed 3001 · budget_timeout (48 steps). Trace at `episodes/e01-s03001-none-B8-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e01-s03001-none-B8-r0/finish.png), [000000.png](../episodes/e01-s03001-none-B8-r0/frames/000000.png), [000001.png](../episodes/e01-s03001-none-B8-r0/frames/000001.png), [000002.png](../episodes/e01-s03001-none-B8-r0/frames/000002.png), [000003.png](../episodes/e01-s03001-none-B8-r0/frames/000003.png), [000004.png](../episodes/e01-s03001-none-B8-r0/frames/000004.png), [000005.png](../episodes/e01-s03001-none-B8-r0/frames/000005.png), [000006.png](../episodes/e01-s03001-none-B8-r0/frames/000006.png), [000007.png](../episodes/e01-s03001-none-B8-r0/frames/000007.png), [000008.png](../episodes/e01-s03001-none-B8-r0/frames/000008.png), [000009.png](../episodes/e01-s03001-none-B8-r0/frames/000009.png), [000010.png](../episodes/e01-s03001-none-B8-r0/frames/000010.png), [000011.png](../episodes/e01-s03001-none-B8-r0/frames/000011.png), [000012.png](../episodes/e01-s03001-none-B8-r0/frames/000012.png), [000013.png](../episodes/e01-s03001-none-B8-r0/frames/000013.png), [000014.png](../episodes/e01-s03001-none-B8-r0/frames/000014.png), [000015.png](../episodes/e01-s03001-none-B8-r0/frames/000015.png), [000016.png](../episodes/e01-s03001-none-B8-r0/frames/000016.png), [000017.png](../episodes/e01-s03001-none-B8-r0/frames/000017.png), [000018.png](../episodes/e01-s03001-none-B8-r0/frames/000018.png), [000019.png](../episodes/e01-s03001-none-B8-r0/frames/000019.png), [000020.png](../episodes/e01-s03001-none-B8-r0/frames/000020.png), [000021.png](../episodes/e01-s03001-none-B8-r0/frames/000021.png), [000022.png](../episodes/e01-s03001-none-B8-r0/frames/000022.png), [000023.png](../episodes/e01-s03001-none-B8-r0/frames/000023.png), [000024.png](../episodes/e01-s03001-none-B8-r0/frames/000024.png), [000025.png](../episodes/e01-s03001-none-B8-r0/frames/000025.png), [000026.png](../episodes/e01-s03001-none-B8-r0/frames/000026.png), [000027.png](../episodes/e01-s03001-none-B8-r0/frames/000027.png), [000028.png](../episodes/e01-s03001-none-B8-r0/frames/000028.png), [000029.png](../episodes/e01-s03001-none-B8-r0/frames/000029.png), [000030.png](../episodes/e01-s03001-none-B8-r0/frames/000030.png), [000031.png](../episodes/e01-s03001-none-B8-r0/frames/000031.png), [000032.png](../episodes/e01-s03001-none-B8-r0/frames/000032.png), [000033.png](../episodes/e01-s03001-none-B8-r0/frames/000033.png), [000034.png](../episodes/e01-s03001-none-B8-r0/frames/000034.png), [000035.png](../episodes/e01-s03001-none-B8-r0/frames/000035.png), [000036.png](../episodes/e01-s03001-none-B8-r0/frames/000036.png), [000037.png](../episodes/e01-s03001-none-B8-r0/frames/000037.png), [000038.png](../episodes/e01-s03001-none-B8-r0/frames/000038.png), [000039.png](../episodes/e01-s03001-none-B8-r0/frames/000039.png), [000040.png](../episodes/e01-s03001-none-B8-r0/frames/000040.png), [000041.png](../episodes/e01-s03001-none-B8-r0/frames/000041.png), [000042.png](../episodes/e01-s03001-none-B8-r0/frames/000042.png), [000043.png](../episodes/e01-s03001-none-B8-r0/frames/000043.png), [000044.png](../episodes/e01-s03001-none-B8-r0/frames/000044.png), [000045.png](../episodes/e01-s03001-none-B8-r0/frames/000045.png), [000046.png](../episodes/e01-s03001-none-B8-r0/frames/000046.png), [000047.png](../episodes/e01-s03001-none-B8-r0/frames/000047.png), [000048.png](../episodes/e01-s03001-none-B8-r0/frames/000048.png), [start.png](../episodes/e01-s03001-none-B8-r0/start.png), [replay.gif](../episodes/e01-s03001-none-B8-r0/replay.gif)
- development · MiniGrid-MemoryS17Random-v0 · none · B9N seed 3001 · budget_timeout (48 steps). Trace at `episodes/e02-s03001-none-B9N-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e02-s03001-none-B9N-r0/finish.png), [000000.png](../episodes/e02-s03001-none-B9N-r0/frames/000000.png), [000001.png](../episodes/e02-s03001-none-B9N-r0/frames/000001.png), [000002.png](../episodes/e02-s03001-none-B9N-r0/frames/000002.png), [000003.png](../episodes/e02-s03001-none-B9N-r0/frames/000003.png), [000004.png](../episodes/e02-s03001-none-B9N-r0/frames/000004.png), [000005.png](../episodes/e02-s03001-none-B9N-r0/frames/000005.png), [000006.png](../episodes/e02-s03001-none-B9N-r0/frames/000006.png), [000007.png](../episodes/e02-s03001-none-B9N-r0/frames/000007.png), [000008.png](../episodes/e02-s03001-none-B9N-r0/frames/000008.png), [000009.png](../episodes/e02-s03001-none-B9N-r0/frames/000009.png), [000010.png](../episodes/e02-s03001-none-B9N-r0/frames/000010.png), [000011.png](../episodes/e02-s03001-none-B9N-r0/frames/000011.png), [000012.png](../episodes/e02-s03001-none-B9N-r0/frames/000012.png), [000013.png](../episodes/e02-s03001-none-B9N-r0/frames/000013.png), [000014.png](../episodes/e02-s03001-none-B9N-r0/frames/000014.png), [000015.png](../episodes/e02-s03001-none-B9N-r0/frames/000015.png), [000016.png](../episodes/e02-s03001-none-B9N-r0/frames/000016.png), [000017.png](../episodes/e02-s03001-none-B9N-r0/frames/000017.png), [000018.png](../episodes/e02-s03001-none-B9N-r0/frames/000018.png), [000019.png](../episodes/e02-s03001-none-B9N-r0/frames/000019.png), [000020.png](../episodes/e02-s03001-none-B9N-r0/frames/000020.png), [000021.png](../episodes/e02-s03001-none-B9N-r0/frames/000021.png), [000022.png](../episodes/e02-s03001-none-B9N-r0/frames/000022.png), [000023.png](../episodes/e02-s03001-none-B9N-r0/frames/000023.png), [000024.png](../episodes/e02-s03001-none-B9N-r0/frames/000024.png), [000025.png](../episodes/e02-s03001-none-B9N-r0/frames/000025.png), [000026.png](../episodes/e02-s03001-none-B9N-r0/frames/000026.png), [000027.png](../episodes/e02-s03001-none-B9N-r0/frames/000027.png), [000028.png](../episodes/e02-s03001-none-B9N-r0/frames/000028.png), [000029.png](../episodes/e02-s03001-none-B9N-r0/frames/000029.png), [000030.png](../episodes/e02-s03001-none-B9N-r0/frames/000030.png), [000031.png](../episodes/e02-s03001-none-B9N-r0/frames/000031.png), [000032.png](../episodes/e02-s03001-none-B9N-r0/frames/000032.png), [000033.png](../episodes/e02-s03001-none-B9N-r0/frames/000033.png), [000034.png](../episodes/e02-s03001-none-B9N-r0/frames/000034.png), [000035.png](../episodes/e02-s03001-none-B9N-r0/frames/000035.png), [000036.png](../episodes/e02-s03001-none-B9N-r0/frames/000036.png), [000037.png](../episodes/e02-s03001-none-B9N-r0/frames/000037.png), [000038.png](../episodes/e02-s03001-none-B9N-r0/frames/000038.png), [000039.png](../episodes/e02-s03001-none-B9N-r0/frames/000039.png), [000040.png](../episodes/e02-s03001-none-B9N-r0/frames/000040.png), [000041.png](../episodes/e02-s03001-none-B9N-r0/frames/000041.png), [000042.png](../episodes/e02-s03001-none-B9N-r0/frames/000042.png), [000043.png](../episodes/e02-s03001-none-B9N-r0/frames/000043.png), [000044.png](../episodes/e02-s03001-none-B9N-r0/frames/000044.png), [000045.png](../episodes/e02-s03001-none-B9N-r0/frames/000045.png), [000046.png](../episodes/e02-s03001-none-B9N-r0/frames/000046.png), [000047.png](../episodes/e02-s03001-none-B9N-r0/frames/000047.png), [000048.png](../episodes/e02-s03001-none-B9N-r0/frames/000048.png), [start.png](../episodes/e02-s03001-none-B9N-r0/start.png), [replay.gif](../episodes/e02-s03001-none-B9N-r0/replay.gif)

## Outcome distribution

- development · BabyAI-KeyCorridorS3R3-v0 · none — budget_timeout: 10, success: 5
- development · BabyAI-PutNextS5N2-v0 · none — budget_timeout: 10, success: 5
- development · MiniGrid-MemoryS17Random-v0 · none — budget_timeout: 2, success: 13

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `memory-b9-comparison-20261114-172249`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/memory-b9-comparison-20261114-172249/manifest.json`. Source `f088dd2eb968c0ff443e802af014406a018635b5`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-b9-comparison-20261114-172249" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-b9-comparison-20261114-172249/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

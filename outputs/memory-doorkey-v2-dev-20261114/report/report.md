# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes development. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 40 of 40 cells were attempted, 40 validated, 0 excluded and 40 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| development | MiniGrid-DoorKey-8x8-v0 | none | B0 | 5 | 5 | 5 | 0.800 | 21.200 | 7596.800 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B0G | 5 | 5 | 5 | 0.800 | 23.200 | 8323.200 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B3 | 5 | 5 | 5 | 0.400 | 33.600 | 21585.800 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B3G | 5 | 5 | 5 | 0.400 | 32.000 | 20346.600 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B4 | 5 | 5 | 5 | 0.400 | 33.400 | 13056.000 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B5 | 5 | 5 | 5 | 0.000 | 36.000 | 16636.200 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B6 | 5 | 5 | 5 | 0.000 | 36.000 | 17612.200 | — |
| development | MiniGrid-DoorKey-8x8-v0 | none | B7 | 5 | 5 | 5 | 1.000 | 16.200 | 7646.600 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B0G − B0 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B0G − B0 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B0G − B0 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B3G − B3 | 5 | 0.000 | [-0.600, 0.600] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B3G − B3 | 5 | -13.200 | [-20.600, -6.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B3G − B3 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B3G − B0G | 5 | -0.400 | [-0.800, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B3G − B0G | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B3G − B0G | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B4 − B3G | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B4 − B3G | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B4 − B3G | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B5 − B4 | 5 | -0.400 | [-0.800, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B5 − B4 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B5 − B4 | 5 | 14.000 | [12.400, 15.200] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B6 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B6 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B6 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B7 − B5 | 5 | 1.000 | [1.000, 1.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B7 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B7 − B5 | 5 | -14.000 | [-15.200, -12.400] |
| development | MiniGrid-DoorKey-8x8-v0 | none | success | B6 − B7 | 5 | -1.000 | [-1.000, -1.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | blocked_actions | B6 − B7 | 5 | 0.000 | [0.000, 0.000] |
| development | MiniGrid-DoorKey-8x8-v0 | none | verification_requests | B6 − B7 | 5 | 14.000 | [12.400, 15.200] |

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

- development · MiniGrid-DoorKey-8x8-v0 · none · B0 seed 8 · budget_timeout (36 steps). Trace at `episodes/e00-s00008-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s00008-none-B0-r0/finish.png), [000000.png](../episodes/e00-s00008-none-B0-r0/frames/000000.png), [000001.png](../episodes/e00-s00008-none-B0-r0/frames/000001.png), [000002.png](../episodes/e00-s00008-none-B0-r0/frames/000002.png), [000003.png](../episodes/e00-s00008-none-B0-r0/frames/000003.png), [000004.png](../episodes/e00-s00008-none-B0-r0/frames/000004.png), [000005.png](../episodes/e00-s00008-none-B0-r0/frames/000005.png), [000006.png](../episodes/e00-s00008-none-B0-r0/frames/000006.png), [000007.png](../episodes/e00-s00008-none-B0-r0/frames/000007.png), [000008.png](../episodes/e00-s00008-none-B0-r0/frames/000008.png), [000009.png](../episodes/e00-s00008-none-B0-r0/frames/000009.png), [000010.png](../episodes/e00-s00008-none-B0-r0/frames/000010.png), [000011.png](../episodes/e00-s00008-none-B0-r0/frames/000011.png), [000012.png](../episodes/e00-s00008-none-B0-r0/frames/000012.png), [000013.png](../episodes/e00-s00008-none-B0-r0/frames/000013.png), [000014.png](../episodes/e00-s00008-none-B0-r0/frames/000014.png), [000015.png](../episodes/e00-s00008-none-B0-r0/frames/000015.png), [000016.png](../episodes/e00-s00008-none-B0-r0/frames/000016.png), [000017.png](../episodes/e00-s00008-none-B0-r0/frames/000017.png), [000018.png](../episodes/e00-s00008-none-B0-r0/frames/000018.png), [000019.png](../episodes/e00-s00008-none-B0-r0/frames/000019.png), [000020.png](../episodes/e00-s00008-none-B0-r0/frames/000020.png), [000021.png](../episodes/e00-s00008-none-B0-r0/frames/000021.png), [000022.png](../episodes/e00-s00008-none-B0-r0/frames/000022.png), [000023.png](../episodes/e00-s00008-none-B0-r0/frames/000023.png), [000024.png](../episodes/e00-s00008-none-B0-r0/frames/000024.png), [000025.png](../episodes/e00-s00008-none-B0-r0/frames/000025.png), [000026.png](../episodes/e00-s00008-none-B0-r0/frames/000026.png), [000027.png](../episodes/e00-s00008-none-B0-r0/frames/000027.png), [000028.png](../episodes/e00-s00008-none-B0-r0/frames/000028.png), [000029.png](../episodes/e00-s00008-none-B0-r0/frames/000029.png), [000030.png](../episodes/e00-s00008-none-B0-r0/frames/000030.png), [000031.png](../episodes/e00-s00008-none-B0-r0/frames/000031.png), [000032.png](../episodes/e00-s00008-none-B0-r0/frames/000032.png), [000033.png](../episodes/e00-s00008-none-B0-r0/frames/000033.png), [000034.png](../episodes/e00-s00008-none-B0-r0/frames/000034.png), [000035.png](../episodes/e00-s00008-none-B0-r0/frames/000035.png), [000036.png](../episodes/e00-s00008-none-B0-r0/frames/000036.png), [start.png](../episodes/e00-s00008-none-B0-r0/start.png), [replay.gif](../episodes/e00-s00008-none-B0-r0/replay.gif)

## Outcome distribution

- development · MiniGrid-DoorKey-8x8-v0 · none — budget_timeout: 21, success: 19

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `memory-doorkey-v2-dev-20261114`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/memory-doorkey-v2-dev-20261114/manifest.json`. Source `7139195042f97cbf2b519e1359c342acfbb4c0e4`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-doorkey-v2-dev-20261114" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-doorkey-v2-dev-20261114/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

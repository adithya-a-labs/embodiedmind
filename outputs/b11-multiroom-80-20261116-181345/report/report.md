# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes b11-multiroom-80. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 150 of 150 cells were attempted, 150 validated, 0 excluded and 150 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 80.000 | 28420.500 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 80.000 | 28420.700 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 80.000 | 50585.800 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 49.800 | 22073.700 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 49.800 | 21515.900 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 80.000 | 43887.500 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 80.000 | 47274.000 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 80.000 | 48085.900 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 80.000 | 29109.800 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 80.000 | 34831.600 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 80.000 | 34831.600 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 80.000 | 34831.600 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 80.000 | 34893.200 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B9 | 10 | 10 | 10 | 0.000 | 80.000 | 34712.100 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 80.000 | 34712.100 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | total_tokens | B11 − B10 | 10 | -557.800 | [-627.100, -495.900] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.148 | [-0.466, 0.221] |

## Cost per completed mission

Costs sum across every valid episode, including failures. A dash means zero completions.

| Environment | Intervention | Agent | Completions | Actions / completion | Tokens / completion | Seconds / completion |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| MiniGrid-MultiRoom-N6-v0 | none | B0 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B0G | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B1 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B10 | 10 | 49.80 | 22073.70 | 15.59 |
| MiniGrid-MultiRoom-N6-v0 | none | B11 | 10 | 49.80 | 21515.90 | 15.45 |
| MiniGrid-MultiRoom-N6-v0 | none | B2 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B3 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B3G | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B4 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B5 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B7 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B8 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B9 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B9N | 0 | — | — | — |

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

- b11-multiroom-80 · MiniGrid-MultiRoom-N6-v0 · none · B0 seed 11001 · budget_timeout (80 steps). Trace at `episodes/e00-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11001-none-B0-r0/finish.png), [000000.png](../episodes/e00-s11001-none-B0-r0/frames/000000.png), [000001.png](../episodes/e00-s11001-none-B0-r0/frames/000001.png), [000002.png](../episodes/e00-s11001-none-B0-r0/frames/000002.png), [000003.png](../episodes/e00-s11001-none-B0-r0/frames/000003.png), [000004.png](../episodes/e00-s11001-none-B0-r0/frames/000004.png), [000005.png](../episodes/e00-s11001-none-B0-r0/frames/000005.png), [000006.png](../episodes/e00-s11001-none-B0-r0/frames/000006.png), [000007.png](../episodes/e00-s11001-none-B0-r0/frames/000007.png), [000008.png](../episodes/e00-s11001-none-B0-r0/frames/000008.png), [000009.png](../episodes/e00-s11001-none-B0-r0/frames/000009.png), [000010.png](../episodes/e00-s11001-none-B0-r0/frames/000010.png), [000011.png](../episodes/e00-s11001-none-B0-r0/frames/000011.png), [000012.png](../episodes/e00-s11001-none-B0-r0/frames/000012.png), [000013.png](../episodes/e00-s11001-none-B0-r0/frames/000013.png), [000014.png](../episodes/e00-s11001-none-B0-r0/frames/000014.png), [000015.png](../episodes/e00-s11001-none-B0-r0/frames/000015.png), [000016.png](../episodes/e00-s11001-none-B0-r0/frames/000016.png), [000017.png](../episodes/e00-s11001-none-B0-r0/frames/000017.png), [000018.png](../episodes/e00-s11001-none-B0-r0/frames/000018.png), [000019.png](../episodes/e00-s11001-none-B0-r0/frames/000019.png), [000020.png](../episodes/e00-s11001-none-B0-r0/frames/000020.png), [000021.png](../episodes/e00-s11001-none-B0-r0/frames/000021.png), [000022.png](../episodes/e00-s11001-none-B0-r0/frames/000022.png), [000023.png](../episodes/e00-s11001-none-B0-r0/frames/000023.png), [000024.png](../episodes/e00-s11001-none-B0-r0/frames/000024.png), [000025.png](../episodes/e00-s11001-none-B0-r0/frames/000025.png), [000026.png](../episodes/e00-s11001-none-B0-r0/frames/000026.png), [000027.png](../episodes/e00-s11001-none-B0-r0/frames/000027.png), [000028.png](../episodes/e00-s11001-none-B0-r0/frames/000028.png), [000029.png](../episodes/e00-s11001-none-B0-r0/frames/000029.png), [000030.png](../episodes/e00-s11001-none-B0-r0/frames/000030.png), [000031.png](../episodes/e00-s11001-none-B0-r0/frames/000031.png), [000032.png](../episodes/e00-s11001-none-B0-r0/frames/000032.png), [000033.png](../episodes/e00-s11001-none-B0-r0/frames/000033.png), [000034.png](../episodes/e00-s11001-none-B0-r0/frames/000034.png), [000035.png](../episodes/e00-s11001-none-B0-r0/frames/000035.png), [000036.png](../episodes/e00-s11001-none-B0-r0/frames/000036.png), [000037.png](../episodes/e00-s11001-none-B0-r0/frames/000037.png), [000038.png](../episodes/e00-s11001-none-B0-r0/frames/000038.png), [000039.png](../episodes/e00-s11001-none-B0-r0/frames/000039.png), [000040.png](../episodes/e00-s11001-none-B0-r0/frames/000040.png), [000041.png](../episodes/e00-s11001-none-B0-r0/frames/000041.png), [000042.png](../episodes/e00-s11001-none-B0-r0/frames/000042.png), [000043.png](../episodes/e00-s11001-none-B0-r0/frames/000043.png), [000044.png](../episodes/e00-s11001-none-B0-r0/frames/000044.png), [000045.png](../episodes/e00-s11001-none-B0-r0/frames/000045.png), [000046.png](../episodes/e00-s11001-none-B0-r0/frames/000046.png), [000047.png](../episodes/e00-s11001-none-B0-r0/frames/000047.png), [000048.png](../episodes/e00-s11001-none-B0-r0/frames/000048.png), [000049.png](../episodes/e00-s11001-none-B0-r0/frames/000049.png), [000050.png](../episodes/e00-s11001-none-B0-r0/frames/000050.png), [000051.png](../episodes/e00-s11001-none-B0-r0/frames/000051.png), [000052.png](../episodes/e00-s11001-none-B0-r0/frames/000052.png), [000053.png](../episodes/e00-s11001-none-B0-r0/frames/000053.png), [000054.png](../episodes/e00-s11001-none-B0-r0/frames/000054.png), [000055.png](../episodes/e00-s11001-none-B0-r0/frames/000055.png), [000056.png](../episodes/e00-s11001-none-B0-r0/frames/000056.png), [000057.png](../episodes/e00-s11001-none-B0-r0/frames/000057.png), [000058.png](../episodes/e00-s11001-none-B0-r0/frames/000058.png), [000059.png](../episodes/e00-s11001-none-B0-r0/frames/000059.png), [000060.png](../episodes/e00-s11001-none-B0-r0/frames/000060.png), [000061.png](../episodes/e00-s11001-none-B0-r0/frames/000061.png), [000062.png](../episodes/e00-s11001-none-B0-r0/frames/000062.png), [000063.png](../episodes/e00-s11001-none-B0-r0/frames/000063.png), [000064.png](../episodes/e00-s11001-none-B0-r0/frames/000064.png), [000065.png](../episodes/e00-s11001-none-B0-r0/frames/000065.png), [000066.png](../episodes/e00-s11001-none-B0-r0/frames/000066.png), [000067.png](../episodes/e00-s11001-none-B0-r0/frames/000067.png), [000068.png](../episodes/e00-s11001-none-B0-r0/frames/000068.png), [000069.png](../episodes/e00-s11001-none-B0-r0/frames/000069.png), [000070.png](../episodes/e00-s11001-none-B0-r0/frames/000070.png), [000071.png](../episodes/e00-s11001-none-B0-r0/frames/000071.png), [000072.png](../episodes/e00-s11001-none-B0-r0/frames/000072.png), [000073.png](../episodes/e00-s11001-none-B0-r0/frames/000073.png), [000074.png](../episodes/e00-s11001-none-B0-r0/frames/000074.png), [000075.png](../episodes/e00-s11001-none-B0-r0/frames/000075.png), [000076.png](../episodes/e00-s11001-none-B0-r0/frames/000076.png), [000077.png](../episodes/e00-s11001-none-B0-r0/frames/000077.png), [000078.png](../episodes/e00-s11001-none-B0-r0/frames/000078.png), [000079.png](../episodes/e00-s11001-none-B0-r0/frames/000079.png), [000080.png](../episodes/e00-s11001-none-B0-r0/frames/000080.png), [start.png](../episodes/e00-s11001-none-B0-r0/start.png), [replay.gif](../episodes/e00-s11001-none-B0-r0/replay.gif)

## Outcome distribution

- b11-multiroom-80 · MiniGrid-MultiRoom-N6-v0 · none — budget_timeout: 130, success: 20

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `b11-multiroom-80-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-multiroom-80-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-multiroom-80-20261116-181345" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-multiroom-80-20261116-181345/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

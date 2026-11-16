# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes development. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 40 of 40 cells were attempted, 40 validated, 0 excluded and 40 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| development | EmbodiedMind-GoToShift-v0 | relocation | B0 | 5 | 5 | 5 | 1.000 | 27.200 | 8832.000 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B1 | 5 | 5 | 5 | 1.000 | 27.600 | 15210.200 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B2 | 5 | 5 | 5 | 0.400 | 40.200 | 25810.600 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B3 | 5 | 5 | 5 | 1.000 | 27.200 | 17063.400 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B4 | 5 | 5 | 5 | 1.000 | 27.200 | 9911.200 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B5 | 5 | 5 | 5 | 1.000 | 17.800 | 7092.400 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B6 | 5 | 5 | 5 | 1.000 | 17.800 | 7092.400 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B7 | 5 | 5 | 5 | 1.000 | 17.800 | 7092.400 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| development | EmbodiedMind-GoToShift-v0 | relocation | success | B5 − B4 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | blocked_actions | B5 − B4 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | verification_requests | B5 − B4 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | success | B6 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | blocked_actions | B6 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | verification_requests | B6 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | success | B7 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | blocked_actions | B7 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | verification_requests | B7 − B5 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | success | B6 − B7 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | blocked_actions | B6 − B7 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | verification_requests | B6 − B7 | 5 | 0.000 | [0.000, 0.000] |

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

- development · EmbodiedMind-GoToShift-v0 · relocation · B2 seed 5 · budget_timeout (48 steps). Trace at `episodes/e00-s00005-relocation-B2-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s00005-relocation-B2-r0/finish.png), [000000.png](../episodes/e00-s00005-relocation-B2-r0/frames/000000.png), [000001.png](../episodes/e00-s00005-relocation-B2-r0/frames/000001.png), [000002.png](../episodes/e00-s00005-relocation-B2-r0/frames/000002.png), [000003.png](../episodes/e00-s00005-relocation-B2-r0/frames/000003.png), [000004.png](../episodes/e00-s00005-relocation-B2-r0/frames/000004.png), [000005.png](../episodes/e00-s00005-relocation-B2-r0/frames/000005.png), [000006.png](../episodes/e00-s00005-relocation-B2-r0/frames/000006.png), [000007.png](../episodes/e00-s00005-relocation-B2-r0/frames/000007.png), [000008.png](../episodes/e00-s00005-relocation-B2-r0/frames/000008.png), [000009.png](../episodes/e00-s00005-relocation-B2-r0/frames/000009.png), [000010.png](../episodes/e00-s00005-relocation-B2-r0/frames/000010.png), [000011.png](../episodes/e00-s00005-relocation-B2-r0/frames/000011.png), [000012.png](../episodes/e00-s00005-relocation-B2-r0/frames/000012.png), [000013.png](../episodes/e00-s00005-relocation-B2-r0/frames/000013.png), [000014.png](../episodes/e00-s00005-relocation-B2-r0/frames/000014.png), [000015.png](../episodes/e00-s00005-relocation-B2-r0/frames/000015.png), [000016.png](../episodes/e00-s00005-relocation-B2-r0/frames/000016.png), [000017.png](../episodes/e00-s00005-relocation-B2-r0/frames/000017.png), [000018.png](../episodes/e00-s00005-relocation-B2-r0/frames/000018.png), [000019.png](../episodes/e00-s00005-relocation-B2-r0/frames/000019.png), [000020.png](../episodes/e00-s00005-relocation-B2-r0/frames/000020.png), [000021.png](../episodes/e00-s00005-relocation-B2-r0/frames/000021.png), [000022.png](../episodes/e00-s00005-relocation-B2-r0/frames/000022.png), [000023.png](../episodes/e00-s00005-relocation-B2-r0/frames/000023.png), [000024.png](../episodes/e00-s00005-relocation-B2-r0/frames/000024.png), [000025.png](../episodes/e00-s00005-relocation-B2-r0/frames/000025.png), [000026.png](../episodes/e00-s00005-relocation-B2-r0/frames/000026.png), [000027.png](../episodes/e00-s00005-relocation-B2-r0/frames/000027.png), [000028.png](../episodes/e00-s00005-relocation-B2-r0/frames/000028.png), [000029.png](../episodes/e00-s00005-relocation-B2-r0/frames/000029.png), [000030.png](../episodes/e00-s00005-relocation-B2-r0/frames/000030.png), [000031.png](../episodes/e00-s00005-relocation-B2-r0/frames/000031.png), [000032.png](../episodes/e00-s00005-relocation-B2-r0/frames/000032.png), [000033.png](../episodes/e00-s00005-relocation-B2-r0/frames/000033.png), [000034.png](../episodes/e00-s00005-relocation-B2-r0/frames/000034.png), [000035.png](../episodes/e00-s00005-relocation-B2-r0/frames/000035.png), [000036.png](../episodes/e00-s00005-relocation-B2-r0/frames/000036.png), [000037.png](../episodes/e00-s00005-relocation-B2-r0/frames/000037.png), [000038.png](../episodes/e00-s00005-relocation-B2-r0/frames/000038.png), [000039.png](../episodes/e00-s00005-relocation-B2-r0/frames/000039.png), [000040.png](../episodes/e00-s00005-relocation-B2-r0/frames/000040.png), [000041.png](../episodes/e00-s00005-relocation-B2-r0/frames/000041.png), [000042.png](../episodes/e00-s00005-relocation-B2-r0/frames/000042.png), [000043.png](../episodes/e00-s00005-relocation-B2-r0/frames/000043.png), [000044.png](../episodes/e00-s00005-relocation-B2-r0/frames/000044.png), [000045.png](../episodes/e00-s00005-relocation-B2-r0/frames/000045.png), [000046.png](../episodes/e00-s00005-relocation-B2-r0/frames/000046.png), [000047.png](../episodes/e00-s00005-relocation-B2-r0/frames/000047.png), [000048.png](../episodes/e00-s00005-relocation-B2-r0/frames/000048.png), [start.png](../episodes/e00-s00005-relocation-B2-r0/start.png), [replay.gif](../episodes/e00-s00005-relocation-B2-r0/replay.gif)

## Outcome distribution

- development · EmbodiedMind-GoToShift-v0 · relocation — budget_timeout: 3, success: 37

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `memory-relocation-all-48-20261114-123128`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/memory-relocation-all-48-20261114-123128/manifest.json`. Source `c189ad8212bab6f339ad594ef76c4bf9d5184225`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-relocation-all-48-20261114-123128" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-relocation-all-48-20261114-123128/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes development. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 10 of 10 cells were attempted, 10 validated, 0 excluded and 10 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| development | EmbodiedMind-GoToShift-v0 | relocation | B4 | 5 | 5 | 5 | 0.000 | 24.000 | 8621.400 | — |
| development | EmbodiedMind-GoToShift-v0 | relocation | B5 | 5 | 5 | 5 | 0.800 | 14.800 | 5746.200 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| development | EmbodiedMind-GoToShift-v0 | relocation | success | B5 − B4 | 5 | 0.800 | [0.400, 1.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | blocked_actions | B5 − B4 | 5 | 0.000 | [0.000, 0.000] |
| development | EmbodiedMind-GoToShift-v0 | relocation | verification_requests | B5 − B4 | 5 | 0.000 | [0.000, 0.000] |

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

- development · EmbodiedMind-GoToShift-v0 · relocation · B4 seed 5 · budget_timeout (24 steps). Trace at `episodes/e00-s00005-relocation-B4-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s00005-relocation-B4-r0/finish.png), [000000.png](../episodes/e00-s00005-relocation-B4-r0/frames/000000.png), [000001.png](../episodes/e00-s00005-relocation-B4-r0/frames/000001.png), [000002.png](../episodes/e00-s00005-relocation-B4-r0/frames/000002.png), [000003.png](../episodes/e00-s00005-relocation-B4-r0/frames/000003.png), [000004.png](../episodes/e00-s00005-relocation-B4-r0/frames/000004.png), [000005.png](../episodes/e00-s00005-relocation-B4-r0/frames/000005.png), [000006.png](../episodes/e00-s00005-relocation-B4-r0/frames/000006.png), [000007.png](../episodes/e00-s00005-relocation-B4-r0/frames/000007.png), [000008.png](../episodes/e00-s00005-relocation-B4-r0/frames/000008.png), [000009.png](../episodes/e00-s00005-relocation-B4-r0/frames/000009.png), [000010.png](../episodes/e00-s00005-relocation-B4-r0/frames/000010.png), [000011.png](../episodes/e00-s00005-relocation-B4-r0/frames/000011.png), [000012.png](../episodes/e00-s00005-relocation-B4-r0/frames/000012.png), [000013.png](../episodes/e00-s00005-relocation-B4-r0/frames/000013.png), [000014.png](../episodes/e00-s00005-relocation-B4-r0/frames/000014.png), [000015.png](../episodes/e00-s00005-relocation-B4-r0/frames/000015.png), [000016.png](../episodes/e00-s00005-relocation-B4-r0/frames/000016.png), [000017.png](../episodes/e00-s00005-relocation-B4-r0/frames/000017.png), [000018.png](../episodes/e00-s00005-relocation-B4-r0/frames/000018.png), [000019.png](../episodes/e00-s00005-relocation-B4-r0/frames/000019.png), [000020.png](../episodes/e00-s00005-relocation-B4-r0/frames/000020.png), [000021.png](../episodes/e00-s00005-relocation-B4-r0/frames/000021.png), [000022.png](../episodes/e00-s00005-relocation-B4-r0/frames/000022.png), [000023.png](../episodes/e00-s00005-relocation-B4-r0/frames/000023.png), [000024.png](../episodes/e00-s00005-relocation-B4-r0/frames/000024.png), [start.png](../episodes/e00-s00005-relocation-B4-r0/start.png), [replay.gif](../episodes/e00-s00005-relocation-B4-r0/replay.gif)

## Outcome distribution

- development · EmbodiedMind-GoToShift-v0 · relocation — budget_timeout: 6, success: 4

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `memory-relocation-live-20261114-120338`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/memory-relocation-live-20261114-120338/manifest.json`. Source `e97e6b26eb870ebf958fa4fcf853df33737fbe96`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-relocation-live-20261114-120338" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/memory-relocation-live-20261114-120338/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

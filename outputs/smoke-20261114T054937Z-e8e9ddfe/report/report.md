# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes smoke. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 1 of 1 cells were attempted, 1 validated, 0 excluded and 1 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| smoke | BabyAI-GoToObjS6-v1 | none | B0 | 1 | 1 | 1 | 1.000 | 7.000 | 2422.000 | — |

## Primary paired contrasts

The supplied runs contain no planned primary held-out contrasts.

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

No validated task failures were recorded in the supplied rows.

## Outcome distribution

- smoke · BabyAI-GoToObjS6-v1 · none — success: 1

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)

## Provenance and reproduction

- Run `smoke-20261114T054937Z-e8e9ddfe`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/smoke-20261114T054937Z-e8e9ddfe/manifest.json`. Source `995fbb2c0d47a812a57d4ab5b1bceb4e95ed889b`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/smoke-20261114T054937Z-e8e9ddfe" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/smoke-20261114T054937Z-e8e9ddfe/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

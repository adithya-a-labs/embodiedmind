# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes b11-broad. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 450 of 450 cells were attempted, 450 validated, 0 excluded and 451 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B0 | 10 | 10 | 10 | 1.000 | 32.300 | 10675.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B0G | 10 | 10 | 10 | 1.000 | 32.300 | 10675.500 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B1 | 10 | 10 | 10 | 1.000 | 36.000 | 20601.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B10 | 10 | 10 | 10 | 1.000 | 10.100 | 3807.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B11 | 10 | 10 | 10 | 1.000 | 10.100 | 3718.500 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B2 | 10 | 10 | 10 | 0.400 | 42.200 | 27568.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B3 | 10 | 10 | 10 | 1.000 | 32.300 | 20681.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B3G | 10 | 10 | 10 | 1.000 | 32.300 | 20663.400 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B4 | 10 | 10 | 10 | 1.000 | 32.500 | 11871.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B5 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B6 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B7 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B8 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B9 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B9N | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B0 | 10 | 10 | 10 | 1.000 | 32.300 | 10640.500 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B0G | 10 | 10 | 10 | 1.000 | 32.300 | 10641.100 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B1 | 10 | 10 | 10 | 1.000 | 34.100 | 19492.700 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B10 | 10 | 10 | 10 | 1.000 | 10.100 | 3753.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B11 | 10 | 10 | 10 | 1.000 | 10.100 | 3664.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B2 | 10 | 10 | 10 | 0.500 | 40.500 | 26237.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B3 | 10 | 10 | 10 | 1.000 | 32.300 | 20600.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B3G | 10 | 10 | 10 | 1.000 | 32.300 | 20593.400 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B4 | 10 | 10 | 10 | 1.000 | 32.300 | 11763.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B5 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B6 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B7 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B8 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B9 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B9N | 10 | 10 | 10 | 1.000 | 10.400 | 3779.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B0 | 10 | 10 | 10 | 1.000 | 26.400 | 8557.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B0G | 10 | 10 | 10 | 1.000 | 26.400 | 8557.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B1 | 10 | 10 | 10 | 0.900 | 29.500 | 16650.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B10 | 10 | 10 | 10 | 0.400 | 33.600 | 14265.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B11 | 10 | 10 | 10 | 0.400 | 33.600 | 13918.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B2 | 10 | 10 | 10 | 0.300 | 41.200 | 26733.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B3 | 10 | 10 | 10 | 0.900 | 28.500 | 17964.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B3G | 10 | 10 | 10 | 1.000 | 26.400 | 16514.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B4 | 10 | 10 | 10 | 1.000 | 26.400 | 9610.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B5 | 10 | 10 | 10 | 1.000 | 24.500 | 10087.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B6 | 10 | 10 | 10 | 1.000 | 24.500 | 10087.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B7 | 10 | 10 | 10 | 1.000 | 24.500 | 10087.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B8 | 10 | 10 | 10 | 0.800 | 25.600 | 10587.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B9 | 10 | 10 | 10 | 1.000 | 23.900 | 9820.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B9N | 10 | 10 | 10 | 1.000 | 23.900 | 9820.000 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11 − B10 | 10 | -89.100 | [-91.300, -88.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11 − B10 | 10 | 0.300 | [0.000, 0.800] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11 − B10 | 10 | 0.200 | [0.000, 0.500] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11 − B10 | 10 | -0.041 | [-0.106, 0.034] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11 − B10 | 10 | -89.100 | [-91.300, -88.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11 − B10 | 10 | -0.032 | [-0.082, 0.020] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11 − B10 | 10 | -346.600 | [-464.900, -228.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11 − B10 | 10 | 0.104 | [-0.079, 0.311] |

## Cost per completed mission

Costs sum across every valid episode, including failures. A dash means zero completions.

| Environment | Intervention | Agent | Completions | Actions / completion | Tokens / completion | Seconds / completion |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| EmbodiedMind-GoToShift-v0 | dropout | B0 | 10 | 32.30 | 10675.30 | 5.25 |
| EmbodiedMind-GoToShift-v0 | dropout | B0G | 10 | 32.30 | 10675.50 | 5.09 |
| EmbodiedMind-GoToShift-v0 | dropout | B1 | 10 | 36.00 | 20601.60 | 8.26 |
| EmbodiedMind-GoToShift-v0 | dropout | B10 | 10 | 10.10 | 3807.60 | 2.73 |
| EmbodiedMind-GoToShift-v0 | dropout | B11 | 10 | 10.10 | 3718.50 | 2.69 |
| EmbodiedMind-GoToShift-v0 | dropout | B2 | 4 | 105.50 | 68920.75 | 26.38 |
| EmbodiedMind-GoToShift-v0 | dropout | B3 | 10 | 32.30 | 20681.20 | 10.07 |
| EmbodiedMind-GoToShift-v0 | dropout | B3G | 10 | 32.30 | 20663.40 | 8.23 |
| EmbodiedMind-GoToShift-v0 | dropout | B4 | 10 | 32.50 | 11871.80 | 5.95 |
| EmbodiedMind-GoToShift-v0 | dropout | B5 | 10 | 10.30 | 3790.80 | 2.80 |
| EmbodiedMind-GoToShift-v0 | dropout | B6 | 10 | 10.30 | 3790.80 | 2.76 |
| EmbodiedMind-GoToShift-v0 | dropout | B7 | 10 | 10.30 | 3790.80 | 2.78 |
| EmbodiedMind-GoToShift-v0 | dropout | B8 | 10 | 10.30 | 3790.80 | 2.82 |
| EmbodiedMind-GoToShift-v0 | dropout | B9 | 10 | 10.30 | 3790.80 | 2.74 |
| EmbodiedMind-GoToShift-v0 | dropout | B9N | 10 | 10.30 | 3790.80 | 2.81 |
| EmbodiedMind-GoToShift-v0 | no_change | B0 | 10 | 32.30 | 10640.50 | 5.11 |
| EmbodiedMind-GoToShift-v0 | no_change | B0G | 10 | 32.30 | 10641.10 | 9.28 |
| EmbodiedMind-GoToShift-v0 | no_change | B1 | 10 | 34.10 | 19492.70 | 8.36 |
| EmbodiedMind-GoToShift-v0 | no_change | B10 | 10 | 10.10 | 3753.30 | 2.75 |
| EmbodiedMind-GoToShift-v0 | no_change | B11 | 10 | 10.10 | 3664.20 | 2.72 |
| EmbodiedMind-GoToShift-v0 | no_change | B2 | 5 | 81.00 | 52475.60 | 20.07 |
| EmbodiedMind-GoToShift-v0 | no_change | B3 | 10 | 32.30 | 20600.20 | 10.27 |
| EmbodiedMind-GoToShift-v0 | no_change | B3G | 10 | 32.30 | 20593.40 | 8.68 |
| EmbodiedMind-GoToShift-v0 | no_change | B4 | 10 | 32.30 | 11763.90 | 5.88 |
| EmbodiedMind-GoToShift-v0 | no_change | B5 | 10 | 10.50 | 3824.30 | 2.92 |
| EmbodiedMind-GoToShift-v0 | no_change | B6 | 10 | 10.50 | 3824.30 | 2.87 |
| EmbodiedMind-GoToShift-v0 | no_change | B7 | 10 | 10.50 | 3824.30 | 2.87 |
| EmbodiedMind-GoToShift-v0 | no_change | B8 | 10 | 10.50 | 3824.30 | 2.85 |
| EmbodiedMind-GoToShift-v0 | no_change | B9 | 10 | 10.50 | 3824.30 | 2.87 |
| EmbodiedMind-GoToShift-v0 | no_change | B9N | 10 | 10.40 | 3779.90 | 2.93 |
| EmbodiedMind-GoToShift-v0 | relocation | B0 | 10 | 26.40 | 8557.90 | 4.15 |
| EmbodiedMind-GoToShift-v0 | relocation | B0G | 10 | 26.40 | 8557.60 | 4.28 |
| EmbodiedMind-GoToShift-v0 | relocation | B1 | 9 | 32.78 | 18500.67 | 8.62 |
| EmbodiedMind-GoToShift-v0 | relocation | B10 | 4 | 84.00 | 35663.00 | 24.02 |
| EmbodiedMind-GoToShift-v0 | relocation | B11 | 4 | 84.00 | 34796.50 | 24.28 |
| EmbodiedMind-GoToShift-v0 | relocation | B2 | 3 | 137.33 | 89110.00 | 29.77 |
| EmbodiedMind-GoToShift-v0 | relocation | B3 | 9 | 31.67 | 19960.00 | 9.95 |
| EmbodiedMind-GoToShift-v0 | relocation | B3G | 10 | 26.40 | 16514.20 | 6.68 |
| EmbodiedMind-GoToShift-v0 | relocation | B4 | 10 | 26.40 | 9610.00 | 4.90 |
| EmbodiedMind-GoToShift-v0 | relocation | B5 | 10 | 24.50 | 10087.90 | 6.98 |
| EmbodiedMind-GoToShift-v0 | relocation | B6 | 10 | 24.50 | 10087.90 | 7.07 |
| EmbodiedMind-GoToShift-v0 | relocation | B7 | 10 | 24.50 | 10087.90 | 7.03 |
| EmbodiedMind-GoToShift-v0 | relocation | B8 | 8 | 32.00 | 13234.75 | 8.98 |
| EmbodiedMind-GoToShift-v0 | relocation | B9 | 10 | 23.90 | 9820.00 | 6.72 |
| EmbodiedMind-GoToShift-v0 | relocation | B9N | 10 | 23.90 | 9820.00 | 6.79 |

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

- b11-broad · EmbodiedMind-GoToShift-v0 · dropout · B2 seed 11001 · budget_timeout (48 steps). Trace at `episodes/e00-s11001-dropout-B2-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11001-dropout-B2-r0/finish.png), [000000.png](../episodes/e00-s11001-dropout-B2-r0/frames/000000.png), [000001.png](../episodes/e00-s11001-dropout-B2-r0/frames/000001.png), [000002.png](../episodes/e00-s11001-dropout-B2-r0/frames/000002.png), [000003.png](../episodes/e00-s11001-dropout-B2-r0/frames/000003.png), [000004.png](../episodes/e00-s11001-dropout-B2-r0/frames/000004.png), [000005.png](../episodes/e00-s11001-dropout-B2-r0/frames/000005.png), [000006.png](../episodes/e00-s11001-dropout-B2-r0/frames/000006.png), [000007.png](../episodes/e00-s11001-dropout-B2-r0/frames/000007.png), [000008.png](../episodes/e00-s11001-dropout-B2-r0/frames/000008.png), [000009.png](../episodes/e00-s11001-dropout-B2-r0/frames/000009.png), [000010.png](../episodes/e00-s11001-dropout-B2-r0/frames/000010.png), [000011.png](../episodes/e00-s11001-dropout-B2-r0/frames/000011.png), [000012.png](../episodes/e00-s11001-dropout-B2-r0/frames/000012.png), [000013.png](../episodes/e00-s11001-dropout-B2-r0/frames/000013.png), [000014.png](../episodes/e00-s11001-dropout-B2-r0/frames/000014.png), [000015.png](../episodes/e00-s11001-dropout-B2-r0/frames/000015.png), [000016.png](../episodes/e00-s11001-dropout-B2-r0/frames/000016.png), [000017.png](../episodes/e00-s11001-dropout-B2-r0/frames/000017.png), [000018.png](../episodes/e00-s11001-dropout-B2-r0/frames/000018.png), [000019.png](../episodes/e00-s11001-dropout-B2-r0/frames/000019.png), [000020.png](../episodes/e00-s11001-dropout-B2-r0/frames/000020.png), [000021.png](../episodes/e00-s11001-dropout-B2-r0/frames/000021.png), [000022.png](../episodes/e00-s11001-dropout-B2-r0/frames/000022.png), [000023.png](../episodes/e00-s11001-dropout-B2-r0/frames/000023.png), [000024.png](../episodes/e00-s11001-dropout-B2-r0/frames/000024.png), [000025.png](../episodes/e00-s11001-dropout-B2-r0/frames/000025.png), [000026.png](../episodes/e00-s11001-dropout-B2-r0/frames/000026.png), [000027.png](../episodes/e00-s11001-dropout-B2-r0/frames/000027.png), [000028.png](../episodes/e00-s11001-dropout-B2-r0/frames/000028.png), [000029.png](../episodes/e00-s11001-dropout-B2-r0/frames/000029.png), [000030.png](../episodes/e00-s11001-dropout-B2-r0/frames/000030.png), [000031.png](../episodes/e00-s11001-dropout-B2-r0/frames/000031.png), [000032.png](../episodes/e00-s11001-dropout-B2-r0/frames/000032.png), [000033.png](../episodes/e00-s11001-dropout-B2-r0/frames/000033.png), [000034.png](../episodes/e00-s11001-dropout-B2-r0/frames/000034.png), [000035.png](../episodes/e00-s11001-dropout-B2-r0/frames/000035.png), [000036.png](../episodes/e00-s11001-dropout-B2-r0/frames/000036.png), [000037.png](../episodes/e00-s11001-dropout-B2-r0/frames/000037.png), [000038.png](../episodes/e00-s11001-dropout-B2-r0/frames/000038.png), [000039.png](../episodes/e00-s11001-dropout-B2-r0/frames/000039.png), [000040.png](../episodes/e00-s11001-dropout-B2-r0/frames/000040.png), [000041.png](../episodes/e00-s11001-dropout-B2-r0/frames/000041.png), [000042.png](../episodes/e00-s11001-dropout-B2-r0/frames/000042.png), [000043.png](../episodes/e00-s11001-dropout-B2-r0/frames/000043.png), [000044.png](../episodes/e00-s11001-dropout-B2-r0/frames/000044.png), [000045.png](../episodes/e00-s11001-dropout-B2-r0/frames/000045.png), [000046.png](../episodes/e00-s11001-dropout-B2-r0/frames/000046.png), [000047.png](../episodes/e00-s11001-dropout-B2-r0/frames/000047.png), [000048.png](../episodes/e00-s11001-dropout-B2-r0/frames/000048.png), [start.png](../episodes/e00-s11001-dropout-B2-r0/start.png), [replay.gif](../episodes/e00-s11001-dropout-B2-r0/replay.gif)
- b11-broad · EmbodiedMind-GoToShift-v0 · no_change · B2 seed 11001 · budget_timeout (48 steps). Trace at `episodes/e00-s11001-no_change-B2-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11001-no_change-B2-r0/finish.png), [000000.png](../episodes/e00-s11001-no_change-B2-r0/frames/000000.png), [000001.png](../episodes/e00-s11001-no_change-B2-r0/frames/000001.png), [000002.png](../episodes/e00-s11001-no_change-B2-r0/frames/000002.png), [000003.png](../episodes/e00-s11001-no_change-B2-r0/frames/000003.png), [000004.png](../episodes/e00-s11001-no_change-B2-r0/frames/000004.png), [000005.png](../episodes/e00-s11001-no_change-B2-r0/frames/000005.png), [000006.png](../episodes/e00-s11001-no_change-B2-r0/frames/000006.png), [000007.png](../episodes/e00-s11001-no_change-B2-r0/frames/000007.png), [000008.png](../episodes/e00-s11001-no_change-B2-r0/frames/000008.png), [000009.png](../episodes/e00-s11001-no_change-B2-r0/frames/000009.png), [000010.png](../episodes/e00-s11001-no_change-B2-r0/frames/000010.png), [000011.png](../episodes/e00-s11001-no_change-B2-r0/frames/000011.png), [000012.png](../episodes/e00-s11001-no_change-B2-r0/frames/000012.png), [000013.png](../episodes/e00-s11001-no_change-B2-r0/frames/000013.png), [000014.png](../episodes/e00-s11001-no_change-B2-r0/frames/000014.png), [000015.png](../episodes/e00-s11001-no_change-B2-r0/frames/000015.png), [000016.png](../episodes/e00-s11001-no_change-B2-r0/frames/000016.png), [000017.png](../episodes/e00-s11001-no_change-B2-r0/frames/000017.png), [000018.png](../episodes/e00-s11001-no_change-B2-r0/frames/000018.png), [000019.png](../episodes/e00-s11001-no_change-B2-r0/frames/000019.png), [000020.png](../episodes/e00-s11001-no_change-B2-r0/frames/000020.png), [000021.png](../episodes/e00-s11001-no_change-B2-r0/frames/000021.png), [000022.png](../episodes/e00-s11001-no_change-B2-r0/frames/000022.png), [000023.png](../episodes/e00-s11001-no_change-B2-r0/frames/000023.png), [000024.png](../episodes/e00-s11001-no_change-B2-r0/frames/000024.png), [000025.png](../episodes/e00-s11001-no_change-B2-r0/frames/000025.png), [000026.png](../episodes/e00-s11001-no_change-B2-r0/frames/000026.png), [000027.png](../episodes/e00-s11001-no_change-B2-r0/frames/000027.png), [000028.png](../episodes/e00-s11001-no_change-B2-r0/frames/000028.png), [000029.png](../episodes/e00-s11001-no_change-B2-r0/frames/000029.png), [000030.png](../episodes/e00-s11001-no_change-B2-r0/frames/000030.png), [000031.png](../episodes/e00-s11001-no_change-B2-r0/frames/000031.png), [000032.png](../episodes/e00-s11001-no_change-B2-r0/frames/000032.png), [000033.png](../episodes/e00-s11001-no_change-B2-r0/frames/000033.png), [000034.png](../episodes/e00-s11001-no_change-B2-r0/frames/000034.png), [000035.png](../episodes/e00-s11001-no_change-B2-r0/frames/000035.png), [000036.png](../episodes/e00-s11001-no_change-B2-r0/frames/000036.png), [000037.png](../episodes/e00-s11001-no_change-B2-r0/frames/000037.png), [000038.png](../episodes/e00-s11001-no_change-B2-r0/frames/000038.png), [000039.png](../episodes/e00-s11001-no_change-B2-r0/frames/000039.png), [000040.png](../episodes/e00-s11001-no_change-B2-r0/frames/000040.png), [000041.png](../episodes/e00-s11001-no_change-B2-r0/frames/000041.png), [000042.png](../episodes/e00-s11001-no_change-B2-r0/frames/000042.png), [000043.png](../episodes/e00-s11001-no_change-B2-r0/frames/000043.png), [000044.png](../episodes/e00-s11001-no_change-B2-r0/frames/000044.png), [000045.png](../episodes/e00-s11001-no_change-B2-r0/frames/000045.png), [000046.png](../episodes/e00-s11001-no_change-B2-r0/frames/000046.png), [000047.png](../episodes/e00-s11001-no_change-B2-r0/frames/000047.png), [000048.png](../episodes/e00-s11001-no_change-B2-r0/frames/000048.png), [start.png](../episodes/e00-s11001-no_change-B2-r0/start.png), [replay.gif](../episodes/e00-s11001-no_change-B2-r0/replay.gif)
- b11-broad · EmbodiedMind-GoToShift-v0 · relocation · B1 seed 11009 · budget_timeout (48 steps). Trace at `episodes/e00-s11009-relocation-B1-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11009-relocation-B1-r0/finish.png), [000000.png](../episodes/e00-s11009-relocation-B1-r0/frames/000000.png), [000001.png](../episodes/e00-s11009-relocation-B1-r0/frames/000001.png), [000002.png](../episodes/e00-s11009-relocation-B1-r0/frames/000002.png), [000003.png](../episodes/e00-s11009-relocation-B1-r0/frames/000003.png), [000004.png](../episodes/e00-s11009-relocation-B1-r0/frames/000004.png), [000005.png](../episodes/e00-s11009-relocation-B1-r0/frames/000005.png), [000006.png](../episodes/e00-s11009-relocation-B1-r0/frames/000006.png), [000007.png](../episodes/e00-s11009-relocation-B1-r0/frames/000007.png), [000008.png](../episodes/e00-s11009-relocation-B1-r0/frames/000008.png), [000009.png](../episodes/e00-s11009-relocation-B1-r0/frames/000009.png), [000010.png](../episodes/e00-s11009-relocation-B1-r0/frames/000010.png), [000011.png](../episodes/e00-s11009-relocation-B1-r0/frames/000011.png), [000012.png](../episodes/e00-s11009-relocation-B1-r0/frames/000012.png), [000013.png](../episodes/e00-s11009-relocation-B1-r0/frames/000013.png), [000014.png](../episodes/e00-s11009-relocation-B1-r0/frames/000014.png), [000015.png](../episodes/e00-s11009-relocation-B1-r0/frames/000015.png), [000016.png](../episodes/e00-s11009-relocation-B1-r0/frames/000016.png), [000017.png](../episodes/e00-s11009-relocation-B1-r0/frames/000017.png), [000018.png](../episodes/e00-s11009-relocation-B1-r0/frames/000018.png), [000019.png](../episodes/e00-s11009-relocation-B1-r0/frames/000019.png), [000020.png](../episodes/e00-s11009-relocation-B1-r0/frames/000020.png), [000021.png](../episodes/e00-s11009-relocation-B1-r0/frames/000021.png), [000022.png](../episodes/e00-s11009-relocation-B1-r0/frames/000022.png), [000023.png](../episodes/e00-s11009-relocation-B1-r0/frames/000023.png), [000024.png](../episodes/e00-s11009-relocation-B1-r0/frames/000024.png), [000025.png](../episodes/e00-s11009-relocation-B1-r0/frames/000025.png), [000026.png](../episodes/e00-s11009-relocation-B1-r0/frames/000026.png), [000027.png](../episodes/e00-s11009-relocation-B1-r0/frames/000027.png), [000028.png](../episodes/e00-s11009-relocation-B1-r0/frames/000028.png), [000029.png](../episodes/e00-s11009-relocation-B1-r0/frames/000029.png), [000030.png](../episodes/e00-s11009-relocation-B1-r0/frames/000030.png), [000031.png](../episodes/e00-s11009-relocation-B1-r0/frames/000031.png), [000032.png](../episodes/e00-s11009-relocation-B1-r0/frames/000032.png), [000033.png](../episodes/e00-s11009-relocation-B1-r0/frames/000033.png), [000034.png](../episodes/e00-s11009-relocation-B1-r0/frames/000034.png), [000035.png](../episodes/e00-s11009-relocation-B1-r0/frames/000035.png), [000036.png](../episodes/e00-s11009-relocation-B1-r0/frames/000036.png), [000037.png](../episodes/e00-s11009-relocation-B1-r0/frames/000037.png), [000038.png](../episodes/e00-s11009-relocation-B1-r0/frames/000038.png), [000039.png](../episodes/e00-s11009-relocation-B1-r0/frames/000039.png), [000040.png](../episodes/e00-s11009-relocation-B1-r0/frames/000040.png), [000041.png](../episodes/e00-s11009-relocation-B1-r0/frames/000041.png), [000042.png](../episodes/e00-s11009-relocation-B1-r0/frames/000042.png), [000043.png](../episodes/e00-s11009-relocation-B1-r0/frames/000043.png), [000044.png](../episodes/e00-s11009-relocation-B1-r0/frames/000044.png), [000045.png](../episodes/e00-s11009-relocation-B1-r0/frames/000045.png), [000046.png](../episodes/e00-s11009-relocation-B1-r0/frames/000046.png), [000047.png](../episodes/e00-s11009-relocation-B1-r0/frames/000047.png), [000048.png](../episodes/e00-s11009-relocation-B1-r0/frames/000048.png), [start.png](../episodes/e00-s11009-relocation-B1-r0/start.png), [replay.gif](../episodes/e00-s11009-relocation-B1-r0/replay.gif)

## Outcome distribution

- b11-broad · EmbodiedMind-GoToShift-v0 · dropout — budget_timeout: 6, success: 144
- b11-broad · EmbodiedMind-GoToShift-v0 · no_change — budget_timeout: 5, success: 145
- b11-broad · EmbodiedMind-GoToShift-v0 · relocation — budget_timeout: 23, success: 127

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `b11-shift-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-shift-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-shift-20261116-181345" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-shift-20261116-181345/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

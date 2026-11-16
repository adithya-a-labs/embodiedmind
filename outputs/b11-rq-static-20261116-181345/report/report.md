# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes b11-mechanisms. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 300 of 300 cells were attempted, 300 validated, 0 excluded and 300 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11 | 30 | 30 | 30 | 0.433 | 36.033 | 15423.433 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11C | 30 | 30 | 30 | 0.433 | 36.033 | 0.000 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11P | 30 | 30 | 30 | 0.433 | 36.033 | 15423.400 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11R | 30 | 30 | 30 | 0.433 | 36.033 | 15423.433 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11T | 30 | 30 | 30 | 0.433 | 36.033 | 23802.500 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11 | 30 | 30 | 30 | 0.967 | 19.567 | 8895.067 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11C | 30 | 30 | 30 | 0.967 | 19.567 | 0.000 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11P | 30 | 30 | 30 | 0.000 | 48.000 | 22523.267 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11R | 30 | 30 | 30 | 0.967 | 19.567 | 8895.067 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11T | 30 | 30 | 30 | 0.900 | 22.567 | 13820.833 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11P − B11T | 30 | -8379.100 | [-9971.167, -6698.367] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11P − B11T | 30 | -2.544 | [-3.164, -1.957] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11R − B11T | 30 | -8379.067 | [-9971.133, -6698.400] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11R − B11T | 30 | -2.562 | [-3.173, -1.985] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11R − B11P | 30 | 0.033 | [-0.067, 0.133] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11R − B11P | 30 | -0.018 | [-0.090, 0.057] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11 − B11R | 30 | 0.008 | [-0.065, 0.082] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11 − B11C | 30 | 36.033 | [29.933, 41.667] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11 − B11C | 30 | 15423.433 | [12848.133, 17818.500] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11 − B11C | 30 | 9.882 | [8.250, 11.395] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11P − B11T | 30 | -0.900 | [-1.000, -0.800] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11P − B11T | 30 | 25.433 | [21.267, 29.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11P − B11T | 30 | 25.433 | [21.267, 29.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11P − B11T | 30 | 8702.433 | [5645.600, 11353.967] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11P − B11T | 30 | 7.822 | [6.114, 9.330] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11R − B11T | 30 | 0.067 | [0.000, 0.167] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11R − B11T | 30 | -3.000 | [-5.933, -0.667] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11R − B11T | 30 | -3.000 | [-5.933, -0.667] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11R − B11T | 30 | -4925.767 | [-7162.200, -3103.833] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11R − B11T | 30 | -2.197 | [-3.288, -1.275] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11R − B11P | 30 | 0.967 | [0.900, 1.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11R − B11P | 30 | -28.433 | [-30.800, -25.600] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11R − B11P | 30 | -28.433 | [-30.800, -25.600] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11R − B11P | 30 | -13628.200 | [-14822.267, -12262.300] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11R − B11P | 30 | -10.018 | [-10.846, -9.100] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11 − B11R | 30 | -0.030 | [-0.110, 0.049] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11 − B11C | 30 | 19.567 | [17.200, 22.400] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11 − B11C | 30 | 8895.067 | [7865.533, 10111.833] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11 − B11C | 30 | 6.180 | [5.503, 6.975] |

## Cost per completed mission

Costs sum across every valid episode, including failures. A dash means zero completions.

| Environment | Intervention | Agent | Completions | Actions / completion | Tokens / completion | Seconds / completion |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| BabyAI-GoToObjMazeS7-v0 | none | B11 | 13 | 83.15 | 35592.54 | 23.91 |
| BabyAI-GoToObjMazeS7-v0 | none | B11C | 13 | 83.15 | 0.00 | 1.10 |
| BabyAI-GoToObjMazeS7-v0 | none | B11P | 13 | 83.15 | 35592.46 | 23.93 |
| BabyAI-GoToObjMazeS7-v0 | none | B11R | 13 | 83.15 | 35592.54 | 23.89 |
| BabyAI-GoToObjMazeS7-v0 | none | B11T | 13 | 83.15 | 54928.85 | 29.80 |
| MiniGrid-DoorKey-8x8-v0 | none | B11 | 29 | 20.24 | 9201.79 | 6.48 |
| MiniGrid-DoorKey-8x8-v0 | none | B11C | 29 | 20.24 | 0.00 | 0.09 |
| MiniGrid-DoorKey-8x8-v0 | none | B11P | 0 | — | — | — |
| MiniGrid-DoorKey-8x8-v0 | none | B11R | 29 | 20.24 | 9201.79 | 6.52 |
| MiniGrid-DoorKey-8x8-v0 | none | B11T | 27 | 25.07 | 15356.48 | 9.44 |

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

- b11-mechanisms · BabyAI-GoToObjMazeS7-v0 · none · B11 seed 11101 · budget_timeout (48 steps). Trace at `episodes/e01-s11101-none-B11-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e01-s11101-none-B11-r0/finish.png), [000000.png](../episodes/e01-s11101-none-B11-r0/frames/000000.png), [000001.png](../episodes/e01-s11101-none-B11-r0/frames/000001.png), [000002.png](../episodes/e01-s11101-none-B11-r0/frames/000002.png), [000003.png](../episodes/e01-s11101-none-B11-r0/frames/000003.png), [000004.png](../episodes/e01-s11101-none-B11-r0/frames/000004.png), [000005.png](../episodes/e01-s11101-none-B11-r0/frames/000005.png), [000006.png](../episodes/e01-s11101-none-B11-r0/frames/000006.png), [000007.png](../episodes/e01-s11101-none-B11-r0/frames/000007.png), [000008.png](../episodes/e01-s11101-none-B11-r0/frames/000008.png), [000009.png](../episodes/e01-s11101-none-B11-r0/frames/000009.png), [000010.png](../episodes/e01-s11101-none-B11-r0/frames/000010.png), [000011.png](../episodes/e01-s11101-none-B11-r0/frames/000011.png), [000012.png](../episodes/e01-s11101-none-B11-r0/frames/000012.png), [000013.png](../episodes/e01-s11101-none-B11-r0/frames/000013.png), [000014.png](../episodes/e01-s11101-none-B11-r0/frames/000014.png), [000015.png](../episodes/e01-s11101-none-B11-r0/frames/000015.png), [000016.png](../episodes/e01-s11101-none-B11-r0/frames/000016.png), [000017.png](../episodes/e01-s11101-none-B11-r0/frames/000017.png), [000018.png](../episodes/e01-s11101-none-B11-r0/frames/000018.png), [000019.png](../episodes/e01-s11101-none-B11-r0/frames/000019.png), [000020.png](../episodes/e01-s11101-none-B11-r0/frames/000020.png), [000021.png](../episodes/e01-s11101-none-B11-r0/frames/000021.png), [000022.png](../episodes/e01-s11101-none-B11-r0/frames/000022.png), [000023.png](../episodes/e01-s11101-none-B11-r0/frames/000023.png), [000024.png](../episodes/e01-s11101-none-B11-r0/frames/000024.png), [000025.png](../episodes/e01-s11101-none-B11-r0/frames/000025.png), [000026.png](../episodes/e01-s11101-none-B11-r0/frames/000026.png), [000027.png](../episodes/e01-s11101-none-B11-r0/frames/000027.png), [000028.png](../episodes/e01-s11101-none-B11-r0/frames/000028.png), [000029.png](../episodes/e01-s11101-none-B11-r0/frames/000029.png), [000030.png](../episodes/e01-s11101-none-B11-r0/frames/000030.png), [000031.png](../episodes/e01-s11101-none-B11-r0/frames/000031.png), [000032.png](../episodes/e01-s11101-none-B11-r0/frames/000032.png), [000033.png](../episodes/e01-s11101-none-B11-r0/frames/000033.png), [000034.png](../episodes/e01-s11101-none-B11-r0/frames/000034.png), [000035.png](../episodes/e01-s11101-none-B11-r0/frames/000035.png), [000036.png](../episodes/e01-s11101-none-B11-r0/frames/000036.png), [000037.png](../episodes/e01-s11101-none-B11-r0/frames/000037.png), [000038.png](../episodes/e01-s11101-none-B11-r0/frames/000038.png), [000039.png](../episodes/e01-s11101-none-B11-r0/frames/000039.png), [000040.png](../episodes/e01-s11101-none-B11-r0/frames/000040.png), [000041.png](../episodes/e01-s11101-none-B11-r0/frames/000041.png), [000042.png](../episodes/e01-s11101-none-B11-r0/frames/000042.png), [000043.png](../episodes/e01-s11101-none-B11-r0/frames/000043.png), [000044.png](../episodes/e01-s11101-none-B11-r0/frames/000044.png), [000045.png](../episodes/e01-s11101-none-B11-r0/frames/000045.png), [000046.png](../episodes/e01-s11101-none-B11-r0/frames/000046.png), [000047.png](../episodes/e01-s11101-none-B11-r0/frames/000047.png), [000048.png](../episodes/e01-s11101-none-B11-r0/frames/000048.png), [start.png](../episodes/e01-s11101-none-B11-r0/start.png), [replay.gif](../episodes/e01-s11101-none-B11-r0/replay.gif)
- b11-mechanisms · MiniGrid-DoorKey-8x8-v0 · none · B11 seed 11116 · budget_timeout (48 steps). Trace at `episodes/e00-s11116-none-B11-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11116-none-B11-r0/finish.png), [000000.png](../episodes/e00-s11116-none-B11-r0/frames/000000.png), [000001.png](../episodes/e00-s11116-none-B11-r0/frames/000001.png), [000002.png](../episodes/e00-s11116-none-B11-r0/frames/000002.png), [000003.png](../episodes/e00-s11116-none-B11-r0/frames/000003.png), [000004.png](../episodes/e00-s11116-none-B11-r0/frames/000004.png), [000005.png](../episodes/e00-s11116-none-B11-r0/frames/000005.png), [000006.png](../episodes/e00-s11116-none-B11-r0/frames/000006.png), [000007.png](../episodes/e00-s11116-none-B11-r0/frames/000007.png), [000008.png](../episodes/e00-s11116-none-B11-r0/frames/000008.png), [000009.png](../episodes/e00-s11116-none-B11-r0/frames/000009.png), [000010.png](../episodes/e00-s11116-none-B11-r0/frames/000010.png), [000011.png](../episodes/e00-s11116-none-B11-r0/frames/000011.png), [000012.png](../episodes/e00-s11116-none-B11-r0/frames/000012.png), [000013.png](../episodes/e00-s11116-none-B11-r0/frames/000013.png), [000014.png](../episodes/e00-s11116-none-B11-r0/frames/000014.png), [000015.png](../episodes/e00-s11116-none-B11-r0/frames/000015.png), [000016.png](../episodes/e00-s11116-none-B11-r0/frames/000016.png), [000017.png](../episodes/e00-s11116-none-B11-r0/frames/000017.png), [000018.png](../episodes/e00-s11116-none-B11-r0/frames/000018.png), [000019.png](../episodes/e00-s11116-none-B11-r0/frames/000019.png), [000020.png](../episodes/e00-s11116-none-B11-r0/frames/000020.png), [000021.png](../episodes/e00-s11116-none-B11-r0/frames/000021.png), [000022.png](../episodes/e00-s11116-none-B11-r0/frames/000022.png), [000023.png](../episodes/e00-s11116-none-B11-r0/frames/000023.png), [000024.png](../episodes/e00-s11116-none-B11-r0/frames/000024.png), [000025.png](../episodes/e00-s11116-none-B11-r0/frames/000025.png), [000026.png](../episodes/e00-s11116-none-B11-r0/frames/000026.png), [000027.png](../episodes/e00-s11116-none-B11-r0/frames/000027.png), [000028.png](../episodes/e00-s11116-none-B11-r0/frames/000028.png), [000029.png](../episodes/e00-s11116-none-B11-r0/frames/000029.png), [000030.png](../episodes/e00-s11116-none-B11-r0/frames/000030.png), [000031.png](../episodes/e00-s11116-none-B11-r0/frames/000031.png), [000032.png](../episodes/e00-s11116-none-B11-r0/frames/000032.png), [000033.png](../episodes/e00-s11116-none-B11-r0/frames/000033.png), [000034.png](../episodes/e00-s11116-none-B11-r0/frames/000034.png), [000035.png](../episodes/e00-s11116-none-B11-r0/frames/000035.png), [000036.png](../episodes/e00-s11116-none-B11-r0/frames/000036.png), [000037.png](../episodes/e00-s11116-none-B11-r0/frames/000037.png), [000038.png](../episodes/e00-s11116-none-B11-r0/frames/000038.png), [000039.png](../episodes/e00-s11116-none-B11-r0/frames/000039.png), [000040.png](../episodes/e00-s11116-none-B11-r0/frames/000040.png), [000041.png](../episodes/e00-s11116-none-B11-r0/frames/000041.png), [000042.png](../episodes/e00-s11116-none-B11-r0/frames/000042.png), [000043.png](../episodes/e00-s11116-none-B11-r0/frames/000043.png), [000044.png](../episodes/e00-s11116-none-B11-r0/frames/000044.png), [000045.png](../episodes/e00-s11116-none-B11-r0/frames/000045.png), [000046.png](../episodes/e00-s11116-none-B11-r0/frames/000046.png), [000047.png](../episodes/e00-s11116-none-B11-r0/frames/000047.png), [000048.png](../episodes/e00-s11116-none-B11-r0/frames/000048.png), [start.png](../episodes/e00-s11116-none-B11-r0/start.png), [replay.gif](../episodes/e00-s11116-none-B11-r0/replay.gif)

## Outcome distribution

- b11-mechanisms · BabyAI-GoToObjMazeS7-v0 · none — budget_timeout: 85, success: 65
- b11-mechanisms · MiniGrid-DoorKey-8x8-v0 · none — budget_timeout: 36, success: 114

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `b11-rq-static-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-static-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-static-20261116-181345" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-static-20261116-181345/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

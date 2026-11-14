# Verified-subgoal comparison

All variants used the same local model, one inference worker, a 768-byte memory allowance and 48-action and 48-call caps on each of five matched development seeds.

Each variant cell gives success count, mean actions across all episodes and mean total tokens.

| Game | B8 | B9N | B9 |
| --- | ---: | ---: | ---: |
| Key Corridor | 0/5 · 48.0 actions · 21,769 tokens | 0/5 · 48.0 actions · 21,595 tokens | 5/5 · 31.2 actions · 14,670 tokens |
| Put Next | 0/5 · 48.0 actions · 22,803 tokens | 0/5 · 48.0 actions · 22,679 tokens | 5/5 · 11.2 actions · 5,392 tokens |
| Randomized Memory | 5/5 · 16.2 actions · 8,134 tokens | 3/5 · 30.4 actions · 15,168 tokens | 5/5 · 13.0 actions · 6,561 tokens |

## Seed-level outcomes

| Game | Seed | B8 | B9N | B9 |
| --- | ---: | --- | --- | --- |
| Key Corridor | 3001 | budget timeout (48 actions) | budget timeout (48 actions) | success (28 actions) |
| Key Corridor | 3002 | budget timeout (48 actions) | budget timeout (48 actions) | success (27 actions) |
| Key Corridor | 3003 | budget timeout (48 actions) | budget timeout (48 actions) | success (41 actions) |
| Key Corridor | 3004 | budget timeout (48 actions) | budget timeout (48 actions) | success (32 actions) |
| Key Corridor | 3005 | budget timeout (48 actions) | budget timeout (48 actions) | success (28 actions) |
| Put Next | 3001 | budget timeout (48 actions) | budget timeout (48 actions) | success (12 actions) |
| Put Next | 3002 | budget timeout (48 actions) | budget timeout (48 actions) | success (10 actions) |
| Put Next | 3003 | budget timeout (48 actions) | budget timeout (48 actions) | success (14 actions) |
| Put Next | 3004 | budget timeout (48 actions) | budget timeout (48 actions) | success (8 actions) |
| Put Next | 3005 | budget timeout (48 actions) | budget timeout (48 actions) | success (12 actions) |
| Randomized Memory | 3001 | success (23 actions) | budget timeout (48 actions) | success (7 actions) |
| Randomized Memory | 3002 | success (14 actions) | success (16 actions) | success (14 actions) |
| Randomized Memory | 3003 | success (20 actions) | success (22 actions) | success (20 actions) |
| Randomized Memory | 3004 | success (8 actions) | budget timeout (48 actions) | success (8 actions) |
| Randomized Memory | 3005 | success (16 actions) | success (18 actions) | success (16 actions) |

## Evidence from the controller

- **Key Corridor, B9N.** progress aware explore 240.
- **Key Corridor, B9.** explore for subgoal 86, route to subgoal 45, attempt subgoal interaction 15, find key drop tile 5, release key after unlock 5.
- **Put Next, B9N.** progress aware explore 233, model or shared controller 5, forward burst 2.
- **Put Next, B9.** route to placement 25, route to subgoal 14, explore for subgoal 7, attempt subgoal interaction 5, attempt verified placement 5.
- **Randomized Memory, B9N.** progress aware explore 108, approach matching branch 24, scan start cue 20.
- **Randomized Memory, B9.** approach matching branch 35, search hallway 25, inspect toward start room 5.

The full B9 controller uses mission-specific phase and interaction rules for these tasks. It may override the model's proposed action, so success measures the whole policy. The reference archive separately demonstrates 48-action feasibility with no model inference. On these development seeds, the three-condition comparison estimates what the navigation control and full task controller add under this run design. Generalization to other tasks and unseen seeds is open. A separate component comparison would be needed to isolate the hallway cue rule.

[Full report](report.md) · [Metrics](metrics.csv) · [Paired comparisons](comparisons.csv) · [Coverage](coverage.json) · [Success figure](figures/success.png)

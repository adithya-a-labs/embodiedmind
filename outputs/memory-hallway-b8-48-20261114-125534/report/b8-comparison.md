# B8 hallway comparison

Matched development seeds 11, 14, 21 and 36. Each variant had 48 actions and 48 model calls available.

| Variant | Seed 11 | Seed 14 | Seed 21 | Seed 36 | Solved |
| --- | --- | --- | --- | --- | ---: |
| B0 | success (11 actions) | terminated failure (11 actions) | success (9 actions) | terminated failure (9 actions) | 2/4 |
| B1 | budget timeout (48 actions) | budget timeout (48 actions) | success (19 actions) | terminated failure (19 actions) | 1/4 |
| B2 | budget timeout (48 actions) | budget timeout (48 actions) | success (9 actions) | terminated failure (9 actions) | 1/4 |
| B3 | success (11 actions) | terminated failure (11 actions) | success (10 actions) | terminated failure (10 actions) | 2/4 |
| B4 | success (11 actions) | terminated failure (11 actions) | success (9 actions) | terminated failure (9 actions) | 2/4 |
| B5 | budget timeout (48 actions) | budget timeout (48 actions) | budget timeout (48 actions) | budget timeout (48 actions) | 0/4 |
| B6 | budget timeout (48 actions) | budget timeout (48 actions) | budget timeout (48 actions) | budget timeout (48 actions) | 0/4 |
| B7 | budget timeout (48 actions) | budget timeout (48 actions) | budget timeout (48 actions) | budget timeout (48 actions) | 0/4 |
| B8 | success (15 actions) | success (15 actions) | success (13 actions) | success (13 actions) | 4/4 |

## How B8 made the branch decision

| Seed | Cue | Branch chosen on success | Scan turns | Forward-burst moves | Branch-routing actions |
| --- | --- | --- | ---: | ---: | ---: |
| 11 | key | north | 4 | 3 | 8 |
| 14 | ball | south | 4 | 3 | 8 |
| 21 | ball | north | 4 | 1 | 8 |
| 36 | key | south | 4 | 1 | 8 |

30 of 32 B0–B7 reruns matched their earlier outcome and action count.
B8 is a combined change. The fixed start scan, cue storage, object matching, branch routing and forward bursts were evaluated together. The four layouts were used in development, so this comparison leaves held-out generalization and individual effects open.

[Run report](report.md) · [Episode metrics](metrics.csv) · [Paired comparisons](comparisons.csv) · [Success figure](figures/success.png)

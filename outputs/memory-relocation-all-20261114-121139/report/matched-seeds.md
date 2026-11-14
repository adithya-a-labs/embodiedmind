# Matched relocation results

All 30 episodes were valid and the evaluator recorded relocation in every episode. Entries show the outcome and number of steps.

| Seed | B0 | B1 | B2 | B3 | B4 | B5 |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) |
| 6 | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Solved (13) |
| 7 | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Solved (13) |
| 8 | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Solved (12) |
| 9 | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Timeout (24) | Solved (12) |

B5 was the only variant to solve any seed and averaged 14.8 steps and 5,746.2 tokens per episode. All other variants exhausted the 24-step budget. These five development seeds support a comparison of the configured variants on this task. Held-out performance and individual mechanism effects remain open.

[Full report](report.md) · [Episode metrics](metrics.csv) · [Success figure](figures/success.png)
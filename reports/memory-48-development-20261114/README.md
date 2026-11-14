# EmbodiedMind 48-step memory comparison

B0–B7 completed 112 matched development episodes across three tasks. A cell below shows solved episodes and mean executed steps (including failed episodes). Each task used the same model, worker count and per-variant limits.

| Variant | DoorKey | Red-key relocation | Hallway cue matching |
| --- | --- | --- | --- |
| B0 | 4/5, 23.6 steps | 5/5, 27.2 steps | 2/4, 10 steps |
| B1 | 1/5, 41.6 steps | 5/5, 27.6 steps | 2/4, 29.8 steps |
| B2 | 0/5, 48 steps | 2/5, 40.2 steps | 1/4, 28.5 steps |
| B3 | 1/5, 43.2 steps | 5/5, 27.2 steps | 1/4, 19.8 steps |
| B4 | 2/5, 40.4 steps | 5/5, 27.2 steps | 2/4, 10 steps |
| B5 | 0/5, 48 steps | 5/5, 17.8 steps | 0/4, 48 steps |
| B6 | 0/5, 48 steps | 5/5, 17.8 steps | 0/4, 48 steps |
| B7 | 5/5, 16.2 steps | 5/5, 17.8 steps | 0/4, 48 steps |

## Interpretation

- DoorKey isolates the effect of the three routine variants B5–B7 under the same memory and navigation interface. B7 solved all five layouts. B5 and B6 timed out on all five despite the longer budget.
- The evaluator confirmed relocation in 40/40 episodes. B5–B7 shared their navigation policy here because DoorKey cues were inactive. They reached 5/5 at 17.8 actions on average, versus 5/5 at 27.2 for B4. The 24-step and 48-step seed 5 traces share the same action/observation prefix for B4 and B5. Their extended traces solved at 26 and 39 actions, respectively. On seed 8 B4 diverged at trace step 14 between runs, so treat the wider comparison as a rerun with a higher cap.
- The stock hallway task uses seeds 11, 14, 21 and 36. These balance the cue type and the correct fork direction. The prompt describes how to inspect and use the cue without providing its identity. Grounded retrieval has no cue-specific target selection for this mission. Its results test transfer of the current architecture.
- These are development rosters. Seeds match within each task, and no aggregate ranking across tasks is reported.

[Combined report](analysis/report.md) · [Episode metrics](analysis/metrics.csv) · [Paired comparisons](analysis/comparisons.csv) · [Success figure](analysis/figures/success.png)
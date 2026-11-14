# EmbodiedMind held-out results

The completed run used frozen source commit `a44c34e0431322078a368453881366214993b900` and the [registered protocol](../experiments/manifests/frozen-protocol.md). Both held-out rosters passed the coverage audit. The generated [technical report](../results/runs/embodiedmind-20261114-0428-ist/final-report/report.md) and [evidence index](../results/runs/embodiedmind-20261114-0428-ist/final-report/artifact-index.json) are in the local study directory.

## Primary comparisons

| Held-out task | B3 result | Comparator | Matched difference and 95% bootstrap interval |
| --- | ---: | ---: | --- |
| DoorKey success | 8/30 | B1 4/30 | +13.3 percentage points [0, +30.0] |
| GoToObjMaze success | 5/30 | B1 5/30 | 0 percentage points [0, 0] |
| Hidden relocation, explicitly cited stale actions | 3 citations in 720 steps | B2 0 in 720 steps | +0.42 percentage points [0, +1.0] |

The reactive B0 completed 17/30 DoorKey missions. Equal paired outcomes on GoToObjMaze describe this sample. The study found no reduction in cited stale actions for B3 versus B2. Stale-action estimates only cover explicit citations. All 90 assigned relocations occurred, and every dynamic arm included the same two scripted turns before policy control.

## Coverage and reproduction

The static benchmark accounted for 240/240 episodes, and the dynamic benchmark accounted for 270/270. The main report includes 40 paired stock pilot episodes and two separate held-out rosters. The dynamic development pilot is archived separately. No scored episode was excluded or retried.

Reproduction commands are in [README](../README.md). The [research proposal](../RESEARCH_PROPOSAL.md) records hypotheses and references, including BabyAI, MiniGrid and ReAct. See [run status](../STATUS.md) for verification and artifact paths.

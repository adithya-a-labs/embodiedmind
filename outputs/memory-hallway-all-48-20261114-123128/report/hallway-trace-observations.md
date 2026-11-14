# Hallway cue matching at 48 steps

The stock MiniGrid Memory task asks the agent to inspect a start-room object, then choose the branch with the matching object at a hallway fork. This analysis compares 24 saved episodes across six variants and four development seeds. Evaluator poses and object coordinates were used to audit the traces. The cue-visibility checks used the actual policy observations.

| Seed | Start cue | Correct branch | B0 and B4 | B1 | B5–B7 |
| --- | --- | --- | --- | --- | --- |
| 11 | Key | North | North, solved in 11 actions | North, solved in 33 actions | Timed out before the fork |
| 14 | Ball | South | North, wrong branch | Timed out at the fork | Timed out before the fork |
| 21 | Ball | North | North, solved in 9 actions | North, solved in 19 actions | Timed out before the fork |
| 36 | Key | South | North, wrong branch | North, wrong branch | Timed out before the fork |

## Why B5–B7 timed out

On each seed, B5, B6 and B7 produced identical plans and executed actions. Their DoorKey routines were inactive in this task. Each requested `explore` for all 48 decisions. Their observations briefly showed the start cue, but the grounded retriever selects a target type named by the mission. The hallway mission asks for the “matching object” without naming a key or ball, so none of the three retrieved the cue as a target fact.

All twelve episodes stalled at (6,6), five cells short of the fork at (11,6). On seed 11, for example, B5 advanced east at trace steps 8 and 9. At step 10, the planner returned an empty route despite the next tile east being visibly empty. The exploration fallback turned it right to face a wall. The next step turned it left to face east again. This east–south turn loop ran until the cutoff. The longer budget gave the loop more time.

[B5 seed 11 step trace](../episodes/e00-s00011-none-B5-r0/steps.csv) · [Replay](../episodes/e00-s00011-none-B5-r0/replay.gif)

## What B0, B1 and B4 did differently

B0 and B4 used primitive forward actions along the corridor, then turned north at the fork on all four seeds. B1 also reached the fork on every seed, but used additional ineffective actions before heading north on its successful runs. B1 timed out at the fork on seed 14. North happened to be correct on seeds 11 and 21.

None of these three variants saw the start-room cue in the recorded policy observations. B1 cited past views containing fork objects on its successful runs. Those citations do not establish recall of the start cue. These runs distinguish reaching the fork from using the cue to choose the branch. A controller change that prevents the turn loop would address navigation. Cue-based branch selection would still require its own test.

[Episode metrics](metrics.csv) · [Run report](report.md) · [B0 seed 11 replay](../episodes/e00-s00011-none-B0-r0/replay.gif)

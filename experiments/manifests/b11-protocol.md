# B11 fresh-seed protocol

Freeze the source, five configuration files, model digest, and matched rosters before observing any fresh-seed outcomes. These runs are a follow-up to the original frozen study. The older development seeds informed the B11 design and are outside the new rosters.

| Roster | Seeds | Cases | Agents | Episodes |
| --- | --- | --- | --- | ---: |
| Broad stock | 11001–11010 | All 11 project stock games, 48 actions | B0–B11, B0G, B3G, B9N | 1,650 |
| Broad GoToShift | 11001–11010 | No change, dropout, relocation, 48 actions | Same 15 agents | 450 |
| Broad MultiRoom | 11001–11010 | Same layouts, separate 80-action cap | Same 15 agents | 150 |
| Mechanisms, stock | 11101–11130 | DoorKey and GoToObj Maze, 48 actions | B11T, B11P, B11R, B11, B11C | 300 |
| Mechanisms, GoToShift | 11101–11130 | No change, dropout, relocation, 48 actions | B11T, B11P, B11R, B11PA, B11, B11C | 540 |

The broad roster compares complete configured policies. It cannot isolate memory effects. Ten seeds per broad game are a modest sample. The mechanism roster uses 30 pairs per condition for tighter estimates, with no power guarantee for uncommon events or small effects. Primary interpretations are by task and intervention. Do not combine the two MultiRoom caps.

## Mechanism conditions

| Arm | Semantic memory | Verification | Model |
| --- | --- | --- | --- |
| B11T | Bounded text history, live semantic facts for the controller | Fixed | On |
| B11P | Passive structured observations | Fixed | On |
| B11R | Revising structured observations with aging disabled | Fixed | On |
| B11PA | Passive structured observations | Adaptive | On |
| B11 | Revising structured observations with aging disabled | Adaptive | On |
| B11C | As B11 | Adaptive | Off, deterministic explore proposal |

The common executor uses observed route facts, odometry and present interaction preconditions. It obtains remembered task targets only through the experimental semantic memory. B11T receives raw text history in the model prompt and can propose primitive actions; its controller binds target roles from currently visible semantic facts. Accordingly, the text versus structured contrast measures the whole representation interface under a common executor. The passive and revising arms share a recall and controller interface. Re-observing an empty location can retract a semantic claim in a revising arm. A masked or unseen cell contributes no contradictory fact.

Fixed verification applies when the hidden remembered target is within one planned action of a facing pose. Adaptive verification can recheck a hidden fact at least two decisions old via a local side glance or a route of at most four actions. Each arm can spend at most four explicit verification actions. Implicit observations on normal mission routes can still expose a target. Report explicit verification counts independently from re-observation opportunities.

## Outcomes and interpretation

1. **RQ1, structured memory.** Primary comparisons on each of the two stock mechanism games are B11P minus B11T and B11R minus B11T for success. Report paired action and token totals as secondary measures within each game.
2. **RQ2, revision.** Primary contrast is B11R minus B11P on assigned relocation, using continued controller routes to an original target position after the agent has re-observed its absence. B11 minus B11PA is the corresponding adaptive comparison. A movement labeled as verification does not count as an action commitment. This measure covers explicit controller routes, including routes without model citations. Motives of uncited free-form primitive actions are unobservable. Report assignment/exposure, old-location checks and target reacquisition separately. Compare unconditional episode outcomes first. Conditional results after an actual contradiction are descriptive.
3. **RQ3, information acquisition.** Compare B11 minus B11R and B11PA minus B11P within each intervention, with verification actions, actions that expose their checked target, reacquisition in relocation, and success. Distinguish a purposeful verification action from its observed outcome. A move toward a viewpoint can spend budget without exposing the target on that step. Use raw pre/post observations and next-step planning to audit changes of plan.
4. **RQ4, cost and model contribution.** Compare action counts, calls, prompt and completion tokens, inference time and episode wall time. Compare B11 with B11C on the mechanism rosters. All means include valid failed episodes. Cost per completion pools costs across all valid episodes and is undefined with zero completions. B11C measures model contribution relative to the fixed explore fallback.

Preserve the shared Qwen model/options, 768-byte memory budget, symbolic sensor, action vocabulary and executor. Use one inference slot. Pair the layouts and intervention schedules by seed. GoToShift applies two scripted left turns before intervention, as in prior runs. Report assigned conditions, misses, and validation coverage. Keep failed task outcomes. Save per-episode observations, proposals, targets, actions, evaluator state and checksummed artifacts. Record 95% paired seed bootstrap intervals as per-contrast estimates without a joint significance claim.

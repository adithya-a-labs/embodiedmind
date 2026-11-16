# B9 failure analysis and improvement plan

## What the audit covered

This is an offline analysis of **all 170 saved B9 episodes** across the four archived rosters, plus the matched B7 DoorKey and B8 Dynamic Obstacles episodes as comparison traces. The large comparison was the only roster covering every game. Its B9 condition solved **85/140 episodes** and timed out on the other **55**. The earlier comparison and the fixed-explore feasibility roster each contain 15/15 B9 successes on the three tasks used to develop its explicit task rules. Those 30 episodes are included in the audit and kept separate from the large comparison. The fixed-explore records are scripted replay witnesses and contain no model calls.

The audit aligns every pre-action policy observation and executed action with separate evaluator states and checks trace length, step sequence, observation continuity and reward totals. Movement counts use the evaluator position for diagnosis. The policy only had its public observation and the runner-provided movement outcome. Door, pickup and cue claims below use the observations and actions as noted. The offline route search uses full spawn boards. It was kept separate from the policy and has no inference outputs.

Sources are local archive commits 2e308ae (large comparison), f6a83a3 (matched development comparison) and 5e90ba8 (feasibility witnesses).

## Where the 55 failures occurred

| Task | B9 solved | Trace evidence | First intervention to test |
| --- | ---: | --- | --- |
| DoorKey | 2/10 | All ten picked up the key. The eight failures faced the matching locked door 76 times while holding its key, requested verify every time, and never toggled it. B7 picked up the key, toggled, crossed and reached the goal on all ten matched seeds. | Add verified DoorKey phases and convert arrival at a matching locked door into a guarded toggle. |
| GoToObj Maze | 2/10 | The eight failures never saw the requested object. They took 370 exploration turns in 384 decisions and turned with a visibly empty forward cell on 312 of them. B9 executed zero toggles across the ten episodes, although every episode observed a door. | Treat observed closed doors as actionable transitions and search reachable observation frontiers across rooms. |
| MultiRoom | 0/10 | 471 turns and nine actual moves in 480 actions. Every episode saw a door, and none attempted a toggle or crossed a door. Four layouts exceed 48 actions with full map knowledge in the modeled search. | Add a room traversal phase and verified door opening. Run a separate feasible-budget comparison. |
| Blocked Unlock Pickup | 0/10 | 479 turns and one actual move in 480 actions. Every episode saw a key, a ball and a locked door at some point. None tried pickup, drop or toggle, and none observed the target box. All ten spawn boards have modeled 20–25-action solutions. | Add a dependency chain for relocating the blocker, retrieving the key, unlocking, releasing the key and picking up the box. |
| Dynamic Obstacles | 0/10 | All 480 actions were tagged progress-aware exploration. B9 averaged 6.0 unique tiles, took 391 turns and made 81 actual moves. B8 solved 7/10 with the same seeds, averaged 11.7 unique tiles and executed 167 forward-burst actions. Neither variant had terminal collisions in this run. | Preserve B8's guarded local forward behavior as a control. Add a local, goal-directed policy robust to unknown movement. |
| Synth | 1/10 | The nine failures executed 422 exploration turns in 432 steps, with zero pickup, drop or toggle attempts. The ten missions covered GoTo (five), Open (two), PutNext (two) and Pickup (one). B9 activated no explicit task phase on any of them. | Parse mission verbs, articles and optional descriptors into grounded object roles. Add effect checks for each primitive interaction. |
| **Total** | **5/60** | **55 timeouts** across these six tasks. | Compare the fixes in ablations. |

In the 55 failed episodes, 2,399 of 2,640 actions were turns tagged as progress-aware exploration. The failed episodes consumed **1,147,293 tokens**. This is a controller and task coverage problem as well as a memory problem. Increasing the memory budget or allowing more identical decisions would leave the observed loops and missing actions in place.

### What must keep working

B9 went 10/10 each on GoToObj, Memory S13, Randomized Memory, Key Corridor, Put Next and all three GoToShift conditions. Across those eight conditions, 80/80 is the observed regression reference. Both Memory games used the stock corridor geometry to identify the start cue. Key Corridor and Put Next used the task controller for all actions, including 45 toggles and 20 effective pickups across the ten Key Corridor wins, and one observed pickup and one drop per Put Next episode. Preserve the public-observation contracts and add generalization tests before trying to replace these successful rules.

## Prioritized design

### 1. Make exploration move toward an explicit destination

In the generic B9 path, a progress route can overwrite B8's forward burst. It currently searches for an unknown tile directly ahead of a candidate pose. If there is no route, it returns a turn at the current pose. The action resolver treats that turn as a viable plan and can keep using it after a full scan. The six failure groups and the B8 comparator show why a visit count alone is insufficient.

- Score reachable poses by likely **new observation coverage**, action cost and recent failed transitions. Represent an observed closed door as a potential frontier and try a legal toggle at its approach pose. Locked doors create a key dependency.
- Commit to a frontier or door until reaching it, seeing a change that invalidates the route, or confirming the transition failed. Record progress as new cells, a new room, an object or door-state change, or verified mission-phase advancement.
- After a full scan with no gain, suppress that scan pose for the current subgoal and try a mapped route, a passable forward move, or a previously known untried exit. Mark a route as exhausted when none is available. Log the failed transition so it cannot repeat indefinitely without new evidence.
- Measure target first-seen step, distinct rooms, confirmed crossings, turns without movement, and stalls after a full scan. Use the eight failed GoToObj Maze traces as regression fixtures, including seed 4001, where B9 did move briefly but never found the target. A higher move count alone is insufficient if visits produce no information.

### 2. Generalize verified interactions before adding more memory layers

**DoorKey first.** Use B7 as a positive control and separately test adding its frozen routine to B9 versus a deterministic interaction rule. When the verified subgoal is opening a door and the model already faces that door with a visibly matching key, try toggle. Confirm the open door in the next observation before routing across. Detect stale or repeated interaction failures and replan. Use seed 4002 as a focused regression fixture. It had 11 verify decisions at the locked door while holding the correct key. Track key pickup, first approach to the locked door, toggle, open observation, crossing and goal arrival. B7's 10/10 on the exact layouts makes this the strongest actionable comparison in the set. It does not establish that adding the cue alone to B9 will reproduce it.

**Blocked Unlock Pickup second.** Bind each object to its purpose. A ball obstructing the observed door approach becomes a temporary manipulation target. Carry it to a visible free cell off the approach, confirm it has been dropped, then restore the locked-door subgoal. Reuse the successful Key Corridor carrying checks to get the key, open the door, free the carrying slot and take the box. Preserve separate map facts for the door, blocker, key and mission target. Base the success checks on actual carried object, observed occupancy and door state. Seed 4001 is a concrete regression test. The key and blocker were visible during the episode, but all 48 B9 actions were turns.

**Synth after the reusable pieces are stable.** Dispatch on mission structure with optional color and articles rather than matching a single mission string. Bind the source and reference separately for PutNext, including a door as a reference when named. Ground the exact verb and verify its effect. A GoTo should reach the correct adjacent facing pose. Open checks a door state change. Pickup checks carried identity. PutNext checks release and placement relation. Measure each mission family on a balanced new roster. The current ten seeds give only one to five examples per tested verb. Leave ambiguous references unresolved until a public observation supports them.

### 3. Give moving obstacles their own observation-based arbitration

Dynamic Obstacles can move objects after the agent’s observation and before its action. The controller conservatively reports unknown forward motion. This causes a new odometry segment after forward attempts, which limits the visit-weighted planner's map continuity. B9 averaged 9.9 distinct odometry segments per episode, and the goal entered view in all ten episodes. B8 also had fragmented odometry and succeeded on seven. That pairing points to the practical cost of B9's override, with odometry uncertainty as a contributing constraint to test.

Start with a direct **B9 + B8 local fallback** ablation. When movement is uncertain, re-evaluate the currently visible goal and passable cells after every action. Favor a legal forward step toward the goal, using static wall landmarks for local orientation and treating obstacle positions as short-lived observations. Stop a burst when visibility or clearance changes. Retain a way to inspect sideways if forward progress stalls. Do not use evaluator positions to stitch segments. Compare success, actual forward moves, no-progress intervals and terminal collisions. On seed 4001 both variants initially scanned, then B8 made consecutive forward moves and B9 returned to turning after its first forward move.

### 4. Calibrate the budget independently of the controller

An offline breadth-first search on saved evaluator boards modeled primitive turns, movement and task-appropriate door or inventory interactions. This modeled analysis did not run the environments. Treat the feasible lengths as candidate witnesses pending simulator replay, and keep the paths evaluator-only. On MultiRoom, the archived boards have five unlocked doors, one goal and no movable blockers, so the modeled shortest paths give a lower bound under the stock action semantics.

| Game | Modeled actions on seeds 4001–4010 | Implication |
| --- | --- | --- |
| DoorKey | 11–21, all ten at or below 48 | Budget leaves room for the verified-interaction fix. B7 already succeeded on each saved layout under 48. |
| Blocked Unlock Pickup | 20–25, all ten at or below 48 | The cap alone cannot explain the failure pattern. Replay the candidate witnesses through the evaluator before a frozen comparison. |
| MultiRoom | 40–51, six layouts at or below 48 | Seeds 4004, 4007, 4008 and 4009 require 50, 49, 49 and 51 modeled actions. Even the six feasible layouts leave only 0–8 actions beyond the full-information path. Keep the original cap as a stress test and add a predeclared higher-budget condition, such as 80 actions, for a separate comparison. |
| GoToObj Maze | 2–50 with objects left in place | Seed 4010 requires 50 under the modeled movement and door rules. A relaxed walls-only bound is 44, so 50 does not establish impossibility under the full action space. Check a real witness before classifying it. |

## Validation plan

1. **Regression fixtures.** Replay decisions from the archived inputs for the DoorKey toggle, Blocked Unlock Pickup interaction, Maze and MultiRoom scan loops, Dynamic Obstacles first forward divergence, and the three supported B9 task policies. Assert the policy inputs contain public fields only.
2. **Component trials.** On the existing ten diagnostic seeds compare B9, navigation-only changes, verified-interaction changes and the combined candidate. Include B7 on DoorKey and B8 on Dynamic Obstacles. Keep the 48-action limit in this stage and report the MultiRoom feasibility strata. Report mean actions and tokens, first failed milestone, repeated-pose counts and collisions alongside solved counts.
3. **Freeze a broader evaluation.** Register fresh matched seeds, the specific task configurations and both action caps before running. Use at least 30 matched seeds per condition for claims of transfer. Keep the 80/80 observed successes as a regression reference and run the same eight conditions on fresh seeds. Establish separate milestones for approach, verified action and mission completion so another timeout identifies the failure stage. Keep all valid failures.
4. **Test the model's contribution.** Compare deterministic controller-only, model with the same controller, and the navigation baseline. Earlier fixed-explore witnesses already solved 15/15 on the three B9 development tasks. Compare tokens and latency with the same observation stream. Calling the model only for ambiguity or recovery is a separate policy choice and should be labeled as such.

A 10/10 score on one roster is a development milestone. The MultiRoom result rules out 10/10 on this exact roster at 48 under the observed geometry and stock action model. On the feasible tasks, use 10/10 as a regression goal and measure transfer on unseen seeds.

## Evidence and reproduction

- [Episode audit](episode-audit.csv) contains all 170 B9 rows plus 20 comparator rows, with episode paths relative to the repository root.
- [Trace totals](trace-summary.json) groups counts and outcomes by run, game and condition.
- [Evaluator route lengths and modeled action sequences](evaluator-route-lengths.csv) records all 40 audited spawn boards in the four modeled tasks.
- [Audit script](audit.py) and [route search](route_bounds.py) regenerate the derived evidence using the repository's Python environment. Run from the repo root and pass this report directory.
- [Large stock report](../../outputs/memory-large-stock-20261114-173852/report/all-game-comparison.md), [large GoToShift metrics](../../outputs/memory-large-shift-20261114-173852/report/metrics.csv), [development comparison](../../outputs/memory-b9-comparison-20261114-172249/report/b9-comparison.md) and [fixed-explore feasibility](../../outputs/memory-b9-feasibility-20261114-172249/report/feasibility.md).

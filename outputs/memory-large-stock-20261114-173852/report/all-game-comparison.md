# Large all-game memory comparison

700 valid episodes across 14 game or intervention conditions. Each condition used matched seeds 4001–4010, one local inference worker, a 768-byte memory context cap, and 48 actions and model calls at most. GoToShift retained its two scripted initial turns, included in the action cap.

## Solved episodes

| Game or condition | B6 | B7 | B8 | B9 | B9N |
| --- | ---: | ---: | ---: | ---: | ---: |
| GoToObj | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |
| DoorKey | 0/10 | 10/10 | 2/10 | 2/10 | 2/10 |
| GoToObj Maze | 2/10 | 2/10 | 2/10 | 2/10 | 2/10 |
| Memory S13 | 0/10 | 0/10 | 9/10 | 10/10 | 6/10 |
| Randomized Memory | 0/10 | 0/10 | 9/10 | 10/10 | 8/10 |
| MultiRoom | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| Key Corridor | 0/10 | 0/10 | 0/10 | 10/10 | 0/10 |
| Blocked Unlock Pickup | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| Put Next | 0/10 | 0/10 | 0/10 | 10/10 | 0/10 |
| Dynamic Obstacles | 0/10 | 0/10 | 7/10 | 0/10 | 0/10 |
| Synth | 1/10 | 1/10 | 2/10 | 1/10 | 1/10 |
| GoToShift · no change | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |
| GoToShift · dropout | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |
| GoToShift · relocation | 10/10 | 10/10 | 9/10 | 10/10 | 10/10 |

## Mean actions

Means include early task failures and timeouts.

| Game or condition | B6 | B7 | B8 | B9 | B9N |
| --- | ---: | ---: | ---: | ---: | ---: |
| GoToObj | 3.2 | 3.2 | 3.2 | 3.2 | 3.2 |
| DoorKey | 48.0 | 17.2 | 43.2 | 43.2 | 43.2 |
| GoToObj Maze | 39.4 | 39.4 | 39.4 | 39.4 | 39.4 |
| Memory S13 | 48.0 | 48.0 | 13.2 | 12.4 | 27.5 |
| Randomized Memory | 48.0 | 48.0 | 15.9 | 13.0 | 20.2 |
| MultiRoom | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |
| Key Corridor | 48.0 | 48.0 | 48.0 | 32.3 | 48.0 |
| Blocked Unlock Pickup | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |
| Put Next | 48.0 | 48.0 | 48.0 | 10.5 | 48.0 |
| Dynamic Obstacles | 48.0 | 48.0 | 26.8 | 48.0 | 48.0 |
| Synth | 43.5 | 43.5 | 39.1 | 43.5 | 43.5 |
| GoToShift · no change | 10.9 | 10.9 | 11.9 | 10.9 | 10.9 |
| GoToShift · dropout | 11.5 | 11.5 | 12.0 | 12.6 | 12.6 |
| GoToShift · relocation | 18.1 | 18.1 | 19.8 | 18.1 | 18.1 |

## Mean total tokens

| Game or condition | B6 | B7 | B8 | B9 | B9N |
| --- | ---: | ---: | ---: | ---: | ---: |
| GoToObj | 1,421 | 1,420 | 1,420 | 1,420 | 1,420 |
| DoorKey | 23,444 | 8,107 | 19,917 | 19,892 | 19,892 |
| GoToObj Maze | 17,120 | 17,120 | 17,092 | 17,019 | 17,019 |
| Memory S13 | 22,300 | 22,300 | 6,597 | 6,228 | 13,591 |
| Randomized Memory | 22,409 | 22,410 | 7,948 | 6,554 | 10,033 |
| MultiRoom | 20,907 | 20,907 | 20,912 | 20,825 | 20,825 |
| Key Corridor | 21,492 | 21,492 | 21,648 | 15,067 | 21,534 |
| Blocked Unlock Pickup | 21,239 | 21,239 | 21,034 | 21,037 | 21,037 |
| Put Next | 23,074 | 23,074 | 23,093 | 5,195 | 23,035 |
| Dynamic Obstacles | 18,709 | 18,709 | 10,292 | 18,724 | 18,724 |
| Synth | 20,380 | 20,380 | 17,922 | 20,028 | 20,028 |
| GoToShift · no change | 3,995 | 3,995 | 4,450 | 3,995 | 3,995 |
| GoToShift · dropout | 4,325 | 4,325 | 4,549 | 4,819 | 4,819 |
| GoToShift · relocation | 7,244 | 7,244 | 8,041 | 7,250 | 7,250 |

## Outcomes across variants

- **GoToObj.** 50 success.
- **DoorKey.** 34 budget timeout, 16 success.
- **GoToObj Maze.** 40 budget timeout, 10 success.
- **Memory S13.** 24 budget timeout, 25 success, 1 terminated failure.
- **Randomized Memory.** 23 budget timeout, 27 success.
- **MultiRoom.** 50 budget timeout.
- **Key Corridor.** 40 budget timeout, 10 success.
- **Blocked Unlock Pickup.** 50 budget timeout.
- **Put Next.** 40 budget timeout, 10 success.
- **Dynamic Obstacles.** 43 budget timeout, 7 success.
- **Synth.** 44 budget timeout, 6 success.
- **GoToShift · no change.** 50 success.
- **GoToShift · dropout.** 50 success.
- **GoToShift · relocation.** 1 budget timeout, 49 success.

## GoToShift intervention exposure

Counts record whether the environment applied the assigned intervention. Success uses all assigned episodes.

| Game or condition | B6 | B7 | B8 | B9 | B9N |
| --- | ---: | ---: | ---: | ---: | ---: |
| GoToShift · no change | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |
| GoToShift · dropout | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |
| GoToShift · relocation | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |

## Scope

- B6 and B7 retrieve their DoorKey routines on DoorKey. Their results on other games compare the same controller without those cues.
- B9 uses task-specific phase rules on Key Corridor, Put Next and Memory. Differences compare the full configured policies.
- The seeds are fresh relative to earlier rosters. These results cover the development configuration and do not isolate every controller or memory change.

[Stock run report](report.md) · [Stock episode metrics](metrics.csv) · [GoToShift report](../../memory-large-shift-20261114-173852/report/report.md) · [GoToShift metrics](../../memory-large-shift-20261114-173852/report/metrics.csv)

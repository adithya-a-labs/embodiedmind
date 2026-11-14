# Matched B9 and B10 comparison

The 48-action comparison covers 280 episodes across 11 stock games and three GoToShift conditions. A separate MultiRoom roster contributes 20 episodes with an 80-action cap. Each condition uses the same ten development seeds (4001–4010) per variant, one worker, the same model and a 768-byte memory cap.

| Game or condition | Cap | B9 solved | B10 solved | B9 mean actions | B10 mean actions | B9 mean tokens | B10 mean tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| GoToObj | 48 | 10/10 | 10/10 | 3.2 | 3.4 | 1,421 | 1,547 |
| DoorKey | 48 | 0/10 | 10/10 | 48.0 | 18.1 | 22,107 | 8,473 |
| GoToObj Maze | 48 | 2/10 | 4/10 | 39.4 | 38.3 | 17,019 | 16,806 |
| Memory S13 | 48 | 10/10 | 10/10 | 12.4 | 12.4 | 6,228 | 6,228 |
| Randomized Memory | 48 | 10/10 | 10/10 | 13.0 | 13.0 | 6,554 | 6,554 |
| MultiRoom | 48 | 0/10 | 3/10 | 48.0 | 46.9 | 20,825 | 20,631 |
| Key Corridor | 48 | 10/10 | 10/10 | 32.3 | 32.3 | 15,067 | 15,067 |
| Blocked Unlock Pickup | 48 | 0/10 | 10/10 | 48.0 | 27.0 | 21,037 | 12,472 |
| Put Next | 48 | 10/10 | 10/10 | 10.5 | 10.9 | 5,195 | 5,394 |
| Dynamic Obstacles | 48 | 0/10 | 7/10 | 48.0 | 26.8 | 18,724 | 10,292 |
| Synth | 48 | 1/10 | 4/10 | 43.5 | 30.3 | 20,028 | 14,145 |
| GoToShift · no change | 48 | 10/10 | 10/10 | 10.9 | 10.6 | 3,995 | 3,968 |
| GoToShift · dropout | 48 | 10/10 | 10/10 | 12.6 | 10.6 | 4,819 | 4,030 |
| GoToShift · relocation | 48 | 10/10 | 7/10 | 18.1 | 23.1 | 7,250 | 9,612 |
| MultiRoom | 80 | 0/10 | 10/10 | 80.0 | 55.1 | 34,707 | 24,329 |

Action and token means include timeouts and early failures.

## Matched differences

- **GoToObj (48).** Newly solved seeds none. Regressions none.
- **DoorKey (48).** Newly solved seeds 4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010. Regressions none.
- **GoToObj Maze (48).** Newly solved seeds 4001, 4003, 4005. Regressions 4009.
- **Memory S13 (48).** Newly solved seeds none. Regressions none.
- **Randomized Memory (48).** Newly solved seeds none. Regressions none.
- **MultiRoom (48).** Newly solved seeds 4001, 4002, 4005. Regressions none.
- **Key Corridor (48).** Newly solved seeds none. Regressions none.
- **Blocked Unlock Pickup (48).** Newly solved seeds 4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010. Regressions none.
- **Put Next (48).** Newly solved seeds none. Regressions none.
- **Dynamic Obstacles (48).** Newly solved seeds 4001, 4002, 4003, 4006, 4007, 4009, 4010. Regressions none.
- **Synth (48).** Newly solved seeds 4002, 4004, 4009. Regressions none.
- **GoToShift · no change (48).** Newly solved seeds none. Regressions none.
- **GoToShift · dropout (48).** Newly solved seeds none. Regressions none.
- **GoToShift · relocation (48).** Newly solved seeds none. Regressions 4003, 4005, 4009.
- **MultiRoom (80).** Newly solved seeds 4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010. Regressions none.

## GoToShift exposure

- **GoToShift · no change (48).** Intervention applied in 0/10 B9 and 0/10 B10 episodes.
- **GoToShift · dropout (48).** Intervention applied in 10/10 B9 and 10/10 B10 episodes.
- **GoToShift · relocation (48).** Intervention applied in 10/10 B9 and 10/10 B10 episodes.

On the 48-action stock rerun, 108/110 B9 episodes matched their previous outcome and action count.
The architectures were compared as configured policies. This diagnostic roster informed B10’s design. The differences do not isolate individual rules or estimate generalization to unseen layouts.

[Stock metrics](metrics.csv) · [GoToShift metrics](../../memory-b10-shift-20261114-202808/report/metrics.csv) · [80-action MultiRoom metrics](../../memory-b10-multiroom-80-20261114-202808/report/metrics.csv)

# Seven-game B0–B8 challenge comparison

315 valid development episodes. All nine variants shared seeds 3001–3005 within each game, a 48-action and 48-call cap, a 768-byte memory cap, the same local model, and one inference worker.

## Success by game

| Game | B0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Randomized Memory | 4/5 | 4/5 | 1/5 | 2/5 | 4/5 | 0/5 | 0/5 | 0/5 | 4/5 |
| MultiRoom | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |
| Key Corridor | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |
| Blocked Unlock Pickup | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |
| Put Next | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |
| Dynamic Obstacles | 0/5 | 0/5 | 0/5 | 1/5 | 3/5 | 0/5 | 0/5 | 0/5 | 1/5 |
| Synth | 0/5 | 1/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 | 0/5 |

## Mean actions by game

Means include task failures and timeouts. A low mean can reflect early failure.

| Game | B0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Randomized Memory | 9.0 | 22.0 | 39.0 | 24.6 | 9.0 | 48.0 | 48.0 | 48.0 | 21.2 |
| MultiRoom | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |
| Key Corridor | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |
| Blocked Unlock Pickup | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |
| Put Next | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |
| Dynamic Obstacles | 4.0 | 4.0 | 4.0 | 5.0 | 31.2 | 48.0 | 48.0 | 48.0 | 45.2 |
| Synth | 48.0 | 41.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 | 48.0 |

## Outcomes and leaders

- **Randomized Memory.** B0, B1, B4, B8 led with 4/5. Across all variants: 22 budget timeout, 19 success, 4 terminated failure.
- **MultiRoom.** all variants solved 0/5. Across all variants: 45 budget timeout.
- **Key Corridor.** all variants solved 0/5. Across all variants: 45 budget timeout.
- **Blocked Unlock Pickup.** all variants solved 0/5. Across all variants: 45 budget timeout.
- **Put Next.** all variants solved 0/5. Across all variants: 45 budget timeout.
- **Dynamic Obstacles.** B4 led with 3/5. Across all variants: 21 budget timeout, 5 success, 19 terminated failure.
- **Synth.** B1 led with 1/5. Across all variants: 44 budget timeout, 1 success.

Dynamic Obstacles negative-reward terminations by variant: B0 5/5, B1 5/5, B2 5/5, B3 4/5, B4 0/5, B5 0/5, B6 0/5, B7 0/5, B8 0/5.

## Synth missions

| Seed | Mission | B0 | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3001 | pick up the purple key | No | No | No | No | No | No | No | No | No |
| 3002 | pick up the red ball | No | No | No | No | No | No | No | No | No |
| 3003 | open the blue door | No | Yes | No | No | No | No | No | No | No |
| 3004 | pick up the purple box | No | No | No | No | No | No | No | No | No |
| 3005 | go to the purple box | No | No | No | No | No | No | No | No | No |

## Interpretation

- Each game has five matched development seeds. The stock tasks differ in skill demands, and the 48-step cap may constrain longer layouts. A zero success count can reflect navigation, task semantics, memory, or the budget. This run does not establish held-out generalization.
- B6 and B7 do not retrieve their DoorKey routines on these seven tasks. Their rows compare behavior without those cues. B8 can use its start-cue rule on Randomized Memory and its forward fallback across games.
- The report uses final runner outcomes. A task failure is a valid episode. Negative rewards in Dynamic Obstacles reflect failed forward moves under that environment’s collision rule.

[Full report](report.md) · [Episode metrics](metrics.csv) · [Paired comparisons](comparisons.csv) · [Success figure](figures/success.png) · [Coverage](coverage.json) · [Evidence hashes](artifact-index.json)

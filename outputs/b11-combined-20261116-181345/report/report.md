# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes b11-broad, b11-mechanisms, b11-multiroom-80. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 3090 of 3090 cells were attempted, 3090 validated, 0 excluded and 3091 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 48.000 | 17067.500 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 48.000 | 17067.600 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 48.000 | 30810.100 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 27.500 | 12678.700 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 27.500 | 12373.100 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 48.000 | 26824.500 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 48.000 | 30429.600 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 48.000 | 30025.900 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 48.000 | 17465.400 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 21233.200 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 21233.000 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 21233.000 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 48.000 | 21037.300 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B9 | 10 | 10 | 10 | 0.000 | 48.000 | 21039.700 | — |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 48.000 | 21039.700 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B0 | 10 | 10 | 10 | 0.200 | 38.800 | 13646.500 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B0G | 10 | 10 | 10 | 0.200 | 38.800 | 13656.300 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B1 | 10 | 10 | 10 | 0.200 | 38.800 | 23419.000 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B10 | 10 | 10 | 10 | 0.600 | 28.400 | 12539.100 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B11 | 10 | 10 | 10 | 0.600 | 28.400 | 12221.600 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B2 | 10 | 10 | 10 | 0.300 | 35.800 | 22624.900 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B3 | 10 | 10 | 10 | 0.200 | 38.800 | 25252.300 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B3G | 10 | 10 | 10 | 0.200 | 38.800 | 25260.800 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B4 | 10 | 10 | 10 | 0.200 | 38.800 | 13896.300 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B5 | 10 | 10 | 10 | 0.200 | 38.800 | 16755.800 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B6 | 10 | 10 | 10 | 0.200 | 38.800 | 16755.800 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B7 | 10 | 10 | 10 | 0.200 | 38.800 | 16755.800 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B8 | 10 | 10 | 10 | 0.200 | 38.800 | 16759.800 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B9 | 10 | 10 | 10 | 0.200 | 38.800 | 16724.500 | — |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | B9N | 10 | 10 | 10 | 0.200 | 38.800 | 16724.500 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B0 | 10 | 10 | 10 | 1.000 | 5.100 | 1765.000 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B0G | 10 | 10 | 10 | 1.000 | 5.000 | 1729.500 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B1 | 10 | 10 | 10 | 1.000 | 5.000 | 1966.900 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B10 | 10 | 10 | 10 | 1.000 | 4.200 | 1896.700 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B11 | 10 | 10 | 10 | 1.000 | 4.200 | 1850.500 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B2 | 10 | 10 | 10 | 1.000 | 5.000 | 2466.600 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B3 | 10 | 10 | 10 | 1.000 | 5.600 | 2851.200 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B3G | 10 | 10 | 10 | 1.000 | 5.600 | 2851.300 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B4 | 10 | 10 | 10 | 0.700 | 13.300 | 4771.700 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B5 | 10 | 10 | 10 | 1.000 | 3.800 | 1679.600 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B6 | 10 | 10 | 10 | 1.000 | 3.800 | 1679.600 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B7 | 10 | 10 | 10 | 1.000 | 3.800 | 1679.600 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B8 | 10 | 10 | 10 | 1.000 | 3.800 | 1679.600 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B9 | 10 | 10 | 10 | 1.000 | 3.800 | 1679.600 | — |
| b11-broad | BabyAI-GoToObjS6-v1 | none | B9N | 10 | 10 | 10 | 1.000 | 3.800 | 1679.600 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 48.000 | 17233.700 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 48.000 | 17234.000 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 48.000 | 30549.100 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 32.400 | 15083.300 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 32.400 | 14717.900 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 48.000 | 24228.300 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 48.000 | 26530.500 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 48.000 | 26768.000 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 48.000 | 18031.000 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 21560.400 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 21560.700 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 21560.700 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 48.000 | 21707.400 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B9 | 10 | 10 | 10 | 1.000 | 32.400 | 15083.400 | — |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 48.000 | 21589.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 48.000 | 17301.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 48.000 | 17307.000 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 48.000 | 31054.100 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 12.800 | 6210.400 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 12.800 | 6067.000 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 48.000 | 31459.400 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 48.000 | 30519.700 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 48.000 | 31304.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 48.000 | 18825.000 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 23153.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 23153.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 23153.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 48.000 | 23117.200 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B9 | 10 | 10 | 10 | 1.000 | 10.300 | 5035.400 | — |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 48.000 | 23087.100 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 48.000 | 17564.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 48.000 | 17564.300 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 48.000 | 31329.600 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B10 | 10 | 10 | 10 | 0.100 | 43.800 | 20628.200 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B11 | 10 | 10 | 10 | 0.100 | 43.800 | 20183.500 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 48.000 | 26115.600 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 48.000 | 27624.700 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 48.000 | 27571.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 48.000 | 18262.800 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 22293.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 22293.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 22293.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 48.000 | 22047.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B9 | 10 | 10 | 10 | 0.000 | 48.000 | 21992.400 | — |
| b11-broad | BabyAI-SynthS5R2-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 48.000 | 21992.400 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B0 | 10 | 10 | 10 | 1.000 | 32.300 | 10675.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B0G | 10 | 10 | 10 | 1.000 | 32.300 | 10675.500 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B1 | 10 | 10 | 10 | 1.000 | 36.000 | 20601.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B10 | 10 | 10 | 10 | 1.000 | 10.100 | 3807.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B11 | 10 | 10 | 10 | 1.000 | 10.100 | 3718.500 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B2 | 10 | 10 | 10 | 0.400 | 42.200 | 27568.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B3 | 10 | 10 | 10 | 1.000 | 32.300 | 20681.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B3G | 10 | 10 | 10 | 1.000 | 32.300 | 20663.400 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B4 | 10 | 10 | 10 | 1.000 | 32.500 | 11871.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B5 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B6 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B7 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B8 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B9 | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | B9N | 10 | 10 | 10 | 1.000 | 10.300 | 3790.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B0 | 10 | 10 | 10 | 1.000 | 32.300 | 10640.500 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B0G | 10 | 10 | 10 | 1.000 | 32.300 | 10641.100 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B1 | 10 | 10 | 10 | 1.000 | 34.100 | 19492.700 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B10 | 10 | 10 | 10 | 1.000 | 10.100 | 3753.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B11 | 10 | 10 | 10 | 1.000 | 10.100 | 3664.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B2 | 10 | 10 | 10 | 0.500 | 40.500 | 26237.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B3 | 10 | 10 | 10 | 1.000 | 32.300 | 20600.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B3G | 10 | 10 | 10 | 1.000 | 32.300 | 20593.400 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B4 | 10 | 10 | 10 | 1.000 | 32.300 | 11763.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B5 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B6 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B7 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B8 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B9 | 10 | 10 | 10 | 1.000 | 10.500 | 3824.300 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | B9N | 10 | 10 | 10 | 1.000 | 10.400 | 3779.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B0 | 10 | 10 | 10 | 1.000 | 26.400 | 8557.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B0G | 10 | 10 | 10 | 1.000 | 26.400 | 8557.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B1 | 10 | 10 | 10 | 0.900 | 29.500 | 16650.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B10 | 10 | 10 | 10 | 0.400 | 33.600 | 14265.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B11 | 10 | 10 | 10 | 0.400 | 33.600 | 13918.600 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B2 | 10 | 10 | 10 | 0.300 | 41.200 | 26733.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B3 | 10 | 10 | 10 | 0.900 | 28.500 | 17964.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B3G | 10 | 10 | 10 | 1.000 | 26.400 | 16514.200 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B4 | 10 | 10 | 10 | 1.000 | 26.400 | 9610.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B5 | 10 | 10 | 10 | 1.000 | 24.500 | 10087.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B6 | 10 | 10 | 10 | 1.000 | 24.500 | 10087.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B7 | 10 | 10 | 10 | 1.000 | 24.500 | 10087.900 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B8 | 10 | 10 | 10 | 0.800 | 25.600 | 10587.800 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B9 | 10 | 10 | 10 | 1.000 | 23.900 | 9820.000 | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | B9N | 10 | 10 | 10 | 1.000 | 23.900 | 9820.000 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B0 | 10 | 10 | 10 | 0.300 | 38.200 | 13697.300 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B0G | 10 | 10 | 10 | 0.400 | 36.000 | 12917.900 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 48.000 | 29653.000 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 18.000 | 8431.800 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 18.000 | 8234.400 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B2 | 10 | 10 | 10 | 0.100 | 44.700 | 25758.900 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B3 | 10 | 10 | 10 | 0.200 | 42.600 | 27598.200 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B3G | 10 | 10 | 10 | 0.400 | 39.100 | 24995.100 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B4 | 10 | 10 | 10 | 0.200 | 43.500 | 16729.900 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B5 | 10 | 10 | 10 | 0.100 | 44.600 | 20587.800 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 23440.100 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B7 | 10 | 10 | 10 | 1.000 | 16.600 | 7846.400 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B8 | 10 | 10 | 10 | 0.100 | 44.600 | 20578.900 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B9 | 10 | 10 | 10 | 0.100 | 44.600 | 20577.500 | — |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | B9N | 10 | 10 | 10 | 0.100 | 44.600 | 20577.500 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 2.200 | 678.100 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B0G | 10 | 10 | 10 | 0.800 | 28.000 | 8599.900 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 2.100 | 684.100 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B10 | 10 | 10 | 10 | 0.800 | 32.100 | 12340.900 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B11 | 10 | 10 | 10 | 0.800 | 32.100 | 11985.500 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 2.000 | 641.500 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 2.400 | 829.400 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B3G | 10 | 10 | 10 | 0.800 | 30.400 | 12647.000 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B4 | 10 | 10 | 10 | 0.900 | 26.900 | 8601.900 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 18689.100 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 18689.100 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 18689.100 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B8 | 10 | 10 | 10 | 0.800 | 32.100 | 12340.900 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B9 | 10 | 10 | 10 | 0.000 | 48.000 | 18731.600 | — |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 48.000 | 18731.600 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B0 | 10 | 10 | 10 | 0.800 | 6.100 | 2406.400 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B0G | 10 | 10 | 10 | 0.800 | 6.100 | 2406.400 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B1 | 10 | 10 | 10 | 0.300 | 36.800 | 24737.000 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 11.900 | 5967.900 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 11.900 | 5835.700 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B2 | 10 | 10 | 10 | 0.300 | 35.500 | 20410.300 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B3 | 10 | 10 | 10 | 0.200 | 35.300 | 20497.800 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B3G | 10 | 10 | 10 | 0.700 | 6.100 | 3414.600 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B4 | 10 | 10 | 10 | 0.800 | 6.100 | 2485.700 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 22228.600 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 22228.600 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 22228.600 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B8 | 10 | 10 | 10 | 0.800 | 14.200 | 7053.800 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B9 | 10 | 10 | 10 | 1.000 | 11.900 | 5967.900 | — |
| b11-broad | MiniGrid-MemoryS13-v0 | none | B9N | 10 | 10 | 10 | 0.500 | 30.400 | 14993.600 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B0 | 10 | 10 | 10 | 0.200 | 7.000 | 2763.200 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B0G | 10 | 10 | 10 | 0.200 | 7.000 | 2761.900 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B1 | 10 | 10 | 10 | 0.500 | 28.500 | 18723.900 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 14.000 | 7041.600 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 14.000 | 6886.800 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 43.600 | 25809.000 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B3 | 10 | 10 | 10 | 0.200 | 23.000 | 14177.200 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B3G | 10 | 10 | 10 | 0.200 | 7.000 | 4154.600 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B4 | 10 | 10 | 10 | 0.200 | 7.000 | 2850.700 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 22320.400 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 22320.400 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 22320.400 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B8 | 10 | 10 | 10 | 0.400 | 30.800 | 14974.900 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B9 | 10 | 10 | 10 | 1.000 | 14.000 | 7041.600 | — |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | B9N | 10 | 10 | 10 | 0.400 | 35.200 | 17109.100 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 48.000 | 17074.700 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 48.000 | 17055.800 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 48.000 | 29145.400 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B10 | 10 | 10 | 10 | 0.600 | 45.000 | 19919.200 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B11 | 10 | 10 | 10 | 0.600 | 45.000 | 19413.300 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 48.000 | 26362.000 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 48.000 | 28181.700 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 48.000 | 28591.600 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 48.000 | 17452.200 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 48.000 | 20900.200 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 48.000 | 20900.200 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 48.000 | 20900.200 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 48.000 | 20923.400 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B9 | 10 | 10 | 10 | 0.000 | 48.000 | 20825.700 | — |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 48.000 | 20825.700 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11 | 30 | 30 | 30 | 0.433 | 36.033 | 15423.433 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11C | 30 | 30 | 30 | 0.433 | 36.033 | 0.000 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11P | 30 | 30 | 30 | 0.433 | 36.033 | 15423.400 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11R | 30 | 30 | 30 | 0.433 | 36.033 | 15423.433 | — |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | B11T | 30 | 30 | 30 | 0.433 | 36.033 | 23802.500 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | B11 | 30 | 30 | 30 | 1.000 | 10.667 | 3957.600 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | B11C | 30 | 30 | 30 | 1.000 | 10.667 | 0.000 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | B11P | 30 | 30 | 30 | 1.000 | 10.667 | 3957.600 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | B11PA | 30 | 30 | 30 | 1.000 | 10.667 | 3957.600 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | B11R | 30 | 30 | 30 | 1.000 | 10.667 | 3957.600 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | B11T | 30 | 30 | 30 | 0.800 | 33.533 | 20661.767 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | B11 | 30 | 30 | 30 | 1.000 | 10.667 | 3900.800 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | B11C | 30 | 30 | 30 | 1.000 | 10.667 | 0.000 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | B11P | 30 | 30 | 30 | 1.000 | 10.667 | 3900.800 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | B11PA | 30 | 30 | 30 | 1.000 | 10.667 | 3900.800 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | B11R | 30 | 30 | 30 | 1.000 | 10.667 | 3900.800 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | B11T | 30 | 30 | 30 | 1.000 | 22.800 | 13008.767 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | B11 | 30 | 30 | 30 | 0.767 | 20.800 | 8390.033 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | B11C | 30 | 30 | 30 | 0.767 | 20.800 | 0.000 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | B11P | 30 | 30 | 30 | 0.267 | 38.400 | 16920.067 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | B11PA | 30 | 30 | 30 | 0.267 | 38.400 | 16920.067 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | B11R | 30 | 30 | 30 | 0.767 | 20.800 | 8390.033 | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | B11T | 30 | 30 | 30 | 1.000 | 17.800 | 9440.267 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11 | 30 | 30 | 30 | 0.967 | 19.567 | 8895.067 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11C | 30 | 30 | 30 | 0.967 | 19.567 | 0.000 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11P | 30 | 30 | 30 | 0.000 | 48.000 | 22523.267 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11R | 30 | 30 | 30 | 0.967 | 19.567 | 8895.067 | — |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | B11T | 30 | 30 | 30 | 0.900 | 22.567 | 13820.833 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B0 | 10 | 10 | 10 | 0.000 | 80.000 | 28420.500 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B0G | 10 | 10 | 10 | 0.000 | 80.000 | 28420.700 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B1 | 10 | 10 | 10 | 0.000 | 80.000 | 50585.800 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B10 | 10 | 10 | 10 | 1.000 | 49.800 | 22073.700 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B11 | 10 | 10 | 10 | 1.000 | 49.800 | 21515.900 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B2 | 10 | 10 | 10 | 0.000 | 80.000 | 43887.500 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B3 | 10 | 10 | 10 | 0.000 | 80.000 | 47274.000 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B3G | 10 | 10 | 10 | 0.000 | 80.000 | 48085.900 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B4 | 10 | 10 | 10 | 0.000 | 80.000 | 29109.800 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B5 | 10 | 10 | 10 | 0.000 | 80.000 | 34831.600 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B6 | 10 | 10 | 10 | 0.000 | 80.000 | 34831.600 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B7 | 10 | 10 | 10 | 0.000 | 80.000 | 34831.600 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B8 | 10 | 10 | 10 | 0.000 | 80.000 | 34893.200 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B9 | 10 | 10 | 10 | 0.000 | 80.000 | 34712.100 | — |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | B9N | 10 | 10 | 10 | 0.000 | 80.000 | 34712.100 | — |

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | total_tokens | B11 − B10 | 10 | -305.600 | [-334.000, -281.600] |
| b11-broad | BabyAI-BlockedUnlockPickup-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.131 | [-0.354, 0.025] |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11 − B10 | 10 | -317.500 | [-445.500, -197.900] |
| b11-broad | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.585 | [-1.059, -0.178] |
| b11-broad | BabyAI-GoToObjS6-v1 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-GoToObjS6-v1 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-GoToObjS6-v1 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-GoToObjS6-v1 | none | total_tokens | B11 − B10 | 10 | -46.200 | [-61.600, -33.000] |
| b11-broad | BabyAI-GoToObjS6-v1 | none | episode_wall_seconds | B11 − B10 | 10 | 0.027 | [-0.018, 0.074] |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | total_tokens | B11 − B10 | 10 | -365.400 | [-425.900, -302.700] |
| b11-broad | BabyAI-KeyCorridorS3R3-v0 | none | episode_wall_seconds | B11 − B10 | 10 | 0.208 | [0.014, 0.427] |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | total_tokens | B11 − B10 | 10 | -143.400 | [-178.200, -111.400] |
| b11-broad | BabyAI-PutNextS5N2-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.082 | [-0.154, -0.023] |
| b11-broad | BabyAI-SynthS5R2-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-SynthS5R2-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-SynthS5R2-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | BabyAI-SynthS5R2-v0 | none | total_tokens | B11 − B10 | 10 | -444.700 | [-538.500, -326.500] |
| b11-broad | BabyAI-SynthS5R2-v0 | none | episode_wall_seconds | B11 − B10 | 10 | 0.102 | [-0.442, 0.577] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11 − B10 | 10 | -89.100 | [-91.300, -88.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11 − B10 | 10 | 0.300 | [0.000, 0.800] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11 − B10 | 10 | 0.200 | [0.000, 0.500] |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11 − B10 | 10 | -0.041 | [-0.106, 0.034] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11 − B10 | 10 | -89.100 | [-91.300, -88.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11 − B10 | 10 | -0.032 | [-0.082, 0.020] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11 − B10 | 10 | -346.600 | [-464.900, -228.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11 − B10 | 0 | — | — |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11 − B10 | 10 | 0.104 | [-0.079, 0.311] |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11 − B10 | 10 | -197.400 | [-228.200, -169.400] |
| b11-broad | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.254 | [-0.372, -0.135] |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | total_tokens | B11 − B10 | 10 | -355.400 | [-439.800, -263.600] |
| b11-broad | MiniGrid-Dynamic-Obstacles-8x8-v0 | none | episode_wall_seconds | B11 − B10 | 10 | 0.112 | [-0.052, 0.273] |
| b11-broad | MiniGrid-MemoryS13-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MemoryS13-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MemoryS13-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MemoryS13-v0 | none | total_tokens | B11 − B10 | 10 | -132.200 | [-141.100, -123.700] |
| b11-broad | MiniGrid-MemoryS13-v0 | none | episode_wall_seconds | B11 − B10 | 10 | 0.030 | [-0.022, 0.080] |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | total_tokens | B11 − B10 | 10 | -154.800 | [-181.300, -129.600] |
| b11-broad | MiniGrid-MemoryS17Random-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.126 | [-0.298, -0.001] |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | total_tokens | B11 − B10 | 10 | -505.900 | [-527.800, -482.200] |
| b11-broad | MiniGrid-MultiRoom-N6-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.221 | [-0.400, -0.024] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11P − B11T | 30 | -8379.100 | [-9971.167, -6698.367] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11P − B11T | 30 | -2.544 | [-3.164, -1.957] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11R − B11T | 30 | -8379.067 | [-9971.133, -6698.400] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11R − B11T | 30 | -2.562 | [-3.173, -1.985] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11R − B11P | 30 | 0.033 | [-0.067, 0.133] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11R − B11P | 30 | -0.018 | [-0.090, 0.057] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11 − B11R | 30 | 0.008 | [-0.065, 0.082] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | calls | B11 − B11C | 30 | 36.033 | [29.933, 41.667] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | total_tokens | B11 − B11C | 30 | 15423.433 | [12848.133, 17818.500] |
| b11-mechanisms | BabyAI-GoToObjMazeS7-v0 | none | episode_wall_seconds | B11 − B11C | 30 | 9.882 | [8.250, 11.395] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11P − B11T | 30 | 0.200 | [0.067, 0.367] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11P − B11T | 30 | -22.867 | [-27.600, -18.400] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11P − B11T | 30 | -22.867 | [-27.600, -18.400] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11P − B11T | 30 | -16704.167 | [-20103.667, -13474.933] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11P − B11T | 30 | 0.133 | [0.033, 0.267] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11P − B11T | 30 | 0.133 | [0.033, 0.267] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11P − B11T | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11P − B11T | 30 | -8.120 | [-9.984, -6.365] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11R − B11T | 30 | 0.200 | [0.067, 0.367] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11R − B11T | 30 | -22.867 | [-27.600, -18.400] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11R − B11T | 30 | -22.867 | [-27.600, -18.400] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11R − B11T | 30 | -16704.167 | [-20103.667, -13474.933] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11R − B11T | 30 | 0.133 | [0.033, 0.267] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11R − B11T | 30 | 0.133 | [0.033, 0.267] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11R − B11T | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11R − B11T | 30 | -8.148 | [-10.034, -6.380] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11R − B11P | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11R − B11P | 30 | -0.028 | [-0.074, 0.017] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11 − B11PA | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11 − B11PA | 30 | -0.011 | [-0.055, 0.033] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11 − B11R | 30 | 0.300 | [0.100, 0.533] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11 − B11R | 30 | 0.267 | [0.067, 0.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11 − B11R | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11 − B11R | 30 | 0.002 | [-0.032, 0.036] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11PA − B11P | 30 | 0.300 | [0.100, 0.533] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11PA − B11P | 30 | 0.267 | [0.067, 0.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11PA − B11P | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11PA − B11P | 30 | -0.015 | [-0.062, 0.031] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | calls | B11 − B11C | 30 | 8.667 | [8.500, 8.833] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | total_tokens | B11 − B11C | 30 | 3957.600 | [3884.267, 4027.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | verification_actions | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | informative_checks | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | stale_commitments | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | reacquired | B11 − B11C | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | dropout | episode_wall_seconds | B11 − B11C | 30 | 2.791 | [2.716, 2.866] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11P − B11T | 30 | -12.133 | [-12.867, -11.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11P − B11T | 30 | -12.133 | [-12.867, -11.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11P − B11T | 30 | -9107.967 | [-9565.833, -8647.100] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11P − B11T | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11P − B11T | 30 | -4.592 | [-5.115, -4.185] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11R − B11T | 30 | -12.133 | [-12.867, -11.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11R − B11T | 30 | -12.133 | [-12.867, -11.467] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11R − B11T | 30 | -9107.967 | [-9565.833, -8647.100] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11R − B11T | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11R − B11T | 30 | -4.669 | [-5.189, -4.272] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11R − B11P | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11R − B11P | 30 | -0.077 | [-0.133, -0.023] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11 − B11PA | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11 − B11PA | 30 | 0.044 | [-0.015, 0.117] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11 − B11R | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11 − B11R | 30 | 0.028 | [-0.041, 0.103] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11PA − B11P | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11PA − B11P | 30 | -0.093 | [-0.148, -0.042] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | calls | B11 − B11C | 30 | 8.667 | [8.500, 8.833] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | total_tokens | B11 − B11C | 30 | 3900.800 | [3831.067, 3970.300] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | verification_actions | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | informative_checks | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | stale_commitments | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | reacquired | B11 − B11C | 0 | — | — |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | no_change | episode_wall_seconds | B11 − B11C | 30 | 2.781 | [2.706, 2.854] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11P − B11T | 30 | -0.733 | [-0.867, -0.567] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11P − B11T | 30 | 20.600 | [14.733, 25.667] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11P − B11T | 30 | 20.600 | [14.733, 25.667] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11P − B11T | 30 | 7479.800 | [4753.300, 9895.567] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11P − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11P − B11T | 30 | 18.100 | [13.967, 21.500] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11P − B11T | 30 | -0.233 | [-0.400, -0.100] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11P − B11T | 30 | 6.452 | [4.459, 8.253] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11R − B11T | 30 | -0.233 | [-0.400, -0.100] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11R − B11T | 30 | 3.000 | [-1.833, 8.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11R − B11T | 30 | 3.000 | [-1.833, 8.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11R − B11T | 30 | -1050.233 | [-3144.233, 1351.433] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11R − B11T | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11R − B11T | 30 | -0.233 | [-0.400, -0.100] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11R − B11T | 30 | 0.132 | [-1.303, 1.783] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11R − B11P | 30 | 0.500 | [0.333, 0.667] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11R − B11P | 30 | -17.600 | [-23.533, -11.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11R − B11P | 30 | -17.600 | [-23.533, -11.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11R − B11P | 30 | -8530.033 | [-11305.667, -5753.900] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11R − B11P | 30 | -18.100 | [-21.500, -13.967] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11R − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11R − B11P | 30 | -6.320 | [-8.424, -4.230] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11 − B11PA | 30 | 0.500 | [0.333, 0.667] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11 − B11PA | 30 | -17.600 | [-23.533, -11.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11 − B11PA | 30 | -17.600 | [-23.533, -11.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11 − B11PA | 30 | -8530.033 | [-11305.667, -5753.900] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11 − B11PA | 30 | -1.500 | [-2.000, -1.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11 − B11PA | 30 | -0.500 | [-0.667, -0.333] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11 − B11PA | 30 | -16.600 | [-19.800, -12.800] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11 − B11PA | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11 − B11PA | 30 | -6.152 | [-8.187, -4.114] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11 − B11R | 30 | 0.095 | [-0.027, 0.235] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11PA − B11P | 30 | 1.500 | [1.000, 2.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11PA − B11P | 30 | 0.500 | [0.333, 0.667] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11PA − B11P | 30 | -1.500 | [-2.000, -1.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11PA − B11P | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11PA − B11P | 30 | -0.072 | [-0.246, 0.099] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | calls | B11 − B11C | 30 | 18.800 | [14.033, 24.700] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | total_tokens | B11 − B11C | 30 | 8390.033 | [6328.833, 10934.800] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | verification_actions | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | informative_checks | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | stale_commitments | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | reacquired | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | EmbodiedMind-GoToShift-v0 | relocation | episode_wall_seconds | B11 − B11C | 30 | 5.776 | [4.387, 7.416] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11P − B11T | 30 | -0.900 | [-1.000, -0.800] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11P − B11T | 30 | 25.433 | [21.267, 29.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11P − B11T | 30 | 25.433 | [21.267, 29.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11P − B11T | 30 | 8702.433 | [5645.600, 11353.967] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11P − B11T | 30 | 7.822 | [6.114, 9.330] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11R − B11T | 30 | 0.067 | [0.000, 0.167] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11R − B11T | 30 | -3.000 | [-5.933, -0.667] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11R − B11T | 30 | -3.000 | [-5.933, -0.667] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11R − B11T | 30 | -4925.767 | [-7162.200, -3103.833] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11R − B11T | 30 | -2.197 | [-3.288, -1.275] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11R − B11P | 30 | 0.967 | [0.900, 1.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11R − B11P | 30 | -28.433 | [-30.800, -25.600] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11R − B11P | 30 | -28.433 | [-30.800, -25.600] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11R − B11P | 30 | -13628.200 | [-14822.267, -12262.300] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11R − B11P | 30 | -10.018 | [-10.846, -9.100] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11 − B11R | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11 − B11R | 30 | -0.030 | [-0.110, 0.049] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | success | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | steps | B11 − B11C | 30 | 0.000 | [0.000, 0.000] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | calls | B11 − B11C | 30 | 19.567 | [17.200, 22.400] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | total_tokens | B11 − B11C | 30 | 8895.067 | [7865.533, 10111.833] |
| b11-mechanisms | MiniGrid-DoorKey-8x8-v0 | none | episode_wall_seconds | B11 − B11C | 30 | 6.180 | [5.503, 6.975] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | success | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | steps | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | calls | B11 − B10 | 10 | 0.000 | [0.000, 0.000] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | total_tokens | B11 − B10 | 10 | -557.800 | [-627.100, -495.900] |
| b11-multiroom-80 | MiniGrid-MultiRoom-N6-v0 | none | episode_wall_seconds | B11 − B10 | 10 | -0.148 | [-0.466, 0.221] |

## Cost per completed mission

Costs sum across every valid episode, including failures. A dash means zero completions.

| Environment | Intervention | Agent | Completions | Actions / completion | Tokens / completion | Seconds / completion |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| BabyAI-BlockedUnlockPickup-v0 | none | B0 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B0G | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B1 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B10 | 10 | 27.50 | 12678.70 | 8.55 |
| BabyAI-BlockedUnlockPickup-v0 | none | B11 | 10 | 27.50 | 12373.10 | 8.42 |
| BabyAI-BlockedUnlockPickup-v0 | none | B2 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B3 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B3G | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B4 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B5 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B6 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B7 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B8 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B9 | 0 | — | — | — |
| BabyAI-BlockedUnlockPickup-v0 | none | B9N | 0 | — | — | — |
| BabyAI-GoToObjMazeS7-v0 | none | B0 | 2 | 194.00 | 68232.50 | 33.61 |
| BabyAI-GoToObjMazeS7-v0 | none | B0G | 2 | 194.00 | 68281.50 | 34.84 |
| BabyAI-GoToObjMazeS7-v0 | none | B1 | 2 | 194.00 | 117095.00 | 50.35 |
| BabyAI-GoToObjMazeS7-v0 | none | B10 | 6 | 47.33 | 20898.50 | 14.93 |
| BabyAI-GoToObjMazeS7-v0 | none | B11 | 6 | 47.33 | 20369.33 | 13.95 |
| BabyAI-GoToObjMazeS7-v0 | none | B2 | 3 | 119.33 | 75416.33 | 27.97 |
| BabyAI-GoToObjMazeS7-v0 | none | B3 | 2 | 194.00 | 126261.50 | 57.45 |
| BabyAI-GoToObjMazeS7-v0 | none | B3G | 2 | 194.00 | 126304.00 | 59.96 |
| BabyAI-GoToObjMazeS7-v0 | none | B4 | 2 | 194.00 | 69481.50 | 31.06 |
| BabyAI-GoToObjMazeS7-v0 | none | B5 | 2 | 194.00 | 83779.00 | 55.70 |
| BabyAI-GoToObjMazeS7-v0 | none | B6 | 2 | 194.00 | 83779.00 | 56.65 |
| BabyAI-GoToObjMazeS7-v0 | none | B7 | 2 | 194.00 | 83779.00 | 56.98 |
| BabyAI-GoToObjMazeS7-v0 | none | B8 | 2 | 194.00 | 83799.00 | 55.40 |
| BabyAI-GoToObjMazeS7-v0 | none | B9 | 2 | 194.00 | 83622.50 | 61.23 |
| BabyAI-GoToObjMazeS7-v0 | none | B9N | 2 | 194.00 | 83622.50 | 57.53 |
| BabyAI-GoToObjS6-v1 | none | B0 | 10 | 5.10 | 1765.00 | 0.96 |
| BabyAI-GoToObjS6-v1 | none | B0G | 10 | 5.00 | 1729.50 | 0.87 |
| BabyAI-GoToObjS6-v1 | none | B1 | 10 | 5.00 | 1966.90 | 0.83 |
| BabyAI-GoToObjS6-v1 | none | B10 | 10 | 4.20 | 1896.70 | 1.29 |
| BabyAI-GoToObjS6-v1 | none | B11 | 10 | 4.20 | 1850.50 | 1.32 |
| BabyAI-GoToObjS6-v1 | none | B2 | 10 | 5.00 | 2466.60 | 1.09 |
| BabyAI-GoToObjS6-v1 | none | B3 | 10 | 5.60 | 2851.20 | 1.33 |
| BabyAI-GoToObjS6-v1 | none | B3G | 10 | 5.60 | 2851.30 | 1.24 |
| BabyAI-GoToObjS6-v1 | none | B4 | 7 | 19.00 | 6816.71 | 2.82 |
| BabyAI-GoToObjS6-v1 | none | B5 | 10 | 3.80 | 1679.60 | 1.23 |
| BabyAI-GoToObjS6-v1 | none | B6 | 10 | 3.80 | 1679.60 | 1.18 |
| BabyAI-GoToObjS6-v1 | none | B7 | 10 | 3.80 | 1679.60 | 1.19 |
| BabyAI-GoToObjS6-v1 | none | B8 | 10 | 3.80 | 1679.60 | 1.16 |
| BabyAI-GoToObjS6-v1 | none | B9 | 10 | 3.80 | 1679.60 | 1.16 |
| BabyAI-GoToObjS6-v1 | none | B9N | 10 | 3.80 | 1679.60 | 1.27 |
| BabyAI-KeyCorridorS3R3-v0 | none | B0 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B0G | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B1 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B10 | 10 | 32.40 | 15083.30 | 9.77 |
| BabyAI-KeyCorridorS3R3-v0 | none | B11 | 10 | 32.40 | 14717.90 | 9.98 |
| BabyAI-KeyCorridorS3R3-v0 | none | B2 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B3 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B3G | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B4 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B5 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B6 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B7 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B8 | 0 | — | — | — |
| BabyAI-KeyCorridorS3R3-v0 | none | B9 | 10 | 32.40 | 15083.40 | 9.91 |
| BabyAI-KeyCorridorS3R3-v0 | none | B9N | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B0 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B0G | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B1 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B10 | 10 | 12.80 | 6210.40 | 4.18 |
| BabyAI-PutNextS5N2-v0 | none | B11 | 10 | 12.80 | 6067.00 | 4.09 |
| BabyAI-PutNextS5N2-v0 | none | B2 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B3 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B3G | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B4 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B5 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B6 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B7 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B8 | 0 | — | — | — |
| BabyAI-PutNextS5N2-v0 | none | B9 | 10 | 10.30 | 5035.40 | 3.46 |
| BabyAI-PutNextS5N2-v0 | none | B9N | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B0 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B0G | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B1 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B10 | 1 | 438.00 | 206282.00 | 138.37 |
| BabyAI-SynthS5R2-v0 | none | B11 | 1 | 438.00 | 201835.00 | 139.39 |
| BabyAI-SynthS5R2-v0 | none | B2 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B3 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B3G | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B4 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B5 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B6 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B7 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B8 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B9 | 0 | — | — | — |
| BabyAI-SynthS5R2-v0 | none | B9N | 0 | — | — | — |
| EmbodiedMind-GoToShift-v0 | dropout | B0 | 10 | 32.30 | 10675.30 | 5.25 |
| EmbodiedMind-GoToShift-v0 | dropout | B0G | 10 | 32.30 | 10675.50 | 5.09 |
| EmbodiedMind-GoToShift-v0 | dropout | B1 | 10 | 36.00 | 20601.60 | 8.26 |
| EmbodiedMind-GoToShift-v0 | dropout | B10 | 10 | 10.10 | 3807.60 | 2.73 |
| EmbodiedMind-GoToShift-v0 | dropout | B11 | 10 | 10.10 | 3718.50 | 2.69 |
| EmbodiedMind-GoToShift-v0 | dropout | B2 | 4 | 105.50 | 68920.75 | 26.38 |
| EmbodiedMind-GoToShift-v0 | dropout | B3 | 10 | 32.30 | 20681.20 | 10.07 |
| EmbodiedMind-GoToShift-v0 | dropout | B3G | 10 | 32.30 | 20663.40 | 8.23 |
| EmbodiedMind-GoToShift-v0 | dropout | B4 | 10 | 32.50 | 11871.80 | 5.95 |
| EmbodiedMind-GoToShift-v0 | dropout | B5 | 10 | 10.30 | 3790.80 | 2.80 |
| EmbodiedMind-GoToShift-v0 | dropout | B6 | 10 | 10.30 | 3790.80 | 2.76 |
| EmbodiedMind-GoToShift-v0 | dropout | B7 | 10 | 10.30 | 3790.80 | 2.78 |
| EmbodiedMind-GoToShift-v0 | dropout | B8 | 10 | 10.30 | 3790.80 | 2.82 |
| EmbodiedMind-GoToShift-v0 | dropout | B9 | 10 | 10.30 | 3790.80 | 2.74 |
| EmbodiedMind-GoToShift-v0 | dropout | B9N | 10 | 10.30 | 3790.80 | 2.81 |
| EmbodiedMind-GoToShift-v0 | no_change | B0 | 10 | 32.30 | 10640.50 | 5.11 |
| EmbodiedMind-GoToShift-v0 | no_change | B0G | 10 | 32.30 | 10641.10 | 9.28 |
| EmbodiedMind-GoToShift-v0 | no_change | B1 | 10 | 34.10 | 19492.70 | 8.36 |
| EmbodiedMind-GoToShift-v0 | no_change | B10 | 10 | 10.10 | 3753.30 | 2.75 |
| EmbodiedMind-GoToShift-v0 | no_change | B11 | 10 | 10.10 | 3664.20 | 2.72 |
| EmbodiedMind-GoToShift-v0 | no_change | B2 | 5 | 81.00 | 52475.60 | 20.07 |
| EmbodiedMind-GoToShift-v0 | no_change | B3 | 10 | 32.30 | 20600.20 | 10.27 |
| EmbodiedMind-GoToShift-v0 | no_change | B3G | 10 | 32.30 | 20593.40 | 8.68 |
| EmbodiedMind-GoToShift-v0 | no_change | B4 | 10 | 32.30 | 11763.90 | 5.88 |
| EmbodiedMind-GoToShift-v0 | no_change | B5 | 10 | 10.50 | 3824.30 | 2.92 |
| EmbodiedMind-GoToShift-v0 | no_change | B6 | 10 | 10.50 | 3824.30 | 2.87 |
| EmbodiedMind-GoToShift-v0 | no_change | B7 | 10 | 10.50 | 3824.30 | 2.87 |
| EmbodiedMind-GoToShift-v0 | no_change | B8 | 10 | 10.50 | 3824.30 | 2.85 |
| EmbodiedMind-GoToShift-v0 | no_change | B9 | 10 | 10.50 | 3824.30 | 2.87 |
| EmbodiedMind-GoToShift-v0 | no_change | B9N | 10 | 10.40 | 3779.90 | 2.93 |
| EmbodiedMind-GoToShift-v0 | relocation | B0 | 10 | 26.40 | 8557.90 | 4.15 |
| EmbodiedMind-GoToShift-v0 | relocation | B0G | 10 | 26.40 | 8557.60 | 4.28 |
| EmbodiedMind-GoToShift-v0 | relocation | B1 | 9 | 32.78 | 18500.67 | 8.62 |
| EmbodiedMind-GoToShift-v0 | relocation | B10 | 4 | 84.00 | 35663.00 | 24.02 |
| EmbodiedMind-GoToShift-v0 | relocation | B11 | 4 | 84.00 | 34796.50 | 24.28 |
| EmbodiedMind-GoToShift-v0 | relocation | B2 | 3 | 137.33 | 89110.00 | 29.77 |
| EmbodiedMind-GoToShift-v0 | relocation | B3 | 9 | 31.67 | 19960.00 | 9.95 |
| EmbodiedMind-GoToShift-v0 | relocation | B3G | 10 | 26.40 | 16514.20 | 6.68 |
| EmbodiedMind-GoToShift-v0 | relocation | B4 | 10 | 26.40 | 9610.00 | 4.90 |
| EmbodiedMind-GoToShift-v0 | relocation | B5 | 10 | 24.50 | 10087.90 | 6.98 |
| EmbodiedMind-GoToShift-v0 | relocation | B6 | 10 | 24.50 | 10087.90 | 7.07 |
| EmbodiedMind-GoToShift-v0 | relocation | B7 | 10 | 24.50 | 10087.90 | 7.03 |
| EmbodiedMind-GoToShift-v0 | relocation | B8 | 8 | 32.00 | 13234.75 | 8.98 |
| EmbodiedMind-GoToShift-v0 | relocation | B9 | 10 | 23.90 | 9820.00 | 6.72 |
| EmbodiedMind-GoToShift-v0 | relocation | B9N | 10 | 23.90 | 9820.00 | 6.79 |
| MiniGrid-DoorKey-8x8-v0 | none | B0 | 3 | 127.33 | 45657.67 | 19.33 |
| MiniGrid-DoorKey-8x8-v0 | none | B0G | 4 | 90.00 | 32294.75 | 14.60 |
| MiniGrid-DoorKey-8x8-v0 | none | B1 | 0 | — | — | — |
| MiniGrid-DoorKey-8x8-v0 | none | B10 | 10 | 18.00 | 8431.80 | 6.06 |
| MiniGrid-DoorKey-8x8-v0 | none | B11 | 10 | 18.00 | 8234.40 | 5.80 |
| MiniGrid-DoorKey-8x8-v0 | none | B2 | 1 | 447.00 | 257589.00 | 97.07 |
| MiniGrid-DoorKey-8x8-v0 | none | B3 | 2 | 213.00 | 137991.00 | 55.20 |
| MiniGrid-DoorKey-8x8-v0 | none | B3G | 4 | 97.75 | 62487.75 | 27.89 |
| MiniGrid-DoorKey-8x8-v0 | none | B4 | 2 | 217.50 | 83649.50 | 40.03 |
| MiniGrid-DoorKey-8x8-v0 | none | B5 | 1 | 446.00 | 205878.00 | 152.16 |
| MiniGrid-DoorKey-8x8-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-DoorKey-8x8-v0 | none | B7 | 10 | 16.60 | 7846.40 | 5.56 |
| MiniGrid-DoorKey-8x8-v0 | none | B8 | 1 | 446.00 | 205789.00 | 150.39 |
| MiniGrid-DoorKey-8x8-v0 | none | B9 | 1 | 446.00 | 205775.00 | 149.80 |
| MiniGrid-DoorKey-8x8-v0 | none | B9N | 1 | 446.00 | 205775.00 | 149.32 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B0 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B0G | 8 | 35.00 | 10749.88 | 6.43 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B1 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B10 | 8 | 40.12 | 15426.12 | 11.90 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B11 | 8 | 40.12 | 14981.88 | 12.04 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B2 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B3 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B3G | 8 | 38.00 | 15808.75 | 8.35 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B4 | 9 | 29.89 | 9557.67 | 4.98 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B5 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B7 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B8 | 8 | 40.12 | 15426.12 | 11.89 |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B9 | 0 | — | — | — |
| MiniGrid-Dynamic-Obstacles-8x8-v0 | none | B9N | 0 | — | — | — |
| MiniGrid-MemoryS13-v0 | none | B0 | 8 | 7.62 | 3008.00 | 1.58 |
| MiniGrid-MemoryS13-v0 | none | B0G | 8 | 7.62 | 3008.00 | 1.55 |
| MiniGrid-MemoryS13-v0 | none | B1 | 3 | 122.67 | 82456.67 | 43.18 |
| MiniGrid-MemoryS13-v0 | none | B10 | 10 | 11.90 | 5967.90 | 3.79 |
| MiniGrid-MemoryS13-v0 | none | B11 | 10 | 11.90 | 5835.70 | 3.82 |
| MiniGrid-MemoryS13-v0 | none | B2 | 3 | 118.33 | 68034.33 | 25.26 |
| MiniGrid-MemoryS13-v0 | none | B3 | 2 | 176.50 | 102489.00 | 37.72 |
| MiniGrid-MemoryS13-v0 | none | B3G | 7 | 8.71 | 4878.00 | 2.40 |
| MiniGrid-MemoryS13-v0 | none | B4 | 8 | 7.62 | 3107.12 | 1.59 |
| MiniGrid-MemoryS13-v0 | none | B5 | 0 | — | — | — |
| MiniGrid-MemoryS13-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-MemoryS13-v0 | none | B7 | 0 | — | — | — |
| MiniGrid-MemoryS13-v0 | none | B8 | 8 | 17.75 | 8817.25 | 5.41 |
| MiniGrid-MemoryS13-v0 | none | B9 | 10 | 11.90 | 5967.90 | 3.79 |
| MiniGrid-MemoryS13-v0 | none | B9N | 5 | 60.80 | 29987.20 | 18.41 |
| MiniGrid-MemoryS17Random-v0 | none | B0 | 2 | 35.00 | 13816.00 | 6.56 |
| MiniGrid-MemoryS17Random-v0 | none | B0G | 2 | 35.00 | 13809.50 | 6.60 |
| MiniGrid-MemoryS17Random-v0 | none | B1 | 5 | 57.00 | 37447.80 | 17.34 |
| MiniGrid-MemoryS17Random-v0 | none | B10 | 10 | 14.00 | 7041.60 | 4.31 |
| MiniGrid-MemoryS17Random-v0 | none | B11 | 10 | 14.00 | 6886.80 | 4.19 |
| MiniGrid-MemoryS17Random-v0 | none | B2 | 0 | — | — | — |
| MiniGrid-MemoryS17Random-v0 | none | B3 | 2 | 115.00 | 70886.00 | 29.92 |
| MiniGrid-MemoryS17Random-v0 | none | B3G | 2 | 35.00 | 20773.00 | 9.13 |
| MiniGrid-MemoryS17Random-v0 | none | B4 | 2 | 35.00 | 14253.50 | 6.96 |
| MiniGrid-MemoryS17Random-v0 | none | B5 | 0 | — | — | — |
| MiniGrid-MemoryS17Random-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-MemoryS17Random-v0 | none | B7 | 0 | — | — | — |
| MiniGrid-MemoryS17Random-v0 | none | B8 | 4 | 77.00 | 37437.25 | 22.41 |
| MiniGrid-MemoryS17Random-v0 | none | B9 | 10 | 14.00 | 7041.60 | 4.21 |
| MiniGrid-MemoryS17Random-v0 | none | B9N | 4 | 88.00 | 42772.75 | 25.66 |
| MiniGrid-MultiRoom-N6-v0 | none | B0 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B0G | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B1 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B10 | 6 | 75.00 | 33198.67 | 22.29 |
| MiniGrid-MultiRoom-N6-v0 | none | B11 | 6 | 75.00 | 32355.50 | 21.92 |
| MiniGrid-MultiRoom-N6-v0 | none | B2 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B3 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B3G | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B4 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B5 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B7 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B8 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B9 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B9N | 0 | — | — | — |
| BabyAI-GoToObjMazeS7-v0 | none | B11 | 13 | 83.15 | 35592.54 | 23.91 |
| BabyAI-GoToObjMazeS7-v0 | none | B11C | 13 | 83.15 | 0.00 | 1.10 |
| BabyAI-GoToObjMazeS7-v0 | none | B11P | 13 | 83.15 | 35592.46 | 23.93 |
| BabyAI-GoToObjMazeS7-v0 | none | B11R | 13 | 83.15 | 35592.54 | 23.89 |
| BabyAI-GoToObjMazeS7-v0 | none | B11T | 13 | 83.15 | 54928.85 | 29.80 |
| EmbodiedMind-GoToShift-v0 | dropout | B11 | 30 | 10.67 | 3957.60 | 2.90 |
| EmbodiedMind-GoToShift-v0 | dropout | B11C | 30 | 10.67 | 0.00 | 0.11 |
| EmbodiedMind-GoToShift-v0 | dropout | B11P | 30 | 10.67 | 3957.60 | 2.92 |
| EmbodiedMind-GoToShift-v0 | dropout | B11PA | 30 | 10.67 | 3957.60 | 2.91 |
| EmbodiedMind-GoToShift-v0 | dropout | B11R | 30 | 10.67 | 3957.60 | 2.89 |
| EmbodiedMind-GoToShift-v0 | dropout | B11T | 24 | 41.92 | 25827.21 | 13.80 |
| EmbodiedMind-GoToShift-v0 | no_change | B11 | 30 | 10.67 | 3900.80 | 2.91 |
| EmbodiedMind-GoToShift-v0 | no_change | B11C | 30 | 10.67 | 0.00 | 0.12 |
| EmbodiedMind-GoToShift-v0 | no_change | B11P | 30 | 10.67 | 3900.80 | 2.96 |
| EmbodiedMind-GoToShift-v0 | no_change | B11PA | 30 | 10.67 | 3900.80 | 2.86 |
| EmbodiedMind-GoToShift-v0 | no_change | B11R | 30 | 10.67 | 3900.80 | 2.88 |
| EmbodiedMind-GoToShift-v0 | no_change | B11T | 30 | 22.80 | 13008.77 | 7.55 |
| EmbodiedMind-GoToShift-v0 | relocation | B11 | 23 | 27.13 | 10943.52 | 7.81 |
| EmbodiedMind-GoToShift-v0 | relocation | B11C | 23 | 27.13 | 0.00 | 0.27 |
| EmbodiedMind-GoToShift-v0 | relocation | B11P | 8 | 144.00 | 63450.25 | 45.78 |
| EmbodiedMind-GoToShift-v0 | relocation | B11PA | 8 | 144.00 | 63450.25 | 45.51 |
| EmbodiedMind-GoToShift-v0 | relocation | B11R | 23 | 27.13 | 10943.52 | 7.68 |
| EmbodiedMind-GoToShift-v0 | relocation | B11T | 30 | 17.80 | 9440.27 | 5.76 |
| MiniGrid-DoorKey-8x8-v0 | none | B11 | 29 | 20.24 | 9201.79 | 6.48 |
| MiniGrid-DoorKey-8x8-v0 | none | B11C | 29 | 20.24 | 0.00 | 0.09 |
| MiniGrid-DoorKey-8x8-v0 | none | B11P | 0 | — | — | — |
| MiniGrid-DoorKey-8x8-v0 | none | B11R | 29 | 20.24 | 9201.79 | 6.52 |
| MiniGrid-DoorKey-8x8-v0 | none | B11T | 27 | 25.07 | 15356.48 | 9.44 |
| MiniGrid-MultiRoom-N6-v0 | none | B0 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B0G | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B1 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B10 | 10 | 49.80 | 22073.70 | 15.59 |
| MiniGrid-MultiRoom-N6-v0 | none | B11 | 10 | 49.80 | 21515.90 | 15.45 |
| MiniGrid-MultiRoom-N6-v0 | none | B2 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B3 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B3G | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B4 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B5 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B6 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B7 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B8 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B9 | 0 | — | — | — |
| MiniGrid-MultiRoom-N6-v0 | none | B9N | 0 | — | — | — |

Differences use only identical environment, intervention, mission, seed and replicate. Replicate differences are averaged within seed before estimating intervals with a deterministic 4,000-draw seed bootstrap. Intervals are shown for at least five matched seeds. Valid task failures are included. Missing measurements stay missing. The main dynamic comparisons retain episodes under their assigned condition. Exposure counts show how often the intervention was recorded as applied.

## Interpretation and limits

- Treat development evidence as feasibility and diagnostics. The two held-out benchmark rosters must both be supplied for full experiment interpretation.
- Estimates apply to the frozen local model, configured action/prompt budgets and abstract 2D worlds. The study concerns planning in simulation.
- A small paired sample and sparse contradiction events can yield imprecise estimates. The stale-action measure requires an explicit evidence ID and misses uncited intent. Unsupported references are missing, invalid or unprovided IDs, a narrower observation than all model hallucinations.
- B3 adds belief revision, aging warnings and working memory to structured memory. The contrast with B2 evaluates that bundle. The B1 result applies to the specified bounded factual history.
- A hidden relocation can be missed when either cell is visible or a policy changes the world before the trigger. Assigned-arm results include these no-ops. Equal measured rates with rare cited contradictions give limited evidence about revision.
- Traces record prompt usage, which can vary by memory treatment under a shared ceiling. Shorter paths and higher success may compete with greater inference cost.
- The observation encoder and model use symbolic features. Navigation depends on the shared controller and odometry inferred from permitted action feedback. Identical-looking objects can be misidentified.

## Failure evidence

- b11-broad · BabyAI-BlockedUnlockPickup-v0 · none · B0 seed 11001 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e07-s11001-none-B0-r0/replay.gif)
- b11-broad · BabyAI-GoToObjMazeS7-v0 · none · B0 seed 11001 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e02-s11001-none-B0-r0/replay.gif)
- b11-broad · BabyAI-GoToObjS6-v1 · none · B4 seed 11001 · environment_timeout (36 steps). Trace at `../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/frames/000036.png), [start.png](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e00-s11001-none-B4-r0/replay.gif)
- b11-broad · BabyAI-KeyCorridorS3R3-v0 · none · B0 seed 11001 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e06-s11001-none-B0-r0/replay.gif)
- b11-broad · BabyAI-PutNextS5N2-v0 · none · B0 seed 11001 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e08-s11001-none-B0-r0/replay.gif)
- b11-broad · BabyAI-SynthS5R2-v0 · none · B0 seed 11001 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e10-s11001-none-B0-r0/replay.gif)
- b11-broad · EmbodiedMind-GoToShift-v0 · dropout · B2 seed 11001 · budget_timeout (48 steps). Trace at `../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/finish.png), [000000.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000000.png), [000001.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000001.png), [000002.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000002.png), [000003.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000003.png), [000004.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000004.png), [000005.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000005.png), [000006.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000006.png), [000007.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000007.png), [000008.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000008.png), [000009.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000009.png), [000010.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000010.png), [000011.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000011.png), [000012.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000012.png), [000013.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000013.png), [000014.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000014.png), [000015.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000015.png), [000016.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000016.png), [000017.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000017.png), [000018.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000018.png), [000019.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000019.png), [000020.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000020.png), [000021.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000021.png), [000022.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000022.png), [000023.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000023.png), [000024.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000024.png), [000025.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000025.png), [000026.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000026.png), [000027.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000027.png), [000028.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000028.png), [000029.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000029.png), [000030.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000030.png), [000031.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000031.png), [000032.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000032.png), [000033.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000033.png), [000034.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000034.png), [000035.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000035.png), [000036.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000036.png), [000037.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000037.png), [000038.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000038.png), [000039.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000039.png), [000040.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000040.png), [000041.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000041.png), [000042.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000042.png), [000043.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000043.png), [000044.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000044.png), [000045.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000045.png), [000046.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000046.png), [000047.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000047.png), [000048.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/frames/000048.png), [start.png](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/start.png), [replay.gif](../../b11-shift-20261116-181345/episodes/e00-s11001-dropout-B2-r0/replay.gif)
- b11-broad · EmbodiedMind-GoToShift-v0 · no_change · B2 seed 11001 · budget_timeout (48 steps). Trace at `../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/finish.png), [000000.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000000.png), [000001.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000001.png), [000002.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000002.png), [000003.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000003.png), [000004.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000004.png), [000005.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000005.png), [000006.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000006.png), [000007.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000007.png), [000008.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000008.png), [000009.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000009.png), [000010.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000010.png), [000011.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000011.png), [000012.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000012.png), [000013.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000013.png), [000014.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000014.png), [000015.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000015.png), [000016.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000016.png), [000017.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000017.png), [000018.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000018.png), [000019.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000019.png), [000020.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000020.png), [000021.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000021.png), [000022.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000022.png), [000023.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000023.png), [000024.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000024.png), [000025.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000025.png), [000026.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000026.png), [000027.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000027.png), [000028.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000028.png), [000029.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000029.png), [000030.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000030.png), [000031.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000031.png), [000032.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000032.png), [000033.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000033.png), [000034.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000034.png), [000035.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000035.png), [000036.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000036.png), [000037.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000037.png), [000038.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000038.png), [000039.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000039.png), [000040.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000040.png), [000041.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000041.png), [000042.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000042.png), [000043.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000043.png), [000044.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000044.png), [000045.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000045.png), [000046.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000046.png), [000047.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000047.png), [000048.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/frames/000048.png), [start.png](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/start.png), [replay.gif](../../b11-shift-20261116-181345/episodes/e00-s11001-no_change-B2-r0/replay.gif)
- b11-broad · EmbodiedMind-GoToShift-v0 · relocation · B1 seed 11009 · budget_timeout (48 steps). Trace at `../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/finish.png), [000000.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000000.png), [000001.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000001.png), [000002.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000002.png), [000003.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000003.png), [000004.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000004.png), [000005.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000005.png), [000006.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000006.png), [000007.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000007.png), [000008.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000008.png), [000009.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000009.png), [000010.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000010.png), [000011.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000011.png), [000012.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000012.png), [000013.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000013.png), [000014.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000014.png), [000015.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000015.png), [000016.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000016.png), [000017.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000017.png), [000018.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000018.png), [000019.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000019.png), [000020.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000020.png), [000021.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000021.png), [000022.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000022.png), [000023.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000023.png), [000024.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000024.png), [000025.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000025.png), [000026.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000026.png), [000027.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000027.png), [000028.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000028.png), [000029.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000029.png), [000030.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000030.png), [000031.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000031.png), [000032.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000032.png), [000033.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000033.png), [000034.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000034.png), [000035.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000035.png), [000036.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000036.png), [000037.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000037.png), [000038.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000038.png), [000039.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000039.png), [000040.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000040.png), [000041.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000041.png), [000042.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000042.png), [000043.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000043.png), [000044.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000044.png), [000045.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000045.png), [000046.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000046.png), [000047.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000047.png), [000048.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/frames/000048.png), [start.png](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/start.png), [replay.gif](../../b11-shift-20261116-181345/episodes/e00-s11009-relocation-B1-r0/replay.gif)
- b11-broad · MiniGrid-DoorKey-8x8-v0 · none · B0 seed 11003 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e01-s11003-none-B0-r0/replay.gif)
- b11-broad · MiniGrid-Dynamic-Obstacles-8x8-v0 · none · B0 seed 11001 · terminated_failure (3 steps). Trace at `../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/frames/000003.png), [start.png](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e09-s11001-none-B0-r0/replay.gif)
- b11-broad · MiniGrid-MemoryS13-v0 · none · B0 seed 11004 · terminated_failure (4 steps). Trace at `../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/frames/000004.png), [start.png](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e03-s11004-none-B0-r0/replay.gif)
- b11-broad · MiniGrid-MemoryS17Random-v0 · none · B0 seed 11001 · terminated_failure (3 steps). Trace at `../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/frames/000003.png), [start.png](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e04-s11001-none-B0-r0/replay.gif)
- b11-broad · MiniGrid-MultiRoom-N6-v0 · none · B0 seed 11001 · budget_timeout (48 steps). Trace at `../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/finish.png), [000000.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/frames/000048.png), [start.png](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/start.png), [replay.gif](../../b11-stock-20261116-181345/episodes/e05-s11001-none-B0-r0/replay.gif)
- b11-mechanisms · BabyAI-GoToObjMazeS7-v0 · none · B11 seed 11101 · budget_timeout (48 steps). Trace at `../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/finish.png), [000000.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000000.png), [000001.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000001.png), [000002.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000002.png), [000003.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000003.png), [000004.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000004.png), [000005.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000005.png), [000006.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000006.png), [000007.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000007.png), [000008.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000008.png), [000009.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000009.png), [000010.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000010.png), [000011.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000011.png), [000012.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000012.png), [000013.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000013.png), [000014.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000014.png), [000015.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000015.png), [000016.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000016.png), [000017.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000017.png), [000018.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000018.png), [000019.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000019.png), [000020.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000020.png), [000021.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000021.png), [000022.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000022.png), [000023.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000023.png), [000024.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000024.png), [000025.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000025.png), [000026.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000026.png), [000027.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000027.png), [000028.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000028.png), [000029.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000029.png), [000030.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000030.png), [000031.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000031.png), [000032.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000032.png), [000033.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000033.png), [000034.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000034.png), [000035.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000035.png), [000036.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000036.png), [000037.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000037.png), [000038.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000038.png), [000039.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000039.png), [000040.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000040.png), [000041.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000041.png), [000042.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000042.png), [000043.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000043.png), [000044.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000044.png), [000045.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000045.png), [000046.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000046.png), [000047.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000047.png), [000048.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/frames/000048.png), [start.png](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/start.png), [replay.gif](../../b11-rq-static-20261116-181345/episodes/e01-s11101-none-B11-r0/replay.gif)
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · dropout · B11T seed 11103 · budget_timeout (48 steps). Trace at `../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/finish.png), [000000.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000000.png), [000001.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000001.png), [000002.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000002.png), [000003.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000003.png), [000004.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000004.png), [000005.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000005.png), [000006.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000006.png), [000007.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000007.png), [000008.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000008.png), [000009.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000009.png), [000010.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000010.png), [000011.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000011.png), [000012.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000012.png), [000013.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000013.png), [000014.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000014.png), [000015.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000015.png), [000016.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000016.png), [000017.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000017.png), [000018.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000018.png), [000019.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000019.png), [000020.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000020.png), [000021.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000021.png), [000022.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000022.png), [000023.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000023.png), [000024.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000024.png), [000025.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000025.png), [000026.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000026.png), [000027.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000027.png), [000028.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000028.png), [000029.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000029.png), [000030.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000030.png), [000031.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000031.png), [000032.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000032.png), [000033.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000033.png), [000034.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000034.png), [000035.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000035.png), [000036.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000036.png), [000037.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000037.png), [000038.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000038.png), [000039.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000039.png), [000040.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000040.png), [000041.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000041.png), [000042.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000042.png), [000043.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000043.png), [000044.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000044.png), [000045.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000045.png), [000046.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000046.png), [000047.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000047.png), [000048.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/frames/000048.png), [start.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/start.png), [replay.gif](../../b11-rq-shift-20261116-181345/episodes/e00-s11103-dropout-B11T-r0/replay.gif)
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · relocation · B11 seed 11102 · budget_timeout (48 steps). Trace at `../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/finish.png), [000000.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000000.png), [000001.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000001.png), [000002.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000002.png), [000003.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000003.png), [000004.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000004.png), [000005.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000005.png), [000006.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000006.png), [000007.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000007.png), [000008.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000008.png), [000009.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000009.png), [000010.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000010.png), [000011.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000011.png), [000012.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000012.png), [000013.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000013.png), [000014.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000014.png), [000015.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000015.png), [000016.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000016.png), [000017.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000017.png), [000018.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000018.png), [000019.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000019.png), [000020.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000020.png), [000021.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000021.png), [000022.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000022.png), [000023.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000023.png), [000024.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000024.png), [000025.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000025.png), [000026.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000026.png), [000027.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000027.png), [000028.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000028.png), [000029.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000029.png), [000030.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000030.png), [000031.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000031.png), [000032.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000032.png), [000033.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000033.png), [000034.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000034.png), [000035.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000035.png), [000036.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000036.png), [000037.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000037.png), [000038.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000038.png), [000039.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000039.png), [000040.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000040.png), [000041.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000041.png), [000042.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000042.png), [000043.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000043.png), [000044.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000044.png), [000045.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000045.png), [000046.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000046.png), [000047.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000047.png), [000048.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/frames/000048.png), [start.png](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/start.png), [replay.gif](../../b11-rq-shift-20261116-181345/episodes/e00-s11102-relocation-B11-r0/replay.gif)
- b11-mechanisms · MiniGrid-DoorKey-8x8-v0 · none · B11 seed 11116 · budget_timeout (48 steps). Trace at `../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/finish.png), [000000.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000000.png), [000001.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000001.png), [000002.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000002.png), [000003.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000003.png), [000004.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000004.png), [000005.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000005.png), [000006.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000006.png), [000007.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000007.png), [000008.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000008.png), [000009.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000009.png), [000010.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000010.png), [000011.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000011.png), [000012.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000012.png), [000013.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000013.png), [000014.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000014.png), [000015.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000015.png), [000016.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000016.png), [000017.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000017.png), [000018.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000018.png), [000019.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000019.png), [000020.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000020.png), [000021.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000021.png), [000022.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000022.png), [000023.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000023.png), [000024.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000024.png), [000025.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000025.png), [000026.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000026.png), [000027.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000027.png), [000028.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000028.png), [000029.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000029.png), [000030.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000030.png), [000031.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000031.png), [000032.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000032.png), [000033.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000033.png), [000034.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000034.png), [000035.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000035.png), [000036.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000036.png), [000037.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000037.png), [000038.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000038.png), [000039.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000039.png), [000040.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000040.png), [000041.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000041.png), [000042.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000042.png), [000043.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000043.png), [000044.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000044.png), [000045.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000045.png), [000046.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000046.png), [000047.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000047.png), [000048.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/frames/000048.png), [start.png](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/start.png), [replay.gif](../../b11-rq-static-20261116-181345/episodes/e00-s11116-none-B11-r0/replay.gif)
- b11-multiroom-80 · MiniGrid-MultiRoom-N6-v0 · none · B0 seed 11001 · budget_timeout (80 steps). Trace at `../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/finish.png), [000000.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000000.png), [000001.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000001.png), [000002.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000002.png), [000003.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000003.png), [000004.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000004.png), [000005.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000005.png), [000006.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000006.png), [000007.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000007.png), [000008.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000008.png), [000009.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000009.png), [000010.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000010.png), [000011.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000011.png), [000012.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000012.png), [000013.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000013.png), [000014.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000014.png), [000015.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000015.png), [000016.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000016.png), [000017.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000017.png), [000018.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000018.png), [000019.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000019.png), [000020.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000020.png), [000021.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000021.png), [000022.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000022.png), [000023.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000023.png), [000024.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000024.png), [000025.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000025.png), [000026.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000026.png), [000027.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000027.png), [000028.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000028.png), [000029.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000029.png), [000030.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000030.png), [000031.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000031.png), [000032.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000032.png), [000033.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000033.png), [000034.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000034.png), [000035.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000035.png), [000036.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000036.png), [000037.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000037.png), [000038.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000038.png), [000039.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000039.png), [000040.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000040.png), [000041.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000041.png), [000042.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000042.png), [000043.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000043.png), [000044.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000044.png), [000045.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000045.png), [000046.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000046.png), [000047.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000047.png), [000048.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000048.png), [000049.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000049.png), [000050.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000050.png), [000051.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000051.png), [000052.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000052.png), [000053.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000053.png), [000054.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000054.png), [000055.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000055.png), [000056.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000056.png), [000057.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000057.png), [000058.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000058.png), [000059.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000059.png), [000060.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000060.png), [000061.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000061.png), [000062.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000062.png), [000063.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000063.png), [000064.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000064.png), [000065.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000065.png), [000066.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000066.png), [000067.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000067.png), [000068.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000068.png), [000069.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000069.png), [000070.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000070.png), [000071.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000071.png), [000072.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000072.png), [000073.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000073.png), [000074.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000074.png), [000075.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000075.png), [000076.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000076.png), [000077.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000077.png), [000078.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000078.png), [000079.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000079.png), [000080.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/frames/000080.png), [start.png](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/start.png), [replay.gif](../../b11-multiroom-80-20261116-181345/episodes/e00-s11001-none-B0-r0/replay.gif)

## Outcome distribution

- b11-broad · BabyAI-BlockedUnlockPickup-v0 · none — budget_timeout: 130, success: 20
- b11-broad · BabyAI-GoToObjMazeS7-v0 · none — budget_timeout: 111, success: 39
- b11-broad · BabyAI-GoToObjS6-v1 · none — environment_timeout: 3, success: 147
- b11-broad · BabyAI-KeyCorridorS3R3-v0 · none — budget_timeout: 120, success: 30
- b11-broad · BabyAI-PutNextS5N2-v0 · none — budget_timeout: 120, success: 30
- b11-broad · BabyAI-SynthS5R2-v0 · none — budget_timeout: 148, success: 2
- b11-broad · EmbodiedMind-GoToShift-v0 · dropout — budget_timeout: 6, success: 144
- b11-broad · EmbodiedMind-GoToShift-v0 · no_change — budget_timeout: 5, success: 145
- b11-broad · EmbodiedMind-GoToShift-v0 · relocation — budget_timeout: 23, success: 127
- b11-broad · MiniGrid-DoorKey-8x8-v0 · none — budget_timeout: 100, success: 50
- b11-broad · MiniGrid-Dynamic-Obstacles-8x8-v0 · none — budget_timeout: 61, success: 49, terminated_failure: 40
- b11-broad · MiniGrid-MemoryS13-v0 · none — budget_timeout: 56, success: 82, terminated_failure: 12
- b11-broad · MiniGrid-MemoryS17Random-v0 · none — budget_timeout: 57, success: 53, terminated_failure: 40
- b11-broad · MiniGrid-MultiRoom-N6-v0 · none — budget_timeout: 138, success: 12
- b11-mechanisms · BabyAI-GoToObjMazeS7-v0 · none — budget_timeout: 85, success: 65
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · dropout — budget_timeout: 6, success: 174
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · no_change — success: 180
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · relocation — budget_timeout: 65, success: 115
- b11-mechanisms · MiniGrid-DoorKey-8x8-v0 · none — budget_timeout: 36, success: 114
- b11-multiroom-80 · MiniGrid-MultiRoom-N6-v0 · none — budget_timeout: 130, success: 20

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `b11-rq-shift-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-shift-20261116-181345/manifest.json`. Source `7070c1df449dfecf24b45444a91707caffcc4825`.
- Run `b11-rq-static-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-static-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.
- Run `b11-stock-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-stock-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.
- Run `b11-shift-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-shift-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.
- Run `b11-multiroom-80-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-multiroom-80-20261116-181345/manifest.json`. Source `9888e4881b26910a5f61cfea838829098d2b819d`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-shift-20261116-181345" "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-static-20261116-181345" "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-stock-20261116-181345" "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-shift-20261116-181345" "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-multiroom-80-20261116-181345" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-combined-20261116-181345/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.

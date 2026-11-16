# EmbodiedMind experiment report

EmbodiedMind evaluates memory and belief revision with a frozen local language model in partially observable symbolic MiniGrid/BabyAI tasks.

Run scope includes b11-mechanisms. The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance.

Across these runs, 540 of 540 cells were attempted, 540 validated, 0 excluded and 540 attempts recorded.

## Coverage and descriptive results

| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
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

## Primary paired contrasts

| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
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

## Cost per completed mission

Costs sum across every valid episode, including failures. A dash means zero completions.

| Environment | Intervention | Agent | Completions | Actions / completion | Tokens / completion | Seconds / completion |
| --- | --- | --- | ---: | ---: | ---: | ---: |
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

- b11-mechanisms · EmbodiedMind-GoToShift-v0 · dropout · B11T seed 11103 · budget_timeout (48 steps). Trace at `episodes/e00-s11103-dropout-B11T-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11103-dropout-B11T-r0/finish.png), [000000.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000000.png), [000001.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000001.png), [000002.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000002.png), [000003.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000003.png), [000004.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000004.png), [000005.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000005.png), [000006.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000006.png), [000007.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000007.png), [000008.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000008.png), [000009.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000009.png), [000010.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000010.png), [000011.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000011.png), [000012.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000012.png), [000013.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000013.png), [000014.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000014.png), [000015.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000015.png), [000016.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000016.png), [000017.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000017.png), [000018.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000018.png), [000019.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000019.png), [000020.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000020.png), [000021.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000021.png), [000022.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000022.png), [000023.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000023.png), [000024.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000024.png), [000025.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000025.png), [000026.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000026.png), [000027.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000027.png), [000028.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000028.png), [000029.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000029.png), [000030.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000030.png), [000031.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000031.png), [000032.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000032.png), [000033.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000033.png), [000034.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000034.png), [000035.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000035.png), [000036.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000036.png), [000037.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000037.png), [000038.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000038.png), [000039.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000039.png), [000040.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000040.png), [000041.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000041.png), [000042.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000042.png), [000043.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000043.png), [000044.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000044.png), [000045.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000045.png), [000046.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000046.png), [000047.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000047.png), [000048.png](../episodes/e00-s11103-dropout-B11T-r0/frames/000048.png), [start.png](../episodes/e00-s11103-dropout-B11T-r0/start.png), [replay.gif](../episodes/e00-s11103-dropout-B11T-r0/replay.gif)
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · relocation · B11 seed 11102 · budget_timeout (48 steps). Trace at `episodes/e00-s11102-relocation-B11-r0/trajectory.jsonl`.
  - Private visual evidence: [finish.png](../episodes/e00-s11102-relocation-B11-r0/finish.png), [000000.png](../episodes/e00-s11102-relocation-B11-r0/frames/000000.png), [000001.png](../episodes/e00-s11102-relocation-B11-r0/frames/000001.png), [000002.png](../episodes/e00-s11102-relocation-B11-r0/frames/000002.png), [000003.png](../episodes/e00-s11102-relocation-B11-r0/frames/000003.png), [000004.png](../episodes/e00-s11102-relocation-B11-r0/frames/000004.png), [000005.png](../episodes/e00-s11102-relocation-B11-r0/frames/000005.png), [000006.png](../episodes/e00-s11102-relocation-B11-r0/frames/000006.png), [000007.png](../episodes/e00-s11102-relocation-B11-r0/frames/000007.png), [000008.png](../episodes/e00-s11102-relocation-B11-r0/frames/000008.png), [000009.png](../episodes/e00-s11102-relocation-B11-r0/frames/000009.png), [000010.png](../episodes/e00-s11102-relocation-B11-r0/frames/000010.png), [000011.png](../episodes/e00-s11102-relocation-B11-r0/frames/000011.png), [000012.png](../episodes/e00-s11102-relocation-B11-r0/frames/000012.png), [000013.png](../episodes/e00-s11102-relocation-B11-r0/frames/000013.png), [000014.png](../episodes/e00-s11102-relocation-B11-r0/frames/000014.png), [000015.png](../episodes/e00-s11102-relocation-B11-r0/frames/000015.png), [000016.png](../episodes/e00-s11102-relocation-B11-r0/frames/000016.png), [000017.png](../episodes/e00-s11102-relocation-B11-r0/frames/000017.png), [000018.png](../episodes/e00-s11102-relocation-B11-r0/frames/000018.png), [000019.png](../episodes/e00-s11102-relocation-B11-r0/frames/000019.png), [000020.png](../episodes/e00-s11102-relocation-B11-r0/frames/000020.png), [000021.png](../episodes/e00-s11102-relocation-B11-r0/frames/000021.png), [000022.png](../episodes/e00-s11102-relocation-B11-r0/frames/000022.png), [000023.png](../episodes/e00-s11102-relocation-B11-r0/frames/000023.png), [000024.png](../episodes/e00-s11102-relocation-B11-r0/frames/000024.png), [000025.png](../episodes/e00-s11102-relocation-B11-r0/frames/000025.png), [000026.png](../episodes/e00-s11102-relocation-B11-r0/frames/000026.png), [000027.png](../episodes/e00-s11102-relocation-B11-r0/frames/000027.png), [000028.png](../episodes/e00-s11102-relocation-B11-r0/frames/000028.png), [000029.png](../episodes/e00-s11102-relocation-B11-r0/frames/000029.png), [000030.png](../episodes/e00-s11102-relocation-B11-r0/frames/000030.png), [000031.png](../episodes/e00-s11102-relocation-B11-r0/frames/000031.png), [000032.png](../episodes/e00-s11102-relocation-B11-r0/frames/000032.png), [000033.png](../episodes/e00-s11102-relocation-B11-r0/frames/000033.png), [000034.png](../episodes/e00-s11102-relocation-B11-r0/frames/000034.png), [000035.png](../episodes/e00-s11102-relocation-B11-r0/frames/000035.png), [000036.png](../episodes/e00-s11102-relocation-B11-r0/frames/000036.png), [000037.png](../episodes/e00-s11102-relocation-B11-r0/frames/000037.png), [000038.png](../episodes/e00-s11102-relocation-B11-r0/frames/000038.png), [000039.png](../episodes/e00-s11102-relocation-B11-r0/frames/000039.png), [000040.png](../episodes/e00-s11102-relocation-B11-r0/frames/000040.png), [000041.png](../episodes/e00-s11102-relocation-B11-r0/frames/000041.png), [000042.png](../episodes/e00-s11102-relocation-B11-r0/frames/000042.png), [000043.png](../episodes/e00-s11102-relocation-B11-r0/frames/000043.png), [000044.png](../episodes/e00-s11102-relocation-B11-r0/frames/000044.png), [000045.png](../episodes/e00-s11102-relocation-B11-r0/frames/000045.png), [000046.png](../episodes/e00-s11102-relocation-B11-r0/frames/000046.png), [000047.png](../episodes/e00-s11102-relocation-B11-r0/frames/000047.png), [000048.png](../episodes/e00-s11102-relocation-B11-r0/frames/000048.png), [start.png](../episodes/e00-s11102-relocation-B11-r0/start.png), [replay.gif](../episodes/e00-s11102-relocation-B11-r0/replay.gif)

## Outcome distribution

- b11-mechanisms · EmbodiedMind-GoToShift-v0 · dropout — budget_timeout: 6, success: 174
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · no_change — success: 180
- b11-mechanisms · EmbodiedMind-GoToShift-v0 · relocation — budget_timeout: 65, success: 115

## Regenerable figures

- [success](figures/success.png)
- [efficiency](figures/efficiency.png)
- [belief](figures/belief.png)
- [grounding](figures/grounding.png)
- [paired comparisons](figures/paired-comparisons.png)

## Provenance and reproduction

- Run `b11-rq-shift-20261116-181345`. Manifest at `/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-shift-20261116-181345/manifest.json`. Source `7070c1df449dfecf24b45444a91707caffcc4825`.

Regenerate outputs with `python -m embodiedmind.cli report "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-shift-20261116-181345" --output "/home/adithyaa/Projects/EmbodiedMind/outputs/b11-rq-shift-20261116-181345/report"`.

[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · [Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · [Application summary](application-summary.md)

The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.
